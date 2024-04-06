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
    // setTimeout(function(){goto("/")},1000);
</script>
Logging you Out....