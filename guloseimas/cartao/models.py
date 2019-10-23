from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Cartao(models.Model):
	codigo = models.CharField('Código', max_length=50)
	saldo = models.DecimalField('Saldo', max_digits=4, decimal_places=2, validators=[MinValueValidator(limit_value=0, message="Saldo não pode ser negativo")])
	class Meta:
		verbose_name = 'Cartão'
		verbose_name_plural = 'Cartões'

	def __str__(self):
			return self.codigo