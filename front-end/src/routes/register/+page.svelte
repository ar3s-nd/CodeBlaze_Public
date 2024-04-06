<script>
  import supabase from "$lib/db"
  import {goto} from "$app/navigation"
  import {session_user,authHandlers} from "$lib/stores"
  let email,password,c_password;
  let onRegister = async function(){
    if (password==c_password && password.length>=8){
      authHandlers.signup(email,password)
    }
    
  }
</script>

<div class = "size-100 items-center justify-center flex min-h-screen">
    <div class="card shrink-0 w-full max-w-sm shadow-2xl bg-base-100">
      <form class="card-body">
        <img src = "/favicon-32x32.png" class = "self-center" style="width:32px;height:32px;">
        <div class="form-control">
          <label class="label">
            <span class="label-text">Email</span>
          </label>
          <input type="email" placeholder="email" bind:value = {email} class="input input-bordered" required />
        </div>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Password</span>
          </label>
          <input type="password" placeholder="password" bind:value = { password} class="input input-bordered" required />
        </div>
        <div class="form-control">
            <label class="label">
              <span class="label-text">Confirm Password</span>
            </label>
            <input type="password" placeholder="password" bind:value = {c_password} class="input input-bordered" required />
          </div>
          <label class="label">
            <a class="label-text-alt link link-hover" href="\login">Login?</a>
          </label>
        <div class="form-control mt-6">
          <button class="btn btn-primary" on:click={onRegister}>Reigster</button>
        </div>
      </form>
    </div>
  </div>