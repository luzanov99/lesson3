"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print('Длина файла = {}'.format(len(content)))
        content =content.replace('.','!')
        print(content)
        k=0
        f=[]
        word=''
        for i in range (0, len(content)):
            if content[i]!=' ' :
                word+=content[i]
            else :
                f.append(word)
                k+=1
                word=''
        print('Количество слов в тексте = {}'.format(k+1))
    with open('referat2.txt','w', encoding='utf-8') as g:
        g.write(content)

if __name__ == "__main__":
    main()
