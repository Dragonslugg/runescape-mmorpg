# server/KingdomManager.py

class Region:
    def __init__(self, name, allegiance=None, modifiers=None):
        self.name = name
        self.allegiance = allegiance  # e.g., "Red Faction", "Blue Faction"
        self.modifiers = modifiers or {}  # e.g., {"xp_bonus": 0.10}

class KingdomManager:
    def __init__(self):
        self.regions = {}  # region_name -> Region
        self.player_zones = {}  # player_id -> region_name

    def add_region(self, name, allegiance=None, modifiers=None):
        self.regions[name] = Region(name, allegiance, modifiers)

    def set_player_region(self, player_id, region_name):
        if region_name in self.regions:
            self.player_zones[player_id] = region_name

    def get_region_for_player(self, player_id):
        return self.regions.get(self.player_zones.get(player_id))

    def get_effects_for_player(self, player_id):
        region = self.get_region_for_player(player_id)
        return region.modifiers if region else {}