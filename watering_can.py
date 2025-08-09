from tool_type import ToolType
from tools import Tools


class WateringCan(Tools):
    def __init__(self, x, y, size, images):
        super().__init__(x, y, size, images, ToolType.WATERING_CAN)
