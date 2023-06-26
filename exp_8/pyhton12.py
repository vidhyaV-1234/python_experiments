#covert a numpy array and series to dataframe
import numpy as np
import pandas as pd
arr=np.random.randint(1,10,3)
print(arr,type(arr))
pph={'ga':100,'ka':80,'ya':200}
series=pd.Series(pph)
print(series)
x=pd.DataFrame({'hostel_pop':pph,'ad_stutent':arr},index=['ga','ka','ya'])
print(x)
