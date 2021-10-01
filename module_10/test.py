from collections import Counter, deque
from collections import defaultdict
from collections import OrderedDict
import sys
import numpy as np
import pandas as pd

countries = pd.Series(
    data = ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ'],
    name = 'countries'
)

print(countries)