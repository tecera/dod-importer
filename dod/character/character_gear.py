from .base_character import BaseCharacter

PSYCHIC_POWERS = "psychicPowers"
MUTATIONS = "mutations"
ENHANCEMENTS = "enhancements"
WARGEAR = "wargear"
TALENTS = "talents"


class CharacterGear(BaseCharacter):
    def __init__(self, character_json: str):
        self.enhancements: list = character_json[ENHANCEMENTS]
        self.mutations: list = character_json[MUTATIONS]
        self.psychic_powers: list = character_json[PSYCHIC_POWERS]
        self.talents: list = character_json[TALENTS]
        self.wargear: list = character_json[WARGEAR]

    def dict(self):
        return {
            ENHANCEMENTS: self.enhancements,
            MUTATIONS: self.mutations,
            PSYCHIC_POWERS: self.psychic_powers,
            TALENTS: self.talents,
            WARGEAR: self.wargear,
        }

    def __repr__(self):
        return (
            "CharacterGear("
            + f"enhancements=len({len(self.enhancements)}), "
            + f"mutations=len({len(self.mutations)}), "
            + f"psychic_powers=len({len(self.psychic_powers)}), "
            + f"talents=len({len(self.talents)}), "
            + f"wargear=len({len(self.wargear)})"
            + ")"
        )
