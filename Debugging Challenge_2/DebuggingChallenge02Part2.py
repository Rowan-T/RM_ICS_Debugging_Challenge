# Ben Schweighauser
# Runtime error: file not found
# This would read in the data from my desktop
# To fix this error, make sure that the directory is written correctly
import pandas as pd
data = pd.read_csv('/Users/bschweighauser/Desktop/Data.csv', thousands=',')