# pydantic three steps ma kaam karta hai is sab sa pydantic class  ma ap apne data ka idela scema define karte hoo schema ma datatype aur sath hi validation contraints laga sakte hoo
# next step ma ap apni class ka aik  dick bannao ga aur is dick ko ap obje ko bhej doo ga sath hi data ki validation bhi kar rahe hoo sath hi aik va;lidated pydantic class yeh  obj hota hai ap phir apne function ka bhjets hoo aur apka function isko use logic bannat hooaur implement karta hai
# pydantic ma saari fields required hoti hai aur sath hi jis filed ko ap kehte yeh honi chahye mager user na bhi toh de chale ga isko optional kardo ab Anootated aur files ka sath metadara attach kar sakte hoo
from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
  name:Annotated[str,Field(max_length=10,title='name of the person',description='give the name of patient is less than 10 char')]
#   ab hum na datatype ki validation kar di hai 
  email:EmailStr
  linkedin:AnyUrl
  age:int
  schoolnumber:int
  Fathername:str
#   ab yaha field laga kar bata doo is ka neche yeh uer na hoo
  weight:Annotated[float,Field(gt=0,strict=True)]
# ager hum patient ki saari alergies ko rakhna chahte hai toh 
# ager koi allergies nhi batata toh wo by default none ho jae gi
  allergies: Annotated[Optional[List[str]], Field(max_length=5)] = None
# ager dick bhi import karni 
  contact:Dict[str,str]
#ab hum is class ka aik obj bannae ga 
def insert_patient(patient:Patient):
  print(patient.name)
  print(patient.email)
  print(patient.linkedin)
  print(patient.age)
  print(patient.schoolnumber)
  print(patient.Fathername)
  print(patient.allergies)
  print(patient.contact)
Patient_info={'name':'Abdullah','email':'abc@gmail.com','linkedin':'https://www.linkedin.com/in/abdullah-asim-dev/','age':19,'schoolnumber':13,'Fathername':'Asim','weight':55.7,'allergies':['pollen','fever', 'mentalissue'],'contact':{'number':'6397269562'},}
# ab isko inherit kare ga aur sath hi apne pydantic class ka bheje ga
patient1=Patient(**Patient_info)
insert_patient(patient1)