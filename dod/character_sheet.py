import base64
import json
from pathlib import Path
from typing import Union, cast

from dod.character import (
    CharacterGear,
    CharacterInfo,
    CharacterMeta,
    CharacterStats,
    CharacterTrackers,
)
from dod.character.base_character import BaseCharacter


class CharacterSheet(BaseCharacter):
    def __init__(self, character_json: str):
        self.__input: str = character_json
        self.meta = CharacterMeta(self.input)
        self.info = CharacterInfo(self.input)
        self.stats = CharacterStats(self.input)
        self.gear = CharacterGear(self.input)
        self.trackers = CharacterTrackers(self.input)

    @property
    def input(self):
        return self.__input

    @staticmethod
    def from_base64(b64_string: str):
        str_input = base64.b64decode(b64_string).decode("utf-8")
        character_json = json.loads(str_input)
        return CharacterSheet(character_json)

    @staticmethod
    def from_file(file: Union[str, Path]):
        if isinstance(file, str):
            file = Path(file)
        file = cast(Path, file)
        with file.open("r") as f:
            input_text = f.read()
            return CharacterSheet.from_base64(input_text)

    def export(self, as_base64: bool = True):
        pickled = json.dumps(self.dict())
        if as_base64:
            b64_bytes = base64.b64encode(pickled.encode("utf-8"))
            return str(b64_bytes.rstrip(b"="), "utf-8")
        return pickled

    def dict(self):
        return {
            **self.meta.dict(),
            **self.info.dict(),
            **self.stats.dict(),
            **self.gear.dict(),
            **self.trackers.dict(),
        }

    def __repr__(self):
        return f"CharacterSheet(name={self.info.name}, tier={self.meta.tier})"
