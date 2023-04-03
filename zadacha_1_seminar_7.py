slog = input("Ведите текст кричалки: ")

my_dict = {
    "а": 2,
    "я": 4,
    "у": 6,
    "ю": 8,
    "о": 10,
    "е": 12,
    "ё": 14,
    "э": 16,
    "и": 18,
    "ы": 20,
}

sub = slog.split(' ')
count = []
a = 0
for i in range(len(sub)):
    for j in sub[a]:
        if j in my_dict:
            count.append(j)
    count.append(' ')
    a += 1
    
words = ''.join(count).split()

s = 0
cu = 0
for i in range(len(words)-1):
    if len(words[s]) == len(words[s+1]):
        cu += 1
        s += 1

if cu == len(words)-1:
    print('Парам пам-пам')
else:
    print('Пам парам')
        

    
