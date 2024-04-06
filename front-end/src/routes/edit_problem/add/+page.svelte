<script>
    import supabase from "$lib/db";
    import {goto} from "$app/navigation"
    import {
        toastList,
        authHandlers,
        session_user,
        userInfo,
    } from "$lib/stores";
    let SESSION_USER, USER_INFO, user_sub;
    const unsubscribe = session_user.subscribe((value) => {
        SESSION_USER = value;
    });
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });
    let temp = new Date();
    async function addNewQ() {
        const { data, error } = await supabase
            .from("problems")
            .insert([
                {
                    "created_at": temp,
                    "title": "",
                    "description":"",
                    "testcases":"",
                    "output":"",
                    "tags":[""],
                    "difficulty":"easy",
                    "solution":"",
                    "explanation":""
                },
            ])
            .select();
        console.log(data,error);
        goto("/edit_problem/"+data[0].id)
    }
    addNewQ()
</script>
Hello