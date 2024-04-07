<script>
    import { goto } from '$app/navigation';
    import {onMount} from "svelte";
    import { Application } from '@splinetool/runtime';
let exmaple = [];
onMount(async()=>{
const canvas = document.getElementById('canvas3d');
const app = new Application(canvas);
app.load('https://prod.spline.design/NGaxQTs2AbwUvQQC/scene.splinecode');

})
</script>
<div class="navbar bg-base-100">
    <div class="navbar-start">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h8m-8 6h16" /></svg>
        </div>
        <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
          <li><a>Item 1</a></li>
          <li>
            <a>Parent</a>
            <ul class="p-2">
              <li><a>Submenu 1</a></li>
              <li><a>Submenu 2</a></li>
            </ul>
          </li>
          <li><a>Item 3</a></li>
        </ul>
      </div>
      <a class="btn btn-ghost text-xl"><img src = "/codeblaze.png" style="height:30px;"></a>
    </div>
    <div class="navbar-end">
      <a class="btn btn-primary" href='\login'>Login</a>
    </div>
  </div>
<div class="hero min-h-screen bg-base-400">
  <div class="hero-content flex-col lg:flex-row-reverse" style="width:100%;">
    <div style="width:50%; height:100%;">
      <canvas id = "canvas3d"></canvas>
    </div>
    <div>
      <h1 class="text-5xl font-bold">A better way to prepare for coding interviews.</h1>
      <p class="py-6">Practice with peers, and learn how to solve complex problems</p>
      <a class="btn btn-primary" href = '/login'>Get Started</a>
    </div>
  </div>
</div>
<div class="overflow-hidden bg-base-100 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
      <div class="lg:pr-8 lg:pt-4">
        <div class="lg:max-w-lg">
          <h2 class="text-base font-semibold leading-7 text-green-600">Compete and Learn</h2>
          <p class="mt-2 text-3xl font-bold tracking-tight text-white-900 sm:text-4xl">1v1 Battles</p>
          <p class="mt-6 text-lg leading-8 text-white-600">Take part in a coding Duel with similar skills as you, and climb up the leaderboards!</p>
        </div>
      </div>
      <img src="/1.jpg" alt="Product screenshot" class="w-[30rem] max-w-none rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[45rem] md:-ml-4 lg:-ml-0" width="1000" height="500">
    </div>
  </div>
</div>
<div class="overflow-hidden bg-base-100 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
      <div class="lg:pr-8 lg:pt-4">
        <div class="lg:max-w-lg">
          <h2 class="text-base font-semibold leading-7 text-green-600">Learn Effectively</h2>
          <p class="mt-2 text-3xl font-bold tracking-tight text-white-900 sm:text-4xl">Structured Roadmap</p>
          <p class="mt-6 text-lg leading-8 text-white-600">Learn and Practice problems in a structured way.</p>
        </div>
      </div>
      <img src="/image.png" alt="Product screenshot" class="w-[30rem] max-w-none rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[45rem] md:-ml-0 lg:-ml-10" width="1000" height="500">
    </div>
  </div>
</div>
<footer class="footer footer-center p-10 bg-primary text-primary-content">
  <aside>
    <img src = "/mtt-2.png" style="width:50px;height:50px;">
    <p class="font-bold">
      Codeblaze Solutions Ltd. <br> Built part of Zense Hacknite 2024
    </p> 
    <p>Copyright © 2024 - All right reserved</p>
  </aside> 
</footer>