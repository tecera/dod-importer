from .base_character import BaseCharacter

ATTRIBUTES = "attributes"
SKILLS = "skills"


class CharacterStats(BaseCharacter):
    def __init__(self, character_json: str):
        self.attributes: dict = character_json[ATTRIBUTES]
        self.skills: dict = character_json[SKILLS]

    def dict(self):
        return {ATTRIBUTES: self.attributes, SKILLS: self.skills}

    def __repr__(self):
        skills = [k for k, v in self.skills.items() if v > 0]
        return (
            "CharacterStats("
            + f"attributes={self.attributes.values()}, "
            + f"skills={skills}"
            + ")"
        )
