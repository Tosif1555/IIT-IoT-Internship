def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    # This is a concise and correct way to count vowels using a generator expression and sum()
    return sum(1 for ch in s if ch in vowels)