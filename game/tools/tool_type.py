from enum import Enum

class ToolType(str, Enum):
    GLOVE = 'glove'
    HOE = 'hoe'
    SEED = 'seed'
    WATERING_CAN = 'watering_can'
