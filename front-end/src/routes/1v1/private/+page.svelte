<script>
  import Workspace from "../../../components/Workspace.svelte";
  import NavBar from "../../../components/NavBar.svelte";
  import supabase from "$lib/db"
  import { page } from "$app/stores";
import {goto,invalidateAll} from "$app/navigation"
import {
      toastList,
      authHandlers,
      session_user,
      userInfo,
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
let p_tag = "-1"
let channel_p;
async function generateID()
  {
      let {data,error} = await supabase.rpc('get_random_problem',{tag_:p_tag})
      console.log(data,error)
      let p = data.id;
      let k =await supabase
          .from('t_1v1')
          .insert({'user_1': SESSION_USER.user.id,'problem_id': p,time:time_alotted,'user_1_name':USER_INFO.name})
          .select('id');
      private_id_created = k.data[0].id;
          channel_p=supabase     
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
  onDestroy(()=>{
    try{
      supabase.removeChannel('fbwifwofnwo'+SESSION_USER.user.id)
      channel_p.unsubscribe()
    }catch(e){
                
    }
  })
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
              .update({user_2: SESSION_USER.user.id,session_status: "started",started_at:"NOW()",'user_2_name':USER_INFO.name})
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
  <div class="flex flex-row flex-wrap items-center justify-center text-black font-bold" style="margin-top: 10px;margin-right: 10px;margin-bottom: 10px;margin-left: 10px;">
    <div class="card shrink-0 w-full max-w-sm bg-base-100 bg-cover bg-[url('https://img.freepik.com/premium-photo/beautiful-blue-background-that-shades-from-light-dark-concept-sky-air-sea_71793-40.jpg')]" style="margin-top: 10px;margin-right: 10px;margin-bottom: 10px;margin-left: 10px;">
      <form class="card-body">
        Join Contest
        <div class="form-control">
          <label class="label">
            <span class="label-text text-black">Join Code</span>
          </label>
          <input type="text" id="textInput" class="input input-ghost border-black" required bind:value={private_id}/>
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-warning shadow-md shadow-black btn-primary" on:click={joinContest}>Join Contest</button>
        </div>
      </form>
      
    </div>
    <div class="card shrink-0 w-full max-w-sm bg-base-100 bg-cover bg-[url('https://img.freepik.com/premium-photo/beautiful-blue-background-that-shades-from-light-dark-concept-sky-air-sea_71793-40.jpg')]" style="margin-top: 10px;margin-right: 10px;margin-bottom: 10px;margin-left: 10px;">
      <form class="card-body">
        Host Contest
        <div class="form-control">
          <label class="label">
            <span class="label-text text-black">Join Code</span>
          </label>
          <input type="text" readonly class="input input-ghost border-black" required bind:value={private_id_created}/>
        </div>
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
          <button class="btn btn-warning shadow-md shadow-black btn-primary" on:click={generateID}>Host Contest</button>
        </div>
        {#if private_id_created!=null}
          Waiting for Team-mate to join....
        {/if}
      </form>
      
    </div>
  </div>
</body>