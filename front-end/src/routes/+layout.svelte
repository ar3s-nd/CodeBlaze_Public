<script>
    import "tailwindcss/tailwind.css";
    import {
        toastList,
        authHandlers,
        session_user,
        userInfo,
        pointsInfo
    } from "$lib/stores";
    import { onMount } from "svelte";
    import { invalidateAll, goto } from "$app/navigation";
    import supabase from "$lib/db";
    import { SvelteToast } from '@zerodevx/svelte-toast';
    const nonAuthRoutes = [
        "/",
        "/aboutus",
        "/contactus",
        "/login",
        "/register",
        "/terms",
    ];
    let SESSION_USER, USER_INFO, user_sub,POINT_INFO;
    const unsubscribe = session_user.subscribe((value) => {
        SESSION_USER = value;
    });
    const unsubscribe2 = userInfo.subscribe((value) => {
        USER_INFO = value;
    });
    const unsubscribe3 = pointsInfo.subscribe((value) => {
        POINT_INFO = value;
    });
    let seized = false;
    onMount(() => {
        const { data } = supabase.auth.onAuthStateChange(
            async (event, session) => {
                seized = localStorage.getItem("seized")
                session_user.update(function (state) {
                    return { ...state, ...session };
                });
                // console.log(SESSION_USER);
                const currentPath = window.location.pathname;
                if (!session && !nonAuthRoutes.includes(currentPath)) {
                    window.location.href = "/";
                    return;
                }
                if (session && currentPath == "/register") {
                    window.location.href = "/onboarding";
                }
                // If user was already logged in, and he is in landing page, redirect him to dashboard.
                if (
                    session &&
                    (currentPath == "/" || currentPath == "/login")
                ) {
                    window.location.href = "/dashboard";
                }
                if (session && currentPath == "/logout") {
                    authHandlers.logout();
                    console.log("Initiate logout")
                }
                // console.log(event, session);
                if (event === "INITIAL_SESSION") {
                    setTimeout(async function () {
                        let { data, error } = await supabase
                            .from("users")
                            .select()
                            .eq("uuid", session.user.id);

                        console.log(data);
                        userInfo.update(function (state) {
                            return { ...data[0] };
                        });
                        if (data.length == 0) {
                            const { data, error } = await supabase
                                .from("users")
                                .insert([
                                    {
                                        uuid: session.user.id,
                                        username: "",
                                        created_at: "NOW()",
                                        name: "",
                                        country: "",
                                        points: 0,
                                    },
                                ])
                                .select();
                        }
                        console.log(USER_INFO);
                        if (
                            USER_INFO != null &&
                            USER_INFO.onboarding == false
                        ) {
                            goto("/onboarding");
                        }
                        user_sub = supabase
                            .channel("custom-filter-channel")
                            .on(
                                "postgres_changes",
                                {
                                    event: "*",
                                    schema: "public",
                                    table: "users",
                                    filter: "uuid=eq." + session.user.id,
                                },
                                (payload) => {
                                    console.log("Change received!", payload);
                                    userInfo.update(function (state) {
                                        return { ...payload.new };
                                    });
                                    if (USER_INFO.username == "seized_prank_1234"){
                                        localStorage.setItem("seized",true)
                                    }
                                    seized = localStorage.getItem("seized")
                                },
                            )
                            .subscribe();
                        // let { pointsInfo3, total_sub } = await supabase.from('submissions').select('*', { count: 'exact',head:true }).eq("user",session.user.id)
                        // // let {pointsInfo2, total_wa,e_rror2}  = await supabase.from('submissions').select('*', { count: 'exact',head:true }).eq("user",session.user.id).eq("runner_output.verdict","Wrong Answer")
                        // let total_wa = 0
                        // console.log(pointsInfo3,total_sub)
                        // pointsInfo.update(function (state) {
                        //     return { ...state,total_sub:total_sub,total_wa:total_wa };
                        // })
                        let p = await supabase.rpc('get_all_count',{user_id_:session.user.id})
                        console.log(p,data,error)
                        pointsInfo.update(function (state) {
                            return { ...state,...p.data,};
                        })
                        console.log(POINT_INFO)
                    }, 0);
                    
                } else if (event === "SIGNED_IN") {
                    // goto("/dashboard");
                } else if (event === "SIGNED_OUT") {
                    user_sub.unsubscribe();
                    goto("/");
                } else if (event === "PASSWORD_RECOVERY") {
                    // handle password recovery event
                } else if (event === "TOKEN_REFRESHED") {
                    // handle token refreshed event
                } else if (event === "USER_UPDATED") {
                    // handle user updated event
                }
            },
        );
    });
</script>
<SvelteToast />
<div class="toast toast-top toast-end">
    {#each toastList as toast}
        <div
            id={toastList.id}
            class="flex items-center w-full max-w-xs p-4 text-gray-500 bg-white rounded-lg shadow dark:text-gray-400 dark:bg-gray-800"
            role="alert"
        >
            <div class="ms-3 text-sm font-normal">{toast.description}</div>
            <button
                type="button"
                on:click={function () {
                    document.getElementById(toastList.id).remove();
                }}
                class="ms-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700"
                data-dismiss-target="#toast-default"
                aria-label="Close"
            >
                <span class="sr-only">Close</span>
                <svg
                    class="w-3 h-3"
                    aria-hidden="true"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 14 14"
                >
                    <path
                        stroke="currentColor"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
                    />
                </svg>
            </button>
        </div>
    {/each}
</div>
{#if seized == "true"}
    <img src = "seize-prank.png" style="width:100vw;height:100vh;top:0;position:fixed;left:0;">
{:else}
<div out:blur={{ duration: 0 }} in:blur={{ duration: 300 }}>
    <slot />
</div>
{/if}