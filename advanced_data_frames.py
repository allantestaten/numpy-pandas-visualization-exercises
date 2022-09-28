import pymysql
import pandas as pd
import numpy as np
from pydataset import data
from get_db_url import make_db

make_db('employees', 'SELECT * FROM departments LIMIT 10')

# Create the roles DataFrame

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

# Create the users DataFrame.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

#2. (users.merge(roles, 
            left_on='role_id', 
            right_on='id', 
            how='right')
    .drop(columns='role_id')
    .rename(columns={'id_x': 'id', 
                     'name_x': 'employee',
                     'id_y': 'role_id',
                     'name_y': 'role'}
            )
)
#output is 5x4 grid. shows all roles whether filled or not

#3. (users.merge(roles, 
            left_on='role_id', 
            right_on='id', 
            how='outer')
    .drop(columns='role_id')
    .rename(columns={'id_x': 'id', 
                     'name_x': 'employee',
                     'id_y': 'role_id',
                     'name_y': 'role'}
            )
)
#result is 7x4 grid. shows all Ids and all roles 

#4. What happens if you drop the foreign keys from the 
#DataFrames and try to merge them?

# Perform an outer join specifying the left and right DataFrame keys.

# Perform an outer join specifying the left and right DataFrame keys.

users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)

#5. Load the mpg dataset from PyDataset.

mpg = data('mpg')
mpg = pd.DataFrame(mpg)

#7. How many rows and columns are in the dataset?
mpg.shape

#234 rows/ 11 columns 

#8. Check out your column names and perform any 
#cleanup you may want on them.

mpg.hwy

#9 Display the summary statistics for the dataset.
mpg.describe().round(2)

#10 How many different manufacturers are there?
mpg.manufacturer.nunique()

#11 How many different models are there?
mpg.model.nunique()

#12 Create a column named mileage_difference 
#like you did in the DataFrames exercises; this column 
#should contain the difference between 
#highway and city mileage for each car.

mpg['mileage_difference'] = mpg.hwy - mpg.cty

mpg

#13 Create a column named average_mileage like you did 
#in the DataFrames exercises; this is the mean of the 
#city and highway mileage.

mpg['average_mileage'] = (mpg.hwy + mpg.cty)/2

mpg

#14 Create a new column on the mpg dataset named is_automatic 
#that holds boolean values denoting whether 
#the car has an automatic transmission.

mpg['automatic'] = np.where(mpg.trans == 'auto(I5)', False, True)

mpg
