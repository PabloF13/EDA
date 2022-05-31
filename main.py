import pandas as pd
import seaborn as sns

tours=pd.concat([tour2019, tour2018, tour2017, tour2016, tour2015], ignore_index=True )

#Por tiempo
grafico= sns.swarmplot(x="Year" , y="Minutes", hue="Country", data=tours, size=7)
grafico.set_xlabel("Year" , fontsize=20)
grafico.set_ylabel("Minutes", fontsize=20)
grafico.tick_params(labelsize=15)
grafico.invert_yaxis()
print(grafico)