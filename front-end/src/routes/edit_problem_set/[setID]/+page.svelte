<script>
    import NavBar from "../../../components/NavBar.svelte";
    import { onMount } from "svelte";
    import { page } from "$app/stores";
    import supabase from "$lib/db"
    let setID = $page.params.setID;
    let title,premium,problems = [];

    onMount(async () => {
        let { data, error } = await supabase
                            .from("problem_sets")
                            .select()
                            .eq("id", setID);
        title = data[0].title;
        problems = data[0].problems;
        premium = data[0].premium;
    });
    async function updateProblem(){
        const { data, error } = await supabase
            .from("problem_sets")
            .update([
                {
                    "title": title,
                    "problems":problems,
                    "premium":premium,
                },
            ])
            .eq('id', setID);
        console.log(data,error);
    }
    function updateData(id, field, value) {
    problems = problems.map(item => {
      if (item.id === id) {
        return { ...item, [field]: value };
      }
      return item;
    });
  }
    function addRow() {
    const newId = problems.length > 0 ? Math.max(...problems.map(item => item.id)) + 1 : 1;
    problems = [...problems, { id: newId, name: '', age: '' }];
  }

  // Function to delete a row
  function deleteRow(id) {
    problems = problems.filter(item => item.id !== id);
  }
</script>

<NavBar></NavBar>
<div style="width:90%" class="flex flex-col min-h-screen">
    <label class="input input-bordered flex items-center gap-2">
        Problem Title
        <input type="text" class="grow" placeholder="Arrays" bind:value={title}/>
    </label>
    <label class="flex items-center gap-2">
        Premium
        <select type="text" class="input input-bordered" bind:value={premium}>
            <option value="yes">yes</option>
            <option value="no">no</option>
        </select>
    </label>
    <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Link</th>
            <th>Problem ID</th>
            <th>Source</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
          {#each problems as item (item.id)}
            <tr>
              <td>{item.id}</td>
              <td><input class = "input input-primary" type="text" bind:value={item.title} on:input={() => updateData(item.id, 'title', event.target.value)} /></td>
              <td><input class = "input input-primary" type="link" bind:value={item.link} on:input={() => updateData(item.id, 'link', event.target.value)} /></td>
              <td><input class = "input input-primary" type="number" bind:value={item.pID} on:input={() => updateData(item.id, 'pID', event.target.value)} /></td>
              <td><select class = "select select-primary" type="text" bind:value={item.source} on:input={() => updateData(item.id, 'source', event.target.value)} >
                <option val = "codeblaze">Codeblaze</option>
            <option val = "leetcode">Leetcode</option>
            <option val = "codeforces">Codeforces</option>
            <option val = "codechef">Codechef</option>
            <option val = "website">Website</option>
            </select></td>
              <td><select class = "select select-primary" type="text" bind:value={item.type} on:input={() => updateData(item.id, 'type', event.target.value)} >
            <option val = "problem">Problem</option>
            <option val = "description">Description</option>
            </select></td>
            <td><select class = "select select-primary" type="text" bind:value={item.difficulty} on:input={() => updateData(item.id, 'difficulty', event.target.value)} >
                <option val = "easy">Easy</option>
                <option val = "medium">Medium</option>
                <option val = "hard">Hard</option>
                </select></td>
              <td><button on:click={() => deleteRow(item.id)}>Delete</button></td>
            </tr>
            {:else}
            No Problems Added
          {/each}
        </tbody>
      </table>
      <button class="btn btn-primary" on:click = {addRow}>Add Problem</button>
    <button class="btn btn-primary" on:click = {updateProblem}>Update Problem Set</button>
</div>
