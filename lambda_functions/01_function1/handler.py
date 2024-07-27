# lambda_function.py

def lambda_handler(event, context):
    number = event.get('number')
    if number is None:
        return {"message": "No number provided"}

    if number % 2 == 0:
        return {"message": "Even"}
    else:
        return {"message": "Odd"}