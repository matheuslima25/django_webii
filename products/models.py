from django.db import models

class Categoria(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome


class Produto(models.Model):
  nome = models.CharField(max_length=100)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  preco = models.DecimalField(max_digits=5, decimal_places=2)
  imagem = models.FileField(upload_to='produtos/', null=True, blank=True)

  def __str__(self):
        return self.nome
