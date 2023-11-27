#!/usr/bin/python3
def text_indentation(text):
    new_text = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        new_text += char
        if char in [".", ":", "?"]:
            new_text += "\n\n"
            if " " in new_text:
                new_text += ""
    
    print(new_text)
