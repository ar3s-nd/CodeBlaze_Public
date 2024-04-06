<script>
    import Workspace from "../../../components/Workspace.svelte";
    import NavBar from "../../../components/NavBar.svelte";
    import supabase from "$lib/db"
    import { createClient } from '@supabase/supabase-js'
  import {goto} from "$app/navigation"
  import {
        toastList,
        authHandlers,
        session_user,
        userInfo,
    } from "$lib/stores";
    import { onMount } from "svelte";
    let SESSION_USER, USER_INFO, user_sub;
    const unsubscribe = session_user.subscribe((value) => {
        SESSION_USER = value;
    });
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });

    // onMount(async () => {
    //     window.onload=function(){document.querySelector("#inputForm").style.visibility="hidden"};
    //     console.log("hello "+document.querySelector("#inputForm"));
    // })
    
    

  async function generateID()
    {
        const {data,error}=await supabase
            .from('1v1')
            .insert({'user_1': SESSION_USER.user.id,'problem_id': 6})
            .select('id');
        
        // console.log("sesson user"+SESSION_USER.user.id);
        // console.log(data[0].id);
        window.alert("contest code: "+data[0].id);

        const client = createClient('https://dzbcjgkznubfkonozlze.supabase.co','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR6YmNqZ2t6bnViZmtvbm96bHplIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTExOTE5ODIsImV4cCI6MjAyNjc2Nzk4Mn0.3tmfNW-1-w-BZPON2-4Sstkkd_-IwfBL5V4yUILrOFM')
            const channel=client     
                .channel('table_db_changes')
                .on(
                    'postgres_changes',
                    {
                        event:'*',
                        scheme: 'public',
                        table: '1v1',
                        filter: 'session_status=eq."started"',
                    },
                    (payload)=>
                    {
                        if(payload)
                            goto("/1v1/private")
                    }
                )
                .subscribe()
        

    }

    async function joinContest()
    {
        console.log("join contest func started");
        var code=document.querySelector("#textInput").value;
        console.log("code: "+code);
        let { data, error } = await supabase
            .from('1v1')
            .select()
            // Filters
            .eq('id', code)
        
        // console.log(data[0]);
        if(data[0]===undefined)
        {
            window.alert("incorrect code");
        }
        else if(data[0] && data[0].session_status!="started")
        {
            const {error} = await supabase
                .from('1v1')
                .update({user_2: SESSION_USER.user.id,session_status: "started"})
                .eq('id',code)
                console.log("info "+data[0].session_status);
                goto("/1v1/private")
        }   
        else
        {
            window.alert("session expired");
        }
    }
</script>

<NavBar></NavBar>
<body>
    <button class="btn btn-active btn-primary" on:click={generateID}>Host Contest</button>
    <button class="btn btn-active btn-primary">Join Contest</button>
    <form id="inputForm">
        <label for="textInput">Enter Text:</label>
        <input type="text" id="textInput" name="textInput">
        <button type="submit" on:click={joinContest}>Submit</button>
    </form>

    
</body>