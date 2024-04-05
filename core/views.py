from django.shortcuts import render, redirect
from .models import dadosEmpr
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO



def home(request):
    dados = dadosEmpr.objects.all()
    return render(request, 'index.html', {'dados': dados})

def formrec(request):
    a=request.POST['cnpjReme']
    b=request.POST['nomeEprOne']
    c=request.POST['telOne']
    d=request.POST['logOne']
    e=request.POST['ruaOne']
    f=request.POST['cityOne']
    g=request.POST['estateOne']
    h=request.POST['cepOne']
    i=request.POST['contaOne']
    j=request.POST['cnpjDest']
    k=request.POST['nomeEprTwo']
    l=request.POST['telTwo']
    m=request.POST['logTwo']
    n=request.POST['ruaTwo']
    o=request.POST['cityTwo']
    p=request.POST['estateTwo']
    q=request.POST['cepTwo']
    r=request.POST['contaTwo']
    s=request.POST['nuCOT']
    t=request.POST['num1']
    u=request.POST['num2']
    v=request.POST['num3']
    x=request.POST['num4']
    y=request.POST['num5']
    z=request.POST['num6']
    zz=request.POST['num7']
    xz=request.POST['num8']
    xv=request.POST['num9']
    dados=dadosEmpr(cnpjReme=a, nomeEprOne=b, telOne=c, logOne=d, ruaOne=e, cityOne=f, estateOne=g, cepOne=h, contaOne=i, cnpjDest=j, nomeEprTwo=k, telTwo=l, logTwo=m, ruaTwo=n, cityTwo=o, estateTwo=p, cepTwo=q, contaTwo=r, nuCOT=s, num1=t, num2=u, num3=v, num4=x, num5=y, num6=z, num7=zz, num8=xz, num9=xv)
    dados.save()
    return redirect('home')


def cotacao(request):
    return render(request, 'cotacao.html')

def index(request):
    return render(request, 'index')

def delete(request, id):
    dados = dadosEmpr.objects.get(id=id)
    dados.delete()
    return redirect('home')

def update(request, id):
    dados=dadosEmpr.objects.get(id=id)
    return render(request, 'update.html', {'dados':dados})

def updcot(request, id):
    a=request.POST['cnpjReme']
    b=request.POST['nomeEprOne']
    c=request.POST['telOne']
    d=request.POST['logOne']
    e=request.POST['ruaOne']
    f=request.POST['cityOne']
    g=request.POST['estateOne']
    h=request.POST['cepOne']
    i=request.POST['contaOne']
    j=request.POST['cnpjDest']
    k=request.POST['nomeEprTwo']
    l=request.POST['telTwo']
    m=request.POST['logTwo']
    n=request.POST['ruaTwo']
    o=request.POST['cityTwo']
    p=request.POST['estateTwo']
    q=request.POST['cepTwo']
    r=request.POST['contaTwo']
    s=request.POST['nuCOT']
    t=request.POST['num1']
    u=request.POST['num2']
    v=request.POST['num3']
    x=request.POST['num4']
    y=request.POST['num5']
    z=request.POST['num6']
    zz=request.POST['num7']
    xz=request.POST['num8']
    xv=request.POST['num9']
    dados=dadosEmpr.objects.get(id=id)
    dados.cnpjReme=a
    dados.nomeEprOne=b
    dados.telOne=c
    dados.logOne=d
    dados.ruaOne=e
    dados.cityOne=f
    dados.estateOne=g
    dados.cepOne=h
    dados.contaOne=i
    dados.cnpjDest=j
    dados.nomeEprTwo=k
    dados.telTwo=l
    dados.logTwo=m
    dados.ruaTwo=n
    dados.cityTwo=o
    dados.estateTwo=p
    dados.cepTwo=q
    dados.contaTwo=r
    dados.nuCOT=s
    dados.num1=t
    dados.num2=u
    dados.num3=v
    dados.num4=x
    dados.num5=y
    dados.num6=z
    dados.num7=zz
    dados.num8=xz
    dados.num9=xv   
    dados.save()
    return redirect('home')

def cot_list(request):
    dados = dadosEmpr.objects.all()
    context = {'dados': dados}
    return render(request, 'items_list.html', context)

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def generate_pdf(request, id):
    # Recupere os dadosEmpr com o ID fornecido
    dados = dadosEmpr.objects.filter(id=id)
    
    # Verifique se há um objeto correspondente ao ID
    if dados.exists():
        # Renderize o PDF apenas com os dados correspondentes
        context = {'dados': dados}
        pdf = render_to_pdf('items_list.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "cotacao_%s.pdf" % id  # Use o ID no nome do arquivo
            content = "inline; filename='%s'" % filename
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % filename
            response['Content-Disposition'] = content
            return response
    else:
        return HttpResponse("Dados não encontrados para o ID fornecido.")
    
def my_view(request, id):
    return generate_pdf(request, id)