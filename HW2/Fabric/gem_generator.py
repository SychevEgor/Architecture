from item_fabric import ItemFabric
from gem_reward import GemReward


class GemGenerator(ItemFabric):
    def create_item(self):
        return GemReward()
