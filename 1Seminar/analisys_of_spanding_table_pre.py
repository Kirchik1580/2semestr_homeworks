import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import argparse as arp

parser = arp.ArgumentParser()
parser.add_argument('m', type = str, help = 'First argument is number of month')
parser.add_argument('y', type = str, help = 'Second argument is number of year')

args = parser.parse_args()
print(args)


def wordcombine(m, y):
    link = r"/home/kirill/PycharmProjects/pythonProject/"
    #link = link[0:len(link) - 1]

    month_year = link + m + '.' + y + '.csv'
    return month_year

w = wordcombine(args.m, args.y)

_title = args.m + '.' + args.y

xl = pd.read_csv(w)
xl_Category = list(xl['Категория'])
xl_summ = list(xl['Сумма в рублях'])

sns.barplot(x = xl_Category, y= xl_summ, estimator = sum).set(title = _title)
plt.ylabel('траты в руб.')
plt.show()
