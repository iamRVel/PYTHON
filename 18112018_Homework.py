Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> v1 = 'hello world'
>>> v1
'hello world'
>>> print 'update strings : ',
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('update strings : ', end=" ")?
>>> print 'update string :- ',
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('update string :- ', end=" ")?
>>> print "update string :- ",
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("update string :- ", end=" ")?
>>> print 'Updated string :- ',
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Updated string :- ', end=" ")?
>>> print "Updated string :- ",
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Updated string :- ", end=" ")?
>>> print "Updated String :- ", var1[:6] + 'Python'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Updated String :- ", var1[:6] + 'Python')?
>>> print "Updated String :- ", var1[:4] + 'Python'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Updated String :- ", var1[:4] + 'Python')?
>>> print "Updated String :- ", v1[:6] + 'Python'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Updated String :- ", v1[:6] + 'Python')?
>>> print "Updated String :- ", v1[:5] + 'Python'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Updated String :- ", v1[:5] + 'Python')?
>>> print "Updated String :- ", v1[:4] + 'Python'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Updated String :- ", v1[:4] + 'Python')?
>>> print 'Updated String :- ', v1[:5] + 'Python'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Updated String :- ', v1[:5] + 'Python')?
>>> str.join(sequence)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    str.join(sequence)
NameError: name 'sequence' is not defined
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'v1']
>>> dir(v1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(doc)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dir(doc)
NameError: name 'doc' is not defined
>>> dir('doc')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(join)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dir(join)
NameError: name 'join' is not defined
>>> dir('join')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(join)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    help(join)
NameError: name 'join' is not defined
>>> help('join')
No Python documentation found for 'join'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> $ python test.py
SyntaxError: invalid syntax
>>> python test.py
SyntaxError: invalid syntax
>>> v1
'hello world'
>>> v1 * 2
'hello worldhello world'
>>> v1
'hello world'
>>> v1 + 'CHITTI'
'hello worldCHITTI'
>>> var1 = 'Hello World!'

print "Updated String :- ", var1[:6] + 'Python'
SyntaxError: multiple statements found while compiling a single statement
>>> var1 = 'Hello World!'
print "Updated String :- ", var1[:6] + 'Python'
SyntaxError: multiple statements found while compiling a single statement
>>> para_str = """this is a long string that is made up of several lines and non-printable characters such as TAB ( \t ) and they will show up that way when displayed. NEWLINEs within the string, whether explicitly given like this within the brackets [ \n ], or just a NEWLINE within the variable assignment will also show up."""
>>> para_str
'this is a long string that is made up of several lines and non-printable characters such as TAB ( \t ) and they will show up that way when displayed. NEWLINEs within the string, whether explicitly given like this within the brackets [ \n ], or just a NEWLINE within the variable assignment will also show up.'
>>> print "My name is %s and weight is %d kg!" % ('Zara', 21)
SyntaxError: invalid syntax
>>> print 'My name is %s and weight is %d kg!' % ('Zara', 21)
SyntaxError: invalid syntax
>>> aa = "_",
>>> seq = ("a","b","c"),
>>> seq
(('a', 'b', 'c'),)
>>> aa.join(seq)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    aa.join(seq)
AttributeError: 'tuple' object has no attribute 'join'
>>> aa = "_";

>>> seq = ("a","b","c");
SyntaxError: multiple statements found while compiling a single statement
>>> aa = "_";
>>> seq = ("a","b","c");
>>> aa.join( seq )
'a_b_c'
>>> aa.join(seq)
'a_b_c'
>>> test =  {'2', '1', '3'}
s = ', '
print(s.join(test))
test = {'2', '5', '10'}
SyntaxError: multiple statements found while compiling a single statement
>>> test1 = {'2', '5', '10'}
>>> s1 = ','
>>> s1.join(test1)
'5,10,2'
>>> t1 = {'rama','sita','ravana'}
>>> n1 = ','
>>> n1.join(t1)
'rama,sita,ravana'
>>> t2 = {'rama','sita','ravana'}
>>> n2 = '->->'
>>> n2.join(t2)
'rama->->sita->->ravana'
>>> test2 = {'mat':1, 'ram':2}
>>> f2 = '->'
>>> f2.join(test2)
'mat->ram'
>>> test3 = {1:'mat', 2:'ram'}
>>> f3 = ','
>>> f3.join(test3)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    f3.join(test3)
TypeError: sequence item 0: expected str instance, int found
>>> test3 = {1:'mat', 2:'ram'}
>>> f3 = '->'
>>> f3.join(test3)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    f3.join(test3)
TypeError: sequence item 0: expected str instance, int found
>>> #str.format examples:
>>> a = ('Hello{}, your balance is {}.'.format('chitti' 789.6790))
SyntaxError: invalid syntax
>>> a = ("Hello{}, your balance is {}.".format('chitti' 789.6790))
SyntaxError: invalid syntax
>>> a = ("Hello{0}, your balance is {1}.". format('chitti' 789.6790))
SyntaxError: invalid syntax
>>> a = ("Hello{}, your balance is {}.".format('chitti' 789))
SyntaxError: invalid syntax
>>> a = ("Hello{}, your balance is {}.".format('chitti', 789.6790))
>>> a
'Hellochitti, your balance is 789.679.'
>>> a = ("Hello {}, your balance is {}.".format('chitti' 789.6790))
SyntaxError: invalid syntax
>>> a = ("Hello {}, your balance is {}.".format('chitti', 789.6790))
>>> a
'Hello chitti, your balance is 789.679.'
>>> a = ("Hello {0}, your balance is {1}.".format('chitti', 789.6790))
>>> a
'Hello chitti, your balance is 789.679.'
>>> y = ("{:5d}".format(12))
>>> y
'   12'
>>> z = ("{:8.3f}".format(12.2346))
>>> z
'  12.235'
>>> gh = ("{:+f} {:+f}".format(12.23, -12.23))
>>> gh
'+12.230000 -12.230000'
>>> string.lstrip([chars])
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    string.lstrip([chars])
NameError: name 'string' is not defined
>>> rs = '             this is good'
>>> rs
'             this is good'
>>> rs.lstrip()
'this is good'
>>> ls = 'Druvan is a baby boy             '
>>> ls
'Druvan is a baby boy             '
>>> ls.rstrip()
'Druvan is a baby boy'
>>> rs.lstrip('sti')
'             this is good'
>>> ls.rstrip('sti')
'Druvan is a baby boy             '
>>> 
KeyboardInterrupt
>>> ls.rstrip('s ti')
'Druvan is a baby boy'
>>> s = 'Druvan is a baby boy'
>>> s.strip()
'Druvan is a baby boy'
>>> s.strip('boy')
'Druvan is a baby '
>>> s.strip('babyb')
'Druvan is a baby bo'
>>> s1 = 'Druvan is a baby boy'
>>> s1.split()
['Druvan', 'is', 'a', 'baby', 'boy']
>>> s1.split(',')
['Druvan is a baby boy']
>>> s1.split(':')
['Druvan is a baby boy']
>>> s4 = 'Druvan is a baby boy'
>>> s4.rsplit()
['Druvan', 'is', 'a', 'baby', 'boy']
>>> 
