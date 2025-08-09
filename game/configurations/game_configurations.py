from game.configurations.object_configurations import ObjectConfiguration


class GameConfigurations():
    def __init__(self):
        self.patch = ObjectConfiguration(210, 110, 120, 30)
        self.hoe = ObjectConfiguration(640, 210, 100, 0)
        self.glove = ObjectConfiguration(640, 350, 100, 0)
        self.seed = ObjectConfiguration(100, 210, 100, 0)
        self.watering_can = ObjectConfiguration(100, 350, 100, 0)