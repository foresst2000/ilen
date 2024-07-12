# slen
A basic module for Python that is an alternative to ``len()``. Rather then returning the full length of the table, 
it returns the location of the last item in that table.

## Usage
```py
from slen import slen

slen("hello world!") # 11
slen([1, 5, 7, 2, 9, 31, 5]) # 6
slen() # 0
```