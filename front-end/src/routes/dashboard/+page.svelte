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
	
	let ctx,chart;
	let chartCanvas;
    $: console.log(chartValues,chartLabels)
	onMount(async (promise) => {
		    $: ctx = document.getElementById("myChart")?.getContext('2d');
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
		})});

    // Create parent div
    onMount(async()=>{
        const div = document.createElement('div');
        div.classList.add('overflow-x-auto');

        // Create table
        const table = document.createElement('table');
        table.classList.add('table');

        // Create table head
        const thead = document.createElement('thead');
        const headRow = document.createElement('tr');
        const headColumns = ['Problem Name', 'Date'];

        headColumns.forEach(column => {
        const th = document.createElement('th');
        th.textContent = column;
        headRow.appendChild(th);
        });

        thead.appendChild(headRow);
        table.appendChild(thead);

        // Create table body
        const tbody = document.createElement('tbody');

        // const rowData = [
        // [1, 'Cy Ganderton', 'Quality Control Specialist', 'Blue'],
        // [2, 'Hart Hagerty', 'Desktop Support Technician', 'Purple'],
        // [3, 'Brice Swyre', 'Tax Accountant', 'Red']
        // ];
        var rowData=[];

        const { data, error } = await supabase
        .from('users')
        .select()
        .eq('uuid', SESSION_USER.user.id)
    
        var DA=data[0].solved_problem;
        // console.log("len "+DA.length);
        for(let i=0;i<DA.length;i++)
        {   
            rowData[i]=[];
            rowData[i][0]=DA[i].id;
            rowData[i][1]=DA[i].date.slice(0,10);
        }
        // console.log(SESSION_USER.user.id);
        console.log("check "+rowData);

        rowData.forEach(row => {
        const tr = document.createElement('tr');
        row.forEach((cellData, index) => {
            const cell = index === 0 ? document.createElement('th') : document.createElement('td');
            cell.textContent = cellData;
            tr.appendChild(cell);
        });
        tbody.appendChild(tr);
        });

        table.appendChild(tbody);

        // Append table to parent div
        div.appendChild(table);

        // Append parent div to div with id "allSubs"
        const allSubsDiv = document.getElementById('solvedQs');
        if (allSubsDiv) {
        allSubsDiv.appendChild(div);
        } else {
        console.error("Div with id 'allSubs' not found.");
        }
    });

</script>
<NavBar></NavBar>
{#if session}
<div style="display: flex;flex-direction:row;">
<div class="stats stats-vertical lg:stats-horizontal shadow">
  
    <div class="stat">
      <div class="stat-title">Accepted Problems</div>
      <div class="stat-value">{problem_solved}</div>
      <div class="stat-desc">Start - {new Date().toLocaleDateString()}</div>
    </div>
    
    <div class="stat">
      <div class="stat-title">Total Submissions</div>
      <div class="stat-value">{POINT_INFO.total_sub}</div>
      <div class="stat-desc">↗︎ 400 (22%)</div>
    </div>
    
    <div class="stat">
      <div class="stat-title">Total Wrong Submissions</div>
      <div class="stat-value">{POINT_INFO.total_wa}</div>
      <div class="stat-desc">↘︎ 90 (14%)</div>
    </div>
    
  </div>
    <div style="width:30vw;height:30vh">
        <canvas style="width:10vw;height:10vh" bind:this={chartCanvas} id="myChart"></canvas>
        <center>Growth of Points</center>
    </div>
</div>

<div role="tablist" class="tabs tabs-lifted tabs-lg">
    <input type="radio" name="my_tabs_2" role="tab" class="tab" aria-label="All" />
    <div role="tabpanel" class="tab-content bg-base-100 border-base-300 rounded-box p-6">Tab content 1</div>
  
    <input type="radio" name="my_tabs_2" role="tab" class="tab" aria-label="Solved" checked />
    <div role="tabpanel" class="tab-content bg-base-100 border-base-300 rounded-box p-6" id="solvedQs"></div>
  
    <input type="radio" name="my_tabs_2" role="tab" class="tab" aria-label="Wrong" />
    <div role="tabpanel" class="tab-content bg-base-100 border-base-300 rounded-box p-6">Tab content 3</div>
  </div>
{:else}
    
{/if}