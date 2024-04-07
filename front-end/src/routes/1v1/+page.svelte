<script>  
  import NavBar from "../../components/NavBar.svelte";
  import supabase from "$lib/db";
  import { goto,invalidateAll } from "$app/navigation";
  import { toastList, authHandlers, session_user, userInfo } from "$lib/stores";
  import { onMount } from "svelte";
  invalidateAll();
  let SESSION_USER, USER_INFO, user_sub;
  const unsubscribe = session_user.subscribe((value) => {
    SESSION_USER = value;
  });
  const unsubscribe2 = userInfo.subscribe((value) => {
    USER_INFO = value;
  });
</script>

<NavBar></NavBar>
<div class="flex flex-row justify-center flex-wrap" style="width:100vw;height:40%;color:#1f2937;margin-top: 10px;margin-right: 10px;margin-bottom: 10px;margin-left: 10px;">
  <div class="font-bold card w-96 bg-primary shadow-black bg-cover bg-[url('https://img.freepik.com/premium-photo/beautiful-blue-background-that-shades-from-light-dark-concept-sky-air-sea_71793-40.jpg')]" style="margin-top: 10px;margin-right: 10px;margin-bottom: 10px;margin-left: 10px;">
    <div class="card-body">
      <h2 class="card-title">Blind</h2>
      <p>Blind Duel with someone from around the world</p>
      <div class="card-actions justify-end">
        <button class="btn btn-warning shadow-md shadow-black" on:click={function(){goto("/1v1/blind")}}>Go.</button>
      </div>
    </div>
  </div>
  <div class="font-bold card w-96 bg-primary shadow-black bg-cover bg-[url('https://img.freepik.com/premium-photo/beautiful-blue-background-that-shades-from-light-dark-concept-sky-air-sea_71793-40.jpg')]" style="margin-top: 10px;margin-right: 10px;margin-bottom: 10px;margin-left: 10px;">
    <div class="card-body">
      <h2 class="card-title">Private</h2>
      <p>1v1 Duel with a Friend</p>
      <div class="card-actions justify-end">
        <button
          class="btn btn-warning shadow-md shadow-black"
          on:click={function () {
            goto("/1v1/private");
          }}>Go.</button
        >
      </div>
    </div>
  </div>
</div>