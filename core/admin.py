from django.contrib import admin
from .models import dadosEmpr

class dados(admin.ModelAdmin):
     list_display='cnpjReme','nomeEprOne','telOne','logOne','ruaOne','cityOne','estateOne','cepOne','contaOne','cnpjDest', 'nomeEprTwo', 'telTwo', 'cnpjDest', 'logTwo', 'ruaTwo', 'cityTwo', 'estateTwo', 'cepTwo', 'contaTwo', 'nuCOT','num1','num2','num4','num5','num6','num7','num8','num9', 
admin.site.register(dadosEmpr, dados)