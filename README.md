# RussianRoulette

A Limnoria plugin that plays Russian roulette with **randomized, configurable
phrases** — safe for **unregistered** users (no shell, no network access).

## Command

| Command | Description |
| --- | --- |
| `russianroulette` | Spins the cylinder (1 in 6 chance of BANG). On BANG, shows a random phrase from the `bang` list in `phrases.json`; otherwise a random phrase from the `safe` list. |

This is a **separate** command from Limnoria's built-in `roulette` (Fun
plugin) — named `russianroulette` so it does not conflict.

## Configuration: phrases.json

Edit `phrases.json` (in this directory) to change the messages. Two lists:

```json
{
  "bang": [
    "BANG! Your brains exit stage left in a fine red mist...",
    "..."
  ],
  "safe": [
    "Click. Empty. You get to keep your head, and the wall stays clean...",
    "..."
  ]
}
```

The shipped file contains 15 bloody (Tarantino-flavoured) `bang` phrases and
15 `safe` phrases, all in English. Add your own — the bot picks one at random
each time, so you never see the same line twice in a row.

## Installation

```bash
cp -r RussianRoulette /path/to/your/bot/plugins/
rm -rf /path/to/your/bot/plugins/RussianRoulette/__pycache__
# in the bot:
load RussianRoulette
```

If you are replacing a previously loaded copy and the bot keeps running old
code, remove the `__pycache__` directory and `touch` the `.py` files (or
unload, delete, re-copy under a new name, then load) before reloading — a
stale `.pyc` will keep the old code live.

## Troubleshooting

- **`Failed to load phrases.json: ...`** — the JSON file is missing or
  invalid. Fix `phrases.json` in the plugin directory.
- **`phrases.json needs non-empty "bang" and "safe" lists.`** — one of the
  two lists is empty. Add at least one phrase to each.
