# The imports correctly reference the functions from the modules within the package
from operations.arithmetic import add, multiply
from operations.string_ops import reverse_string, count_vowels

print(add(5, 3))
print(multiply(4, 2))
print(reverse_string("Hello"))
print(count_vowels("Hello World"))