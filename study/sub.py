import re

# Inserts a dash between odd numbers
def insert_dash(num):
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))

print(insert_dash(123455567))

# Notes
# re.sub(regex, new_string, string_to_be_processed)

# r'string' is Python's raw string notation
# This allows you to use backslashes (Python doesn't recognize backslashes)
# General rule: use raw strings for all regular expression strings

# '?=' is a lookahead assertion that cbecks for a pattern further along
# NB: a negative lookahead is '?!'

# r'\1-' adds a hyphen after the first capture group
# this in addition to using a lookahead eliminates the problem of changing
# the next digit to a hyphen
