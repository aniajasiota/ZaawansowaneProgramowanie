def ispalindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    ptext = text[::-1]

    if ptext == text:
        return True
    else:
        return False