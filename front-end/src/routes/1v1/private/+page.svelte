<script>
    import Workspace from "../../../components/Workspace.svelte";
    import NavBar from "../../../components/NavBar.svelte";
    import supabase from "$lib/db"
  import {goto} from "$app/navigation"
  import {session_user,authHandlers} from "$lib/stores"
</script>

<NavBar></NavBar>
<Workspace problemID=8></Workspace>