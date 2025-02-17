<h1>The Red Show - Adventure Game</h1>

<h2>Languages and Utilities Used</h2>
<ul>
  <li>Java for game logic and functionality</li>
  <li>Console-based UI for text-based gameplay</li>
</ul>

<h2>Description</h2>
The Red Show is a thrilling text-based adventure game that plunges players into a creepy and mysterious circus. As players explore different attractions, they’ll face puzzles, challenges, and encounters that impact their progress and sanity. The goal is to collect keys from each attraction to escape the circus, but players must balance risk and reward as they navigate a world full of eerie surprises.
<br />

<h3>Game Mechanics</h3>
<ul>
  <li><b>Three Main Attractions:</b> Explore the Haunted House, Big Top, and House of Mirrors, each with its own set of puzzles and eerie encounters.</li>
  <li><b>Sanity System:</b> Your character’s sanity is crucial. Every encounter with creepy clowns and failed puzzles drains your sanity. If it hits zero, the game ends.</li>
  <li><b>Movement Choices:</b> Choose between sneaking or running to move to the next attraction. Sneaking minimizes encounters but takes longer, while running speeds things up at the cost of more encounters.</li>
  <li><b>Puzzle Solving:</b> Solve unique puzzles and challenges in each attraction to collect keys necessary for escaping.</li>
  <li><b>Randomized Gameplay:</b> Experience unpredictable gameplay with random elements like the number of turns to reach an attraction and random outcomes from your choices.</li>
</ul>

<h3>Objective</h3>
The primary goal of the game is to collect all the keys from the attractions and escape the circus. Players need to manage their choices carefully to maintain their sanity and overcome the obstacles within each attraction. The game ends when the player either escapes by collecting all the keys or loses all their sanity, leading to a game over.

<p align="center">
<br />
Game Intro: <br/>
<img src="https://i.imgur.com/D4pcAJU.png" height="80%" width="80%" alt="Game Intro"/>
<br />
<br />

<h2>Main Attractions</h2>
<h3>🎫 House of Mirrors</h3>
<p>The attraction features a random mix of riddles and clown encounters. Players must solve riddles to progress while avoiding the disorienting effects of clowns.</p>
<ul>
  <li><b>Riddles:</b> Players encounter mirrors with a riddle, and must provide the correct answer to proceed. If they answer correctly, they feel closer to finding the key. An incorrect answer drains sanity.</li>
  <li><b>Clowns:</b> Random clown encounters reduce the player’s sanity by 2 points.</li>
</ul>

<h4>Key Collection:</h4>
<p>The main objective in this attraction is to find a key by solving riddles and avoiding the sanity-draining effects of the environment. The key is randomly assigned after a correct answer, and the player may not find it after solving a riddle.</p>
<p>Once the key is found, the player regains a 5 points of sanity and proceeds to the next stage.</p>

<h4>Movement and Choices:</h4>
<p>Players can choose from three directions: left, right, or straight. The direction determines the type of encounter that follows. If an invalid direction is chosen, the game prompts the player to make a valid choice.</p>

<h3>🏚 Haunted House</h3>
<p>This attraction features a puzzle that requires arranging a series of paintings in the correct narrative order. The paintings depict stages of a knight’s journey, from setting out on a quest to returning victorious with treasure.</p>

<h4>Attempts:</h4>
<p>The player has three attempts to arrange the paintings correctly. Each incorrect attempt results in a loss of sanity by 2 points.</p>
<p>If the player’s sanity drops to zero due to incorrect attempts and being unable to solve the puzzle, the game ends.</p>

<h4>Correct Order and Randomization:</h4>
<p>The correct order of paintings is predefined and represents a narrative. The paintings are shuffled at the start, creating a puzzle that players must solve. The player is asked to input the correct order of painting numbers.</p>
<p>If the player succeeds in ordering the paintings correctly, they are rewarded with a key, and their sanity is restored by 5 points.</p>

<h4>Gameplay Flow:</h4>
<ul>
  <li>Players are asked to input their guesses one at a time. If they input the correct sequence, they find the key, regain some sanity, and move forward in the game.</li>
  <li>Incorrect orders reduce the number of attempts and sanity. If the player runs out of attempts or loses all sanity, they fail to solve the puzzle and are left in a state of despair.</li>
</ul>

<h3>Big Top:</h3>
<p>The Big Top attraction challenges the player to cross a tightrope to reach a key at the other end. The player must choose from three actions during the tightrope walk:</p>

<h4>Tightrope Walking:</h4>
<p>The player must select from three actions:</p>
<ul>
    <li><b>Hop:</b> Advance quickly, but with a higher risk of losing balance.</li>
    <li><b>Walk:</b> Advance slowly with the least chance of losing balance.</li>
    <li><b>Wait:</b> Stay still to regain balance, but may lead to a clown encounter that drains sanity.</li>
</ul>
  
<b>Balance System:</b> 
<p>The player starts with a balance meter at 5. Each action impacts this balance:</p>
<ul>
    <li><b>Hop:</b> Advances more steps but risks a larger loss of balance.</li>
    <li><b>Walk:</b> Advances slower with a smaller chance of losing balance.</li>
    <li><b>Wait:</b> Regains balance without progressing but may trigger a clown encounter (20% chance), draining 1 sanity.</li>
</ul>

<h4>Steps and Progressions:</h4>
<ul>
    <li>The player must take 15 total steps to reach the key. Each action advances the player by a random amount between 1 and 4 steps.</li>
    <li>Waiting may lead to a clown encounter that causes a 1 point sanity decrease</li>
    <li>If the balance drops to zero, the player falls, losing 3 sanity points and making them leave the attraction.</li>
</ul>

<p>The game ends if the player either successfully crosses the tightrope and collects the key or loses all balance and falls off.</p>
