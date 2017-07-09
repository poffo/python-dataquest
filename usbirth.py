def read_csv(file_name):
    data = open(file_name).read()
    data_list = data.split('\r')
    string_list = data_list[1:]
    final_list = []
    
    for item in string_list:
        int_fields = []
        string_fields = item.split(',')
        int_fields = []
        for field in string_fields:
            int_fields.append(int(field))

        final_list.append(int_fields)
    return final_list

cdc_list = read_csv('US_births_1994-2003_CDC_NCHS.csv')
print(cdc_list[:10])

lista = [1,2,3,4,5,6,7]
print(lista[:3])

def calc_counts(file_name, column):
    data = open(file_name).read();
    data_list = data.split('\r')
    string_list = data_list[1:]
    column_index = ['year','month','date_of_month','day_of_week','births']
    final_dict = {}

    for line in string_list:
        line_list = line.split(',')
        if line_list[column_index.index(column)] not in final_dict:
            final_dict[line_list[column_index.index(column)]] = int(line_list[column_index.index('births')])
        else:
            final_dict[line_list[column_index.index(column)]] = final_dict[line_list[column_index.index(column)]]+int(line_list[column_index.index('births')])
    
    return final_dict


column_index = ['year','month','date_of_month','day_of_week','births']
print(column_index.index('year'))
#year,month,date_of_month,day_of_week,births

cdc_year_births = calc_counts('US_births_2000-2014_SSA.csv', 'year')
cdc_month_births = calc_counts('US_births_2000-2014_SSA.csv', 'month')
cdc_dom_births = calc_counts('US_births_2000-2014_SSA.csv', 'date_of_month')
cdc_dow_births = calc_counts('US_births_2000-2014_SSA.csv', 'day_of_week')

print("cdc_year_births: ", cdc_year_births)
print("cdc_month_births: ", cdc_month_births)
print("cdc_dom_births: ", cdc_dom_births)
print("cdc_dow_births: ", cdc_dow_births)







