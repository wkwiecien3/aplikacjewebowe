import copy
from rest_framework import permissions

class CustomDjangoModelPermissions(permissions.DjangoModelPermissions):

    def __init__(self):
       self.perms_map = copy.deepcopy(self.perms_map) 
       self.perms_map['GET'] = ['%(app_label)s.view%(model_name)s']
       self.perms_map['DELETE'] = ['%(app_label)s.delete%(model_name)s']
