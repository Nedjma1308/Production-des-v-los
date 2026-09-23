# Create your models here.
class QuantiteProduit(models.Model):
 quantite = models.IntegerField()
 matiere_premiere = models.ForeignKey(
 Produit,
 on_delete=models.PROTECT,
 )
 class Meta:
 abstract = True

