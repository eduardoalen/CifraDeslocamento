# Recebe uma mensagem do usuário e a quantidade vezes que ele deseja
# rotacionar o alfabeto para que sua mensagem seja criptografada.

#Recebe a mensagem e uma chave
def Encriptar(mensagem, key):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    #Variavel que vai conter a mensagem encriptada
    codificado = ""

    for i in mensagem: # (ord(b)=98 - ord(a)=97 + 1) Modulo 26(resto) = 2
        indice_letra_codificada = ((ord(i) - ord('a')) + key) % 26
        codificado += alfabeto[indice_letra_codificada] #alfabeto[2] = c

    return codificado

def Decriptar(cripto, key):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    mensagemDecriptada = ""
    
    for i in cripto:
        indice_letra_decodificada = ((ord(i) - ord('a')) + 26 - key) % 26
        mensagemDecriptada += alfabeto[indice_letra_decodificada]
    
    return mensagemDecriptada

print("---> Cifra de Cesar (Deslocamento) <---\n")
mensagem = str(input("Digite em minúsculo a palavra que será codificado: "))
num_posicoes = int(input("Digite o número de posições que o alfabeto será rotacionado: "))

mensagemEncriptada = Encriptar(mensagem, num_posicoes)
mensagemDecriptada = Decriptar(mensagemEncriptada, num_posicoes)
print("Sua palavra criptografada é ", mensagemEncriptada)
print("Sua palavra decriptografada é ", mensagemDecriptada)