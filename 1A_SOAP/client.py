from zeep import Client

client = Client("http://127.0.0.1:10000/?wsdl")

result_add = client.service.add_numbers(5, 10)
result_sub = client.service.sub_numbers(2, 3)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")