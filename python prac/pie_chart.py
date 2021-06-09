import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_file='data.csv'
data = pd.read_csv(csv_file)
Votes = data["TotalVotes"]
Genre = data["Genre"]

x=[]
y=[]
x=list(Genre)
y=list(Votes)

plt.scatter(x,y)
plt.xlabel('Genre->')
plt.ylabel('Total Votes->')
plt.title('Data')
plt.show()