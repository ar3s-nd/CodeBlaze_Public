<script>
    import {session_user,pointsInfo} from "$lib/stores"
    import NavBar from "../../components/NavBar.svelte";
    import supabase from "$lib/db"
    import { Chart } from "chart.js/auto";
    import { onMount } from "svelte";
    import {
        toastList,
        authHandlers,
        userInfo,
    } from "$lib/stores";
    import { goto } from "$app/navigation";
    let session,POINT_INFO;
    const unsubscribe4 = session_user.subscribe((val)=>{
        session = val;
    })
    let SESSION_USER, USER_INFO, user_sub;
    const unsubscribe = session_user.subscribe((value) => {
        SESSION_USER = value;
    });
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });
    const unsubscribe3 = pointsInfo.subscribe((value) => {
        POINT_INFO = value;
    });
    let chartValues = [];
    let chartLabels = [];
    let problem_solved = 0;
    console.log(USER_INFO)
    let valueSum = 0;
    $: USER_INFO?.solved_problem?.forEach(element => {
        valueSum+=element.points
        chartValues.push(valueSum)
        chartLabels.push(element.date)
        problem_solved+=1;
    });;
	
	let ctx,chart,chart2,ctx2;
	let chartCanvas,chartCanvas2;
    $: console.log(chartValues,chartLabels)
  async function fder(events){
    try{
      $: ctx = chartCanvas?.getContext('2d');
			chart = new Chart(ctx, {
				type: 'line',
                responsive:true,
				data: {
						labels: chartLabels,
						datasets: [{
								label: 'Points',
								backgroundColor: 'rgb(255, 99, 132)',
								borderColor: 'rgb(255, 99, 132)',
								data: chartValues
						}]
				}
		})}catch(e){

    }
    try{
      ctx2= chartCanvas2?.getContext('2d');
			chart2 = new Chart(ctx2, {
				type: 'pie',
                responsive:true,
				data: {
						labels: ["Correct Answer","Wrong Answer","Time Limit Exceeded","Runtime Error","Compilation Error"],
						datasets: [{
								label: 'Points',
								// backgroundColor: 'rgb(255, 99, 132)',
								// borderColor: 'rgb(255, 99, 132)',
								data: [POINT_INFO.accepted_count,POINT_INFO.wa_count,POINT_INFO.tle_count,POINT_INFO.re_count,POINT_INFO.ce_count]
						}]
				}
		})}catch(e){

    }
  }
	onMount(async (promise) => {
    fder("1");
    });
  $:fder(chartCanvas,chartLabels,SESSION_USER,chartValues,USER_INFO,POINT_INFO,chartCanvas2)

  var pointsArray=[];
  async function fetchData() {
    const { data, error } = await supabase.rpc('get_user_points')
    pointsArray=data
  }

// Call the fetchData function when the page is loaded
onMount(async()=>{
  await fetchData();
})

</script>
<NavBar></NavBar>
{#if session}
<div style="display:flex;flex-wrap:wrap" id="top-level">
<div class="flex" style="flex-direction:column;">
    <div class="text-lg m-5 font-bold card w-96 bg-cover bg-[url('https://img.freepik.com/premium-vector/abstract-fluid-background-with-blue-yellow-color-vector-illustration_500223-973.jpg')] shadow-xl background-size: cover">
        <div class="card-body">
          <h2 class="card-title" style="text-shadow: 0 0 3px black">Roadmap</h2>
          <p style="text-shadow: 0 0 3px black">Follow our curated sequence of topics and problems to master your skills</p>
          <div class="card-actions justify-end">
            <button class="btn btn-primary shadow-md shadow-black" on:click={function(){goto("/roadmap")}}>Go.</button>
          </div>
        </div>
      </div>

    <div class="text-lg m-5 font-bold card w-96 bg-cover bg-[url('https://static.vecteezy.com/system/resources/previews/012/672/269/non_2x/abstract-background-with-light-wave-blurred-backdrop-illustration-for-your-graphic-design-banner-wallpaper-template-or-poster-vector.jpg')] shadow-xl background-size: cover">
      <div class="card-body">
        <h2 class="card-title" style="text-shadow: 0 0 3px black">Compete</h2>
        <p style="text-shadow: 0 0 3px black">Choose from a wide range of problem categories and compete with others</p>
        <div class="card-actions justify-end">
          <button class="btn btn-primary shadow-md shadow-black" on:click={function(){goto("/1v1")}}>Go.</button>
        </div>
      </div>
    </div>

    <!-- <div role="tablist" class="tabs tabs-lifted tabs-lg" style=";margin-top:20px;margin-right:20px;margin-bottom:20px;margin-left:20px;">
      <input type="radio" name="my_tabs_2" role="tab" class="tab" aria-label="Solved Recently" checked /> -->
      
      <div class="m-5 rounded-lg bg-cover bg-[url('https://media.istockphoto.com/id/1390631668/photo/modern-abstract-purple-background.jpg?b=1&s=612x612&w=0&k=20&c=kkrC_IE_kYbZBLnpgd4YSWBq9L1DY6N-EaoT55bZ7qk=')]">
        <h1 class="m-5 font-medium" style="align-self:center;font-size:larger">Leaderboard</h1> 
        <table class="table font-medium" style="width:90%;font-size:17px;">
          <thead>
            <tr class="font-medium">
              <th>Rank</th>
              <th>Player</th>
              <th>Points</th>
            </tr>
          </thead>
          <tbody>
          {#each {length:Math.min(pointsArray.length,10)} as _ ,i }
          <tr>
            <td>{i+1}</td>
            <td>{pointsArray[i].name_}</td>
            <!-- <td >{USER_INFO?.solved_problem[USER_INFO?.solved_problem.length-i-1].date}</td> -->
            <td>{pointsArray[i].points_}</td>
          </tr>
          {/each}
        </tbody>
        </table>
        </div>
  
  </div>

  <div class="flex flex-col items-center" id="sub-level">
    <div style="width:60vw" class="stats stats-vertical lg:stats-horizontal shadow m-5 bg-cover bg-[url('https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjEwMTYtYy0wOF8xLWtzaDZtemEzLmpwZw.jpg')] background-size:cover">
  
        <div class="stat ">
          <div class="stat-title">Accepted Problems</div>
          <div class="stat-value">{problem_solved}</div>
          <div class="stat-desc">Start - {new Date().toLocaleDateString()}</div>
        </div>
        
        <div class="stat">
          <div class="stat-title">Accepted Submissions</div>
          <div class="stat-value">{POINT_INFO.accepted_count}</div>
          <!-- <div class="stat-desc">↗︎ 400 (22%)</div> -->
        </div>
        
        <div class="stat">
          <div class="stat-title">Total WA Submissions</div>
          <div class="stat-value">{POINT_INFO.wa_count+POINT_INFO.re_count+POINT_INFO.ce_count+POINT_INFO.tle_count}</div>
          <!-- <div class="stat-desc">↘︎ 90 (14%)</div> -->
        </div>
        
    </div>
    <div role="tablist" class="tabs tabs-lifted tabs-lg" style="width:60vw;margin-top:20px;margin-right:20px;margin-bottom:20px;margin-left:20px;">
        <input type="radio" name="my_tabs_2" role="tab" class="tab" aria-label="Solved Recently" checked />
        <div role="tabpanel" class="tab-content bg-base-100 border-base-300 rounded-box p-6" id="solvedQs">
          <table id = "tbl" class="table" style="font-size:20px;">
            <thead>
              <tr>
                <th>No</th>
                <th>Problem ID</th>
                <th>Date</th>
                <th>Submission ID</th>
              </tr>
            </thead>
            <tbody>
          {#if USER_INFO?.solved_problem != undefined}
            {#each {length:Math.min(USER_INFO?.solved_problem.length,10)} as _ ,i }
            <tr id="prob_list">
              <td>{i+1}</td>
              <td ><a href = {"/problem/"+USER_INFO?.solved_problem[USER_INFO?.solved_problem.length-i-1].id}>Problem {USER_INFO?.solved_problem[USER_INFO?.solved_problem.length-i-1].id}</a></td>
              <td >{USER_INFO?.solved_problem[USER_INFO?.solved_problem.length-i-1].date}</td>
              <td><a href = {"/submission/"+USER_INFO?.solved_problem[USER_INFO?.solved_problem.length-i-1].subID}>Submission {USER_INFO?.solved_problem[USER_INFO?.solved_problem.length-i-1].subID}</a></td>
            </tr>
            {/each}
          {/if}
          </tbody>
          </table>
        </div>
    
  </div>
  <div class="flex flex-row flex-wrap justify-center" style="">
    <div id="item1">
      <canvas bind:this={chartCanvas2} id="myChart2"></canvas>
      <center>Submission Distribution</center>
    </div> 
    <div id="item2" style="height:100%;">
      <canvas bind:this={chartCanvas} id="myChart" style="min-width:300px;min-height:250px;"></canvas>
      <center>Growth of Points</center>
    </div> 
  </div> 
</div>
</div>
<!--         
        <input type="radio" name="my_tabs_2" role="tab" class="tab" aria-label="Wrong" />
        <div role="tabpanel" class="tab-content bg-base-100 border-base-300 rounded-box p-6">Tab content 3</div> -->



<!-- <div id="top-level2" class="flex flex-col items-center">
  <div class="carousel w-2/5">
    <div id="item1" class="carousel-item w-full">
      <canvas bind:this={chartCanvas2} id="myChart2"></canvas>
      <center>Submission Distribution</center>
    </div> 
    <div id="item2" class="carousel-item w-full">
      <canvas bind:this={chartCanvas} id="myChart"></canvas>
      <center>Growth of Points</center>
    </div> 
    <div id="item3" class="carousel-item w-full">
      <img src="https://daisyui.com/images/stock/photo-1414694762283-acccc27bca85.jpg" class="w-full" />
    </div> 
    <div id="item4" class="carousel-item w-full">
      <img src="https://daisyui.com/images/stock/photo-1665553365602-b2fb8e5d1707.jpg" class="w-full" />
    </div>
  </div> 
  <div class="flex justify-center w-2/5 py-2 gap-2">
    <a href="#item1" class="btn btn-xs">1</a> 
    <a href="#item2" class="btn btn-xs">2</a> 
    <a href="#item3" class="btn btn-xs">3</a> 
    <a href="#item4" class="btn btn-xs">4</a>
  </div>
</div> -->
<!-- 
<div style="margin-top:20px;margin-right:20px;margin-bottom:20px;margin-left:20px;">
  <canvas bind:this={chartCanvas2} id="myChart2"></canvas>
  <center>Submission Distribution</center>
</div>
<div style="margin-top:20px;margin-right:20px;margin-bottom:20px;margin-left:20px;">
  <canvas bind:this={chartCanvas} id="myChart"></canvas>
  <center>Growth of Points</center>
</div> -->
{:else}
    
{/if}

<style>
  #prob_list
  {
    background-color: #1f2937;
  }
  #prob_list:hover
  {
    filter:contrast(0.75);
  }
  td,th
  {
    text-align: center;
  }
  @media only screen and (max-width: 600px) {
    #tbl{
      font-size:13px !important;
      display:none;
    }
  }
</style>
