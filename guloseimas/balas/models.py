from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Bala(models.Model):
	nome = models.CharField('Nome', max_length=50)
	preco = models.DecimalField('Preço', max_digits=4, decimal_places=2, validators=[MinValueValidator(limit_value=0, message="Preço não pode ser negativo")])
	#id = models.AutoField(primary_key=True)
	quantidade = models.IntegerField('Quantidade', validators=[MinValueValidator(limit_value=0, message="Quantidade não pode ser menor que 0")])
	tipo = models.BooleanField('Bala para diabéticos')
	class Meta:
		verbose_name = 'Bala'
		verbose_name_plural = 'Balas'

	def __str__(self):
			return self.nome