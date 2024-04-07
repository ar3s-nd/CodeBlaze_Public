
# ![Codeblaze](https://github.com/ar3s-nd/CodeBlaze_Public/assets/64828294/b65b474a-943a-4135-81e9-1d444ead0698)
An All-Feature integrated platform where coders across the learning curve, can learn, hone their skills, and test themselves.  
🌐 Live at: [CodeBlaze](https://code-blaze.netlify.app)
## Tech Stack
![Svelte](https://img.shields.io/badge/svelte-%23f1413d.svg?style=for-the-badge&logo=svelte&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![DaisyUI](https://img.shields.io/badge/daisyui-5A0EF8?style=for-the-badge&logo=daisyui&logoColor=white)
![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Netlify](https://img.shields.io/badge/netlify-%23000000.svg?style=for-the-badge&logo=netlify&logoColor=#00C7B7)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)

## Problem Statement
The absence of an online coding platform featuring 1v1 duels deprives learners of a dynamic environment where they can apply their coding skills under time constraints, hindering their ability to experience real-time problem-solving and competitive learning opportunities.

## Features
#### Dashboard (/dashboard)
- Top 10 players and their points on the global leaderboard.
- Graphical representation of different types of Submissions made by the user, (AC, WA, TLE, RE, CE)
- Latest 10 recently accepted problems. 
- Graphical representation of the growth of points. 

#### Roadmap (/roadmap)
- List of subtopics/problem_sets.

#### Problem Sets (/problem_set)
- List of documentation/ reading material, and coding problems along with their difficulty, and solved status. 

#### Practice problem (/problem)
- View Problem description, past submissions, solution of the problem. 
- Ability to edit and submit code in C++, Python from the browser itself. 
- See if the made submission is correct(AC), incorrect(WA), took a lot of time(TLE), Compilation error (CE), Runtime error (RE).

#### 1v1 Duel (/1v1)
- Provides two modes, Private and Blind(public)
- In Private, one can generate a code, and invite his/her friends to a duel.
- In Blind, one can do a live duel, from anyone in the world at random. 
- Both modes have options of selecting max time , and selecting problem categories (refered as tags) and the two players who are of similar level and have selected the same options are matched. 
- On starting a live duel, the two people are given the same problem, and the one who completes it fastest in the time allotted, else the match timesout. 



## Installation and Deployment

1. Download this github repository as ZIP, Extract the zip file. 
2. Create a new database inside a new project in supabase with schema as mentioned in the `(schema.png)` image in the `supabase-functions` directory. 
3. Keep note of three things, the anon api key, the service_role api key, and the url. 
4. In the backend `reel.py` file change the two variables at the top with the service_role api key and the url.
5. In the frontend, use the command `npm install` to install all dependencies, then create a new `.env` file with the following things
```
VITE_SUPA_URL=url
VITE_SUPA_ANON_PUB=anon api key
```
6. Type the command `npm run dev` and also run the python script `python reel.py`
7. The website will be live on `localhost:5173`. 
## Applications
1. Education - The curated roadmaps provides the best learning experience for beginners in coding.
2. Coding Competitions - The 1v1 duels feature can be utilized for coding competitions or friendly matches. 
3. Skill assessment: Employers can use the platform to get more knowledge on their potential recruit's coding skills. The users get more understanding on the topics they need to improve to build their coding skills.
4. Network building: it allows for coding enthusiasts from all over the world to connect with each other.

## Further Improvements
1.	Personalized Learning path and problem sets depending on the current activities of the user, identifying their weak and strong points.
2.	Live intractability between competitors in 1v1, through chat, powerups, etc
3.	Include hints for each problem, which progressively reveal the solution.
4.	Give the user options to chose from a vide range of themes on the website.

## Contributors
With ❤️ By Team "Muralidhara Fan Boys"
- Pramatha V Rao
- R Ricky Roger
- Navaneeth D
