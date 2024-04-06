<script>
    import {session_user} from "$lib/stores"
    import NavBar from "../../components/NavBar.svelte";
    let session;
    const unsubscribe = session_user.subscribe((val)=>{
        session = val;
    })
</script>
<NavBar></NavBar>
{#if session}
    <p>Welcome. {session?.user.email}</p>
{:else}
l
{/if}