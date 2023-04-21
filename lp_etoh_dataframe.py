"""Creating models with pandas and matplotlib for executive team. Using variables declared in supply_info.py"""


import pandas as pd
import matplotlib.pyplot as plt


data = {'Current Yearly Spend ($)': [190538],
        'Proposed Yearly Spend ($)': [11544]}

index = ['Cost reduced by 9%']

spend_dataframe = pd.DataFrame({'Cost Saving = $178,994 (94% Reduction)': ['Current', 'Proposed'],
                                'Spend': [190538, 11544]},)

model = spend_dataframe.plot.bar(rot=0, title= 'Yearly Loose Pack Ethanol Waste Stream Spend ($)', x='Cost Saving = $178,994 (94% Reduction)', y='Spend')

# auto labels column with value from dataframe
model.bar_label(model.containers[0], fmt='${:,.0f}')

plt.show()