def guia():
    if questao == 1:
        idade = int(input('Informe sua idade: '))
        if idade >= 18:
            print('Usuário maior de idade')
        elif idade >0:
            print('Usuário menor de idade')
        else:
            print('Idade indevida')


    if questao == 2:
        lista = [1, 3, False, 'Cachorro', 3.1, 'Jacaré', True, 21.1, 'True', False, 2, 'Romário', 4.32, 'Dinossauro', 98]
        cont_int = 0
        cont_float = 0
        cont_str = 0
        cont_bool = 0
        for i in range (len(lista)):
            if type(lista[i]) == int:
                cont_int += 1
            elif type(lista[i]) == float:
                cont_float += 1
            elif type(lista[i]) == str:
                cont_str += 1
            elif type(lista[i]) == bool:
                cont_bool += 1
        print('O número de inteiros é igual a: ', cont_int)
        print('O número de floats é igual a: ', cont_float)
        print('O número de strings é igual a: ', cont_str)
        print('O número de booleanos é igual a: ', cont_bool)


    if questao == 3:
        import datetime
        atual = datetime.datetime.now()
        dia = int(input('Dia do nascimento: ')) 
        mes = int(input('Mês do nascimento: ')) 
        ano = int(input('Ano do nascimento: ')) 
        total = datetime.datetime(ano, mes, dia)
        dias = atual - total
        hoje = "%d dias" % dias.days
        print('Você está vivo(a) a:', hoje)


    if questao == 4:
        numero = int(input('Digite um número: '))
        contador = 0
        total = []
        t = 0
        while t < 100:
            t = numero*contador
            contador += 1
            total.append(t)
            for i in total:
                if i > 100:
                    total.pop(-1)
        print(total)

    if questao == 5:
        numero = int(input("Digite um número: "))
        print(f'{[numero * i for i in range(1, 100 // numero + 1)]}')


    if questao == 6:
        lista = []
        for i in range (2):
            numero = int(input('Digite um número: '))
            lista.append(numero)
            lista.sort()
        print(lista)


    if questao == 7:
        velocidade = float(input('Informe a velocidade do veículo(KM/h): '))
        peso = float(input('Informe o peso do veículo(Kg): '))
        mps = velocidade/3.6
        cinetica = ((peso/2)*(mps)**2)
        print(f'A velocidade do veículo é de: {round(mps,2)}m/s')
        print(f'A energia cinética gerada é de: {round(cinetica/1000,2)}KJ')


    if questao == 8:
        temp_u = float(input("Temperatura em ºC: "))
        temp_f = (temp_u*1.8)+32
        print(temp_f, 'ºF')


    if questao == 9:
        raio = float(input("Informe o raio da circunferência(m): "))
        area = 3.14159*raio**2
        print(f'A área da circunferência é de {area}m²')


    if questao == 10:
        b = float(input('Informe a base do triângulo(m): '))
        h = float(input('Informe a altura do triângulo(m): '))
        a = (b*h)/2
        print(f'A área do triângulo é de {a}m²')


    if questao == 11:
        lista = []
        for i in range(3):
            lista.append(float(input('Informe os lados do triângulo: ')))
        if lista[0] == lista[1] and lista[0] == lista[2]:
            print('O triângulo é equilátero')
        elif lista[0] != lista[1] and lista[1] == lista[2] or lista[0] == lista[1] and lista[1] != lista[2] or lista[0] == lista[2] and lista[1] != lista[2]:
            print('O triângulo é isósceles')
        else:
            print('O triângulo é escaleno')


    if questao == 12:
        soma = 0
        for i in range(101):
            if i %2 == 0:
                soma +=i
        print(soma)


    if questao == 13:
        texto = input("Digite um texto: ").lower().split()
        vogais = ['a', 'á', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'y']
        letras_t = 0
        vogal_t = 0
        l2 = []
        for i in texto:
            l1 = []
            for l in i:
                l1.append(l)
                letras_t += 1
            l2.append(l1)
        l3 = [k for p in l2 for k in p]
        for g in l3:
            if g in vogais:
                vogal_t += 1       
        print(vogal_t, 'vogais totais')
        print(letras_t, 'letras totais')
        print(len(texto), 'palavras inseridas')


    if questao == 14:
        import random
        l_nomes = ['Walter', 'Marcos', 'Bruno', 'Lucas', 'Samuel', 'Letícia', 'Pedro', 'Bernardo', 'Ingrid', 'João', 'Wallace', 'Mariana', 'Janaína', 'Priscila', 'Fabio', 'Yernadez', 'Rubem', 'Samuel', 'Letícia', 'Fernando', 'Pedro', 'João', 'Ronaldo', 'Pricila']
        n = len(l_nomes)
        sorteio = set()
        while len(sorteio) < 5:
            sorteio.add(random.choice(l_nomes))
        print(sorteio)


    if questao == 15:
        import random
        senha = []
        simb = ['!', '@', '#', '$', '%', '&', '*']
        nume = [0, 1, 2, 3, 4, 5, 6, 7 , 8, 9]
        le_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        le_mai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        tamanho = int(input('Defina quantos caracteres deseja na sua senha: '))
        ysimb = input('Deseja adicionar símbolos a sua senha?(s/n): ').upper()
        ynume = input('Deseja adicionar números a sua senha?(s/n): ').upper()
        yle_min = input('Deseja adicionar letras minúsculas a sua senha?(s/n): ').upper()
        yle_mai = input('Deseja adicionar letras maiúsculs a sua senha?(s/n): ').upper()
        if ysimb == 'S':
            senha += simb
        if ynume == 'S':
            senha += nume
        if yle_min == 'S':
            senha += le_min
        if yle_mai == 'S':
            senha += le_mai
        senhaf = ''.join(random.choice(senha) for i in range(tamanho))
        print(senhaf)


    if questao == 16:
        m = float(input('Informe a massa da lata(g): '))
        h = float(input('Informe a altura da lata(cm): '))
        r = float(input('Informe o raio da lata(cm): '))
        v_lata = round(3.14*r**2*h,2)
        d_lata = round(m/v_lata,2)
        if d_lata >= 1:
            print('A lata irá afundar na água')
        #elif d_lata == 1:
        #    print('A lata ficará suspensa no meio da água')
        else:
            print('A lata irá boiar na água')


    if questao == 17:
        from statistics import mean
        notas = []
        nota = []
        n1 = 0
        print('Caso deseje finalizar, digite "Fim"')
        while n1 != 'fim':
            n1 = input('Nota: ').lower()
            if 'fim' in n1:
                continue
            else:
                notas.append(n1)
                notas = [float(i) for i in notas]
        print(mean(notas))



    if questao == 18:
        #amigos = ('Ana', 'Bia', 'Carlos', 'Sofia')
        #novos_amigos = ('Will', 'Victor')
        #for amigo in novos_amigos:
        #    amigos.append(amigo)
        #    print(amigos)
        #Criou uma Turple, portanto imutável
        #Solução em lista
        amigos = ['Ana', 'Bia', 'Carlos', 'Sofia']
        novos_amigos = ['Will', 'Victor']
        for amigo in novos_amigos:
            amigos.append(amigo)
            print(amigos)
        #Solução em set
        amigos = {'Ana', 'Bia', 'Carlos', 'Sofia'}
        novos_amigos = {'Will', 'Victor'}
        amigos.update(novos_amigos)
        print(amigos)


    if questao == 19:
        palavra = ['P', 'Y', 'T', 'H', 'O', 'N']
        vidas = 7
        tentativa = []
        prototipo = ['_', '_', '_', '_', '_', '_']
        letra_e = []
        print('A palavra tem', len(palavra), 'letras')
        while tentativa != palavra and vidas > 0:
            letra = (input('Insira uma letra: ')).upper()
            if letra in 'PYTHON':
                if len(tentativa) >= len(palavra):
                    tentativa.pop()
                for i in range(len(palavra)):    
                    if letra == palavra[i]:
                        tentativa.insert(i, letra)
                        print('Letra correta')
                        print(''.join(tentativa))
            else:
                letra_e.append(letra)
                vidas -= 1
                print('Letra errada.', vidas, 'restantes!')
            print('Letras erradas: ', letra_e)
        if vidas == 0:
            print('Acabou, a palavra certa era:', ''.join(palavra).lower())
        else:
            print('Parabéns! Você acertou! A palavra certa é:', ''.join(palavra).lower())


    if questao == 20:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        resultado = (n1**2 + n2**2)
        print(resultado)


    if questao == 21:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        resultado = (n1 + n2)**2
        print(resultado)


    if questao == 22:
        from statistics import mean
        notas = []
        aulas = int(input('Quantidade total de aulas: '))
        presenca = int(input('Aulas que compareceu: '))
        presencas = presenca*100/aulas
        for i in range(5):
            i = float(input(f'Digite a {i+1}º nota '))
            notas.append(i)
            media = mean(notas)
        if media >= 6 and presencas >= 70:
            print('Aluno aprovado')
        elif media < 6 and presencas < 70:
            print('Aluno reprovado por nota e faltas')
        elif media >= 6 and presencas <70:
            print('Aluno reprovado por faltas')
        else:
            print('Aluno reprovado por nota')


    if questao == 23:
        palavra = input('Digite uma frase: ')
        np = palavra.split()
        print(np)


    if questao == 24:
        dados = ['João', 56, 'Gilberto', 46, 'Antonio', 35, 'Enzo', 12]
        t = len(dados)
        tamanho = int(t/2)
        for i in range(tamanho):
            print('A pessoa', dados[0], 'tem', dados[1], 'anos de vida')
            dados.remove(dados[0])
            dados.remove(dados[0])
        #Preservando a lista original
        #dados = ['João', 56, 'Gilberto', 46, 'Antonio', 35, 'Enzo', 12]
        #t = len(dados)
        #tamanho = int(t/2)
        #for i in range(tamanho):
        #    print('A pessoa', dados[2*i], 'tem', dados[2*i + 1], 'anos de vida')


    if questao == 25:
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        print([numero for numero in range(len(numeros)) if numero %3 == 0])


    if questao == 26:
        #for X in range(10):
        #print(X)
        #Erro de identação
        for X in range(10):
            print(X)    


    if questao == 27:
        lista = [['Ximiun','Yakborgob','Gefoouil','Zoetuso' ],
        ['Cawao', 'Tarfeura', 'Haykui', 'Esuma' ],
        ['Dauceyarn', 'Harriric', 'Celeblyaborn', 'Khadpu' ],
        ['Hayla', 'Diono', 'Olficiolu', 'Venbou']]
        print(lista[1][1])


    if questao == 28:
        amigos = ['Ana', 'Bia', 'Carlos', 'Sofia']
        novos_amigos = ['Will', 'Victor']
        amigos.append(novos_amigos[0])
        amigos.append(novos_amigos[1])
        print(amigos)


    if questao == 29:
        todos = ['Ximiun','Yakborgob','Gefoouil','Zoetuso', 'Cawao', 'Tarfeura', 'Haykui', 'Esuma', 'Dauceyarn', 'Harriric', 'Celeblyaborn', 'Khadpu', 'Hayla', 'Diono', 'Olficiolu', 'Venbou']
        banidos = ['Yakborgob', 'Cawao', 'Celeblyaborn', 'Hayla']
        convidados = todos
        for i in banidos:
            convidados.remove(i)
        print(convidados)


    if questao == 30:
        Valor = 0
        quant = int(input('Quantidade do produto 1324: '))
        while quant != 0:
            Valor += 6.45*quant
            quant = 0
        quant = int(input('Quantidade do produto 6548: '))
        while quant != 0:
            Valor += 2.37*quant
            quant = 0
        quant = int(input('Quantidade do produto 0987: '))
        while quant != 0:
            Valor += 5.32*quant
            quant = 0
        quant = int(input('Quantidade do produto 7623: '))
        while quant != 0:
            Valor += 6.45*quant
            quant = 0
        quant = int(input('Quantidade do produto 1001: '))
        while quant != 0:
            quant = int(input('Quantidade do produto: '))
            Valor += 5.32*quant
            quant = 0
        print(Valor)


    if questao == 31:
        vezes = int(input('Informe quantas pessoas serão registradas: '))
        for i in range(vezes):
            signo = input('Infrome sua data de aniversário(d/m): ')
            dia, mes = map(int, signo.split('/'))
            if (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 20):
                print('Você é do signo de Áries')
            elif (mes == 4 and 21 <= dia <= 30) or (mes == 5 and 1 <= dia <= 20):
                print('Você é do signo de Touro')
            elif (mes == 5 and 21 <= dia <= 31) or (mes == 6 and 1 <= dia <= 20):
                print('Você é do signo de Gêmeos')
            elif (mes == 6 and 21 <= dia <= 30) or (mes == 7 and 1 <= dia <= 22):
                print('Você é do signo de Câncer')
            elif (mes == 7 and 23 <= dia <= 31) or (mes == 8 and 1 <= dia <= 22):
                print('Você é do signo de Leão')
            elif (mes == 8 and 23 <= dia <= 31) or (mes == 9 and 1 <= dia <= 22):
                print('Você é do signo de Virgem')
            elif (mes == 9 and 23 <= dia <= 30) or (mes == 10 and 1 <= dia <= 22):
                print('Você é do signo de Libra')
            elif (mes == 10 and 23 <= dia <= 31) or (mes == 11 and 1 <= dia <= 21):
                print('Você é do signo de Escorpião')
            elif (mes == 11 and 22 <= dia <= 30) or (mes == 12 and 1 <= dia <= 21):
                print('Você é do signo de Sagitário')
            elif (mes == 12 and 22 <= dia <= 31) or (mes == 1 and 1 <= dia <= 19):
                print('Você é do signo de Capricórnio')
            elif (mes == 1 and 20 <= dia <= 31) or (mes == 2 and 1 <= dia <= 18):
                print('Você é do signo de Aquário')
            elif (mes == 2 and 19 <= dia <= 29) or (mes == 3 and 1 <= dia <= 20):
                print('Você é do signo de Peixes')
            else:
                print('Data inválida')


    if questao == 32:
        quadros = 64
        graos = 1
        for i in range(quadros):
            graos *= i+1
        print(graos)


    if questao == 33:
        entrada = input('Digite um texto: ')
        proibido = ['futebol', 'religião', 'política']
        texto = entrada.lower().split()
        letras = 0
        for i in texto:
            l1 = []
            for l in i:
                l1.append(l)
                letras += 1
        for k in texto:
            if k in proibido:
                print('Texto não autorizado')
                break
        else:
            print(entrada)
            print('Total de letras:', letras)


    if questao == 34:
        texto = ('No meio o caminho tinha uma pedra tinha uma pedra no meio do caminho tinha uma pedra no meio do caminho tinha uma pedra').split()
        for i in range(len(texto)):
            texto[i] = texto[i].replace('pedra', 'Repitiliana')
        print(' '.join(texto))


    if questao == 35:
        quant = int(input('Quantos nomes serão adicionados: '))
        nomes = []
        for i in range(quant):
            nome = input('Digite um nome: ')
            nomes.append(nome)
        nomes.sort()
        print(nomes)


    if questao == 36:
        n = int(input('Digite um número: '))
        contador = 1000
        while contador > 0:
            contador -= 1
            if n % 2 == 0:
                n = n/2
            else:
                n = n*3+1
            print(n)


    if questao == 37:
        p_secreta = ['C', 'A', 'R', 'R', 'O']
        prototipo = ['_', '_', '_', '_', '_']
        contador = 7
        usuario = []
        p_usuario = []
        while p_secreta != prototipo and contador > 0:
            print('Você tem', contador, 'tentativas restante')
            contador -= 1
            tentativa = input('Digite uma palavra: ')
            usuario = tentativa.upper()
            p_usuario = usuario.split()
            for i in p_usuario:
                l1 = []
                for l in i:
                    l1.append(l)
            for k in range(5):
                if l1[k] == p_secreta[0]:
                    prototipo.pop(k)
                    prototipo.insert(k, '?')
                if l1[k] == p_secreta[1]:
                    prototipo.pop(k)
                    prototipo.insert(k, '?')
                if l1[k] == p_secreta[2]:
                    prototipo.pop(k)
                    prototipo.insert(k, '?')
                if l1[k] == p_secreta[3]:
                    prototipo.pop(k)
                    prototipo.insert(k, '?')
                if l1[k] == p_secreta[4]:
                    prototipo.pop(k)
                    prototipo.insert(k, '?')
            for n in range(len(p_secreta)):
                if l1[n] == p_secreta[n]:
                    prototipo.pop(n)
                    prototipo.insert(n, p_secreta[n])
            print(prototipo)
            if prototipo == p_secreta:
                print('Parabéns, a palavra é', ''.join(p_secreta).lower())
                break
            if contador == 0:
                print('Uma pena, você perdeu, a palavra era:', ''.join(p_secreta).lower())
            prototipo = ['_', '_', '_', '_', '_']


    if questao == 38:
        animal = {'Cor': 'laranja', 'Dieta': 'carnívoro', 'Raça': 'felinos', 
          'País': 'sibéria', 'Continente': 'asiático',
          'Nada': 'sim', 'Escala': 'sim', 'Salta': 'sim',
          'Olfato aguçado': 'sim', 'Visão noturna': 'sim',
          'Dias de gestação': '103'
        }
        resposta = 'tigre'
        continuar = True
        l1 = []
        while continuar == True:
            for i in animal:
                l1.append(i)
            for l in range(len(animal)):
                pergunta = input(f'{l1[l]}?: ').lower()
                if pergunta in animal.get(l1[l]):
                    print('Sim')
                else:
                    print('Não')
                palpite = input('O animal é: ').lower()
                if palpite == resposta:
                    print('Parabéns, resposta correta')
                    continuar = False
                    break            


    if questao == 39:
        agenda = {'Nome': ['João Doe', 'Pedro Henrique', 'Marcos Vinícius', 'João Silva', 'Maria Santos', 'Pedro Oliveira', 'Samuel Oliveira', 'Letícia Campos'],
                'Telefone': ['11 98765-4321', '21 91234-5678', '31 92345-6789', '31 91515-4861', '21 94732-5658', '11 93684-9834', '31 93456-7890', '31 94567-8901'],
                'Email': ['jaodoe@gmail.com', 'pedroh@gmail.com', 'marckv@gmail.com', 'joaosilva@gmail.com', 'mariasantos@gmail.com', 'pedrooliveira@gmail.com', 'samoliveira @gmail.com', 'letcampos@gmail.com']}
        rodar = 1
        while rodar == 1:
            acao = int(input('Adicionar[1] Pesquisar[2] Remover[3] Editar[4] Parar[5] '))
            if acao == 1:
                agenda.get('Nome').append(input('Nome: '))
                agenda.get('Telefone').append(input('Telefone: '))
                agenda.get('Email').append(input('Email: '))
            if acao == 2:
                p = input('Nome que deseja pesquisar: ')
                if p in agenda['Nome']:
                    r = agenda['Nome'].index(p)
                    print('Nome:', agenda.get('Nome')[r])
                    print('Telefone:', agenda.get('Telefone')[r])
                    print('Email:', agenda.get('Email')[r])
            if acao == 3:
                r = input('Quem deseja remover: ')
                if r in agenda['Nome']:
                    d = agenda['Nome'].index(r)
                    agenda.get('Nome').pop(d)
                    agenda.get('Telefone').pop(d)
                    agenda.get('Email').pop(d) 
            if acao == 4:
                e = input('Quem deseja Editar: ')
                if e in agenda['Nome']:
                    r = agenda['Nome'].index(e)
                    agenda.get('Nome').insert(r, input('Nome: '))
                    agenda.get('Telefone').insert(r, input('Telefone: '))
                    agenda.get('Email').insert(r, input('Email: '))
            if acao == 5:
                rodar = 0       


    if questao == 40:
        opção = input('Decodificar (1). Codificar (2): ')
        if opção == '1':
            decode = {'._': 'a', '_...': 'b', '_._.': 'c', '_..': 'd', '.': 'e', '.._.': 'f', '__.': 'g', '....': 'h', 
                    '..': 'i', '.___': 'j', '_._': 'k', '._..': 'l', '__': 'm', '_.': 'n', '___': 'o', '.__.': 'p', 
                    '__._': 'q', '._.': 'r', '...': 's', '_': 't', '.._': 'u', '..._': 'v', '.__': 'w', '_.._': 'x', '_.__': 'y', '__..': 'z'}
            entrada = [input('Digite o texto que deseja decodificar(_/.): ').split()]
            letras = []
            deco = []
            for i in entrada:
                l1 = []
                for l in i:
                    l1.append(l)
                letras.append(l1)    
            l2 = [k for j in letras for k in j]
            for g in l2:
                deco.append(decode.get(g))
            print(' '.join(deco))
        elif opção == '2':
            code = {'a': '._', 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.', 'f': '.._.', 'g': '__.', 'h': '....',
                    'i': '..', 'j': '.___', 'k': '_._', 'l': '._..', 'm': '__', 'n': '_.', 'o': '___', 'p': '.__.', 
                    'q': '__._', 'r': '._.', 's': '...', 't': '_', 'u': '.._', 'v': '..._', 'w': '.__', 'x': '_.._', 'y': '_.__', 'z': '__..'}
            entrada = input('Digite o texto que deseja codificar(sem acentos): ')
            texto = entrada.lower().split()
            letras = []
            co = []
            for i in texto:
                l1 = []
                for l in i:
                    l1.append(l)
                letras.append(l1) 
            l2 = [k for j in letras for k in j]
            for g in l2:
                co.append(code.get(g))
            print(' '.join(co))
        else:
            print('Opção inválida')


    if questao == 41:
        jogo = {'modelo': 'uno', 
        'ano':2015}
        jogo['cor'] = 'preto'
        print(jogo)


    if questao == 42:
        especies = {
                "Gato": {
                "Silvestre": {"nome": "Silvestre", "tamanho": "pequeno", "cor": "preto"},
                "Amendoim": {"nome": "Amendoim", "tamanho": "pequeno", "cor": "branco"},
            },
                'Humano': {
                "André": {"nome": "André", "tamanho": "médio", "cor": "pardo"},
                "Katharine": {"nome": "Katharine", "tamanho": "médio", "cor": "negra"},
            },
        }
        print(especies.get('Humano').get('Katharine').get('cor'))


    if questao == 43:
        opção = input('Decodificar (1). Codificar (2): ')
        if opção == '1':
            decode = {'._': 'a', '_...': 'b', '_._.': 'c', '_..': 'd', '.': 'e', '.._.': 'f', '__.': 'g', '....': 'h', 
                    '..': 'i', '.___': 'j', '_._': 'k', '._..': 'l', '__': 'm', '_.': 'n', '___': 'o', '.__.': 'p', 
                    '__._': 'q', '._.': 'r', '...': 's', '_': 't', '.._': 'u', '..._': 'v', '.__': 'w', '_.._': 'x', '_.__': 'y', '__..': 'z'}
            entrada = [input('Digite o texto que deseja decodificar(_/.): ').split()]
            letras = []
            deco = []
            for i in entrada:
                l1 = []
                for l in i:
                    l1.append(l)
                letras.append(l1)    
            l2 = [k for j in letras for k in j]
            for g in l2:
                deco.append(decode.get(g))
            print(' '.join(deco))
        elif opção == '2':
            code = {'a': '._', 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.', 'f': '.._.', 'g': '__.', 'h': '....',
                    'i': '..', 'j': '.___', 'k': '_._', 'l': '._..', 'm': '__', 'n': '_.', 'o': '___', 'p': '.__.', 
                    'q': '__._', 'r': '._.', 's': '...', 't': '_', 'u': '.._', 'v': '..._', 'w': '.__', 'x': '_.._', 'y': '_.__', 'z': '__..'}
            entrada = input('Digite o texto que deseja codificar(sem acentos): ')
            texto = entrada.lower().split()
            letras = []
            co = []
            for i in texto:
                l1 = []
                for l in i:
                    l1.append(l)
                letras.append(l1) 
            l2 = [k for j in letras for k in j]
            for g in l2:
                co.append(code.get(g))
            print(' '.join(co))
        else:
            print('Opção inválida')


    if questao == 44:
        l_nomes = {'Ingrid', 'Bruno', 'Fabio', 'Yernadez', 'Marcos', 'Wallace', 'Walter', 'Priscila', 'Pricila', 'Ronaldo', 'Rubem', 'Mariana', 'Janaína', 'Samuel', 'Pedro', 'Letícia', 'João', 'Lucas', 'Fernando', 'Bernardo'}
        quant = int(input('Quantos nomes deseja verificar: '))
        for i in range(quant):
            nome = input('Nome: ')
            if nome in l_nomes:
                print('Está na turma')
            else:
                print('Não está na turma')


    if questao == 45:
        l_nomes = {'Ximiun','Yakborgob','Gefoouil','Zoetuso', 'Cawao', 'Tarfeura', 'Haykui', 'Esuma', 'Dauceyarn', 'Harriric', 'Celeblyaborn', 'Khadpu', 'Hayla', 'Diono', 'Olficiolu', 'Venbou'}
        tamanho = len(l_nomes)
        remover = tamanho - 5
        for i in range(remover):
            l_nomes.pop()
        print(l_nomes)


    if questao == 46:
        import random
        import copy
        dados = {'Nome': [],
                'Matrícula': [],
                'Curso': []
        }
        notas = {'Notas': []}
        nota = []
        adicionar = 1
        while adicionar == 1:
            acao = int(input('Adicionar[1], Parar[2]: '))
            if acao == 1:
                dados.get('Nome').append(input('Nome: '))
                dados.get('Curso').append(input('Curso: '))
                dados.get('Matrícula').append(random.randint(1000, 9999))
                quant = int(input('Quantas notas serão adicionadas: '))
                for i in range(quant):
                    nota.append(float(input('Nota: ')))
                notas.get('Notas').append(copy.deepcopy(nota))
                nota.clear()
            if acao == 2:
                adicionar = 0
        catalogo = {}
        for l in range(len(dados['Nome'])):
            nome = dados['Nome'][l]
            catalogo[nome] = {
                'Matrícula': dados['Matrícula'][l],
                'Curso': dados['Curso'][l],
                'Notas': notas['Notas'][l]
            }
        print(catalogo)


    if questao == 47:
        controle = {'Código': ['1234', '5678', '9012', '3456', '7890', '2345', '6789', '0123', '4567', '8901', '5432'],
                'Nível': [0, 3, 5, 1, 4, 3, 2, 2, 4, 3, 0]
                }
        acesso = input('Digite seu cógido de acesso: ')
        lab = int(input('Qual laboratório deseja acessar: '))
        if acesso in controle['Código']:
            r = controle['Código'].index(acesso)
            nivel = controle.get('Nível')[r]
            if lab <= nivel:
                print('Acesso permitido ao laboratório', lab)
            else:
                print('Acesso negado')


    if questao == 48:
        import random
        armazem = {
            '8723': {
                'Tipo': 'Seguro',
                'Origem': 'China',
                'Local': 'Sítio 3'
            },
            '5491': {
                'Tipo': 'Euclídeo',
                'Origem': 'Brasil',
                'Local': 'Sítio 1'
            },
            '1234': {
                'Tipo': 'Euclídeo',
                'Origem': 'Argentina',
                'Local': 'Sítio 3'
            },
            '9876': {
                'Tipo': 'Keter',
                'Origem': 'Estados Unidos',
                'Local': 'Sítio 5'
            },
            '4312': {
                'Tipo': 'Keter',
                'Origem': 'Portugal',
                'Local': 'Sítio 4'
            },
            '7890': {
                'Tipo': 'Euclídeo',
                'Origem': 'França',
                'Local': 'Sítio 4'
            },
            '5678': {
                'Tipo': 'Keter',
                'Origem': 'Japão',
                'Local': 'Sítio 1'
            },
            '2345': {
                'Tipo': 'Seguro',
                'Origem': 'Alemanha',
                'Local': 'Sítio 2'
            },
            '9021': {
                'Tipo': 'Euclídeo',
                'Origem': 'Coreia do Sul',
                'Local': 'Sítio 5'
            },
            '3456': {
                'Tipo': 'Seguro',
                'Origem': 'Itália',
                'Local': 'Sítio 3'
            }
        }
        quant = int(input('Quantos itens irá adicionar: '))
        for i in range(quant):
            cod = random.randint(1000, 9999)
            armazem[str(cod)] = {'Tipo': input('Tipo: '),
                    'Origem': input('Origem: '),
                    'Local': input('Local: ')
                }
        print(armazem)


    if questao == 49:
        contador = 1000
        set3 = set()
        set4 = set()
        n3_n4 = set()
        while contador >= 0:
            if contador %3 == 0:
                set3.add(contador)
            if contador %4 == 0:
                set4.add(contador)
            contador -= 1
            if contador %3 != 0 and contador %4 !=0:
                n3_n4.add(contador)
        print(set3.intersection(set4))
        print(n3_n4)
        print(set3)
        print(set4)

    if questao == 50:
        xingamento = ['idiota', 'imbecil', 'arrombado', 'estúpido', 'porra', 'cretino', 'cretina', 'cu', 'babaca', 'caralho', 'desgraça', 'otário', 'vagabundo', 'vagabunda', 'burro', 'puta']
        frase = input('Digite um frase: ')
        palavras = frase.split()
        frase_c = []
        x = []
        for i in xingamento:
            x.append(len(i))
        for l in range(len(palavras)):
            for k in range(len(xingamento)):
                if palavras[l].lower() == xingamento[k]:
                    frase_c.append('*' * x[k])
                    break
            else:
                frase_c.append(palavras[l])
        print(' '.join(frase_c))


    if questao == 51:
        texto = input("Digite um texto: ")
        vogais = ['a', 'á', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'y']
        alterar = texto.lower().split()
        consoantes_t = 0
        espacos_t = 0
        vogal_t = 0
        l2 = []
        for i in alterar:
            l1 = []
            for l in i:
                l1.append(l)
            l2.append(l1)
        l3 = [k for p in l2 for k in p]
        for g in l3:
            if g in vogais:
                vogal_t += 1   
            elif g not in vogais:
                consoantes_t += 1
        for r in range(len(texto)):
            if ' ' in texto[r]:
                espacos_t += 1
        palavras = set(alterar)
        informacoes = {'Vogais': vogal_t,
                    'Consoantes': consoantes_t,
                    'Espaços': espacos_t,
                    'Palavras únicas': len(palavras)}
        print(informacoes)


    if questao == 52:
        import random
        funcionarios = {}
        cods = []
        cont = 1
        while cont == 1:    
            opcoes = int(input('Cadastrar[1]. Remover[2]. Procurar por cargo[3]. Parar[4] '))
            if opcoes == 1:
                cod = random.randint(1000, 9999)
                funcionarios[str(cod)] = {'Nome': input('Nome: '),
                'DN': input('Data de nascimento: '),
                'CPF': input('CPF: '),
                'Cargo': input('Cargo: '),
            'Salario': input('Salário: '),
                'Escala': []}
                dias = int(input('Quantos dias o funcionário trabalhará: '))
                for i in range(dias):
                    escala = input(f'{i+1}º dia: ' )
                    funcionarios[str(cod)]['Escala'].append(escala)
                cods.append(str(cod))
            if opcoes == 2:
                print(cods)
                remover = input('Código do funcionário: ')
                funcionarios.pop(remover)
                cods.remove(remover)
            if opcoes == 3:
                achar = input('Cargo do(s) funcionário(s): ')
                for c, p in funcionarios.items():
                    if p['Cargo'].lower() == achar.lower():
                        print(c, ':', p)
                        print()
            if opcoes == 4:
                cont = 0
        print(funcionarios)


    if questao == 53:
        pessoas = {'Carlos': {'João', 'Ricardo', 'Renata', 'Maria', 'Pedro', 'Renata', 'Leonardo', 'Amanda', 'Letícia', 'Samuel', 'Ana', 'Carlos', 'Mariana', 'Paulo', 'Isabela', 'Fernando', 'Gabriela'},
                'Ronaldo': {'José', 'Luiza', 'Lucas', 'Laura', 'Antônio', 'Camila', 'Leonardo', 'Gustavo', 'Amanda', 'Juliana', 'Thiago', 'Rafael', 'Carolina', 'Marcos', 'Vanessa', 'Carlos', 'Mariana'},
                'Katrina': {'Felipe', 'Juliana' 'Thiago', 'Larissa', 'Samuel', 'Renata', 'Leonardo','Marcelo', 'Laura', 'Beatriz', 'Rodrigo', 'Natália', 'Vinícius', 'Patrícia'},
                'Lorenzo': {'Marcos', 'Vanessa', 'Diego', 'Bianca', 'Ricardo', 'Renata', 'Leonardo', 'Letícia', 'Eduardo', 'Jéssica'},
                'Rosa': {'Rafael', 'Carla', 'Daniel', 'Amanda', 'Juliana', 'Gabrielle', 'Henrique', 'Mônica', 'Alexandre', 'Leonardo', 'Marcos', 'Vanessa','Valentina', 'Samuel', 'Giovanni', 'Tatiane'}}
        convidados = set()
        o1 = input('Carlos é organizador(s/n)? ').lower()
        o2 = input('Ronaldo é organizador(s/n)? ').lower()
        o3 = input('Katrina é organizador(s/n)? ').lower()
        o4 = input('Lorenzo é organizador(s/n)? ').lower()
        o5 = input('Rosa é organizador(s/n)? ').lower()
        conv = int(input('Todos os amigos[1]. Amigos em comum[2] '))
        if o1 == 's':
            convidados.update(pessoas.get('Carlos'))
        if o2 == 's':
            convidados.update(pessoas.get('Ronaldo'))
        if o3 == 's':
            convidados.update(pessoas.get('Katrina'))
        if o4 == 's':
            convidados.update(pessoas.get('Lorenzo'))
        if o5 == 's':
            convidados.update(pessoas.get('Rosa'))
        if conv == 2:
            if o1 == 's':
                convidados.intersection_update(pessoas.get('Carlos'))
            if o2 == 's':
                convidados.intersection_update(pessoas.get('Ronaldo'))
            if o3 == 's':
                convidados.intersection_update(pessoas.get('Katrina'))
            if o4 == 's':
                convidados.intersection_update(pessoas.get('Lorenzo'))
            if o5 == 's':
                convidados.intersection_update(pessoas.get('Rosa'))
        if conv == 1:
            print(convidados)
        if conv == 2:
            print(convidados)


    if questao == 54:
        biblioteca = {'Título': ['Dom Casmurro', '1984', 'A Revolução dos Bichos', 'O Senhor dos Anéis: A Sociedade do Anel', 'O Pequeno Príncipe', "Harry Potter and the Philosopher's Stone", 'To Kill a Mockingbird', 'The Great Gatsby', 'Pride and Prejudice', 'The Catcher in the Rye'],
                    'Autor': ['Machado de Assis', 'George Orwell', 'George Orwell', 'J.R.R. Tolkien', 'Antoine de Saint-Exupéry', 'J.K. Rowling', 'Harper Lee', 'F. Scott Fitzgerald', 'Jane Austen', 'J.D. Salinger'],
                    'Gênero': ['Romance', 'Ficção distópica', 'Fábula política', 'Fantasia', 'Literatura infantojuvenil', 'Fantasia', 'Literatura clássica', 'Literatura clássica', 'Romance', 'Romance'],
                    'Editora': ['Garnier', 'Secker & Warburg', 'Secker & Warburg', 'Allen & Unwin', 'Reynal & Hitchcock', 'Bloomsbury Publishing', 'Harper & Brothers', "Charles Scribner's Sons", 'Thomas Egerton', 'Little, Brown and Company'],
                    'Ano': [1899, 1949, 1945, 1954, 1943, 1997, 1960, 1925, 1813, 1951],
                    'Disponibilidade': ['Disponível', 'Indisponível', 'Disponível', 'Disponível', 'Disponível', 'Indisponível', 'Disponível', 'Indisponível', 'Indisponível', 'Disponível']
                    }
        rodar = 1
        while rodar == 1:
            acao = int(input('Parar(0), Adicionar(1), Remover (2), Ver todos (3), Buscar por autor(4) por título (5), Conferir cadastro(6): '))
            if acao == 1:
                biblioteca.get('Título').append(input('Título: '))
                biblioteca.get('Autor').append(input('Autor: '))
                biblioteca.get('Gênero').append(input('Gênero: '))
                biblioteca.get('Editora').append(input('Editora: '))
                biblioteca.get('Ano').append(input('Ano: '))
                biblioteca.get('Disponibilidade').append(bool(input('Disponibilidade(Disponível/Indisponível): ')))
            if acao == 2:
                c = input('Nome do título que deseja remover: ')
                if c in biblioteca['Título']:
                    r = biblioteca['Título'].index(c)
                    biblioteca['Título'].pop(r)
                    biblioteca['Autor'].pop(r)
                    biblioteca['Gênero'].pop(r)
                    biblioteca['Editora'].pop(r)
                    biblioteca['Ano'].pop(r)
                    biblioteca['Disponibilidade'].pop(r)
            if acao == 3:
                for i in range(len(biblioteca['Título'])):
                    print(f'Livro {i + 1}:')
                    print('Título:', biblioteca['Título'][i])
                    print('Autor:', biblioteca['Autor'][i])
                    print('Gênero:', biblioteca['Gênero'][i])
                    print('Editora:', biblioteca['Editora'][i])
                    print('Ano:', biblioteca['Ano'][i])
                    print('Disponibilidade:', biblioteca['Disponibilidade'][i])
            if acao == 4:
                c = input('Nome do autor que deseja procurar: ')
                for i in range(len(biblioteca['Autor'])):
                    if biblioteca['Autor'][i] == c:
                        print('Título:', biblioteca["Título"][i])
                        print('Autor:', biblioteca["Autor"][i])
                        print('Gênero:', biblioteca["Gênero"][i])
                        print('Editora:', biblioteca["Editora"][i])
                        print('Ano:', biblioteca["Ano"][i])
                        print('Disponibilidade:', biblioteca["Disponibilidade"][i])
            if acao == 5:
                c = input('Nome do título que deseja procurar: ')
                if c in biblioteca['Título']:
                    r = biblioteca['Título'].index(c)
                    print('Título:', biblioteca.get('Título')[r])
                    print('Autor:', biblioteca.get('Autor')[r])
                    print('Gênero:', biblioteca.get('Gênero')[r])
                    print('Editora:',  biblioteca.get('Editora')[r])
                    print('Ano:', biblioteca.get('Ano')[r])
                    print('Disponibilidade:', biblioteca.get('Disponibilidade')[r])
            if acao == 6:
                c = input('Nome do título que deseja procurar: ')
                if c in biblioteca['Título']:
                    print('Livro cadastrado na biblioteca')
                else:
                    print('Livro não cadastrado na biblioteca')   
            if acao == 0:
                rodar = 0


    if questao == 55:
        import random
        import copy
        nume = ['2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠']
        letras = ['K♥', 'Q♥', 'J♥', 'K♣', 'Q♣', 'J♣', 'K♦', 'Q♦', 'J♦', 'K♠', 'Q♠', 'J♠']
        a = ['A♥', 'A♣', 'A♦', 'A♠']
        continuar = 's'
        while continuar == 's': 
            pos = nume + letras + a
            random.shuffle(pos)
            mostrar = []
            tentar = 's'
            mao1 = []
            soma = 0
            mao = []
            mao.append(random.choice(pos))
            mao.append(random.choice(pos))
            mao1.append(copy.deepcopy(mao))
            while tentar == 's' and soma < 21:
                for c in mao:
                    print(c)
                    if c in pos:
                        pos.remove(c)
                mostrar = [i for k in mao1 for i in k]
                print("Sua mão:", mostrar)
                for l in mao:  
                    if l in letras:
                        soma += 10
                    elif l in a:
                        v = int(input('A valerá 11 ou 1?: '))
                        if v == 11:
                            soma += 11
                        else:
                            soma += 1
                    else:
                        soma += int(l[0])
                if soma < 21:
                    tentar = input('Deseja outra carta (s/n)?: ')
                    if tentar == 's':
                        mao.clear()
                        mao.append(random.choice(pos))
                        mao1.append(copy.deepcopy(mao))
                        continue
                print(soma)
                if soma == 21:
                    print('Parabéns! Você ganhou')
                    break
                elif soma > 21:
                    print('Você perdeu!', soma-21, 'a mais')
                    break
                elif soma < 21:
                    print('Você perdeu, faltaram', 21-soma)
            soma = 0
            continuar = input('Deseja outro jogo(s/n)?: ').lower()


while True:
    questao = int(input('Qual questão deseja acessar: '))
    guia()