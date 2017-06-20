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
