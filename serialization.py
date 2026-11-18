# is ma hum as pydontic object ko asa dick aur json  kese export kar sakte hai 
from pydantic import BaseModel
# ager hum aik pyandtic obj ko dusre model ma as a field use kar sake toh isko nested model kehte hai 
class Address(BaseModel):
    city:str
    state:str
    pincode:int


class Patient(BaseModel):
    name:str
    age:int
    gender:str='Male'
    address: Address
    # sab sa pehle hum address ki dick bannae ga 
address_dick={'city':'lahore','state':'androon','pincode':'7674836'}    
# ab is dick sa hum address pydantci ka aik obj
address1=Address(**address_dick)
# ab hum patient model ka liye dick bannaw ga 
patient_dick={'name':'abdullah','age':19,'gender':'male','address':address1}
patient1=Patient(**patient_dick)
# dick ma export karne ka liye apne obj ko call karna hai 
dick_export=patient1.model_dump()
dick_export=patient1.model_dump(include=['name'],exclude=['age'])
print(dick_export)
# dick ma export karne ka liye apne obj ko call karna hai 
# ager moje sari ki jagah sirf name 
json_export=patient1.model_dump_json()
print(json_export)
print(type(json_export))