<script>
    import Workspace from "../../../components/Workspace.svelte";
    import NavBar from "../../../components/NavBar.svelte";
    import supabase from "$lib/db";
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import {
        toastList,
        authHandlers,
        session_user,
        userInfo,
    } from "$lib/stores";
    import { onDestroy, onMount } from "svelte";
    let SESSION_USER, USER_INFO, user_sub;
    const unsubscribe = session_user.subscribe((value) => {
        SESSION_USER = value;
    });
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });
    let playID = $page.params.playID;
    let playInfo_, play_listen, countdowntimer, timerInterval;
    function updatePlayInfo(playInfo) {
        console.log(playInfo)
        if (playInfo == undefined) {
            async function _() {
                let { data, error } = await supabase
                    .from("t_1v1")
                    .select()
                    .eq("id", playID);
                console.log(data);
                playInfo_ = data[0];
                console.log(playInfo_);
            }
            _();
        } else if (
            playInfo.user_1 != SESSION_USER.user.id &&
            playInfo.user_2 != SESSION_USER.user.id
        ) {
            alert("You Cannot Participate in this 1v1!");
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
            alert("This 1v1 has ended." + b);
            goto("/1v1/");
        } else if (playInfo.session_status == "timeout") {
            alert("This 1v1 has ended. Neither player won.");
            goto("/1v1/");
        } else {
            console.log(timerInterval);
            if (timerInterval == undefined) {
                timerInterval = setInterval(function () {
                    console.log(countdowntimer,timerInterval,playInfo)
                    if (countdowntimer == undefined || countdowntimer > 0) {
                        console.log(countdowntimer);
                        let t = Date.now();
                        let p = Date.parse(playInfo_.started_at)
                        console.log(playInfo, t);
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
                    }
                }, 1000);
            } else {
                console.log("help");
            }
        }
    }
    $: updatePlayInfo(playInfo_);
    onDestroy(() => {
        play_listen.unsubscribe();
    });
    onMount(() => {
        play_listen = supabase
            .channel("player-play"+SESSION_USER.user.id)
            .on(
                "postgres_changes",
                {
                    event: "*",
                    schema: "public",
                    table: "t_1v1",
                    filter: "id=eq." + playID,
                },
                (payload) => {
                    console.log(playInfo_);
                    playInfo_ = payload.new;
                },
            )
            .subscribe();
    });
</script>

<NavBar></NavBar>
<div id="play_1v1">
    <span
        ><span class="countdown">
            <span style={"--value:" + (countdowntimer/60)%60}/>m<span style={"--value:" + countdowntimer%60}/>m
        </span></span
    >
</div>
<Workspace
    problemID={playInfo_?.problem_id}
    view_past_sub={false}
    view_expln={false}
    one_v_oneID={playID}
></Workspace>
