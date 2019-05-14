#Import from CSV to Dataframe
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data = pd.read_csv('tips.csv')
#Calculated column
data['total_with_tip'] = data['total_bill'] + data['tip']
print(data)
#Conditional subsetting
condition = data.loc[data['smoker'] == 'Yes']
print(condition) 
#Correlation 
corr = data['total_bill'].corr(data['tip'])
if (corr > 0.8 or corr < -0.8):
    print("The Correlation Coefficient between total bill and tip is: " + str(corr) + " and is significant")
else:
    print("The Correlation Coefficient between total bill and tip is: " + str(corr) + " and is not significant")
#Data visualisation
ax = data['sex'].value_counts().plot(kind='bar',
                                    figsize=(10,5),
                                    title="Count of Each Gender",
                                    color=['green','purple'])
ax.set_xlabel("Gender")
ax.set_ylabel("Frequency")
plt.show()