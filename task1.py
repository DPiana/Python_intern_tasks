import pandas as pd
import re
import calendar

def group_by(stream, field, success=None):
    
    #assertions
    assert(field == "month" or field == "year")
    assert( success == None or success == True or success == False)
    
    # months abbreviations, first element is empty string so we skip
    months = [month for month in calendar.month_abbr][1:]
    
    # data frame for keeping results
    results = pd.DataFrame(columns = ['year', 'month', 'success'])
    
    # skip first 2 lines (clumns names and hashes)
    for i in range(2):
        next(stream)
        
    # regexp for date
    r_date = '\d{4}\s\w{3}\s{1,2}\d{1,2}'
    
    # regexp for success
    r_success = '\s+(S|F)\s+'
    
    # filling data frame
    for line in iter(stream):
        re_search = re.search(r_date, line)
        if re_search:
            substring = re_search.group(0)
            split_substring = str.split(substring)
            if split_substring[1] in months:
                re_search = re.search(r_success, line)
                if re_search:
                    substring = re_search.group(0).strip()
                    results.loc[results.shape[0]] = [split_substring[0], split_substring[1], substring]                  
    
    if success is None:
        grouped_results = results.groupby([field])[field].count()
    elif success is True:
        grouped_results = results[results.success == 'S'].groupby([field])[field].count()
    else:
        grouped_results = results[results.success == 'F'].groupby([field])[field].count()
    
    
    return grouped_results.to_dict()
   
