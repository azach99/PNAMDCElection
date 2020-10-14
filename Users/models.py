
from django.db import models
from multiselectfield import MultiSelectField
from PNAM.utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.

class Subs(models.Model):
    SELECTIONS_1 = (
        ("Candidate A", "Candidate A"),
        ("Candidate B", "Candidate B"),
        ("Candidate C", "Candidate C"),
        ("Candidate D", "Candidate D"),
    )
    SELECTIONS_4 = (
        ("Candidate A", "Candidate A"),
        ("Candidate B", "Candidate B"),
        ("Candidate C", "Candidate C"),
        ("Candidate D", "Candidate D"),
        ("Candidate E", "Candidate E"),
        ("Candidate F", "Candidate F"),
        ("Candidate G", "Candidate G"),
        ("Candidate 1", "Candidate 1"),
        ("Candidate 2", "Candidate 2"),
        ("Candidate 3", "Candidate 3"),
        ("Candidate 4", "Candidate 4"),
        ("Candidate 5", "Candidate 5")
    )
    PRESIDENT_ELECT = (
        ("Christine Pabico", "Christine Pabico"),
        ("Abstain", "Abstain"),
    )
    RECORDING_SECRETARY = (
        ("Rosabelle Dela Pena", "Rosabelle Dela Pena"),
        ("Abstain", "Abstain"),
    )
    ASSISTANT_RECORDING_SECRETARY = (
        ("Maricon Danz", "Maricon Danz"),
        ("Abstain", "Abstain"),
    )
    CORRESPONDING_SECRETARY = (
        ("Amabelle Estreba", "Amabelle Estreba"),
        ("Abstain", "Abstain"),
    )
    ASSISTANT_CORRESPONDING_SECRETARY = (
        ("Arlyn Soriano", "Arlyn Soriano"),
        ("Abstain", "Abstain"),
    )
    TREASURER = (
        ("Mizpah Amados", "Mizpah Amados"),
        ("Abstain", "Abstain"),
    )
    ASSISTANT_TREASURER = (
        ("Febes Galvez", "Febes Galvez"),
        ("Abstain", "Abstain"),
    )
    AUDITOR = (
        ("Alicia Calayag", "Alicia Calayag"),
        ("Abstain", "Abstain"),
    )
    PRO = (
        ("Linda Cabacar", "Linda Cabacar"),
        ("Edna Guerrero", "Edna Guerrero"),
        ("Lenny Icayan", "Lenny Icayan"),
        ("Teresita Delima", "Teresita Delima"),
        ("Vicky Luceriaga", "Vicky Luceriaga"),
    )
    BOARD_OF_DIRECTORS = (
        ("Resurrection Jao", "Resurrection Jao"),
        ("Prima Colburn", "Prima Colburn"),
        ("Aida Imperio", "Aida Imperio"),
        ("Elsa Aquino", "Elsa Aquino"),
        ("Florina Reynoso-Ray", "Florina Reynodo-Ray"),
        ("Dolly Grey", "Dolly Grey"),
    )

    ASSISTANT_AUDITOR = (
        ("Tess Valencia", "Tess Valencia"),
        ("Abstain", "Abstain")
    )

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    slug = models.SlugField(max_length = 250)
    random_key = models.CharField(max_length = 250, blank = True)
    admin_email = models.EmailField(max_length = 100, default = 'admin_user@gmail.com')
    #phone_number = models.CharField(max_length = 200, default = '')
    question_1 = models.CharField(max_length = 100, default = '', choices = PRESIDENT_ELECT)
    question_2 = models.CharField(max_length = 100, default = '', choices = RECORDING_SECRETARY)
    question_3 = models.CharField(max_length = 100, default = '', choices = ASSISTANT_RECORDING_SECRETARY)
    question_4 = MultiSelectField(choices = PRO, default = '')
    question_5 = MultiSelectField(choices = BOARD_OF_DIRECTORS, default = '')
    question_6 = models.CharField(max_length=100, default='', choices=CORRESPONDING_SECRETARY)
    question_7 = models.CharField(max_length=100, default='', choices=ASSISTANT_CORRESPONDING_SECRETARY)
    question_8 = models.CharField(max_length=100, default='', choices=TREASURER)
    question_9 = models.CharField(max_length=100, default='', choices=ASSISTANT_TREASURER)
    question_10 = models.CharField(max_length=100, default='', choices=AUDITOR)
    question_11 = models.CharField(max_length = 100, default = '', choices = ASSISTANT_AUDITOR)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender = Subs)