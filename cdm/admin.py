from django.contrib import admin
from cdm.models import ConditionOccurrence_ANAM, Death_ANAM, Person_ANAM, ProcedureOccurrence_ANAM
from cdm.models import ConditionOccurrence_ANSAN, Death_ANSAN, Person_ANSAN, ProcedureOccurrence_ANSAN
from cdm.models import ConditionOccurrence_GURO, Death_GURO, Person_GURO, ProcedureOccurrence_GURO

class PersonAdmin(admin.ModelAdmin):
	list_display = ('gender_concept_id','year_of_birth')

admin.site.register(Person_ANAM, PersonAdmin)
admin.site.register(Person_ANSAN, PersonAdmin)
admin.site.register(Person_GURO, PersonAdmin)


class DeathAdmin(admin.ModelAdmin):
	list_display = ('person_id','death_date','death_datetime','death_type_concept_id','cause_concept_id')

admin.site.register(Death_ANAM, DeathAdmin)

class ConditionOccurrenceAdmin(admin.ModelAdmin):
	list_display = ('person_id','condition_occurrence_id')

admin.site.register(ConditionOccurrence_ANAM, ConditionOccurrenceAdmin)

# Register your models here.
