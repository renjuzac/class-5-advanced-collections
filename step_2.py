from step_1 import transform_products_to_list


def group_products_by_customer(products_string):
    products_list = transform_products_to_list(products_string)
    result = {}
    
    for item in products_list:
        cust_id = item[-2] 
        result.setdefault(cust_id,[])
        result[cust_id].append(item)
    return result
    


