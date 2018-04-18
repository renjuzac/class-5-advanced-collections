from step_1 import transform_products_to_list
from step_3 import group_products_by_customer_and_invoice


def calculate_total_per_invoices(products_string):
    result ={}
    product_groups = group_products_by_customer_and_invoice(products_string)
    
    for customer_id, customer_data in product_groups.items():
        result.setdefault(customer_id,{})
        for invoice_id,products in customer_data.items():
            # print(customer_id,invoice_id,products)
            sum = 0 
            for product in products:
                sum += float(product[3]) * float(product[5])
            result[customer_id][invoice_id] = round(sum,2)
    return result
            
            
            

