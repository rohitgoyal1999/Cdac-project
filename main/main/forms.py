from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

# COUNTRY_CHOICES=[
#     ('0', 'Select Country'),
#     ('1', 'France'),
#     ('2', 'Germany'),
#     ('3', 'USA'),
#     ('4', 'Netherlands'),
#     ('5', 'Belgium'),
#     ('6', 'Irish Republic'),
#     ('7', 'Australia'),
#     ('8', 'Canada'),
#     ('9', 'Italy'),
#     ('10', 'Spain'),
#     ('11', 'Switzerland'),
#     ('12', 'Norway'),
#     ('13', 'Japan'),
#     ('14', 'Poland'),
#     ('15', 'South Africa'),
#     ('16', 'Denmark'),
#     ('17', 'Central & South America'),
#     ('18', 'Russia'),
#     ('19', 'New Zealand'),
#     ('20', 'Sweden'),
#     ('21', 'India'),
#     ('22', 'Hong Kong'),
#     ('23', 'Portugsl'),
#     ('24', 'Austria'),
#     ('25', 'Greece'),
#     ('26', 'Israel'),
#     ('27', 'Middle East'),
#     ('28', 'Other Africa'),
#     ('29', 'Other Western Europe'),
#     ('30', 'Other Asia'),
#     ('31', 'Brazil'),
#     ('32', 'Eastern Europe'),
#     ('33', 'United Arab Emirates'),
#     ('34', 'Singapore'),
#     ('35', 'Czech Republic'),
#     ('36', 'Malasia'),
#     ('37', 'Saudi Arabia'),
#     ('38', 'Nigeria'),
#     ('39', 'Finland'),
#     ('40', 'South Korea'),
#     ('41', 'Mexico'),
#     ('42', 'China'),
#     ('43', 'Hungary'),
#     ('44', 'Pakistan'),
#     ('45', 'Turkey'),
#     ('46', 'Thailand'),
#     ('47', 'Egypt'),
#     ('48', 'Taiwan'),
#     ('49', 'Kenya'),
#     ('50', 'Kuwait'),
#     ('51', 'Other Eastern Europe'),
#     ('52', 'Romania')]   

# QUARTER_CHOICES = [
#     ('0', 'Select Quarter'),
#     ('1', 'January-March'),
#     ('2', 'April-June'),
#     ('3', 'July-September'),
#     ('4', 'October-December'),
# ]

# PURPOSE_CHOICES = [
#     ('0', 'Select Purpose'),
#     ('1', 'Holiday'),
#     ('2', 'VFR'),
#     ('3', 'Business'),
#     ('4', 'Miscellaneous'),
#     ('5', 'Study')
# ]

# MODE_CHOICES = [
#     ('0', 'Select Travelling Mode'),
#     ('1', 'Air'),
#     ('2', 'Tunnel'),
#     ('3', 'Sea')
# ]
gender_CHOICES = [
    ('0', 'Select Gender'),
    ('1', 'Female'),
    ('2', 'Male')
]
ap_lo_CHOICES= [
    ('0', 'Type of Blood Pressure (Diastolic)'),
    ('1', 'Low'),
    ('2', 'High')
]
cholesterol_CHOICES= [
    ('0', 'Do you have Cholesterol ?'),
    ('1', 'Yes'),
    ('2', 'No')
]
gluc_CHOICES= [
    ('0', 'Are you Diebetics Patient?'),
    ('1', 'Yes'),
    ('2', 'No')
]
ap_hi_CHOICES= [
    ('0', 'Type of Blood Pressure (Systolic)?'),
    ('1', 'low'),
    ('2', 'high')
]
smoke_CHOICES= [
    ('0', 'Do you smoke?'),
    ('1', 'Yes'),
    ('2', 'No')
]
alco_CHOICES= [
    ('0', 'Do you Drink Alcohol?'),
    ('1', 'Yes'),
    ('2', 'No')
]
active_CHOICES= [
    ('0','Do you do Exercise Daily?'),
    ('1', 'Yes'),
    ('2', 'No')
]

class TourismForm(forms.Form):
    Age = forms.IntegerField(label="Age(in year)", 
                              validators=[MinValueValidator(0, message="age is invalid!"), 
                              MaxValueValidator(100, message="Please enter valid age")])
    gender = forms.CharField(label="Gender", widget=forms.Select(choices=gender_CHOICES))
    height = forms.FloatField(label="Height(cm)")
    weight = forms.FloatField(label="Weight(Kg)", validators=[MinValueValidator(0.1, message="Enter valid weight")])
    ap_lo = forms.CharField(label="", widget=forms.Select(choices=ap_lo_CHOICES))
    ap_hi = forms.CharField(label="Blood Pressure (Systolic)", widget=forms.Select(choices=ap_hi_CHOICES))
    cholesterol	 = forms.CharField(label="cholesterol", widget=forms.Select(choices=cholesterol_CHOICES))
    gluc = forms.CharField(label="Diebetics Patient", widget=forms.Select(choices=gluc_CHOICES))
    smoke = forms.CharField(label="Do you smoke?", widget=forms.Select(choices=smoke_CHOICES))
    alco = forms.CharField(label="Do you Drink Alcohol", widget=forms.Select(choices=alco_CHOICES))
    active = forms.CharField(label="Do you do Exercise Daily?", widget=forms.Select(choices=active_CHOICES),
                             validators=[MinValueValidator(0, message="age is invalid!"), 
                              MaxValueValidator(100, message="Please enter valid age")])