import random
import re
import string

from uwuify import uwu, UwuifyFlag

UWU_FLAGS = UwuifyFlag.YU | UwuifyFlag.SMILEY | UwuifyFlag.STUTTER


def uwuify(text: str):
    text_final = ''
    words = text.split(' ')
    words_transformed = []
    for i in range(len(words)):
        words_transformed.append(i)
        if random.randint(0, 5) == 1:
            words_transformed.append(random.choice(
                ["uwu", "owo", ">" + "/" * random.randint(3, 7) + "<", "a" + "wa" * random.randint(2, 4),
                    ''.join(random.choices(string.ascii_lowercase, k=random.randint(10, 40)))]))

    for i in words:
        if re.match(r'[a-zA-Z]+', i):
            i = i.lower()  # bottom speech
            i = uwu(i, flags=UWU_FLAGS)

        text_final += i + " "

    text_final = text_final[:-1]
    return text_final


if __name__ == '__main__':
    with open('messages.properties', encoding='utf8') as f:
        data = f.read()

    lines = data.splitlines()
    outlines = []
    for i in lines:
        if i.startswith('#'):
            outlines.append(i)
            continue

        split = i.split('=')
        key = split[0]
        value = ''.join(split[1:])
        value = uwuify(value)
        outlines.append(f"{key}={value}")

    with open("messages-uwu.properties", "w", encoding='utf8') as f:
        f.write('\n'.join(outlines))
