from .base_character import BaseCharacter

ID = "id"
VERSION = "version"
SETTING_SELECTED = "settingSelected"
SETTING_TIER = "settingTier"
SETTING_TITLE = "settingTitle"
SETTING_HOMEBREW = "settingHomebrewContent"
SETTING_HOUSERULES = "settingHouserules"
CUSTOM_XP = "customXp"
CUSTOM_RANK = "customRank"


class CharacterMeta(BaseCharacter):
    def __init__(self, character_json: str):
        self._id: str = character_json[ID]
        self.version: int = character_json[VERSION]
        self.setting_selected: bool = character_json[SETTING_SELECTED]
        self.tier: int = character_json[SETTING_TIER]
        self.title: str = character_json[SETTING_TITLE]
        self.homebrew_content: list = character_json[SETTING_HOMEBREW]
        self.houserules: dict = character_json[SETTING_HOUSERULES]
        self.custom_xp: str = character_json[CUSTOM_XP]
        self.custom_rank: str = character_json[CUSTOM_RANK]

    def dict(self):
        return {
            ID: self._id,
            VERSION: self.version,
            SETTING_SELECTED: self.setting_selected,
            SETTING_TIER: self.tier,
            SETTING_TITLE: self.title,
            SETTING_HOMEBREW: self.homebrew_content,
            SETTING_HOUSERULES: self.houserules,
            CUSTOM_XP: self.custom_xp,
            CUSTOM_RANK: self.custom_rank,
        }

    def __repr__(self):
        return (
            "CharacterMeta("
            + f"version={self.version}, "
            + f"tier={self.tier}, "
            + f"custom_xp={self.custom_xp}, "
            + f"custom_rank={self.custom_rank}"
            + ")"
        )
