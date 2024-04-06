<script>
  import Workspace from "../../../components/Workspace.svelte";
  import NavBar from "../../../components/NavBar.svelte";
  import supabase from "$lib/db"
  import { page } from "$app/stores";
import {goto} from "$app/navigation"
import {
      toastList,
      authHandlers,
      session_user,
      userInfo,
  } from "$lib/stores";
  import { onMount } from "svelte";
  let SESSION_USER, USER_INFO, user_sub;
  const unsubscribe = session_user.subscribe((value) => {
      SESSION_USER = value;
  });
  const unsubscribe2 = userInfo.subscribe((value) => {
      USER_INFO = value;
  });

async function generateID()
  {
      let {data,error} = await supabase.rpc('get_random_problem')
      console.log(data,error)
      let p = data.id;
      let k =await supabase
          .from('t_1v1')
          .insert({'user_1': SESSION_USER.user.id,'problem_id': p,time:time_alotted})
          .select('id');
      private_id_created = k.data[0].id;
          const channel=supabase     
              .channel('fbwifwofnwo'+SESSION_USER.user.id)
              .on(
                  'postgres_changes',
                  {
                      event:'*',
                      scheme: 'public',
                      table: 't_1v1',
                      filter: 'session_status=eq."started"',
                  },
                  (payload)=>
                  {
                      if(payload)
                        goto("/1v1/"+payload.new.id)
                  }
              )
              .subscribe()
      

  }

  async function joinContest()
  {
      let { data, error } = await supabase
          .from('t_1v1')
          .select()
          // Filters
          .eq('id', private_id)
      
      // console.log(data[0]);
      if(data==undefined)
      {
          window.alert("incorrect code");
      }
      else if(data[0].session_status!="started" && data[0].user_1!=SESSION_USER.user.id && data[0].user_2 !="")
      {
          const {data, error} = await supabase
              .from('t_1v1')
              .update({user_2: SESSION_USER.user.id,session_status: "started",started_at:"NOW()"})
              .eq('id',private_id)
              .select()
              console.log("info "+data[0].session_status);
              goto("/1v1/"+private_id)
      }   
      else if (data[0].user_1==SESSION_USER.user.id){
        window.alert("Cannot play against yourself. ")
      }else
      {
          window.alert("session expired/running");
      }
  }
  let private_id,private_id_created,time_alotted;
</script>

<NavBar></NavBar>
<body>
  <div class="flex flex-row items-center justify-center">
    <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
      <form class="card-body">
        Join Contest
        <div class="form-control">
          <label class="label">
            <span class="label-text">Join Code</span>
          </label>
          <input type="text" id="textInput" class="input input-bordered" required bind:value={private_id}/>
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-active btn-primary" on:click={joinContest}>Join Contest</button>
        </div>
      </form>
      
    </div>
    <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
      <form class="card-body">
        Host Contest
        <div class="form-control">
          <label class="label">
            <span class="label-text">Join Code</span>
          </label>
          <input type="text" readonly class="input input-bordered" required bind:value={private_id_created}/>
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Time (mins)</span>
          </label>
          <select type="text" readonly class="input input-bordered" required bind:value={time_alotted}>
            <option value="20">20sec</option>
            <option value="{5*60}">5</option>
            <option value="{10*60}">10</option>
            <option value="{15*60}">15</option>
            <option value="{20*60}">20</option>
          </select>
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-active btn-primary" on:click={generateID}>Host Contest</button>
        </div>
        {#if private_id_created!=null}
          Waiting for Team-mate to join....
        {/if}
      </form>
      
    </div>
  </div>
</body>