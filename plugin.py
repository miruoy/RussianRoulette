###
# RussianRoulette — a roulette game with randomized, configurable phrases.
#
#   russianroulette   Spins the cylinder (1/6 chance of BANG). On BANG, a
#                      random phrase from phrases.json "bang" list is shown;
#                      otherwise a random phrase from the "safe" list.
#
# All phrases come from a LOCAL file (phrases.json) — no network access, no
# shell, so unregistered users can play safely.
###
import os
import json
import random

import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring
_ = PluginInternationalization('RussianRoulette')


def _load_phrases():
    """Load phrases.json from the plugin directory. Returns dict or {'__error__': ...}."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'phrases.json')
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        out = {}
        for key in ('bang', 'safe'):
            val = data.get(key)
            if isinstance(val, (list, tuple)):
                out[key] = [str(x).strip() for x in val if x]
        return out
    except (OSError, ValueError) as e:
        return {'__error__': str(e)}


class RussianRoulette(callbacks.Plugin):
    """Russian roulette with randomized, configurable phrases."""

    threaded = True
    priority = 100

    @internationalizeDocstring
    def russianroulette(self, irc, msg, args):
        """takes no argument

        Spins the cylinder. 1 in 6 chance of BANG (a random bloody phrase
        from phrases.json); otherwise a random 'safe' phrase. The phrases
        are configurable — edit phrases.json in the plugin directory.
        """
        phrases = _load_phrases()
        if '__error__' in phrases:
            irc.error(_('Failed to load phrases.json: %s') % phrases['__error__'], Raise=True)
        if not phrases.get('bang') or not phrases.get('safe'):
            irc.error(_('phrases.json needs non-empty "bang" and "safe" lists.'), Raise=True)

        if random.randint(1, 6) == 1:
            line = random.choice(phrases['bang'])
            irc.reply(line)
        else:
            line = random.choice(phrases['safe'])
            irc.reply(line)

    russianroulette = wrap(russianroulette)


Class = RussianRoulette

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
