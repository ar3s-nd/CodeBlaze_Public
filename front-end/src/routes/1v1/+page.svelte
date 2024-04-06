<script>  
  import NavBar from "../../components/NavBar.svelte";
  import supabase from "$lib/db";
  import { goto } from "$app/navigation";
  import { toastList, authHandlers, session_user, userInfo } from "$lib/stores";
  import { onMount } from "svelte";
  let SESSION_USER, USER_INFO, user_sub;
  const unsubscribe = session_user.subscribe((value) => {
    SESSION_USER = value;
  });
  const unsubscribe2 = userInfo.subscribe((value) => {
    USER_INFO = value;
  });

  async function dbdb() {
    // var selfpoints=getSession().session.user.points;
    // console.log(selfpoints);

    const { data, error } = await supabase
      .from("1v1")
      .select("id")
      // Filters
      .eq("contest_type", "public")
      .eq("session_status", "not started")
      // .rangeLte('user1_points','[500,1000)')
      .gte("user1_points", 500)
      .lte("user1_points", 1000);

    // console.log("data "+data[0].id)
    // if()
    // {
    //   var DATA=data[0].id
    // }

    var DATA;
    if (!(data === undefined)) {
      DATA = data[0].id;
    }
    if (data === undefined) {
      console.log(data[0]);
      const { data, error } = await supabase
        .from("1v1")
        .insert({ user_1: SESSION_USER.user.id, contest_type: "public" });
    } else {
      const { data, error } = await supabase
        .from("1v1")
        .update({ user_2: SESSION_USER.user.id, session_status: "started" })
        .eq("id", DATA);
      // DATA=data[0].id;
      // let {data,error} = await supabase
      //   .from('1v1')
      //   .select('user1_points')
      //   // Filters
      //   .eq('id', DATA)
      // console.log("pls look "+data[0].user1_points);
      // if(data[0].user1_points-0>=500 && data[0].user1_points-0<=1000)
      // {
      //   console.log("if enterd ");
      //   const {data,error} = await supabase
      //     .from('1v1')
      //     .update({user_2: SESSION_USER.user.id, session_status: 'started'})
      //     .eq('id',DATA)
      // }
      // else
      // {
      //   const {data,error}=await supabase
      //     .from('1v1')
      //     .insert({user_1: SESSION_USER.user.id,contest_type: 'public'})
      // }
    }

    // const client = createClient('https://dzbcjgkznubfkonozlze.supabase.co','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6YmNqZ2t6bnViZmtvbm96bHplIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTExOTE5ODIsImV4cCI6MjAyNjc2Nzk4Mn0.3tmfNW-1-w-BZPON2-4Sstkkd_-IwfBL5V4yUILrOFM')
    //           const channel=client
    //               .channel('table_db_changes')
    //               .on(
    //                   'postgres_changes',
    //                   {
    //                       event:'*',
    //                       scheme: 'public',
    //                       table: '1v1',
    //                       filter: 'session_status=eq."started"',
    //                   },
    //                   (payload)=>
    //                   {
    //                       if(payload)
    //                           goto("/1v1/private")
    //                   }
    //               )
    //               .subscribe()
  }
</script>

<NavBar></NavBar>
<div class="flex flex-row" style="width:100vw;height:100%;">
  <div class="card w-96 bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title">Blind</h2>
      <p>Blind Duel with someone from around the world</p>
      <div class="card-actions justify-end">
        <button class="btn btn-primary" on:click={dbdb}>Go.</button>
      </div>
    </div>
  </div>
  <div class="card w-96 bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title">Private</h2>
      <p>1v1 Duel with a Friend</p>
      <div class="card-actions justify-end">
        <button
          class="btn btn-primary"
          on:click={function () {
            goto("/1v1/private");
          }}>Go.</button
        >
      </div>
    </div>
  </div>
</div>
