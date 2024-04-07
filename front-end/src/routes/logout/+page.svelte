<script>
    import { goto } from "$app/navigation";
    import {
        toastList,
        authHandlers,
        session_user,
        userInfo,
    } from "$lib/stores";
    authHandlers.logout();
    console.log("Initiate logout")
</script>
Logging you Out....