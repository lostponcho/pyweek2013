Underworld Kerfuffle
====================

Created for pyweek 2013

DONE
----

* Collisions with tile layer (no more weird diagonal wall walking.)
* Camera follows player, and tile layer

TODO
----

* Store entities in data structures
  - Lists based on collision/update type

* Level Generation
  - Better API for drawing to the map
  - More tools:
    - Lines (such that they will block movement)
    - Generate from a tree structure (containing points where the areas should be generated)
    - mini tilesets (like floor tiles, themes, wall tiles...) to generate a circle of tiles from a mini tileset
  - Tile fixing according to rules (for wallsets and door direction, etc.)
    - Generation should just use a basic member of each wall type, and this pass would fix the edges
  
* Terrain manipulation
  - Digging dirt
  - Opening/Closing doors
  
* Entities
  - Separate sprites into collision and drawing sprites (Pygame uses the same Rect for both, which sucks)
  
* AI
  - Currently just a draft of behaviours
  - Need queries of entity lists (i.e. nearest enemy, etc.)
    - Need this for AoE stuff as well
  - Find an openspace (for summoning) (could just be a 'if the random space is blocked, don't summon)
  
* Triggered boss fight (allows for a proper ending)
  - mid way mini boss fight
  - come with entourage?
  - summon help
  - Based on level scripts (i.e. behaviour with a test)

* Split the level into branches
  - non-linear progression
  - rewards for finishing a branch
