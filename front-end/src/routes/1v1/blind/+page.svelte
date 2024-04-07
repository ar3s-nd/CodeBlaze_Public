<script>
    import NavBar from "../../../components/NavBar.svelte";
    import supabase from "$lib/db"
    import {goto,invalidateAll} from "$app/navigation"
    import {
        toastList,
        authHandlers,
        session_user,
        userInfo,
    } from "$lib/stores";
    import { onMount,onDestroy } from "svelte";
    import { toast } from "@zerodevx/svelte-toast";
    invalidateAll();
    let SESSION_USER, USER_INFO, user_sub;
    const unsubscribe = session_user.subscribe((value) => {
        SESSION_USER = value;
    });
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });
    let finding_match = false;
    let p_tag = "-1";
    let channel_p;
  async function findMatch(){
        finding_match = true;
    let {data,error} = await supabase.rpc('get_matchmaking_data',{user_:SESSION_USER.user.id,t:time_alotted,tag_:p_tag})
    console.log(data);
    if (data?.join_match==false){
        channel_p=supabase     
                .channel('blind-listen-er3'+SESSION_USER.user.id)
                .on(
                    'postgres_changes',
                    {
                        event:'*',
                        scheme: 'public',
                        table: 'matchmaking',
                        filter: 'id=eq.'+data?.mat_id,
                    },
                    (payload)=>
                    {
                        if(payload.new.matchid!=-1)
                          goto("/1v1/"+payload.new.matchid)
                    }
                )
                .subscribe()
    }else if (data?.join_match==true){
        goto("/1v1/"+data?.match_id)
    }else{
        toast.push("Something went wrong.")
    }
  }
  onDestroy(()=>{
    try{
      supabase.removeChannel('blind-listen-er3'+SESSION_USER.user.id)
    }catch(e){
                
    }
  })
    let private_id,private_id_created,time_alotted;
  </script>
  
  <NavBar></NavBar>
  <body>
    <div class="flex flex-row flex-wrap items-center justify-center text-black font-bold" style="margin-top: 10px;margin-right: 10px;margin-bottom: 10px;margin-left: 10px;">
      <div class="card shrink-0 w-full max-w-sm bg-base-100 bg-cover bg-[url('https://img.freepik.com/premium-photo/beautiful-blue-background-that-shades-from-light-dark-concept-sky-air-sea_71793-40.jpg')]" style="margin-top: 10px;margin-right: 10px;margin-bottom: 10px;margin-left: 10px;">
        <form class="card-body">
          Join Contest
          <!-- <div class="form-control">
            <label class="label">
              <span class="label-text text-black">Join Code</span>
            </label>
            <input type="text" readonly class="input input-ghost border-black" required bind:value={private_id_created}/>
          </div> -->
          <div class="form-control">
            <label class="label">
              <span class="label-text text-black">Time (mins)</span>
            </label>
            <select type="text" class="input input-ghost border-black" required bind:value={time_alotted}>
              <option value="20">20sec</option>
              <option value="{5*60}">5</option>
              <option value="{10*60}">10</option>
              <option value="{15*60}">15</option>
              <option value="{20*60}">20</option>
            </select>
          </div>
          <div class="form-control">
            <label class="label">
              <span class="label-text text-black">Tags</span>
            </label>
            <select type="text" class="input input-ghost border-black" required bind:value={p_tag}>
              <option value="-1">Random</option>
              <option value="Arrays">Arrays</option>
              <option value="Two Pointers">Two Pointers</option>
              <option value="Sortings">Sortings</option>
              <option value="Binary Search">Binary Search</option>
              <option value="Dynamic Programming">Dynamic Programming</option>
            </select>
          </div>
          <div class="form-control mt-6">
            <button class="btn btn-warning shadow-md shadow-black btn-primary" disabled = {finding_match==true?"disabled":""} on:click={findMatch}>Find Match</button>
          </div>
          {#if finding_match}
            Waiting for Opponent to join....
          {/if}
        </form>
        
      </div>
    </div>
  </body>