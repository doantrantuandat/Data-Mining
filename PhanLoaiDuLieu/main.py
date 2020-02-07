
import pandas as pd
import TT_ID3 as tt

df = pd.read_csv('weather.csv')
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
tree = tt.DecisionTreeID3(max_depth = 3, min_samples_split = 2)
tree.fit(X, y)
print(tree.predict(X))	

