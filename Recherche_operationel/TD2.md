---
layout: default
nav_order: 6
title: TD2
parent: Recherche operationel
---
<link rel="stylesheet" href="../assets/css/gantstyle.css">


3) le chemin critique est le cehmine qui fait A->F->G

5) Les marges totales:
   - A = 0
   - B = 1
   - C = 3
   - D = 1
   - e = 2
   - f = 0
   - g = 0

<div id="cbwrap">
  <!-- (X) NOT IMPORTANT -->
  <h1 id="cbtitle">Pure HTML CSS Gantt Chart</h1>
  
  <div class="gantt">
    <!-- (A) FIRST ROW : DAYS -->
    <div class="head">1</div> <div class="head">2</div>
    <div class="head">3</div> <div class="head">4</div>
    <div class="head">5</div> <div class="head">6</div>
    <div class="head">7</div> <div class="head">8</div>
    <div class="head">9</div>
    <!-- (B) FOLLOWING : TASKS -->
    <div style="background: #ffdddd; grid-row: 2; grid-column: 1 / span 2">
      1
    </div>
    <div style="background: #d6ffd8; grid-row: 3; grid-column: 3 / span 3">
      2
    </div>
    <div style="background: #e2e5ff; grid-row: 4; grid-column: 5 / span 3">
      3
    </div>
  </div>

</div>