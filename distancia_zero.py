
import re
import sys

def main():
    a = input('Digite algo se desejar sair digite "s": ')
    if a.lower() == 's':
        sys.exit() 
    conta_texto(a)


def conta_texto(txt):
    if txt == '':
        print('Redirecionando ao menu.')
        main()
    else:
        text = re.findall(r'0+', txt)
        var = max(text)
        cont = var.count('0')
        print(f'A maior sequencia de zeros é: {cont}')

if __name__ ==  '__main__':
    main()