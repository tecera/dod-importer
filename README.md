# README

A library for importing Doctors of Doom characters into Python

It's currently not much more than a glorified base64 to class converter.

A lot of the values are still dicts and list that should be Python classes. But I'll get to that eventually.

For now, manually editing values and then exporting should work correctly. Due to the way that DoD sorts the output the
base64 string that's used as input will not be the same as the one that `CharacterSheet.export` outputs, not much I can do about that.

## Installation

```bash
pip install -e .
```

## Usage

It's all fairly basic at the moment. All attributes names are all directly ported from the DoD export and converted to snake case from pascal case.

```python
>>> from dod import CharacterSheet
>>> character = CharacterSheet.from_base64("{dod_export_string}")
>>> character
CharacterSheet(name=Tecera, tier=2)

>>> character.meta
CharacterMeta(version=11, tier=2, custom_xp=40, custom_rank=2)

>>> character.info
CharacterInfo(name=Tecera)

>>> character.stats
CharacterStats(attributes=dict_values([5, 3, 3, 2, 4, 3, 5]), skills=['athletics', 'awareness', 'ballisticSkill', 'intimidation', 'scholar', 'survival', 'weaponSkill'])

>>> character.powers
CharacterGear(enhancements=len(2), mutations=len(0), psychic_powers=len(0), talents=len(3), wargear=len(7))

>>> character.trackers
CharacterTrackers(wealth={'points': 0, 'spend': 0}, wrath={'points': 2, 'spend': 0}, faith={'points': 0, 'spend': 0})
```

## Contributing

Install the requirements in a virtual environment with `make venv`.

Create a branch or fork the repo.

Add your own code, then check that it doesn't break anything with either `make` or by installing the pre-commit hooks.

Install the pre-commit hooks with `pre-commit install`.

If you add any functionality use unittests to confirm that the functionality works.

Once you have your stuff ready. Make a PR and I'll take a look at it.
