def count_vowels(text: str) -> int:
    text = text.lower()
    vowels = 0
    for i in text:
        if i in ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']:
            vowels += 1

    return vowels