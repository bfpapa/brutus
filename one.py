import os
import pandas

FILE_PATH = r"C:\FILES"

A_FILE = 'a.csv'
D_FILE = 'd.csv'
T_FILE = 't.csv'
B_FILE = 'b.csv'

a = pandas.readcsv(os.path.join(FILE_PATH,A_FILE))
b = pandas.readcsv(os.path.join(FILE_PATH,B_FILE))
d = pandas.readcsv(os.path.join(FILE_PATH,D_FILE))
t = pandas.readcsv(os.path.join(FILE_PATH,T_FILE))

