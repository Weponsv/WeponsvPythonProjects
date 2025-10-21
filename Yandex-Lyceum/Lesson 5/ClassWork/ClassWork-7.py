lang = str(input())
move = int(input())
text = str(input())


def check_in_alphabet(char, move, language):
    num = ord(char) + move

    if language.lower() == 'eng':
        if not 65 <= num <= 90:
            while True:
                num = num - 26
                if 65 <= num <= 90:
                    break
        return chr(num)

    elif language.lower() == 'рус':
        if not 1040 <= num <= 1071:
            while True:
                num = num - 32
                if 1040 <= num <= 1071:
                    break
        return chr(num)

    else:
        return chr(num)


converted_text = ''

for letter in text:
    converted_letter = check_in_alphabet(letter, move, lang)
    converted_text += converted_letter

print(converted_text)