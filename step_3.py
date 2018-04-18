from step_1 import transform_products_to_list


def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)
    result = {}
    
    for item in products_list:
        cust_id = item[-2] 
        invoice_num = item[0]
        result.setdefault(cust_id,{})
        result[cust_id].setdefault(invoice_num,[])
        result[cust_id][invoice_num].append(item)
    return result

