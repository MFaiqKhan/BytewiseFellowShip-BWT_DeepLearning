import pandas as pd
import numpy as np

# Replace method vs fillna method
# Replace method replaces the value with the given value
# Fillna method replaces the NaN value with the given value
""" 
Filling in missing data with the fillna method is a special case of more general value
replacement. As you've already seen, map can be used to modify a subset of values in
an object but replace provides a simpler and more flexible way to do so.
"""

s_data = pd.Series([0,0,1,22,33,11,2,1,22])
print(s_data)

# Replace method replaces the value with the given value
s_data.replace(0, 100, inplace=True) # Replaces 0 with 100
print(s_data)

# replacing multiple values with multiple values
print(s_data.replace([1,2], [200,300]))