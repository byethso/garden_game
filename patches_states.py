from enum import Enum

class PatchesStates(str, Enum):
    EMPTY = 'empty'
    HOED = 'hoed'
    GROWING = 'growing'
    HARVESTED = 'harvested'
    HOED_SEEDED = 'hoed_seeded'
    HOED_WATERED = 'hoed_watered'
    HOED_WATERED_SEEDED = 'hoed_watered_seeded'
