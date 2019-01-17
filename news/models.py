from django.db import models

# Create your models here.
class cuencas(models.Model):
    nombrecuenca = models.CharField(max_length=250)
    # DESPUES DEL PUNTO VA LO QUE VA A INCLUIR ESTA INSTRUCCION , EN ESTE CASO LETRAS
    contaminacion = models.CharField(max_length=500)  # lo que va despues del length son lo caracteres disp
    combatir_contaminacion = models.CharField(max_length=100)
    direccionp = models.CharField(max_length=1000)


    def __str__(self):
        return self.nombrecuenca


class partes(models.Model):

    cuencas=models.ForeignKey(cuencas, on_delete=models.CASCADE)
    #si se borra alguna cuenca se elima esa parte del rio-/ondelete, cascade
    periodico = models.CharField(max_length=100)
    tituloN = models.CharField(max_length=1000)