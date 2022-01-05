from django.db import models

class Death_ANAM(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    death_date = models.DateField()
    death_datetime = models.DateTimeField(blank=True, null=True)
    death_type_concept_id = models.IntegerField()
    cause_concept_id = models.IntegerField(blank=True, null=True)
    cause_source_value = models.CharField(max_length=50, blank=True, null=True)
    cause_source_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "default"
        db_table = 'death'

class ConditionOccurrence_ANAM(models.Model):
    condition_occurrence_id = models.BigIntegerField()
    person_id = models.BigIntegerField(primary_key=True)
    condition_concept_id = models.IntegerField()
    condition_start_date = models.DateField()
    condition_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_end_date = models.DateField(blank=True, null=True)
    condition_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_type_concept_id = models.IntegerField()
    stop_reason = models.CharField(max_length=20, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence_id = models.BigIntegerField(blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    condition_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_source_concept_id = models.IntegerField(blank=True, null=True)
    condition_status_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_status_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "default"
        db_table = 'condition_occurrence'


class Person_ANAM(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    gender_concept_id = models.IntegerField()
    year_of_birth = models.IntegerField()
    month_of_birth = models.IntegerField(blank=True, null=True)
    day_of_birth = models.IntegerField(blank=True, null=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    race_concept_id = models.IntegerField()
    ethnicity_concept_id = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.IntegerField(blank=True, null=True)
    person_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_concept_id = models.IntegerField(blank=True, null=True)
    race_source_value = models.CharField(max_length=50, blank=True, null=True)
    race_source_concept_id = models.IntegerField(blank=True, null=True)
    ethnicity_source_value = models.CharField(max_length=50, blank=True, null=True)
    ethnicity_source_concept_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        app_label = "default"
        db_table = 'person'


class ProcedureOccurrence_ANAM(models.Model):
    procedure_occurrence_id = models.BigIntegerField()
    person_id = models.BigIntegerField(primary_key=True)
    procedure_concept_id = models.IntegerField()
    procedure_date = models.DateField()
    procedure_datetime = models.DateTimeField(blank=True, null=True)
    procedure_type_concept_id = models.IntegerField()
    modifier_concept_id = models.IntegerField()
    quantity = models.IntegerField()
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence_id = models.BigIntegerField(blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    procedure_source_value = models.CharField(max_length=50, blank=True, null=True)
    procedure_source_concept_id = models.IntegerField(blank=True, null=True)
    modifier_source_value = models.IntegerField()

    class Meta:
        managed = False
        app_label = "default"
        db_table = 'procedure_occurrence'


class Death_ANSAN(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    death_date = models.DateField()
    death_datetime = models.DateTimeField(blank=True, null=True)
    death_type_concept_id = models.IntegerField()
    cause_concept_id = models.IntegerField(blank=True, null=True)
    cause_source_value = models.CharField(max_length=50, blank=True, null=True)
    cause_source_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "ansan_DB"
        db_table = 'death'

class ConditionOccurrence_ANSAN(models.Model):
    condition_occurrence_id = models.BigIntegerField()
    person_id = models.BigIntegerField(primary_key=True)
    condition_concept_id = models.IntegerField()
    condition_start_date = models.DateField()
    condition_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_end_date = models.DateField(blank=True, null=True)
    condition_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_type_concept_id = models.IntegerField()
    stop_reason = models.CharField(max_length=20, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence_id = models.BigIntegerField(blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    condition_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_source_concept_id = models.IntegerField(blank=True, null=True)
    condition_status_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_status_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "ansan_DB"
        db_table = 'condition_occurrence'


class Person_ANSAN(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    gender_concept_id = models.IntegerField()
    year_of_birth = models.IntegerField()
    month_of_birth = models.IntegerField(blank=True, null=True)
    day_of_birth = models.IntegerField(blank=True, null=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    race_concept_id = models.IntegerField()
    ethnicity_concept_id = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.IntegerField(blank=True, null=True)
    person_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_concept_id = models.IntegerField(blank=True, null=True)
    race_source_value = models.CharField(max_length=50, blank=True, null=True)
    race_source_concept_id = models.IntegerField(blank=True, null=True)
    ethnicity_source_value = models.CharField(max_length=50, blank=True, null=True)
    ethnicity_source_concept_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        app_label = "ansan_DB"
        db_table = 'person'


class ProcedureOccurrence_ANSAN(models.Model):
    procedure_occurrence_id = models.BigIntegerField()
    person_id = models.BigIntegerField(primary_key=True)
    procedure_concept_id = models.IntegerField()
    procedure_date = models.DateField()
    procedure_datetime = models.DateTimeField(blank=True, null=True)
    procedure_type_concept_id = models.IntegerField()
    modifier_concept_id = models.IntegerField()
    quantity = models.IntegerField()
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence_id = models.BigIntegerField(blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    procedure_source_value = models.CharField(max_length=50, blank=True, null=True)
    procedure_source_concept_id = models.IntegerField(blank=True, null=True)
    modifier_source_value = models.IntegerField()

    class Meta:
        managed = False
        app_label = "ansan_DB"
        db_table = 'procedure_occurrence'

class Death_GURO(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    death_date = models.DateField()
    death_datetime = models.DateTimeField(blank=True, null=True)
    death_type_concept_id = models.IntegerField()
    cause_concept_id = models.IntegerField(blank=True, null=True)
    cause_source_value = models.CharField(max_length=50, blank=True, null=True)
    cause_source_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "guro_DB"
        db_table = 'death'

class ConditionOccurrence_GURO(models.Model):
    condition_occurrence_id = models.BigIntegerField()
    person_id = models.BigIntegerField(primary_key=True)
    condition_concept_id = models.IntegerField()
    condition_start_date = models.DateField()
    condition_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_end_date = models.DateField(blank=True, null=True)
    condition_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_type_concept_id = models.IntegerField()
    stop_reason = models.CharField(max_length=20, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence_id = models.BigIntegerField(blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    condition_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_source_concept_id = models.IntegerField(blank=True, null=True)
    condition_status_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_status_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "guro_DB"
        db_table = 'condition_occurrence'

class Person_GURO(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    gender_concept_id = models.IntegerField()
    year_of_birth = models.IntegerField()
    month_of_birth = models.IntegerField(blank=True, null=True)
    day_of_birth = models.IntegerField(blank=True, null=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    race_concept_id = models.IntegerField()
    ethnicity_concept_id = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.IntegerField(blank=True, null=True)
    person_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_concept_id = models.IntegerField(blank=True, null=True)
    race_source_value = models.CharField(max_length=50, blank=True, null=True)
    race_source_concept_id = models.IntegerField(blank=True, null=True)
    ethnicity_source_value = models.CharField(max_length=50, blank=True, null=True)
    ethnicity_source_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = "guro_DB"
        db_table = 'person'

class ProcedureOccurrence_GURO(models.Model):
    procedure_occurrence_id = models.BigIntegerField()
    person_id = models.BigIntegerField(primary_key=True)
    procedure_concept_id = models.IntegerField()
    procedure_date = models.DateField()
    procedure_datetime = models.DateTimeField(blank=True, null=True)
    procedure_type_concept_id = models.IntegerField()
    modifier_concept_id = models.IntegerField()
    quantity = models.IntegerField()
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence_id = models.BigIntegerField(blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    procedure_source_value = models.CharField(max_length=50, blank=True, null=True)
    procedure_source_concept_id = models.IntegerField(blank=True, null=True)
    modifier_source_value = models.IntegerField()

    class Meta:
        managed = False
        app_label = "guro_DB"
        db_table = 'procedure_occurrence'
