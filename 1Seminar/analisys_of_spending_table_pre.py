import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import argparse as arp

parser = arp.ArgumentParser()
parser.add_argument('m', type = str, help = 'First argument is number of month', choices = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
parser.add_argument('y', type = int, help = 'Second argument is number of year', choices = range(1991, 2025))

args = parser.parse_args()
print(args)


def wordcombine(m, y):
    link = r"/home/kirill/PycharmProjects/pythonProject/"
    #link = link[0:len(link) - 1]

    month_year = link + str(m) + '.' + str(y) + '.csv'
    return month_year

w = wordcombine(args.m, args.y)

_title = str(args.m) + '.' + str(args.y)

xl = pd.read_csv(w)
xl_Category = list(xl['Категория'])
xl_summ = list(xl['Сумма в рублях'])

sns.barplot(x = xl_Category, y= xl_summ, estimator = sum).set(title = _title)
plt.ylabel('траты в руб.')
plt.show()
