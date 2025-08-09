# garden_game
Garden game with growing carrots

Libraries: pygame, enum

**How to play:** for growing a carrot, you need to hoe patch first, then watered and seeded(no matter in what order), then wait for 10 sec and pick up carrot using glove.
Patch is ready for new seed!

When you choose tool, you'll see a frame around tool. It means you'll work exactly with this thing. If you interact with patch with wrong tool for its state, the frame will disappear. For example,* you can't seed until patch is hoed.*

Patch states: empty, hoed, hoed_watered, hoed_seeded, hoed_watered_seeded, growing, harvested

