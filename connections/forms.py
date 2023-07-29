from django import forms
from connections.models import Consumer, Circle, Division, SubDivision,Loads

class PersonCreationForm(forms.ModelForm):
    required_css_class = 'form-container'

    class Meta:
        model = Consumer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 800px;'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'Applied_Category': forms.Select(attrs={'class': 'form-control1','label':'Applied_Category', 'id':'Applied_Category','onchange': 'updateAppliedLoad()' }),
            'Applied_Load': forms.TextInput(attrs={'class': 'form-control1', 'label':'Applied Load','id': 'id_Applied_Load', }),
            'circle': forms.Select(attrs={'class': 'form-control1',  }),
            'division': forms.Select(attrs={'class': 'form-control1', }),
            'subdivision': forms.Select(attrs={'class': 'form-control1', }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['division'].queryset = Division.objects.none()
        self.fields['subdivision'].queryset = SubDivision.objects.none()

        if 'circle' in self.data:
            try:
                circle_id = int(self.data.get('circle'))
                self.fields['division'].queryset = Division.objects.filter(circle_id=circle_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty division queryset

        if 'division' in self.data:
            try:
                division_id = int(self.data.get('division'))
                self.fields['subdivision'].queryset = SubDivision.objects.filter(division_id=division_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Subdivision queryset

        elif self.instance.pk:
            self.fields['division'].queryset = self.instance.circle.division_set.order_by('name')
            self.fields['subdivision'].queryset = self.instance.division.subdivision_set.order_by('name')