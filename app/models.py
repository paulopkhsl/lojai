from django.db import models
# Create your models here.
class Categoria(models.Model): #tabela
    nome = models.CharField(max_length=100) #campo tabela

    class Meta:
        verbose_name_plural = "Categorias"

        def __str__(self):
            return self.nome
        

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to= 'static/')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria =  models.ForeignKey(Categoria, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural= "Produtos"

    def __str__(self):
        return f'{self.categoria} {self.nome}'