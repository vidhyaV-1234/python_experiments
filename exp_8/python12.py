#to add, subtract, multiple and divide two Pandas Series.
import numpy as np
import pandas as pd
animals=pd.Series({'elephant':200,'horse':300,'rabbit':2050})
incre_pop=pd.Series({'elephant':100,'horse':50,'rabbit':200})
total_pop=animals+incre_pop
print(total_pop)
total_pop=animals-incre_pop
print(total_pop)
total_pop=animals*incre_pop
print(total_pop)
total_pop=animals/incre_pop
print(total_pop)
