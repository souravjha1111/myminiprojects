from django import forms

class TitanicForm(forms.Form):
    Age = forms.IntegerField(label='Your age', max_value=999,min_value=0)
    Gender = forms.CharField(label='please type M or F')
    Parch = forms.IntegerField(label='Your parch', max_value=999,min_value=0)
    Pclass = forms.IntegerField(label = 'Enter your class as 1 or 2 or 3',min_value=1, max_value=3)
    SibSp = forms.IntegerField(label='enter number of familiy members from 0 to 8',max_value=8, min_value=0)
    Embarked = forms.CharField(label = 'enter embarked status')
    Fare = forms.IntegerField(label = 'your price in $ btw 7$ to 150$')
    class Meta:
        fields = ['Age', 'Gender', 'Parch', 'SibSp', 'Embarked', 'Fare']


class StockForm(forms.Form):
    stock_name = forms.CharField(label='Enter stock initials')
    day_hour = forms.CharField(label = 'enter 1d or 1h')
    class Meta:
        fields = ['stock_name', 'day_hour']