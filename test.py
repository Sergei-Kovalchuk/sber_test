import datetime
from pprint import pprint
import json
from re import sub
with open('operations.json', encoding='utf-8') as f: 
    templates = json.load(f)
    # pprint(templates)
executed_list = []
transactions = templates[-5::]
by_date = transactions[::-1]
list_executed = []
for executed in by_date:
    if 'date' in executed:
        date = datetime.datetime.strptime(executed['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        list_executed.append(date)
    if 'description' in executed:
        description =  executed['description']
        list_executed.append(description)
        list_executed.append('\n') 
    if 'from' in executed:
        from_ = executed['from']
       
        if len(from_) == 24:
            new_from = sub(r'(\d{4})(\d{2})\d{6}(\d{4})', r'\1 \2** **** \3', from_)
        else:
            new_from = sub(r'(\d{4})(\d{2})\d{10}(\d{4})', r'\1 \2** **** **** \3', from_)
        list_executed.append(new_from)
        list_executed.append('->')
    if 'to' in executed:
        to = sub(r'(\d{0})\d{2}(\d{4})', r'\1Счет **\2', executed['to'][-6:])
        
        list_executed.append(to)
        list_executed.append('\n')
    if 'operationAmount' in executed:
        operationAmount = executed['operationAmount']
        if 'amount' in operationAmount:
            amount = operationAmount['amount']
            list_executed.append(amount)
        if 'currency' in operationAmount:
            currency = operationAmount['currency']
            
            if 'name' in currency:
                name_currency = currency['name']
                list_executed.append(name_currency)
                list_executed.append('\n')
                list_executed.append('\n')

print(''.join(list_executed))




