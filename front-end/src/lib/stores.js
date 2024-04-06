import { writable } from "svelte/store";
import supabase from "$lib/db"
const { data: { user_ } } = await supabase.auth.getSession()
export let session_user = writable( user_||0)
console.log(user_)

export let userInfo = writable(0);
export const authHandlers = {
    signup: async (email, password) => {
        let { data, error } = await supabase.auth.signUp({
            email: email,
            password: password
        })
        session_user = data;
        return error;
    },
    login: async (email, password) => {
        let { data, error } = await supabase.auth.signInWithPassword({
            email: email,
            password: password
        })
        session_user = data;
        return error;
    },
    logout: async() => {
        const { error } = await supabase.auth.signOut()
        return error;
    }
}
export let toastList = [];
