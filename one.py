import os
import pandas as pd
import numpy as np

FILE_PATH = r"C:\FILES"

A_FILE = 'a.csv'
D_FILE = 'd.csv'
T_FILE = 't.csv'
B_FILE = 'b.csv'

A_DF = pd.read_csv(os.path.join(FILE_PATH,A_FILE))
B_DF = pd.read_csv(os.path.join(FILE_PATH,B_FILE))
D_DF = pd.read_csv(os.path.join(FILE_PATH,D_FILE))
T_DF = pd.read_csv(os.path.join(FILE_PATH,T_FILE))

src = {'a': {'file': A_FILE, 'DF': A_DF},
       'b': {'file': B_FILE, 'DF': B_DF},
       'd': {'file': D_FILE, 'DF': D_DF},
       't': {'file': T_FILE, 'DF': T_DF}
      }


