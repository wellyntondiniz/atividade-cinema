def convertAvaliacao(avaliacao):
    if (avaliacao == 1):
        return "Ótimo"
    if (avaliacao == 2):
        return "Bom"
    if (avaliacao == 3):
        return "Regular"
    if (avaliacao == 4):
        return "Péssimo"
    


quantidade = 0
quantidadeOtimo = 0
quantidadeBom = 0
quantidadeRegular = 0
quantidadePessimo = 0
idadeMaisVelho = 0
avaliacaoMaisVelho = 0
idadeMaisNovo = 0
avaliacaoMaisNovo = 0

while (True):
    avaliacao = int(input("Informe sua avaliação (1-Ótimo 2-Bom 3-Regular 4-Péssimo): "))
    idade = int(input("Informe sua idade:"))
    
    quantidade += 1
    
    if avaliacao == 1:
        quantidadeOtimo += 1
    if avaliacao == 2:
        quantidadeBom += 1
    if avaliacao == 3:
        quantidadeRegular += 1
    if avaliacao == 4:
        quantidadePessimo += 1
    
    if (idade > idadeMaisVelho):
        idadeMaisVelho = idade
        avaliacaoMaisVelho = avaliacao
    
    if (idade < idadeMaisNovo) or (idadeMaisNovo == 0):
        idadeMaisNovo = idade
        avaliacaoMaisNovo = avaliacao
    
    continua = int(input("Deseja continuar? (1-Sim 2-Não): "))
    if continua == 2:
        break
    
print("Total de respondentes: ", quantidade)
print("Total de resposta Ótimo: ", quantidadeOtimo)
print("Total de resposta Bom: ", quantidadeBom)
print("Total de resposta Regular: ", quantidadeRegular)
print("Total de resposta Péssimo: ", quantidadePessimo)
print("O respondente mais velho tem ", idadeMaisVelho)
print("A resposta do respondente mais velho foi: ", convertAvaliacao(avaliacaoMaisVelho))
print("O respondente mais novo tem ", idadeMaisNovo)
print("A resposta do respondente mais novo foi: ", convertAvaliacao(avaliacaoMaisNovo))







