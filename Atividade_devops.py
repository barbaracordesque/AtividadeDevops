nApart = int(input('Digite o número de apartametos:\n'))
valDiaria = float (input('Digite o valor da diária:\n'))
valDesconto = valDiaria / 100 * 25
valPromo = valDiaria - valDesconto

print ('O valor da diária com desconto é: %.2f' %valPromo)

arredTotal = nApart * valPromo

print ('O valor caso atinja a ocupação total é: %2.f' %arredTotal)

arredParcial = nApart / 100 * 70
valParcial = arredParcial * valPromo

print ('O valor caso atinja a ocupação parcial é: %2.f' %valParcial)

diariaTotal = (nApart * valDiaria) - arredTotal

print ('O valor que o hotel deixará de arrecadar com a promoção é: %2.f' %diariaTotal)

input ()


