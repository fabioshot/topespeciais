from django.db import models

class Cidade(models.Model):

    # nome do atributo = tipo(caracteristicas)

    nome = models.CharField(max_length = 50)
    estado = models.CharField(max_length = 2, help_text='Infome apenas as sigla')

    #apenas imprimir o objeto

    def __str__(self):
        #Paranavaí (PR)
        return self.nome + '('+ self.estado + ')'



class Tipo(models.Model):
    descricao = models.CharField(max_length=50, help_text = 'Tipo do Aminal')

    def __str__(self):
        return self.descricao




class Animais(models.Model):
    doador = models.CharField(max_length=50, help_text = 'nome completo')
    email = models.CharField(max_length= 50)
    telefone = models.CharField(max_length= 15)
    nascimento = models.DateField('Data de nascimento')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    raca = models.CharField(max_length= 50)
    apelido = models.CharField(max_length= 50)
    vacinas = models.BooleanField() 

    def __str__(self):
        return self.nome + ' - ' + str(self.nascimento)



