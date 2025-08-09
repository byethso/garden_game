from game.tools.tool_type import ToolType
from game.tools.tools import Tools


class Hoe(Tools):
    def __init__(self, x, y, size, images):
        super().__init__(x, y, size, images, ToolType.HOE)
