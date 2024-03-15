from ..models import Oferta

def obtener_ofertas():
    ofertas = Oferta.objects.all()
    return ofertas

def obtener_oferta(var_pk):
    oferta = Oferta.objects.get(pk=var_pk)
    return oferta

# def actualizar_oferta(var_pk, new_var):
#     oferta = obtener_oferta(var_pk)
#     oferta.name = new_var["name"]
#     oferta.save()
#     return oferta

# def crear_oferta(var):
#     oferta = Oferta(monto=var["monto"], tipo=var["tipo"],)
#     oferta.save()
#     return oferta