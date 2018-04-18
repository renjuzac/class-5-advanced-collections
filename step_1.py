
def transform_products_to_list(products_string):
    result = []
    lines = products_string.split("\n")
    for line in lines:
        if line :
            product = line.split(",")
            result.append(product)
    return result


