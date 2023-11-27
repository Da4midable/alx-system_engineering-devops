I'll post my function, my expected output, and my current output (after running ./5-main.py | cat -e). Please help me fix my function so my current output matched the expected output (the code you provided didn't work:

current (the space at the start of some  newlines shouldn't be there; you'll see what I mean in the expected output):

LLorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
 Quonam modo?$
$
 Utrum igitur tibi litteram videor an totas paginas commovere?$
$
 Non autem hoc:$
$
 igitur ne illud quidem.$
$
 Fortasse id optimum, sed ubi illud:$
$
 Plus semper voluptatis?$
$
 Teneo, inquit, finem illi videri nihil dolere.$
$
 Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
 Si id dicis, vicimus.$
$
 Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
 Sin aliud quid voles, postea.$
$
 Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
 Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres$


expected:

Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres


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
