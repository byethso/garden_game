from game.configurations.object_configurations import ObjectConfiguration


class GameConfigurations():
    def __init__(self):
        self.hoe = ObjectConfiguration(560, 220, 70, 0)
        self.patch = ObjectConfiguration(190, 130, 100, 30)
        self.watering_can = ObjectConfiguration(110, 350, 70, 0)
        self.glove = ObjectConfiguration(560, 350, 70, 0)
        self.seed = ObjectConfiguration(110, 220, 70, 0)