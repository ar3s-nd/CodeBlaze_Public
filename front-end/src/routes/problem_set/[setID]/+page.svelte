<script>
    import NavBar from "../../../components/NavBar.svelte";
    import { onMount } from "svelte";
    import { page } from "$app/stores";
    import supabase from "$lib/db"
    import {
        toastList,
        authHandlers,
        userInfo,
    } from "$lib/stores";
    let setID = $page.params.setID;
    let title,premium,problems = [];
    let USER_INFO;
    let solved_probs = [];
    function u(){
      for (let i = 0;i<USER_INFO?.solved_problem?.length;i++){
        solved_probs.push(USER_INFO?.solved_problem[i]?.id)
      }
      console.log(solved_probs)
    }
    $:u(USER_INFO)
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });
    onMount(async () => {
        let { data, error } = await supabase
                            .from("problem_sets")
                            .select()
                            .eq("id", setID);
        title = data[0].title;
        problems = data[0].problems;
        premium = data[0].premium;
    });
</script>

<NavBar></NavBar>
<div style="width:90%" class="flex flex-col min-h-screen items-center">
    <center style="font-size:30px;font-weight:bold;">{title}</center>
    <div class="overflow-x-auto">
    <table class="table" style="font-size:20px;">
        <thead>
          <tr>
            <th>Solved</th>
            <th>ID</th>
            <th>Title</th>
            <th>Source</th>
            <th>Difficulty</th>
          </tr>
        </thead>
        <tbody>
          {#each problems as item (item.id)}
            <tr>
              <td>{#if solved_probs.includes(parseInt(item.pID))}
                    <input type="checkbox" checked="checked" disabled class="checkbox" />
                  {:else if item.type == "description"}
                    <input type="checkbox" class="checkbox" />
                  {:else if item.source != "Codeblaze"}
                    <input type="checkbox" class="checkbox" />
                  {:else}
                    <input type="checkbox" disabled class="checkbox" />
                  {/if}
              </td>
              <td>{item.id}</td>
              <td><a style="font-weight:bold" target="_blank" href = {item.source=="Codeblaze"?"/problem/"+item.pID:item.link}>{item.title}</a></td>
              <td>
                {#if item.type == "description"}
                    <img style = "width:16px;height:16px" src="https://img.icons8.com/external-inipagistudio-mixed-inipagistudio/64/external-documentation-business-process-inipagistudio-mixed-inipagistudio.png"/>
                {:else if item.source == "Codeblaze"}
                    <img style = "width:16px;height:16px" src = "/favicon-32x32.png"/>
                {:else if item.source == "Leetcode"}
                    <img style = "width:16px;height:16px" src = "https://assets.leetcode.com/static_assets/public/icons/favicon-16x16.png"/>
                {:else if item.source == "Codeforces"}
                    <img style = "width:16px;height:16px" src = "https://codeforces.org/s/67471/favicon-16x16.png"/>
                {:else if item.source == "Codechef"}
                    <img style = "width:16px;height:16px" src = "https://s3.amazonaws.com/codechef_shared/favicon.ico"/>
                {:else}
                    web
                {/if}
            </td>
              <td>{item.difficulty}</td>
            </tr>
            {:else}
            No Problems Added
          {/each}
        </tbody>
      </table>
    </div>
</div>
