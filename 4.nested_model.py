from pydantic import BaseModel
# ager hum aik pyandtic obj ko dusre model ma as a field use kar sake toh isko nested model kehte hai 
class Address(BaseModel):
    city:str
    state:str
    pincode:int


class Patient(BaseModel):
    name:str
    age:int
    gender:str
    address: Address
    # sab sa pehle hum address ki dick bannae ga 
address_dick={'city':'lahore','state':'androon','pincode':'7674836'}    
# ab is dick sa hum address pydantci ka aik obj
address1=Address(**address_dick)
# ab hum patient model ka liye dick bannaw ga 
patient_dick={'name':'abdullah','age':19,'gender':'male','address':address1}
patient1=Patient(**patient_dick)
print(patient1)
print(patient1.address.state)