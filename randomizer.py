import random
import os.path
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./picked.csv")

def sierra_retro_randomizer():
  penguin_picker = {1: 'Andrea Leach',
2: 'Anthony Johnson',
3: 'Benjamin Melvin',
4: 'Bryan Clay',
5: 'Cameron Wilke',
6: 'Christopher (Chris) Neal',
7: 'Corbin Waugh',
8: 'Darius Roberts',
9: 'DeKayla (Kayla) Phillips',
10: 'Destin Royer',
11: 'Eric Chou',
12: 'Eric Dominguez',
13: 'Gabriel (Gabo) Seda-Wilmarth',
14: 'Garrett Silong',
15: 'Hasan Nguyen',
16: 'Jacob Jean',
17: 'Jacorious (Jay) Smith',
18: 'Jaedyn Keister',
19: 'James (Jim) Thalacker',
20: 'Jason Sodenkamp',
21: 'Joseph Aubrey',
22: 'Joseph Barron',
23: 'Kenneth Kinder',
24: 'Kevin Lusk',
25: 'Lily Yang',
26: 'Luigi Vernon Yebra',
27: 'Luis Figueroa',
28: 'Maricco Allen',
29: 'Matthew Weil',
30: 'Michael Boyles',
31: 'Netanel Frankel',
32: 'Nicholas Kinnamon',
33: 'Nicholas Smith',
34: 'Ricardo Orozco Chang',
35: 'Robert Ryan',
36: 'Samuel Son',
37: 'Sevastian Schlau',
38: 'Sid Reddy',
39: 'Spencer Schanzer',
40: 'Thomas Vesser',
41: 'Yazide (Yaz) Chitou',
42: 'Zachary (Zack) Hanley'
}

  already_picked = penguin_reader()
  print(already_picked)
  
  penguin = random.randint(1, 46)
  if penguin_picker[penguin] not in already_picked:
    already_picked += penguin_picker[penguin]
    penguin_writer(penguin_picker[penguin])
    return penguin_picker[penguin]
  else: 
    return sierra_retro_randomizer()


def penguin_reader():

  already_picked =[]

  with open(path) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        already_picked.append(row)
    return already_picked

def penguin_writer(newly_picked):

  header = ['name']

  with open(path, 'a') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([newly_picked])
  
  return 'Appended.'

print(sierra_retro_randomizer())