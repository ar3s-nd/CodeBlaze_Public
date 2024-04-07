<script>
    import { goto } from "$app/navigation";
  import supabase from "$lib/db";
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
  function getAvatarURL(name) {
    function getInitials(name) {
      let initials = '';
      const words = name.split(' ');
      for (let i = 0; i < words.length; i++) {
        const word = words[i];
        if (word.length > 0) {
          initials += word[0].toUpperCase();
        }
      }
      return initials;
    }
    function hashCode(string) {
    let hash = 0;
    if (string.length == 0) {
        return hash;
    }
    for (let i = 0; i < string.length; i++) {
        let char = string.charCodeAt(i);
        hash = ((hash<<5)-hash)+char;
        hash = hash & hash;
    }
    return hash;
}
    const num = hashCode(name)
    return "https://api.dicebear.com/6.x/bottts/svg?seed=" + getInitials(name) + num.toString()
  }
  let avatarimg = getAvatarURL(USER_INFO.name||"");
</script>
<div class="navbar bg-neutral">
  <div class="flex-1">
    <a class="btn btn-ghost text-xl"><img src = "/codeblaze.png" style="height:30px;" on:click={function(){goto("/dashboard")}}></a>
  </div>
  <div class="flex-none">
        <div style="display: flex;flex-direction:row-reverse;justify-content:center;align-items:center;margin-right:10px;">
          <span>{USER_INFO.points}</span><img style = "width:30px;height:30px;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAABpElEQVR4nO2ZPU7DQBCFTUeBOEME3IOWiIqCeAaQEB2cghpOgYSouEJCCwegCuwucSiIwq8ihfIhmxBHpgjYO2tb2idNtdLu+7x+O8UEgVfNBUWbUPwITX2YsBnUTYiNa8akoqBuQmo+qdrdEOYBVP2GMMdg9QFM2JyYjGBo47/rXl5ewvoOIUfZ51KgeiIhTzaWN4+kFBsBABo6A9A0FADgjjsAbtsHUHTqEAAzt/EBzZfo7awUA9BhWA4A/4AMYMJGfoC7vbVyATiui/wACBag6K1UAEXPuQEcBrkzPc+EjQzAa/WDrPhket49H2QArmoQZGqlH4zPMmvHxQBcBLmXPpdQ9JBZXy8GkASZXxzkAL9/LfqE2V8sBFBCR8ZMnRc2X2JHfircicvpyDSIm5c18+JB7oar1oyWEOT3eG9xAMEgt52YFwuySjuwPICmlmQHFhdut5egeWQRYITu7rK881kIxUfWAAwdOjU/hTC0BcU3UDzO8c+Poeg63iPw8vKSUzrbst555/WFvpVZWmY05LoiD4B0tuX868PP0ry8gr/qC3dbUda3yYbJAAAAAElFTkSuQmCC">
        </div>
    <div class="dropdown dropdown-end">
      <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
        <div class="w-10 rounded-full">
          <img alt="Tailwind CSS Navbar component" src={avatarimg} />
        </div>
      </div>
      <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
        <li><a href = "\logout">Logout</a></li>
      </ul>
    </div>
  </div>
</div>