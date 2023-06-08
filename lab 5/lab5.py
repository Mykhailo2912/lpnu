from num2words import num2words

def number_to_words():
    while True:
        try:
            number = int(input("Enter a number (0 to exit): "))
            if number == 0:
                break
            words = num2words(number)
            print(words)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if name == "main":
    number_to_words()

    def number_to_words(number):
    word_dict = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        # Р”РѕРґР°С‚РєРѕРІС– Р·РЅР°С‡РµРЅРЅСЏ РјРѕР¶РЅР° РїСЂРѕРґРѕРІР¶РёС‚Рё
    }

    if number in word_dict:
        return word_dict[number]
    else:
        return str(number)

def main():
    while True:
        try:
            number = int(input("Enter a number (0 to exit): "))
            if number == 0:
                break
            words = number_to_words(number)
            print(words)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if name == "main":
    main()
