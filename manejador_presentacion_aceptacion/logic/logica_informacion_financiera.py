from ..models import InformacionFinanciera

# def get_cliente():
#     queryset = Cliente.objects.all()
#     return (queryset)


def crear_informacion_financiera(form):
    informacion_financiera = form.save()
    informacion_financiera.save()
    return()
