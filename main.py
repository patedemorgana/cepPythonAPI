import requests

def main():

    print('###############################')
    print('######   Consulta Cep    ######')
    print('###############################')
    print()

    cep_input = input("Digita o cep para consulta:")

    if len(cep_input) != 8:
        print("Cep invalido")
        exit()

    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    a = r.json()

    if 'erro' not in a:

        print('CEP: {}'.format(a['cep']))
        print('Logradouro: {}'.format(a['logradouro']))
        print('Complemento: {}'.format(a['complemento']))
        print('Bairro: {}'.format(a['bairro']))
        print('Localidade: {}'.format(a['localidade']))
        print('UF: {}'.format(a['uf']))
        print('IBGE: {}'.format(a['ibge']))
        print('GIA: {}'.format(a['gia']))
        print('DDD: {}'.format(a['ddd']))
        print('SIAFI: {}'.format(a['siafi']))
        
    else:
        print("CEP não encontrado")

    o = int(input('Procurar outro cep? \n1. Sim\n2. Sair\n'))
    if o == 1:
        main()
    else:
        exit()
        
if __name__ == '__main__':
    main()