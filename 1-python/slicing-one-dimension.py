#Assign all the rows and the first 2 columns of world_alcohol to first_two_columns.
#Assign the first 10 rows and the first column of world_alcohol to first_ten_years.
#Assign the first 10 rows and all of the columns of world_alcohol to first_ten_rows.

first_two_columns = world_alcohol[:,0:2]
2
​
3
first_ten_years = world_alcohol[0:10,0]
4
​
5
first_ten_rows = world_alcohol[0:10,:]
Variables
 first_ten_rowsndarray (<class 'numpy.ndarray'>)
array([['1986', 'Western Pacific', 'Viet Nam', 'Wine', '0'],
       ['1986', 'Americas', 'Uruguay', 'Other', '0.5'],
       ['1985', 'Africa', "Cte d'Ivoire", 'Wine', '1.62'],
       ['1986', 'Americas', 'Colombia', 'Beer', '4.27'],
       ['1987', 'Americas', 'Saint Kitts and Nevis', 'Beer', '1.98'],
       ['1987', 'Americas', 'Guatemala', 'Other', '0'],
       ['1987', 'Africa', 'Mauritius', 'Wine', '0.13'],
       ['1985', 'Africa', 'Angola', 'Spirits', '0.39'],
       ['1986', 'Americas', 'Antigua and Barbuda', 'Spirits', '1.55'],
       ['1984', 'Africa', 'Nigeria', 'Other', '6.1']], 
      dtype='<U75')
 first_ten_yearsndarray (<class 'numpy.ndarray'>)
array(['1986', '1986', '1985', '1986', '1987', '1987', '1987', '1985',
       '1986', '1984'], 
      dtype='<U75')
 first_two_columnsndarray (<class 'numpy.ndarray'>)
array([['1986', 'Western Pacific'],
       ['1986', 'Americas'],
       ['1985', 'Africa'],
       ..., 
       ['1986', 'Europe'],
       ['1987', 'Western Pacific'],
       ['1986', 'Africa']], 
      dtype='<U75')
 world_alcohol