from import_export import resources
from .models import CitiesModel,CountiesModel,skills

class CountryResource(resources.ModelResource):
    class Meta:
        model = CountiesModel

class CitiesResource(resources.ModelResource):
    class Meta:
        model = CitiesModel

class SkillsResource(resources.ModelResource):
    class Meta:
        model = skills