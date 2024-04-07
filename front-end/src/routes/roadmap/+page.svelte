<script>
    import NavBar from "../../components/NavBar.svelte";
    import supabase from "$lib/db"
  import {goto} from "$app/navigation"
  import {session_user,authHandlers} from "$lib/stores"
    import { onMount } from "svelte";
    // import {gsap,Draggable,InertiaPlugin} from "gsap";
  onMount(() => {
  })
  let roadmapArray = [
  {
    'title':'Time Complexity',
    'description':'How to calculate/predict Time complexity of a given algorithm?',
    'difficulty':'Beginner',
    'problem_set':'-1'
  },
  {
    'title':'Sorting and Binary Search',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Beginner',
    'problem_set':'3'
  },
  {
    'title':'Two Pointers and Sliding Window',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Beginner',
    'problem_set':'4'
  },
  {
    'title':'Recursions',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Beginner',
    'problem_set':'-1'
  },
  {
    'title':'Applications of Merge Sort and Quick Sort',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Hashing',
    'description':'Storing Items in a Smaller Space',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Greedy Algorithms',
    'description':'Storing Items in a Smaller Space',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Math and Implementation',
    'description':'Storing Items in a Smaller Space',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Dynamic Programming',
    'description':'Storing Items in a Smaller Space',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Linked Lists',
    'description':'Data Structures',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Stacks and Queues',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Binary Trees, Binary Heaps, and Fibonacci Heaps',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Hardcore',
    'problem_set':'-1'
  },
  {
    'title':'Segment Trees',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Binary Index Trees',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Binary Search Trees and AVL Trees',
    'description':'Various Basic Searching and Sorting Algorithms',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  },
  {
    'title':'Coming Soon.',
    'description':'Many of the roadmap problems sets are incomplete and are being curated. Please wait.',
    'difficulty':'Intermediate',
    'problem_set':'-1'
  }
  ]
</script>
<NavBar></NavBar>
<center><span style="font-size:32px;font-weight:bold">Roadmap</span></center>
<ul style="background-image: linear-gradient(45deg, #00A6B751, #1f2937);" class="timeline timeline-snap-icon max-md:timeline-compact timeline-vertical">
  {#each roadmapArray as set_ ,i(i)}
    <li>
      <div class="timeline-middle">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="h-5 w-5"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z" clip-rule="evenodd" /></svg>
      </div>
      <div class={i%2==0?"timeline-start md:text-end mb-10":"timeline-end mb-10"}>
        <time class="font-mono italic">{i+1}</time>
        <div class="card w-96 bg-base-100 shadow-xl text-black"id="info_card">
          <div class="card-body flex justify-evenly" style="background-image: url('https://img.freepik.com/free-vector/minimalistic-style-abstract-blurred-yellow-gradient-banner-vector_1017-49017.jpg');">
            <h2 style="text-align:center gap: 0.5rem/* 8px */;font-size: 1.25rem/* 20px */;line-height: 1.75rem/* 28px */;font-weight: 600;">
              {set_.title}
            </h2>
            <p>{set_.description}</p>
            <div class="card-actions justify-end">
              <div class="badge badge-outline badge-base-100 text-indigo-950">{set_.difficulty}</div>
              {#if set_.problem_set==-1}
                <div class="badge badge-outline badge-base-100">In Development</div>
              {/if}
            </div>
            <div class="flex justify-evenly">
              <button class="btn btn-primary w-3/5 margin-2 shadow-md shadow-black" on:click={function(){goto("/problem_set/"+set_.problem_set)}}>Learn</button>
              <!-- <button class="btn btn-primary w-2/5 margin-2 shadow-md shadow-black" on:click={function(){goto("/1v1")}}>Compete</button> -->
            </div>
          </div>
        </div>
      </div>
      <hr/>
    </li>
  {/each}
</ul>

<style>
  #info_card
  {
    /* width: 200px;
    height: 200px;
    background-color: lightblue; */
    transition: transform 0.2s ease;
    overflow: hidden;
    position: relative;
  }
  #info_card:hover
  {
    transform: scale(1.05);
  }
</style>