#!/usr/bin/python3

try:
    from pdfrw import PdfReader, PdfWriter
except ImportError:
    print("Instale em seu sistema a biblioteca pdfrw!\n\n")
    print("sudo apt install python3-pdfrw\n")
    quit()

# Limpa o \n do final da linha na lista


def remove_quebra_de_linha(linha):
    return linha.replace('\n', '')


# Vai ser o responsável em escrever o PDFao
writer = PdfWriter()

# Lista contendo arquivos pdf, linha a linha, com o caminho completo do sistema de arquivos
# Deve estar algo como:
# /home/meu_usuario/arquivos_pdf/arquivo1.pdf
# /home/meu_usuario/arquivos_pdf/arquivo2.pdf
pdf_list = open("my_pdfs.txt")

# caminho completo do arquivo de saída. Dessa forma abaixo, gera na pasta do script
pdefao = 'super.pdf'

# Lê linha a linha da lista de pdfs e adiciona ao arquivao
for arquivo in pdf_list:
    arquivo = remove_quebra_de_linha(arquivo)
    writer.addpages(PdfReader(arquivo).pages)

writer.write(pdefao)
