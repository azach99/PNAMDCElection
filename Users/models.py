
from django.db import models
from multiselectfield import MultiSelectField
from PNAM.utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.

class Subs(models.Model):
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
    SELECTIONS = (
        ("Choose", "Choose"),
        ("Candidate A", "Candidate A"),
        ("Candidate B", "Candidate B"),
        ("Candidate C", "Candidate C"),
        ("Candidate D", "Candidate D"),
    )
    PRESIDENT_ELECT = (
        ("Kanye West", "Kanye West"),
        ("Joe Biden", "Joe Biden"),
        ("Donald Trump", "Donald Trump"),
    )
    RECORDING_SECRETARY = (
        ("Rodrigo Duterte", "Rodrigo Duterte"),
        ("Leni Robredo", "Leni Robredo"),
        ("Manny Pacquiao", "Manny Pacquiao"),
    )
    ASSISTANT_RECORDING_SECRETARY = (
        ("Sharon Cuneta", "Sharon Cuneta"),
        ("Dawn Zulueta", "Dawn Zulueta"),
        ("Gretchen Barreto", "Gretchen Barreto"),
    )
    CORRESPONDING_SECRETARY = (
        ("George Washington", "George Washington"),
        ("Thomas Jefferson", "Thomas Jefferson"),
        ("Ulysses Grant", "Ulysses Grant"),
    )
    TREASURER = (
        ("Barack Obama", "Barack Obama"),
        ("George Bush", "George Bush"),
        ("Bill Clinton", "Bill Clinton"),
    )
    ASSISTANT_TREASURER = (
        ("Mike Pence", "Mike Pence"),
        ("Kamala Harris", "Kamala Harris"),
        ("Bernie Saunders", "Bernie Saunders"),
    )
    AUDITOR = (
        ("Wolf Blitzer", "Wolf Blitzer"),
        ("Anderson Cooper", "Anderson Cooper"),
        ("Chris Cuomo", "Chris Cuomo"),
    )
    PRO = (
        ("Taylor Swift", "Taylor Swift"),
        ("Beyonce", "Beyonce"),
        ("Katy Perry", "Katy Perry"),
        ("Britney Spears", "Britney Spears"),
        ("Christina Aguilera", "Christina Aguilera"),
        ("Jennifer Lopez", "Jennifer Lopez"),
        ("Ariana Grande", "Ariana Grande"),
        ("P!nk", "P!nk"),
    )
    BOARD_OF_DIRECTORS = (
        ("Zach Amados", "Zach Amados"),
        ("Rianna Talento", "Rianna Talento"),
        ("Reinny Florido", "Reinny Florido"),
        ("Ryan Robles", "Ryan Robles")
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
    question_7 = models.CharField(max_length=100, default='', choices=ASSISTANT_RECORDING_SECRETARY)
    question_8 = models.CharField(max_length=100, default='', choices=TREASURER)
    question_9 = models.CharField(max_length=100, default='', choices=ASSISTANT_TREASURER)
    question_10 = models.CharField(max_length=100, default='', choices=AUDITOR)

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender = Subs)