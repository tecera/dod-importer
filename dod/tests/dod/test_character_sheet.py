import base64
import json
import unittest
from pathlib import Path

from dod import CharacterSheet


class TestCharacterSheet(unittest.TestCase):
    def setUp(self):
        self.file = Path(__file__).parent / "test_char.b64"
        self.maxDiff = None  # pylint ignore: C0103

    def test_create_from_file(self):
        file_character = CharacterSheet.from_file(self.file)

        with self.file.open("r") as f:
            text = f.read()

        b64_character = CharacterSheet.from_base64(text)

        self.assertEqual(file_character, b64_character)

    def test_export(self):
        file_character = CharacterSheet.from_file(self.file)
        export = file_character.export(False)
        with self.file.open("r") as f:
            text = f.read()

        str_character = base64.b64decode(text).decode("utf-8")

        self.assertEqual(json.loads(export), json.loads(str_character))
