<script>
    import Workspace from "../../../components/Workspace.svelte";
    import NavBar from "../../../components/NavBar.svelte";
    import supabase from "$lib/db";
    import { toast } from '@zerodevx/svelte-toast'
    import { goto,invalidateAll } from "$app/navigation";
    import { page } from "$app/stores";
    import {
        toastList,
        authHandlers,
        session_user,
        userInfo,
        play_Info
    } from "$lib/stores";
    import { onDestroy, onMount } from "svelte";
    invalidateAll();
    let SESSION_USER, USER_INFO, user_sub;
    const unsubscribe = session_user.subscribe((value) => {
        SESSION_USER = value;
    });
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });
    
    let playID = $page.params.playID;
    let playInfo_, play_listen, countdowntimer, timerInterval;
    const unsubscribe3 = play_Info.subscribe((value) => {
        playInfo_ = value;
        console.log(playInfo_)
    });
    function updatePlayInfo(playInfo) {
        console.log(playInfo)
        if (playInfo == undefined) {
            async function _() {
                let { data, error } = await supabase
                    .from("t_1v1")
                    .select()
                    .eq("id", playID);
                console.log(data);
                play_Info.update(function(state){return data[0]});
                // playInfo_ = data[0];
                console.log(playInfo_);
            play_listen = supabase
            .channel("player-playxx"+SESSION_USER.user.id+playID)
            .on(
                "postgres_changes",
                {
                    event: "*",
                    schema: "public",
                    table: "t_1v1",
                    filter: "id=eq." + playID,
                },
                (payload) => {
                    console.log(payload)
                    play_Info.update(function(state){return payload.new});
                    updatePlayInfo(playInfo_)
                },
            )
            .subscribe();
            }
            _();
        } else if (
            playInfo.user_1 != SESSION_USER.user.id &&
            playInfo.user_2 != SESSION_USER.user.id
        ) {
            toast.push("You Cannot Participate in this 1v1!");
        } else if (playInfo.session_status == "ended") {
            let b = "";
            if (
                playInfo.user_1 == SESSION_USER.user.id &&
                playInfo.winner == SESSION_USER.user.id
            ) {
                b += "You have won.";
            } else if (
                playInfo.user_2 == SESSION_USER.user.id &&
                playInfo.winner == SESSION_USER.user.id
            ) {
                b += "You have won.";
            } else {
                b += "Your opponent has won.";
            }
            toast.push("This 1v1 has ended." + b);
            try{
                play_Info.update(function(state){return undefined});
                console.log("1",playInfo_)
                clearInterval(timerInterval);
            }catch(e){

            }
            goto("/1v1/");
        } else if (playInfo.session_status == "resigned"){
            let b = "";
            if (
                playInfo.winner == SESSION_USER.user.id
            ) {
                b += "Your opponent has resgined. You win.";
            } else if (
                playInfo.winner == SESSION_USER.user.id
            ) {
                b += "You resigned.";
            } else {
                b += "Your opponent has won.";
            }
            try{
                play_Info.update(function(state){return undefined});
                console.log("1",playInfo_)
                clearInterval(timerInterval);
            }catch(e){
                
            }
            toast.push("This 1v1 has ended." + b);
            goto("/1v1/");
        }else if (playInfo.session_status == "timeout") {
            toast.push("This 1v1 has ended. Neither player won.");
            try{
                play_Info.update(function(state){return undefined});
                console.log("1",playInfo_)
                clearInterval(timerInterval);
            }catch(e){
                
            }
            goto("/1v1/");
        } else {
            console.log(timerInterval);
            if (timerInterval == undefined) {
                timerInterval = setInterval(function () {
                    // console.log(countdowntimer,timerInterval,playInfo)
                    if (countdowntimer == undefined || countdowntimer > 0) {
                        // console.log(countdowntimer);
                        let t = Date.now();
                        let p = Date.parse(playInfo_.started_at)
                        // console.log(playInfo, t);
                        countdowntimer =
                            parseInt(playInfo.time - (t - p) /1000);
                    } else {
                        setTimeout(async function () {
                            const { data, error } = await supabase
                                .from("t_1v1")
                                .update({ session_status: "timeout" })
                                .eq("id", playID)
                                .select();
                        }, 0);
                        clearInterval(timerInterval);
                        
                        play_Info.update(function(state){return undefined});
                        console.log("1",playInfo_)
                        unsubscribe3();
                    }
                }, 1000);
            } else {
                console.log("help");
            }
        }
    }
    async function giveUp(){
        let winner = ""
        let loser = ""
        if (playInfo_.user_1==SESSION_USER.user.id){
            winner = playInfo_.user_2;
            loser = playInfo_.user_1;
        }else{
            winner=playInfo_.user_1;
            loser = playInfo_.user_2;
        }
        let {data, error} = await supabase
              .from('t_1v1')
              .update({winner:winner,session_status:"resigned"})
              .eq('id',playID)
              .select()
        data, error = await supabase.rpc('handle_user_points',{one_id:playID})
    }
    onMount(()=>{
        play_Info.update(function(state){return undefined});
    })
    $: updatePlayInfo(playInfo_);
    onDestroy(()=>{
    try{
        console.log("destoryed")
        supabase.removeChannel('player-playxx'+SESSION_USER.user.id+playID)
    }catch(e){
                
    }
    try{
        unsubscribe3();
        console.log("nuked")
                play_Info.update(function(state){return undefined});
                console.log("1",playInfo_)
                clearInterval(timerInterval);
            }catch(e){
                
            }
  })
</script>
<NavBar></NavBar>
<div id="play_1v1" class = "bg-neutral flex items-center justify-between flex-row" style="">
        <span>Player {playInfo_?.user_1_name}</span>
        <span class="countdown text-xl">
            <span style={"--value:" + (countdowntimer/60)%60}/>m&nbsp;<span style={"--value:" + countdowntimer%60}/>s
        </span>
        <button class = "btn btn-primary" on:click={giveUp}>Give Up!</button>
        <span>Player {playInfo_?.user_2_name}</span>
</div>
{#if playInfo_?.problem_id != undefined}
<Workspace
    problemID={playInfo_?.problem_id}
    view_past_sub={false}
    view_expln={false}
    one_v_oneID={playID}
></Workspace>
{/if}