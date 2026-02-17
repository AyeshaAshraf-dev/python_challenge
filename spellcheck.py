from spellchecker import SpellChecker


spell = SpellChecker()
print("------SPELLCHECKER-------")
print("Type q for quit!")
while True:
    user_input = input("Enter words or sentences for spell checking: ".lower().strip())

    if user_input == "q":
        print("-----ENDED----")
        break

    misspelled = spell.unknown([user_input])

    if not misspelled:
        print("Its perfect! ")

    else:
        correction = spell.correction(user_input)
        print(f"Corrected words: {correction}")

