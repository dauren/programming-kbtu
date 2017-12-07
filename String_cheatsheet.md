Cases
-------
`s.lower()` Lowercase s # 'HELLO' => 'hello'
`s.upper()` Uppercase s # 'hello' => 'HELLO'
`s.islower()` Return true if s is lowercase
`s.istitle()` Return true if s is titlecased # 'Hello World' => true
`s.isupper()` Return true if s is uppercase

Sequence Operations
---------------------
`s2 in s` Return true if s contains s2
`s + s2` Concat s and s2
`len(s)` Length of s
`s2 not in s` Return true if s does not contain s2
`s[index]` Character at index of s
`s[i:j:k]` Slice of s from i to j with step k
`s.count(s2)` Count of s2 in s

Find / Replace
----------------
`s.index(s2, i, j)` Index of first occurrence of s2 in s after index i and before index j
`s.find(s2)` Find and return lowest index of s2 in s
`s.replace(s2, s3)` Replace s2 with s3 in s
`s.replace(s2, s3, count)` Replace s2 with s3 in s at most count times
`s.rfind(s2)` Return highest index of s2 in s

Inspection
----------
`s.isalnum()` Return true if s is alphanumeric
`s.isalpha()` Return true if s is alphabetic
`s.isdecimal()` Return true if s is decimal
`s.isnumeric()` Return true if s is numeric
`s.startswith(s2)` Return true is s starts with s2
`s[i:j]` Slice of s from i to j
`s.endswith((s1, s2, s3)`) Return true if s ends with any of string tuple s1, s2, and s3
`s.isdigit()` Return true if s is digit

Splitting
-----------
`sep.join(s)` Return s joined by sep
`s.split(sep)` Return list of s split by sep
