from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from caixas.models import Conta
from pessoas.models import Pessoa

def buscaFluxo(request):
    if ((request.method == 'POST') & (request.POST.get('Inicial') != '') & (request.POST.get('Final') != '')) :
        
        Inicial = datetime.strptime(request.POST.get('Inicial', ''), '%d/%m/%Y %H:%M:%S')
        Final  = datetime.strptime(request.POST.get('Final', ''), '%d/%m/%Y %H:%M:%S')

        somaTotal = 0

        try:
            contas = Conta.objects.filter(data__range=(Inicial, Final))

            for conta in contas:
                if conta.tipo == 'E':
                    somaTotal += conta.valor
                else:
                    somaTotal -= conta.valor
        except:
            contas = []

        return render(request, 'fluxo/fluxoCaixa.html', {'contas' : contas, 'somaTotal': somaTotal ,'Inicial': Inicial, 'Final': Final})

    return render(request, 'fluxo/fluxoCaixa.html', {'contas' : []})