import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmi': lst})
data.head()

unique_values = data['whoAmi'].uniqe() #Получаем уникальные значения из столбцов 'whoAmi'
one_hot_data = pd.DataFrame() #Создаем пустой DataFrame

#Для каждого уникального значения создаем новый столбец и заполняем его значениями 0 или 1

for value in unique_values:
    one_hot_data[value] = (data['whoAmi'] == value).astype(int)

one_hot_data.head()
