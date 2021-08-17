
class Customers:
    customerList=[]
    def create(self,Company):
        self.customerList.append(Company)


class Company:
        address=""
        website=""
        tags=[]
        phone =""
        mobile=""
        fax=""
        email=""
        languages=""
        def __init__(self,address,website,tags,phone,mobile,fax,email,languages):
             self.address =address
             self.website =website
             self.tags =self.getTag()
             self.phone =phone
             self.mobile =mobile
             self.fax =fax
             self.email =email
             self.languages =languages
        
        def getTag():
             return Tag.tags

class Tag:
        def  __init__(self,contact_name,title,job_description,email,phone,mobile,notes):
                self.contact_name=contact_name
                self.title=title
                self.job_description=job_description
                self.email=email
                self.phone=phone
                self.mobile=mobile
                self.notes=notes
        def createTag(self):
            self.tags = ["Ar group"]
            
''
Customers and Company --> one to many relationships
Company and tag --> one to many relationships

''''''
