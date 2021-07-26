from .base_character import BaseCharacter

MAX_WOUNDS = "maxWounds"
MAX_SHOCK = "maxShock"
WEALTH = "wealth"
WRATH = "wrath"
FAITH = "faith"
RELOADS = "reloads"
DEFIANCE = "defiance"


class CharacterTrackers(BaseCharacter):
    def __init__(self, character_json: str):
        self.max_wounds: dict = character_json[MAX_WOUNDS]
        self.max_shock: dict = character_json[MAX_SHOCK]
        self.wealth: dict = character_json[WEALTH]
        self.wrath: dict = character_json[WRATH]
        self.faith: dict = character_json[FAITH]
        self.reloads: dict = character_json[RELOADS]
        self.defiance: dict = character_json[DEFIANCE]

    def dict(self):
        return {
            MAX_WOUNDS: self.max_wounds,
            MAX_SHOCK: self.max_shock,
            WEALTH: self.wealth,
            WRATH: self.wrath,
            FAITH: self.faith,
            RELOADS: self.reloads,
            DEFIANCE: self.defiance,
        }

    def __repr__(self):
        return (
            "CharacterTrackers("
            + f"wealth={self.wealth}, "
            + f"wrath={self.wrath}, "
            + f"faith={self.faith}"
            + ")"
        )
