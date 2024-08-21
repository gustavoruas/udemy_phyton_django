import math
from django.db import connection

#debug function for SQLs   
def print_raw_query(query, params):   
    formatted_query = query % tuple(params)
    print("*********DEBUG SQL**********")
    print(formatted_query)


#returns dictionary {}
def json_datatable_data(
    request,
    class_object,
    query,
    search_columns    
):

    objects = class_object.objects.raw(query)
    #objects = Difficulty.objects.all()
    total = class_object.objects.count()  
    
    #this acquires the get parameter search, fro mdatatables
    search_word = request.GET.get("search[value]")
    
    if search_word:    
        
        #validate if first the query already contains where
        if "where" not in query.lower():
            query_search = (
                query + " \n"                
                "WHERE 1=1 "
            )                 
        
        loop_num = 0
        for iter_col in search_columns:
            
            loop_num = loop_num + 1
            
            if len(search_columns) == 1:
                query_search = (query_search +
                    "AND lower("+ iter_col +") LIKE lower(%s) \n"               
                ) 
            else:
                
                if loop_num == 1:
                    query_search = (query_search +
                        "AND ( \n"
                        "lower("+ iter_col +") LIKE lower(%s) \n"               
                    ) 
                    
                #last element of list
                elif loop_num == len(search_columns) :
                     query_search = (query_search +
                        "  OR lower("+ iter_col +") LIKE lower(%s) ) \n"               
                    )        
                     
                else:
                     query_search = (query_search +
                        "  OR lower("+ iter_col +") LIKE lower(%s) \n"               
                    )  
        
        #looping amount of times for parameter list
        query_param_list =[]
        query_param_list = [f'%{search_word}%' for iteration in range(len(search_columns))] 
        
        print_raw_query(query_search, query_param_list)
        
        #SQL use of % must be done differently
        objects = class_object.objects.raw(query_search, query_param_list)
        
    
    _start = request.GET.get("start")
    _length = request.GET.get("length")
    
    if _start and _length:
        start  = int(_start)
        length = int(_length)
        
        page = math.ceil(start / length) + 1
        
        per_page = page
        
        objects = objects[start:start + length]
    
    #orders columns according per column selected
    #order_flag = request.GET("order[")    
    if (request.GET.get("order[0][column]")):
        column = int(request.GET.get("order[0][column]"))
        order_dir = str(request.GET.get("order[0][dir]")).lower()
        column_name = str(request.GET.get(("columns[{}][data]").format(column))).lower()
        
        if order_dir.__eq__('asc'):
            print("order is {}".format(order_dir))
            objects = sorted(objects, key=lambda class_object: getattr(class_object,column_name))  
        else:
            print("order is {}".format(order_dir))
            objects = sorted(objects, key=lambda class_object: getattr(class_object,column_name),reverse=True)
                    
    data = [diff.to_dict_json() for diff in objects]
    
    response = {
        "data" : data,
        "recordsTotal" : total,
        "recordsFiltered" : total
    }
    
    return response
