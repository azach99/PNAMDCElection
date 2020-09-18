from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Subs


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']

class SubsForm(forms.ModelForm):
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
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    #phone_number = forms.CharField(required = False)
    question_1 = forms.ChoiceField(label = "President Elect", required = True, choices = PRESIDENT_ELECT, widget = forms.RadioSelect)
    question_2 = forms.ChoiceField(label = "Recording Secretary", required = True, choices = RECORDING_SECRETARY, widget = forms.RadioSelect)
    question_3 = forms.ChoiceField(label = "Assistant Recording Secretary", required = True, choices = ASSISTANT_RECORDING_SECRETARY, widget = forms.RadioSelect)
    question_4 = forms.MultipleChoiceField(label = "Public Relations Officers (Choose 7)", widget = forms.CheckboxSelectMultiple, choices = PRO)
    question_5 = forms.MultipleChoiceField(label = "Board of Directors (Choose 2)", widget=forms.CheckboxSelectMultiple, choices=BOARD_OF_DIRECTORS)
    question_6 = forms.ChoiceField(label="Corresponding Secretary", required=True, choices=CORRESPONDING_SECRETARY, widget = forms.RadioSelect)
    question_7 = forms.ChoiceField(label = "Assistant Corresponding Secretary", required=True, choices=ASSISTANT_RECORDING_SECRETARY, widget = forms.RadioSelect)
    question_8 = forms.ChoiceField(label = "Treasurer", required=True, choices=TREASURER, widget = forms.RadioSelect)
    question_9 = forms.ChoiceField(label="Assistant Treasurer", required=True, choices=ASSISTANT_TREASURER, widget = forms.RadioSelect)
    question_10 = forms.ChoiceField(label = "Auditor", required=True, choices=AUDITOR, widget = forms.RadioSelect)

    def verify_num(self):
        value = self.cleaned_data['question_4']
        if len(value) > 7:
            raise forms.ValidationError("You cannot select more than 7 items.")
        return value

    class Meta:
        model = Subs
        fields = ['first_name', 'last_name', 'email',
                 'question_1', 'question_2', 'question_3',
                 'question_6', 'question_7', 'question_8', 'question_9',
                 'question_10', 'question_4', 'question_5']