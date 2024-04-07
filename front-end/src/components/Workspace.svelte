<script>
    import { onMount,onDestroy } from "svelte";
    import supabase from "$lib/db";

    import {
        toastList,
        authHandlers,
        session_user,
        userInfo,
    } from "$lib/stores";
    let Monaco, editor;
    export let problemID = -1;
    export let view_past_sub = true;
    export let view_expln = true;
    export let one_v_oneID = -1;
    let pData;
    let SESSION_USER, USER_INFO, user_sub, sub_status, sub_listen;
    const unsubscribe = session_user.subscribe((value) => {
        SESSION_USER = value;
    });
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });
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
        });
        let { data, error } = await supabase
            .from("problems")
            .select()
            .eq("id", problemID);
        console.log(data, error);
        pData = data[0];
    });

    let selectedlang = "python";
    let view_ = "description";
    let sub_running = false;
    let past_submission = []
    function setLanguage(language) {
        if (Monaco?.editor == null) {
            return;
        }
        Monaco.editor.setModelLanguage(editor.getModel(), language);
    }
    $: setLanguage(selectedlang);
    async function getPastSubmission(){
        let { data, error } = await supabase
            .from("submissions")
            .select("id,runner_output")
            .eq("user_id",SESSION_USER.user.id)
            .eq("problemID", problemID);
        console.log(data)
        past_submission = data;
    }
    async function addSubmission() {
        if (sub_running == true){
            alert("A submission is already running. Please wait.")
            return;
        }
        var codeFromUser = editor.getValue();
        if (codeFromUser == "") {
            return false;
        }
        const { data, error } = await supabase
            .from("submissions")
            .insert([
                {
                    created_at: "NOW()",
                    code: codeFromUser,
                    ex_status: "WAITING",
                    runner_output: {},
                    code_lang: selectedlang,
                    user_id: SESSION_USER.user.id,
                    problemID: problemID,
                    one_v_oneID: one_v_oneID,
                },
            ])
            .select();
        sub_running = true;
        let subID = data[0].id;
        console.log(data, error);
        sub_listen = supabase
            .channel("sub_channel")
            .on(
                "postgres_changes",
                {
                    event: "*",
                    schema: "public",
                    table: "submissions",
                    filter: "id=eq." + subID,
                },
                (payload) => {
                    console.log("Change received!", payload);
                    sub_status = payload.new;
                    sub_status.subID = subID;
                    console.log(sub_status);
                    sub_listen.unsubscribe();
                    sub_running = false;
                },
            )
            .subscribe();
        // goto("/problem/"+data[0].id)
    }
    onDestroy(()=>{
    try{
        supabase.removeChannel('sub_channel'+SESSION_USER.user.id)
    }catch(e){
                
    }
  })
</script>

<div class="workspace">
    <div
        style="min-height:50vh;min-width:45vw;"
        class=" bg-base-300 rounded-box flex-nowrap p-2 flex flex-col w-full lg:flex-row"
    >
        <div class = "grid flex-grow h-32 card bg-base-300 rounded-box"
            style="min-height:80vh;max-height:80vh;overflow-y:scroll;padding:10px;"
            id="expl"
        >
            <div
                class="run bar flex justify-center flex-nowrap flex-row min-w-screen"
            >
                <button
                    class="btn tst_btn"
                    id="btn_code_description"
                    on:click={function () {
                        view_ = "description";
                    }}>Description</button
                >
                {#if view_past_sub == true}
                <button
                    class="btn tst_btn"
                    id="btn_code_past_sub"
                    on:click={function () {getPastSubmission();
                        view_ = "past_submission";
                    }}>Past Submissions</button
                >
                {/if}
                {#if view_expln == true}
                <button
                    class="btn tst_btn"
                    id="btn_code_explanation"
                    on:click={function () {
                        view_ = "explanation";
                    }}>Explanation</button
                >
                {/if}
                <select
                    class=" btn max-w-xs"
                    bind:value={selectedlang}
                    placeholder="Select Language"
                >
                    <option value="cpp">C++</option>
                    <option value="python">Python</option>
                </select>
                <button class="btn" on:click={addSubmission}>
                    <a style="display: flex;flex-direction:row;"> Submit </a>
                </button>
            </div>
            {#if view_ == "description"}
                <div style="margin:10px;padding:10px;" id="code_description">
                    <span style="font-size:30px" id="cdh_name"
                        >{pData?.title}</span
                    ><br />
                    <span class="tst_btn" style="font-size:12px" id="cdh_tag">
                        {#if pData?.tags != null}
                            {#each pData?.tags as tag}
                                <span class="badge badge-primary badge-outline">
                                    {tag}</span
                                >
                            {:else}
                                <span>No tag</span>
                            {/each}
                        {/if}
                    </span>
                    <span
                        style="color:green"
                        id="cdh_difficulty"
                        class="badge badge-info badge-outline"
                    >
                        {pData?.difficulty}</span
                    >
                    <br /><br />
                    <hr />
                    <div id="cdh_description" style="min-height: 40vh;">
                        {@html pData?.description}
                    </div>
                    <hr />
                    <span><b>Constraints: </b></span><br>
                    <span>Time Limit: {pData?.tle} seconds</span><br><span>Memory Limit: {pData?.meml/(1000000)} Mb</span><br>
                </div>
            {:else if view_ == "past_submission"}
                <span style="font-size:30px" id="cdh_name">Past Submisssions</span><br/><hr>
                <div class="overflow-x-auto">
                    <table class="table">
                      <!-- head -->
                      <thead>
                        <tr>
                          <th>Submission ID</th>
                          <th>Status</th>
                          <th>Link</th>
                        </tr>
                      </thead>
                      <tbody>
                        {#each past_submission as sub}
                        <tr>
                            <!-- <th>{i}</th> -->
                            <th>{sub.id}</th>
                            <td>{sub.runner_output.verdict}</td>
                            <td><a href = {"/submission/"+sub.id}>Link</a></td>
                          </tr>
                        {:else}
                          No Past Submissions
                        {/each}
                      </tbody>
                    </table>
                  </div>
            {:else if view_ == "explanation"}
                <span style="font-size:30px" id="cdh_name">Explanation</span><br
                />
                <div id="cdh_explanation" style="min-height: 40vh;">
                    {@html pData?.explanation}
                </div>
            {:else}
                Not Valid
            {/if}
        </div>
        <div class="divider divider-horizontal m-1"></div>
        <div
            style="min-height:80vh;"
            class=" flex-col flex-nowrap flex-grow grid h-32 card bg-base-300 rounded-box" 
        >
            <div id="editor" style="height: 50vh;max-height:50vh;width:100%"></div>
            <div class="divider"></div>
            <div id="result" style="height: 30vh;max-height:50vh">
                {#if sub_running == true}
                    [Note] Your code is getting executed, please wait for a few seconds. 
                {:else if sub_status != null}
                    <span class="text-xs"
                        >Submission {sub_status.subID} Complete</span
                    ><br />
                    {#if sub_status.runner_output.verdict == "Accepted"}
                        <span class="text-lg" style="color:green">Accepted</span
                        ><br />
                        <span class="text-base"
                            >Time Taken: {sub_status.runner_output.time} seconds</span
                        ><br />
                        <span class="text-base"
                            >Memory Used: {sub_status.runner_output.memory} bytes</span
                        ><br />
                    {:else}
                        <span class="text-lg" style="color:red"
                            >{sub_status.runner_output.verdict}</span
                        ><br />
                        <span class="text-base"
                            >Time Taken: {sub_status.runner_output.time} seconds</span
                        ><br />
                        <span class="text-base"
                            >Memory Used: {sub_status.runner_output.memory} bytes</span
                        ><br />
                        <span class="text-base"
                            >stderr: {sub_status.runner_output.error}</span
                        ><br />
                    {/if}      
                {:else}
                    [Note] Please make a Submission to see submission details.
                {/if}
            </div>
        </div>
    </div>
</div>
<pre></pre>

<style>
    pre,
    code {
        background-color: #1c1c1c !important;
        color: black;
    }
</style>
