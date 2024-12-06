# ilen (index-len)
This is a very basic Python module that checks for length of strings and lists like ``len()``, however, it returns the **index of the last item**, rather than the length of the whole table.

## Usage Example
```py
from ilen import ilen

# Get the last item in the table
table_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 01, 11]
table_1_last_item = ilen(table_1) # 11

string_1 = "1 2 3 4 5 6 7 8 9 01 11"
string_1_last_char = ilen(string_1) # 1

print(str(table_1_last_item) + string_1_last_char) # 111
```
