<script>
    import NavBar from "../../../components/NavBar.svelte";
    import { onMount } from "svelte";
    import { page } from "$app/stores";
    import supabase from "$lib/db"
    let problemID = $page.params.problemID;
    let title,description,testcases,output,difficulty,tags,explanation,tle,meml;

    onMount(async () => {
        setHTML("ed_description","html")
        setHTML("ed_explanation","html")
        let { data, error } = await supabase
                            .from("problems")
                            .select()
                            .eq("id", problemID);
        title = data[0].title;
        setHTML("ed_description",data[0].description)
        testcases = data[0].testcases;
        output = data[0].output;
        difficulty = data[0].difficulty;
        tags = data[0].tags.toString();
        tle = data[0].tle;
        meml = data[0].meml;
        setHTML("ed_explanation",data[0].explanation)
    });
    async function updateProblem(){
        const { data, error } = await supabase
            .from("problems")
            .update([
                {
                    "title": title,
                    "description":getHTML("ed_description"),
                    "testcases":testcases,
                    "output":output,
                    "tags":tags.split(","),
                    "difficulty":difficulty,
                    "tle":tle,
                    "meml":meml,
                    "solution":"",
                    "explanation":getHTML("ed_expanation")
                },
            ])
            .eq('id', problemID);
        console.log(data,error);
    }
</script>

<NavBar></NavBar>
<div style="width:90%" class="flex flex-col min-h-screen">
    <label class="input input-bordered flex items-center gap-2">
        Problem Title
        <input type="text" class="grow" placeholder="Add Two Numbers" bind:value={title}/>
    </label>
    <label class="flex flex-col">
        Description
        <div
            style="width:80vw;height:50vh;background-color:white;"
            class="input-bordered summernote"
            id="ed_description"
        ></div>
    </label>
    <span>Testcases</span>
    <textarea
        placeholder="Testcases"
        class="textarea textarea-bordered textarea-lg w-full max-w" bind:value = {testcases}
    ></textarea>
    <span>Output</span>
    <textarea
        placeholder="Output"
        class="textarea textarea-bordered textarea-lg w-full max-w" bind:value = {output}
    ></textarea>
    <label class="input input-bordered flex items-center gap-2">
        Tags
        <input type="text" class="grow" placeholder="Two Pointers, Strings" bind:value={tags}/>
    </label>
    <label class="flex items-center gap-2">
        Difficulty
        <select type="text" class="input input-bordered" bind:value={difficulty}>
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
        </select>
    </label>
    <label class="input input-bordered flex items-center gap-2">
        Timeout Time
        <input type="text" class="grow" placeholder="Add Two Numbers" bind:value={tle}/>
    </label>
    <label class="input input-bordered flex items-center gap-2">
        Max Memory Use
        <input type="text" class="grow" placeholder="Add Two Numbers" bind:value={meml}/>
    </label>
    <label class="flex flex-col">
        Explanation
        <div
            style="width:80vw;height:50vh;background-color:white;"
            class="input-bordered summernote"
            id="ed_explanation"
        ></div>
    </label>
    <button class="btn btn-primary" on:click = {updateProblem}>Primary</button>
</div>
