import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--train_list', required=True, help='path to train_list file')
parser.add_argument('--test_list', required=True, help='path to test_list file')
opt = parser.parse_args()

char_set = set()
train_list = pd.read_csv(opt.train_list, sep="\t", names=["width", "height", "img_name", "img_text"])
test_list = pd.read_csv(opt.test_list, sep="\t", names=["width", "height", "img_name", "img_text"])

train_list = list(train_list.img_text)
test_list = list(test_list.img_text)

for s in train_list:
    for c in s:
        char_set.add(c)

for s in test_list:
    for c in s:
        char_set.add(c)

print (len(char_set))

f = open("char_set.txt", "w", encoding="utf-8")
for i, c in enumerate(char_set):
    f.write("{}\t{}\n".format(i, c))
f.close()
