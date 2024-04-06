<script>
    import NavBar from "../../../components/NavBar.svelte";
    import Workspace from "../../../components/Workspace.svelte";
    import { page } from "$app/stores";
    let problemID = $page.params.problemID;
</script>
<NavBar>
</NavBar>
<Workspace problemID = {problemID} view_past_sub = {true} view_expln = {true}>

</Workspace>