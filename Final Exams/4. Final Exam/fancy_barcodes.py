import re

count_of_barcodes = int(input())
for num in range(count_of_barcodes):
    barcodes = input()
    pattern = r"(@\#{1,})([A-Z]([A-Za-z0-9]{4,})+[A-Z])@\#{1,}"
    result = re.search(pattern, barcodes)
    if result is None:
        print("Invalid barcode")
    else:
        product_group = []

        for symbols in result.group(2):

            if result.group(2).isalpha():
                product_group.append('00')
                break
            if symbols.isdigit():
                product_group.append(symbols)
        print(f"Product group: {''.join(product_group)}")

#
#
# import re
#
# count_of_barcodes = int(input())
# for num in range(count_of_barcodes):
#     barcodes = input()
#     pattern = r"(@\#{1,})([A-Z]([A-Za-z0-9]{4,})+[A-Z])@\#{1,}"
#     result = re.search(pattern, barcodes)
#
#     if not result:
#         print("Invalid barcode")
#     else:
#         extract_numbers = re.findall('\d', result.group())
#         if not extract_numbers:
#             print('Product group: 00')
#         else:
#             print(f"Product group: {''.join(extract_numbers)}")