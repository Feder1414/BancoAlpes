from django import forms

from .models import Cliente, InformacionFinanciera


class ClienteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                                     'type':"date"}))
                                                    
    class Meta:
        
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'direccion',
            'ciudad',
            'departamento',
            'codigo_postal',
            'pais',
            'telefono',
            'email',
            'fecha_nacimiento',
        ]
        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'direccion' : 'Direccion',
            'ciudad' : 'Ciudad',
            'departamento' : 'Departamento',
            'codigo_postal' : 'Codigo Postal',
            'pais' : 'País',
            'telefono' : 'Teléfono',
            'email' : 'Email',
            'fecha_nacimiento': 'Fecha de nacimiento',
        }

class InformacionFinancieraForm(forms.ModelForm):                                                
    class Meta:
        
        model = InformacionFinanciera
        fields = [
            'ingresos',
            'egresos',
            'activos',
            'pasivos',
            'historial_crediticio',
            'puntuacion_crediticia',
            'antiguedad_laboral',
            'tipo_empleo',
            'estado_civil',
            'numero_dependientes',
            'historial_bancario',
            'garantias',
            'tipo_vivienda',
            'educacion',
            'cliente'
        ]
        labels = {
            'ingresos' : 'Ingresos',
            'egresos' : 'Egresos',
            'activos' : 'Activos',
            'pasivos' : 'Pasivos',
            'historial_crediticio': 'Historial crediticio',
            'puntuacion_crediticia' : 'Puntuacion creditica',
            'antiguedad_laboral':'Antiguedad laboral',
            'tipo_empleo' : 'Tipo de empleo',
            'estado_civil' : 'Estado civil',
            'numero_dependientes' : 'Numero dependientes',
            'historial_bancario' : 'Historial bancario',
            'garantias' : 'Garantías',
            'tipo_vivienda' : 'Tipo vivienda',
            'educacion' : 'Educación ',
            'cliente' : 'Cliente'
        }



        
