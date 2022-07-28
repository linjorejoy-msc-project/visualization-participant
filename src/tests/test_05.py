# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.randn(1000, 4), index=ts.index, columns=list('ABCD'))

a = {"1": 1, "2": 2}

one = a["1"]
a["1"] = 111
print(f'{one=} and {a["1"]=}')
# def first():
#     print("first")
#     return True


# def second():
#     print("Second")
#     return True


# if first() or second():
#     print("Both")
