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
      <a class="btn btn-ghost text-xl"><img src = "/codeblaze.png" style="height:30px;"></a>
    </div>
    <div class="navbar-end">
      <a class="btn btn-primary" href='\login'>Login</a>
    </div>
  </div>

<div class="hero min-h-screen bg-base-400">
  <div class="hero-content flex-col lg:flex-row-reverse" style="width:100%;height:100%;justify-content:center;">
    <div id = "canvas3" style="width:50%; height:100%;">
      <canvas id = "canvas3d"></canvas>
    </div>
    <div>
      <h1 class="text-5xl font-bold">A better way to prepare for coding interviews.</h1>
      <p class="py-6" style = 'font-size: 22.5px'>Practice with peers, and learn how to solve complex problems</p>
      <a class="btn btn-primary" href = '/login'>Get Started</a>
    </div>
  </div>
</div>

<div class="overflow-hidden bg-base-100 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
      <div class="lg:pr-8 lg:pt-4" style = 'display: flex; flex-direction: column; flex-wrap: wrap; align-content: center; justify-content: center; align-items: center;'>
        <div class="lg:max-w-lg">
          <h2 class="text-base font-semibold leading-7 text-green-600" style = "font-size: 24px;">Compete and Learn</h2>
          <p class="mt-2 text-3xl font-bold tracking-tight text-white-900 sm:text-4xl" >1v1 Battles</p>
          <p class="mt-6 text-lg leading-8 text-white-600" style = 'font-size: 22.5px'>Take part in coding duels to climb up the leaderboards!</p>
        </div>
      </div>
      <img src="/1.jpg" alt="Product screenshot" class="w-[30rem] max-w-none rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[45rem] md:-ml-4 lg:-ml-0" width="1000" height="500">
    </div>
  </div>
</div>

<div class="overflow-hidden bg-base-100 py-24 sm:py-32">
  <div class="mx-auto max-w-7xl px-6 lg:px-8">
    <div class="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
      <div class="lg:pr-8 lg:pt-4" style = 'display: flex; flex-flow: column wrap;place-content: center; justify-content: center; flex-direction: column; flex-wrap: nowrap;'>
        <div class="lg:max-w-lg">
          <h2 class="text-base font-semibold leading-7 text-green-600" style = "font-size: 24px;">Learn Effectively</h2>
          <p class="mt-2 text-3xl font-bold tracking-tight text-white-900 sm:text-4xl">Structured Roadmap</p>
          <p class="mt-6 text-lg leading-8 text-white-600" style = 'font-size: 22.5px'>Learn and practice problems in a structured way.</p>
        </div>
      </div>
      <img src="/image.png" alt="Product screenshot" class="w-[30rem] max-w-none rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[45rem] md:-ml-0 lg:-ml-10" width="1000" height="500">
    </div>
  </div>
</div>

<div id = "reviews" class="carousel carousel-center p-4 space-x-4 bg-neutral rounded-box" style = "width: 50vw; margin-left: 25vw; height: 30vw;min-width:350px;min-height:200px">
  <div class = 'carousel-item'>
    <div class="card lg:card-side bg-base-100 shadow-xl" >
      <div class="card-body" style = "width: 48vw ">
        <p style = 'font-size: 28px; height:1vw'>"An immersive platform that seamlessly guides your coding journey while offering thrilling challenges, ensuring continuous growth and excitement."</p>
        <div align = 'right'>
          <div class="w-24 mask mask-squircle" >
            <img src="man2.jpg" height = '200' width = '200'alt = 'Paul Eduardo'>
          </div>
          <p style = 'font-size: 28px; ;'>-Paul Eduardo</p>
        </div>        
      </div>
    </div>
  </div>
  <div class = 'carousel-item w-full' id = 'i2'>
    <div class="card lg:card-side bg-base-100 shadow-xl" >
      <div class="card-body" style = "width: 48vw ">
        <p style = 'font-size: 28px; height:1vw'>"A fantastic platform that revolutionizes the way we approach coding, offering insightful roadmaps and engaging challenges."</p>
        <div align = 'right'>
          <div class="w-24 mask mask-squircle">
            <img src="man1.png" alt = 'Mark Chase' height = '200' width = '200'>
          </div>
          <p style = 'font-size: 28px; text-align: right;'>-Mark Chase</p>
        </div> 
      </div>
    </div>
  </div>
  <div class = 'carousel-item w-full' id = 'i3'>
    <div class="card lg:card-side bg-base-100 shadow-xl" >
      <div class="card-body" style = "width: 48vw ">
        <p style = 'font-size: 28px; height:1vw'>"A fantastic platform that revolutionizes the way we approach coding, offering insightful roadmaps and engaging challenges."</p>
        <div align = 'right'>
          <div class="w-24 mask mask-squircle">
            <img src="woman1.jpeg" alt = 'Great Thomas' height = '200' width = '200'>
          </div>
          <p style = 'font-size: 28px; text-align: right;'>-Greta Thomas</p>
        </div> 
      </div>
    </div>
  </div>
</div>

<div class="flex justify-center w-full py-2 gap-2" style = 'height: 5vw'>
  <a href="#i1" class="btn btn-xs">1</a> 
  <a href="#i2" class="btn btn-xs">2</a> 
  <a href="#i3" class="btn btn-xs">3</a> 
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
<style>
  @media only screen and (max-width: 600px) {
  #canvas3{
    display: none !important;
  }
  #reviews{
    display: none !important;
  }
}
</style>
<!-- <style>
  .Carousel{
    animation: carousel 10s linear infinite;
    display: flex;
    flex-wrap: nowrap;
    width: calc(90vw);
    /* overflow: hidden; */
}
.Block{
    flex-shrink: 0;
    width: 48vw;
}
@keyframes carousel{
    0%   { transform: translate3d(0, 0, 0); }
    100% { transform: translate3d(calc(3 * -48vw), 0, 0); }
}
</style> -->