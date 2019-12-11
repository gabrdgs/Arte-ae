# -*- coding: utf-8 -*-
from django import forms
from arte_ae.models import Evento

class EventoForm(forms.ModelForm):
    class Meta():
        model = Evento
        fields = [
            'logradouro',
            'cep',
            'bairro',
            'localidade',
            'uf',
            'numero',
            'imagem',
            'nome',
            'data',
            'horario',
            'descricao'
        ]

        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.DateInput(attrs={'type': 'time'})
        }