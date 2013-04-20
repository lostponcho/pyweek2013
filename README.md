Underworld Kerfuffle
====================

Entry in PyWeek 16 (2013)

URL: http://www.pyweek.org/e/underworldwar/

Members: vwood <vwood.org@gmail.com>, mieponcho

License: see LICENSE.txt (except the font, which has its own license)


DONE
----

* Collisions with tile layer (no more weird diagonal wall walking.)

* Camera follows player, and tile layer

* Store entities in data structures

* Better API for drawing to the map
  - Lines (such that they will block movement)
  - mini tilesets (like floor tiles, themes, wall tiles...) to generate a circle of tiles from a mini tileset  

* Entities
  - Separate sprites into collision and drawing sprites (Pygame uses the same Rect for both, which sucks)

* Level Generation
  - Tile fixing according to rules (for wallsets and door direction, etc.)
    - Generation should just use a basic member of each wall type, and this pass would fix the edges


TODO
----

* Entity Lists based on collision/update type

* Level Generation
  - Generate from a tree structure (containing points where the areas should be generated)
  
* Terrain manipulation
  - Digging dirt
  - Opening/Closing doors
  
* AI
  - Currently just a draft of behaviours
  - Need queries of entity lists (i.e. nearest enemy, etc.)
    - Need this for AoE stuff as well
  - Find an openspace (for summoning) (could just be a 'if the random space is blocked, don't summon)
  
* Gameplay
  - Player switching to control different entities
  - Shooting
  
* Triggered boss fight (allows for a proper ending)
  - mid way mini boss fight
  - come with entourage?
  - summon help
  - Based on level scripts (i.e. behaviour with a test)

* Split the level into branches
  - non-linear progression
  - rewards for finishing a branch
