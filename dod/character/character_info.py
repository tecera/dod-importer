from .base_character import BaseCharacter

NAME = "name"
CUSTOM_SKILS = "customSkills"
LANGUAGES = "languages"
KEYWORDS = "keywords"
ASCENSION_PACKAGES = "ascensionPackages"
OBJECTIVES = "objectives"
OBJECTIVE_ARCHIVED = "objectiveArchived"
SPECIES = "species"
FACTION = "faction"
ARCHETYPE = "archetype"
BACKGROUND = "background"
ASSETS = "assets"
FLUFF = "fluff"


class CharacterInfo(BaseCharacter):
    def __init__(self, character_json: str):
        self.name: str = character_json[NAME]
        self.custom_skills: list = character_json[CUSTOM_SKILS]
        self.languages: list = character_json[LANGUAGES]
        self.keywords: list = character_json[KEYWORDS]
        self.ascension_packages: list = character_json[ASCENSION_PACKAGES]
        self.objectives: list = character_json[OBJECTIVES]
        self.objectives_archived: bool = character_json[OBJECTIVE_ARCHIVED]
        self.species: dict = character_json[SPECIES]
        self.faction: dict = character_json[FACTION]
        self.archetype: dict = character_json[ARCHETYPE]
        self.background: dict = character_json[BACKGROUND]
        self.assets: dict = character_json[ASSETS]
        self.fluff: dict = character_json[FLUFF]

    def dict(self):
        return {
            NAME: self.name,
            CUSTOM_SKILS: self.custom_skills,
            LANGUAGES: self.languages,
            KEYWORDS: self.keywords,
            ASCENSION_PACKAGES: self.ascension_packages,
            OBJECTIVES: self.objectives,
            OBJECTIVE_ARCHIVED: self.objectives_archived,
            SPECIES: self.species,
            FACTION: self.faction,
            ARCHETYPE: self.archetype,
            BACKGROUND: self.background,
            ASSETS: self.assets,
            FLUFF: self.fluff,
        }

    def __repr__(self):
        return f"CharacterInfo(name={self.name})"
