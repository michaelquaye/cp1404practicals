from prac_07.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    languages = [ruby, python, visual_basic]
    dynamics = []
    #dynamics = [language for language in languages if language.typing is 'Dynamic']
    for language in languages:
        if language.is_dynamic():
            print(language.name)
    # for i in range (len(languages)):
    #     if languages[i]. typing is 'Dynamic':
    #         dynamics.append(languages[i])
    # print(len(dynamics))
    # print('The dynamically typed languages are:')
    # for i in range (len(dynamics)):
    #     print(dynamics[i].name)

    #
    # numbers = [1,2,3,4,5,6]
    # for i in range (len())


main()