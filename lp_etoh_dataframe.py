"""Creating models with pandas and matplotlib for executive team. Using variables declared in supply_info.py"""


import pandas as pd
import matplotlib.pyplot as plt
from supply_info import etoh_waste_supplies, kingfisher_plates_to_biohaz_box


data = {'Current Yearly Spend ($)': [240009],
        'Proposed Yearly Spend ($)': [14404]}

index = ['Cost reduced by 96.54%']

spend_dataframe = pd.DataFrame({'Cost Saving = $225,605 (96.54% Reduction)': ['Current', 'Proposed'],
                                'Spend': [240009, 14404]},)


model = spend_dataframe.plot.bar(rot=0, title= 'Yearly LP EtOH Spend ($)', x='Cost Saving = $225,605 (96.54% Reduction)', y='Spend')

# auto labels column with value from dataframe
model.bar_label(model.containers[0])

plt.show()