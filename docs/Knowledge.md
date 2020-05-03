# What needs to be planned in advance? #

The story, theme and setting. These determine practically everything. 
The world. How it will look. How big it will be. 
The terrain (e.g. town, wilderness, dungeons, special places...) 
The Scheduling system (eg, how turns and speed work, whether and how actions can be interrupted by other actions, etc). 
The items. Major categories (e.g. weapons, armour, potions, scrolls, food...). Leave detail (e.g. how much the minor healing potion heals you by) for later. Think about how the items will be used and by whom. Plan the basic rules (e.g. you can only wield 2 weapons if you are a fighter, you need space for arrows if you equip a bow, how many rings can someone wear, etc). 
The magic system. Spell types. Who uses spells and when. How you learn spells. What they cost. Which classes can use them. How to implement permanent spells (e.g. enchantments that last, like recharging a staff). 
Shopping. If your game will have shops, how will they work? Will the Player be able to rob them? If so how does that work? 
Interaction with other creatures (maybe negotiating your way out of battles?). 
Saving and restoring games Level loading system. 
Win Conditions How to finish the game and what happens when you do. 

 [Сюжет](https://ru.wikipedia.org/wiki/%D0%A1%D1%8E%D0%B6%D0%B5%D1%82)

The term "plot" in RPGs refers to the background of the game and the events that guide the player. Almost all roguelikes have some sort of plot.

Contents [hide] 

1. Theme
2. Background
3. Story
4. Player Narrative
5. Narrative
6. See also

### Theme ###

This is the least specific plot. A background is not explicitly given, but the game features, such as monsters and items, are often related to each other somehow. A fantasy theme, for example, tends to have magic and melee weapons, along with kings, castles, dwarves, elves, and other mythical elements. Most roguelikes use a fantasy theme, but a few have a futuristic theme.

### Background ###

A background gives the player a goal. Often there is no specific story or events to follow, and the player is free to do whatever he feels necessary to achieve the goal. Almost every game has a background, but very few plots stop there.

### Story ###

A story builds upon a background by affecting the player in some way. The player will have to complete certain preset tasks before he can accomplish the goal. However, aside from a few parts of the game, the player is largely responsible for his fate and determines how he will go about doing things.

### Player Narrative ###

The game has a story, but now the player is restricted in the choices he makes. At several points in the game, the player is given a set of options; his choice determines the part of the storyline he must complete next. The game has many preset paths, and the player's choices only minimally affect how the game must be played.

### Atmosphere ### 

Atmosphere, (noun): the psychological environment, the feeling and tone created by something. The atmosphere in roguelikes varies. In Angband it is often dark and desperate, because you're kilometers under the earth with a failing source of light, near death and with no way to escape your foes. In NetHack, it is quite challenging but somewhat humorous. 

How do you create a monster AI?
AI (artificial intelligence) is not so easy to create. There is several different techniques you might want to use.

State machines are probably the easiest way to do AI. Firstly, get a piece of paper. Then write a set of states (e.g. attacking, walking somewhere, running away, stealing), circle those states, and draw arrows (with directions) from each state to every state you can get to from that state. These arrows are called transitions. Label each transition with the circumstances under which it occurs.

Of course, it would be a lot more complicated. There is far more decisions to be made, and there is more actions (one for each item / spell). Now how do you implement this? Instead of using the usual massive nested "if" or "switch" statement, you make a 2 dimensional array, with the number of states being its width and height. This is the state transition table.

TODO: table

You keep a variable with each monster that tells you which state it is in. This tells you about the row of the state transition table. You then go through that row, and run tests to see if the circumstances in it are fulfilled. If they are, pick the one with the highest priority, and switch to that state. For instance, you are in the "ATTACK" state. Look in the left-most column for "ATTACK" (it's at the top). Right, now look along the row. Under the first column ("ATTACK") there is a blank space, so there is nothing to check there. Under the "APPROACH" column there is "Player runs away". Say that is true - the player is leaving. Under the "RUN" column there is "Likely to die". Say that is also true - the monster is badly hurt. The monster's life takes priority over the player's pursuit, so the state machine switches to the "RUN" state (you could of course make the monster's life less important :-). Behavior is then based on the states. This is also where big "if" statements can come in. If you want to avoid them, use function pointers as well in your state transition table, and make a function for each action / state. 

State machines are very good, and unlike a quick AI you make using hacks, they stand up well to difficult situations and don't require a lot of processing or calculation. They are used in many programming situations, so it is worthwhile to learn them. 

Battle

Basically, combat works like this. Everybody gets a certain number of turns, they do what they think will inflict the most damage on their opponent while minimising their own damage taken. Damage is inflicted with weapons, and it is reduced (or blocked entirely) with armor. 

The point of combat is very simple. Kill as many opponents as possible while staying alive yourself. When do you die? Every roguelike (and most other games) I've seen use a "hit point" (or "health point") rating, abbreviated HP. You have a certain amount of HP, and a maximum. The maximum grows when you reach the next level, and the current HP grows when you rest/drink healing potions/use healing spells and so on. When your current HP is maxed out, you are completely healthy. When it drops to 0, you are dead. Damage reduces it by the amount of damage taken, and healing increases it by the amount of health points gained. How do you calculate this? Instead of the slow and problematic way of checking overflows like roguelikes usually do it, do this: When a hit occurs: If the damage is greater than or equal to the current HP, the HP drops to zero and you die. Otherwise subtract the damage from the current HP. When you are healed: If the health gained is greater than the difference between your maximum and your current HP, your current HP takes on the value of the maximum HP. Otherwise, you add the health gained to the current HP.

When you process monsters, the monster AI decides what action to take.

Taken from [Roguebasin](http://www.roguebasin.com/)
