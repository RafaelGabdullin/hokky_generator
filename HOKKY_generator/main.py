import random

nouns_cnt = 51301
adjective_cnt = 3555
verbs_cnt = 3656

id_nouns = set()
while len(id_nouns) != 5:
    id_nouns.add(random.randint(0, nouns_cnt - 1))
id_nouns = list(id_nouns)
id_nouns.sort()

id_adjective = set()
while len(id_adjective) != 3:
    id_adjective.add(random.randint(0, adjective_cnt - 1))
id_adjective = list(id_adjective)
id_adjective.sort()

id_verb = [random.randint(0, verbs_cnt)]

with open(file="nouns.txt", mode="r", encoding="utf-8") as f:
    for i in range(id_nouns[-1] + 1):
        line = f.readline()
        if i == id_nouns[0]:
            print(line.strip(), end=' ')
            del id_nouns[0]
print()

with open(file="adjective.txt", mode="r", encoding="utf-8") as f:
    for i in range(id_adjective[-1] + 1):
        line = f.readline()
        if i == id_adjective[0]:
            print(line.strip(), end=' ')
            del id_adjective[0]
print()

with open(file="verbs.txt", mode="r", encoding="utf-8") as f:
    for i in range(id_verb[-1] + 1):
        line = f.readline()
        if i == id_verb[0]:
            print(line.strip(), end=' ')
            del id_verb[0]
