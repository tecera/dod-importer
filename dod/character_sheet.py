import base64
from pathlib import Path
from typing import Union, cast

import jsonpickle
from utils import PublicState


class CharacterSheet(PublicState):
    def __init__(self, character_json: str):
        self.__input: str = character_json

    @property
    def input(self):
        return self.__input

    @staticmethod
    def from_base64(b64_string: str):
        str_input = base64.b64decode(b64_string).decode("utf-8")
        return CharacterSheet(str_input)

    @staticmethod
    def from_file(file: Union[str, Path]):
        if isinstance(file, str):
            file = Path(file)
        file = cast(Path, file)
        with file.open("r") as f:
            input_text = f.read()
            return CharacterSheet.from_base64(input_text)

    def export(self, as_base64: bool = True):
        pickled = jsonpickle.encode(self, unpicklable=False)
        if as_base64:
            return base64.b64encode(pickled)
        return pickled
