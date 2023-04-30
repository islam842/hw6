from django import forms
from . import models, parser, forms


class ParserForm(forms.form):
    MEDIA_CHOICES = (
        ('kaktus.kg', 'kaktus.kg'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'kaktus.kg':
            kaktus_parser = parser.parser()
            for i in kaktus_parser:
                models.Kaktus.objects.create(**i)


