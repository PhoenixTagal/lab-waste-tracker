"""EHS Metadata for active labs in 1165. Number of eyewash/shower stations.
Types of waste streams and amount used in labs"""

adaptive_1165_lab_info = {}
"""Parent dict that will be used to access all relevant data for the 1165 labs."""

labs = open('lab_names')
for i in labs:
    i = i.rstrip()
    if i == '':
        continue
    adaptive_1165_lab_info[i] = 0

print(adaptive_1165_lab_info)


