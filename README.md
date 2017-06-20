# Task 1
Sometimes we need a "rocket science" script. We need to parse log of satellite orbital lauches /space/log/launch.html).

Write a function group_by(stream, field, success=None) which will parse stream object, aggregate count by field, filter if launch succeeded (or not) and return dict of aggregations.

## Inputs
* stream - stream object like from open
* field - "year" or "month"
* success - None (don't filter) , True (success), False (failed) - please use column Suc

## Output
dict with format {FIELD: int}

## Example
    In [3]: group_by(open("launchlog.txt"), 'year')
    Out[3]: {
    '1957': 4,
    '1958': 28,
    '1959': 31,
    '1960': 66,
    …
    }
    In [4]: group_by(open("launchlog.txt"), 'month', success=False)
    Out[4]: {
    'Apr': 940,
    'Aug': 847,
    …
    }
    
    
# Task 2
Write a method calculating damage done by a spell of the famous polish wizard.
Eg. https://www.youtube.com/watch?v=XkeVYHJ6AG8 - 'fejejeeaindaiyaiai'
Spell consists of subspells. Each subspell add points of damage respectively:
'fe' - 1
'je' - 2
'jee' - 3
'ain'- 3
'dai'- 5
'ne' - 2
'ai'- 2

Spell start with 'fe' and end with 'ai'. Spell body can have subspells or other letters, but every single letter (not in a subspell) decrease damage of
spell by 1 point. 'fe' can occur only once and 'ai' always end the spell. If you can use different sets of subspells in spell, choose the one with the
biggest damage (in example fedaineai: fe-dai-ne-ai: 2+5+2+2, not fe-d-ain-e-ai 2-1+3-1+2).
Method should return 0 if damage is negative or if spell is incorrect.

    def damage(spell):
    """
    Function calculating damage
    :param str spell: string with spell
    :rtype: int
    :return: points of damage
    """
    pass
