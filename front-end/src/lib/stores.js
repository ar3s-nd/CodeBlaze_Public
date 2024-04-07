import { writable } from "svelte/store";
import supabase from "$lib/db"
const { data: { user_ } } = await supabase.auth.getSession()
export let session_user = writable( user_||0)
export let pointsInfo = writable({})
export let play_Info = writable(undefined)
// $: console.log(play_Info)
console.log(user_)
// export let one_v_one = writable(0);
export let userInfo = writable(0);
export const authHandlers = {
    signup: async (email, password) => {
        let { data, error } = await supabase.auth.signUp({
            email: email,
            password: password
        })
        session_user.update(function (state){return data});
        return error;
    },
    login: async (email, password) => {
        let { data, error } = await supabase.auth.signInWithPassword({
            email: email,
            password: password
        })
        session_user.update(function (state){return data});
        return error;
    },
    logout: async() => {
        const { error } = await supabase.auth.signOut()
        return error;
    }
}
export let toastList = [];
