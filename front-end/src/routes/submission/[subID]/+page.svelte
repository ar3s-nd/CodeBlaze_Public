<script>
    import NavBar from "../../../components/NavBar.svelte";
    import Workspace from "../../../components/Workspace.svelte";
    import { page } from "$app/stores";
    import { onMount } from "svelte";
    import supabase from "$lib/db"
    let subID = $page.params.subID;
    let subData = {code:""}
    let Monaco, editor;
    onMount(async () => {
        let divEl = document.getElementById("editor");
        Monaco = await import("monaco-editor");
        editor = Monaco.editor.create(divEl, {
            value: [""].join("\n"),
            language: "python",
            theme: "vs-dark",
            width: "100%",
            height: "100%",
            automaticLayout: true,
            readOnly: true,
        });
        let { data, error } = await supabase
            .from("submissions")
            .select()
            .eq("id", subID);
        console.log(data, error);
        subData = data[0];
        $: editor.getModel().setValue(subData?.code);
    });
    
</script>
<NavBar>
</NavBar>
<div style="display: flex;flex-direction:column;padding:10px;">
    <div style="display: flex;flex-direction:column;border:1px white solid;padding:10px;">
    <span style="font-size:26px;">Submission <b>{subData?.id}</b></span>
    <span>Execution Status: <b>{subData?.ex_status}</b></span>
    {#if subData?.runner_output?.verdict == "Accepted"}
        <span>Status: <span class="text-lg" style="color:green">Accepted</span></span>
    {:else}
        <span>Status: <span class="text-lg" style="color:red">{subData?.runner_output?.verdict}</span></span>
    {/if}
    <!-- <span>Status: {subData?.runner_output?.verdict}</span> -->
    <span>Runtime: <b>{subData?.runner_output?.time}</b></span>
    <span>Memory Usage: <b>{subData?.runner_output?.memory}</b></span>
    <span>Submitted On: <b>{subData?.created_at}</b></span>
    <span class="text-base">stderr: <b>{subData?.runner_output?.error}</b></span>
</div>
<br>
    <div id = "editor" style="height:50vh;border: 1px solid white;"></div>
</div>