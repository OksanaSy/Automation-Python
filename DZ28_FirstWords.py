"""
Есть фрагмент текста, состоящий из предложений.

Предложение - это строка, которая начинается с большой буквы и заканчивается точкой, вопросительным или восклицательным знаком (или несколькими такими знаками).

Предложение может состоять из одного слова. Слова состоят только из букв.

Внутри предложения могут быть запятые.

Составить предложение из первых слов предложений фрагмента.

Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.

Предложение должно заканчиваться точкой.



def generate_sentence(text: str) -> str:
    pass
"""
"""Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""
"""
->
"Happy wish please goodbye."
"""

import re


text1 = """Happy New Year! Wish you good luck.
Please write me how are you doing? Goodbye...
"""

pattern = r"\b(?:^|(?:[.!?]+\s))([A-Z]{1}[a-z]+)\b"


def generate_sentence(text: str) -> str:
    result = re.findall(pattern, text)
    return result


print(' '.join(map(str, generate_sentence(text1))).capitalize(), end='.')
