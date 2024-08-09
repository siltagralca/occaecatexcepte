import pandas as pd

# Assuming dataframe is a Pandas DataFrame
dataframe['CommentYear'] = dataframe['CommentDate'].dt.year
