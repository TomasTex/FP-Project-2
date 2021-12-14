# Helper functions
def exists(fn, iterable):
    return any(map(fn, iterable))


def cria_posicao(x: int, y: int) -> tuple:
    """Recebe os valores correspondentes às coordenadas de uma posição e devolve a posição correspondente.

    Args:
        y (int): ordenada
        x (int): abcissa

    Raises:
        ValueError: 'cria_posicao: argumentos invalidos'

    Returns:
        tuple: par das coordenadas
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError('cria_posicao: argumentos invalidos')

    if x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')

    return (x, y)


def cria_copia_posicao(posicao: tuple) -> tuple:
    """Recebe uma posição e devolve uma cópia nova da posição.

    Args:
        posicao (tuple): par de coordenadas

    Returns:
        tuple: copia das coordenadas fornecidas
    """
    return cria_posicao(obter_pos_x(posicao), obter_pos_y(posicao))


def eh_posicao(arg) -> bool:
    """Devolve True caso o seu argumento seja um TAD posição e False caso contrário.

    Args:
        arg: posição

    Returns:
        bool: é posição?
    """
    if not isinstance(arg, tuple):
        return False

    if len(arg) != 2:
        return False

    x = obter_pos_x(arg)
    y = obter_pos_y(arg)

    if not isinstance(x, int):
        return False

    if not isinstance(y, int):
        return False

    return True  # será que se deve validar ainda se x >= 0 e y >= 0 ??


def nao_eh_posicao(posicao) -> bool:
    """Função que faz o contrário da eh_posição. Existe por motivos de simplificação da leitura do codigo

    Args:
        posicao

    Returns:
        bool: não é posição?
    """
    return not eh_posicao(posicao)


def obter_pos_x(p) -> int:
    """Devolve a componente x da posição p.

    Args:
        p: posição

    Returns:
        int: x da posição
    """
    return p[0]


def obter_pos_y(p) -> int:
    """Devolve a componente y da posição p.

    Args:
        p: posição

    Returns:
        int: y da posição
    """
    return p[1]


def posicoes_iguais(p1, p2) -> bool:
    """Devolve True apenas se p1 e p2 são posições e são iguais.

    Args:
        p1: posição 1
        p2: posição 2

    Returns:
        bool: são iguais?
    """
    return p1[0] == p2[0] and p1[1] == p2[1]


def posicao_para_str(p) -> str:
    """Devolve a cadeia de caracteres ‘(x, y)’ que representa o seu argumento, sendo os valores x e y as coordenadas de p.

    Args:
        p: posição

    Returns:
        str: posição em string
    """
    return f"({p[0]}, {p[1]})"


def obter_posicoes_adjacentes(posicao: tuple) -> tuple:
    """Devolve um tuplo com as posições adjacentes à posição p, começando pela posição acima de p e seguindo no sentido horário.

    Args:
        posicao (tuple)

    Returns:
        tuple: posições adjacentes
    """
    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)

    posicoes_possiveis = []

    if y != 0:
        posicoes_possiveis.append(cria_posicao(x, y - 1))

    posicoes_possiveis.append(cria_posicao(x + 1, y))
    posicoes_possiveis.append(cria_posicao(x, y + 1))

    if x != 0:
        posicoes_possiveis.append(cria_posicao(x - 1, y))

    return tuple(posicoes_possiveis)


def ordenar_posicoes(posicoes: tuple) -> tuple:
    """Devolve um tuplo contendo as mesmas posições do tuplo fornecido como argumento, ordenadas de acordo com a ordem de leitura do prado.

    Args:
        posicoes (tuple): tuplo com as posições a ordenar

    Returns:
        tuple: tuplo com as posições ordenadas
    """
    lista_posicoes = list(posicoes)
    len_lista_posicoes = len(lista_posicoes)

    # bubble sort: https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
    for i in range(len_lista_posicoes):
        ordenado = True

        for j in range(len_lista_posicoes - i - 1):
            posicao1_x = obter_pos_x(lista_posicoes[j])
            posicao1_y = obter_pos_y(lista_posicoes[j])

            posicao2_x = obter_pos_x(lista_posicoes[j + 1])
            posicao2_y = obter_pos_y(lista_posicoes[j + 1])

            if posicao1_y > posicao2_y or (posicao1_y == posicao2_y and posicao2_x < posicao1_x):
                lista_posicoes[j], lista_posicoes[j + 1] = lista_posicoes[j + 1], lista_posicoes[j]
                ordenado = False

        if ordenado:
            break

    return tuple(lista_posicoes)


def cria_animal(s: str, r: int, a: int) -> dict:
    """Recebe uma cadeia de caracteres s não vazia correspondente à espécie do animal e dois valores inteiros correspondentes à frequência
de reprodução r (maior do que 0) e à frequência de alimentação a (maior ou igual que 0); e devolve o animal.

    Args:
        s (str): especie
        r (int): freq de reprodução
        a (int): freq de alimentação

    Raises:
        ValueError: 'cria_animal: argumentos invalidos'

    Returns:
        dict: dicionario que representa o animal
    """
    if not isinstance(s, str) or not isinstance(r, int) or not isinstance(a, int):
        raise ValueError('cria_animal: argumentos invalidos')

    if len(s) == 0 or r <= 0 or a < 0:
        raise ValueError('cria_animal: argumentos invalidos')

    return {
        'especie': s,
        'reproducao': r,
        'alimentacao': a,
        'idade': 0,
        'fome': 0
    }


def cria_copia_animal(animal: dict) -> dict:
    """Recebe um animal (predador ou presa) e devolve uma nova cópia do animal.

    Args:
        animal (dict): animal a copiar

    Returns:
        dict: cópia
    """
    especie = obter_especie(animal)
    reproducao = obter_freq_reproducao(animal)
    alimentacao = obter_freq_alimentacao(animal)

    return cria_animal(especie, reproducao, alimentacao)


def obter_especie(animal: dict) -> str:
    """Devolve a cadeia de caracteres correspondente à espécie do animal.


    Args:
        animal (dict)

    Returns:
        str: espécie
    """
    return animal['especie']


def obter_freq_reproducao(animal: dict) -> int:
    """Devolve a frequência de reprodução do animal.

    Args:
        animal (dict)

    Returns:
        int: freq de reprodução
    """
    return animal['reproducao']


def obter_freq_alimentacao(animal: dict) -> int:
    """Devolve a frequência de alimentação do animal.

    Args:
        animal (dict)

    Returns:
        int: freq de alimentação
    """
    return animal['alimentacao']


def obter_idade(animal: dict) -> int:
    """Devolve a idade do animal a.


    Args:
        animal (dict)

    Returns:
        int: idade
    """
    return animal['idade']


def obter_fome(animal: dict) -> int:
    """Devolve a fome do animal a

    Args:
        animal (dict)

    Returns:
        int: fome
    """
    return animal['fome']


def aumenta_idade(animal: dict) -> dict:
    """Modifica destrutivamente o animal, incrementando o valor da sua idade em uma unidade, e devolve o próprio animal.

    Args:
        animal (dict)

    Returns:
        dict: animal com a idade aumentada
    """
    animal['idade'] += 1
    return animal


def reset_idade(animal: dict) -> dict:
    """Modifica destrutivamente o animal, definindo o valor da sua idade igual a 0, e devolve o próprio animal.

    Args:
        animal (dict)

    Returns:
        dict: animal com a idade resetada
    """
    animal['idade'] = 0
    return animal


def aumenta_fome(animal: dict) -> dict:
    """Modifica destrutivamente o animal predador, incrementando o valor da sua fome em uma unidade, e devolve o próprio animal.

    Args:
        animal (dict)

    Returns:
        dict: animal com a fome aumentada
    """
    if eh_predador(animal):
        animal['fome'] += 1

    return animal


def reset_fome(animal: dict) -> dict:
    """ Modifica destrutivamente o animal predador, definindo o valor da sua fome igual a 0, e devolve o próprio animal.

    Args:
        animal (dict)

    Returns:
        dict: animal com a fome resetada
    """
    if eh_predador(animal):
        animal['fome'] = 0

    return animal


def eh_animal(arg) -> bool:
    """Devolve True caso o seu argumento seja um TAD animal e False caso contrário.

    Args:
        arg

    Returns:
        bool: é um tad animal?
    """
    if not isinstance(arg, dict):
        return False

    if len(arg) != 5:
        return False

    if not isinstance(arg['especie'], str):
        return False

    if not isinstance(arg['reproducao'], int):
        return False

    if not isinstance(arg['alimentacao'], int):
        return False

    if not isinstance(arg['idade'], int):
        return False

    if not isinstance(arg['fome'], int):
        return False

    return True


def eh_predador(arg) -> bool:
    """Devolve True caso o seu argumento seja um TAD animal do tipo predador e False caso contrário.

    Args:
        arg 

    Returns:
        bool: é um predador?
    """
    return eh_animal(arg) and obter_freq_alimentacao(arg) != 0


def eh_presa(arg) -> bool:
    """Devolve True caso o seu argumento seja um TAD animal do tipo presa e False caso contrário.


    Args:
        arg

    Returns:
        bool: é uma presa?
    """
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


def animais_iguais(a1, a2) -> bool:
    """Devolve True apenas se a1 e a2 são animais e são iguais.

    Args:
        a1 : animal 1
        a2 : animal 2

    Returns:
        bool: são iguais?
    """
    return a1 == a2


def animal_para_char(animal) -> str:
    """ Devolve a cadeia de caracteres dum único elemento correspondente ao primeiro carácter da espécie do animal passada por argumento, 
    em maiúscula para animais predadores e em minúscula para animais presa.


    Args:
        animal 

    Returns:
        str: primeiro caracter da especie
    """
    char_especie = obter_especie(animal)[0]
    return char_especie.lower() if eh_presa(animal) else char_especie.upper()


def animal_para_str(animal) -> str:
    """Devolve a cadeia de caracteres que representa o animal

    Args:
        animal 

    Returns:
        str: cadeia de caracteres que representa o animal
    """
    especie = obter_especie(animal)
    idade = obter_idade(animal)
    reproducao = obter_freq_reproducao(animal)

    # https://docs.python.org/3/tutorial/inputoutput.html
    representacao = f"{especie} [{idade}/{reproducao}"

    if eh_predador(animal):
        fome = obter_fome(animal)
        alimentacao = obter_freq_alimentacao(animal)

        representacao += f";{fome}/{alimentacao}"

    return representacao + "]"


def eh_animal_fertil(animal) -> bool:
    """Devolve True caso o animal tenha atingido a idade de reprodução e False caso contrário.

    Args:
        animal

    Returns:
        bool: está fertil?
    """
    return obter_idade(animal) >= obter_freq_reproducao(animal)


def eh_animal_faminto(animal) -> bool:
    """devolve True caso o animal tenha atingindo um valor de
fome igual ou superior à sua frequência de alimentação e False caso contrário. As presas devolvem sempre False.


    Args:
        animal 

    Returns:
        bool: está faminto?
    """
    return obter_fome(animal) >= obter_freq_alimentacao(animal) if eh_predador(animal) else False


def reproduz_animal(animal) -> dict:
    """recebe um animal devolvendo um novo animal da mesma
espécie com idade e fome igual a 0, e modificando destrutivamente o animal passado
como argumento a alterando a sua idade para 0.

    Args:
        animal 

    Returns:
        dict: cria do animal
    """
    return reset_fome(cria_copia_animal(reset_idade(animal)))


def existem_posicoes_repetidas(posicoes: tuple) -> bool:
    """Verifica se existem posições repetidas

    Args:
        posicoes (tuple): tuple com as posições a verificar

    Returns:
        bool: existem repetidas?
    """
    for i in range(len(posicoes)):
        posicao1 = posicoes[i]
        for j in range(i + 1, len(posicoes)):
            posicao2 = posicoes[j]

            if posicoes_iguais(posicao1, posicao2):
                return True

    return False


def existem_posicoes_sobrepostas(posicoes_a_validar: tuple, posicoes_invalidas: tuple) -> bool:
    """Valida se há posições que estejam sobrepostas

    Args:
        posicoes_a_validar (tuple)
        posicoes_invalidas (tuple)

    Returns:
        bool: há sobrepostas?
    """
    for posicao in posicoes_a_validar:
        if posicao in posicoes_invalidas:
            return True

    return False


def existem_posicoes_fora_do_prado(dimensao_prado: tuple, posicoes: tuple) -> bool:
    """Valida se há posições que saiam fora dos limites

    Args:
        dimensao_prado (tuple)
        posicoes (tuple)

    Returns:
        bool: alguma sai fora?
    """
    dimensao_x = obter_pos_x(dimensao_prado)
    dimensao_y = obter_pos_y(dimensao_prado)

    for posicao in posicoes:
        x = obter_pos_x(posicao)
        if x <= 0 or x >= dimensao_x:
            return True

        y = obter_pos_y(posicao)
        if y <= 0 or y > dimensao_y:
            return True

    return False


def validar_prado(dimensao, rochedos: tuple, animais: tuple, posicoes: tuple) -> bool:
    """Valida se o prado é válido

    Args:
        dimensao 
        rochedos (tuple)
        animais (tuple)
        posicoes (tuple)

    Returns:
        bool: é válido?
    """
    if exists(lambda arg: not isinstance(arg, tuple), [rochedos, animais, posicoes]):
        return False

    if nao_eh_posicao(dimensao):
        return False

    if exists(nao_eh_posicao, rochedos):
        return False
    if exists(lambda animal: not eh_animal(animal), animais):
        return False
    if len(posicoes) == 0 or len(posicoes) != len(animais):
        return False
    if exists(nao_eh_posicao, posicoes):
        return False

    if existem_posicoes_repetidas(rochedos):
        return False

    if existem_posicoes_repetidas(posicoes):
        return False

    if existem_posicoes_fora_do_prado(dimensao, rochedos + posicoes):
        return False

    if existem_posicoes_sobrepostas(rochedos, (dimensao, )):
        return False

    if existem_posicoes_sobrepostas(posicoes, (dimensao,) + rochedos):
        return False

    return True


def cria_prado(d: tuple, r: tuple, a: tuple, p: tuple) -> dict:
    """Cria o prado com d (dimensão), r (rochedos), a (animais), e p(posições dos animais)

    Args:
        d (tuple): dimensão
        r (tuple): rochedos
        a (tuple): animais
        p (tuple): respetivas posições

    Raises:
        ValueError: 'cria_prado: argumentos invalidos'

    Returns:
        dict: prado
    """
    if not validar_prado(d, r, a, p):
        raise ValueError('cria_prado: argumentos invalidos')

    return {'limite': d, 'rochedos': r, 'animais': a, 'posicoes': p}


def cria_copia_prado(prado: dict) -> dict:
    """Cria uma cópia do prado

    Args:
        prado (dict): prado a copiar

    Returns:
        dict: cópia
    """
    return prado.copy()


def obter_tamanho_x(prado: dict) -> int:
    """Devolve o valor inteiro que corresponde ao comprimento do prado.

    Args:
        prado (dict)

    Returns:
        int: Nx
    """
    return obter_pos_x(prado['limite']) + 1


def obter_tamanho_y(prado: dict) -> int:
    """Devolve o valor inteiro que corresponde à largura do prado.

    Args:
        prado (dict)

    Returns:
        int: Ny
    """
    return obter_pos_y(prado['limite']) + 1


def obter_numero_predadores(prado: dict) -> int:
    """Devolve o numero de animais predadores no prado

    Args:
        prado (dict)

    Returns:
        int: numero de predadores
    """
    return len(list(filter(eh_predador, prado['animais'])))


def obter_numero_presas(prado: dict) -> int:
    """Devolve o numero de animais presas no prado

    Args:
        prado (dict)

    Returns:
        int: numero de presas
    """
    return len(list(filter(eh_presa, prado['animais'])))


def obter_posicao_animais(prado: dict) -> tuple:
    """Devolve um tuplo contendo as posições do prado ocupadas por animais, ordenadas em ordem de leitura do prado.

    Args:
        prado (dict)

    Returns:
        tuple: posições dos animais
    """
    return ordenar_posicoes(prado['posicoes'])


def obter_animal(prado: dict, posicao: tuple) -> dict:
    """Devolve o animal do prado que se encontra na posição p.

    Args:
        prado (dict)
        posicao (tuple)

    Returns:
        dict: animal
    """
    for i in range(len(prado['posicoes'])):
        if posicoes_iguais(prado['posicoes'][i], posicao):
            return prado['animais'][i]
    return None


def emendar_tuplo(tuplo: tuple, index: int, valor) -> tuple:
    """Corrige o tuplo fornecido para os dados ficarem corretos

    Args:
        tuplo (tuple)
        index (int)
        valor

    Returns:
        tuple: tuplo corrigido
    """
    lista = list(tuplo)
    lista[index] = valor
    return tuple(lista)


def remover_do_tuplo(tuplo: tuple, index: int) -> tuple:
    """Remove o elemento com o index indicado do tuplo

    Args:
        tuplo (tuple)
        index (int)

    Returns:
        tuple: tuplo corrigido
    """
    return tuplo[0: index] + tuplo[index + 1:]


def procurar_indice_posicao(posicoes, posicao: int) -> int:
    """Procura o indice de uma determinada posição

    Args:
        posicoes
        posicao (int)

    Returns:
        int: indice
    """
    index_posicao_encontrada = -1

    for i in range(len(posicoes)):
        if posicoes_iguais(posicao, posicoes[i]):
            index_posicao_encontrada = i
            break

    return index_posicao_encontrada


def eliminar_animal(prado: dict, posicao_a_procurar: tuple) -> dict:
    """Modifica destrutivamente o prado eliminando o animal da posição deixando-a livre. Devolve o próprio prado.

    Args:
        prado (dict)
        posicao_a_procurar (tuple)

    Returns:
        dict: prado
    """
    index_posicao_encontrada = procurar_indice_posicao(prado['posicoes'], posicao_a_procurar)

    if index_posicao_encontrada != -1:
        prado['animais'] = remover_do_tuplo(prado['animais'], index_posicao_encontrada)
        prado['posicoes'] = remover_do_tuplo(prado['posicoes'], index_posicao_encontrada)

    return prado


def mover_animal(prado: dict, posicao_inicial: tuple, posicao_final: tuple) -> dict:
    """modifica destrutivamente o prado movimentando o animal da posição p1 para a nova posição p2, deixando livre a posição onde
se encontrava. Devolve o próprio prado.

    Args:
        prado (dict)
        posicao_inicial (tuple) 
        posicao_final (tuple) 

    Returns:
        dict: prado
    """
    index_posicao_encontrada = procurar_indice_posicao(prado['posicoes'], posicao_inicial)

    if index_posicao_encontrada != -1:
        prado['posicoes'] = emendar_tuplo(prado['posicoes'], index_posicao_encontrada, posicao_final)

    return prado


def inserir_animal(prado: dict, animal: dict, posicao: tuple) -> dict:
    """Modifica destrutivamente o prado acrescentando na posição do prado o animal passado com argumento. Devolve o próprio prado.


    Args:
        prado (dict)
        animal (dict)
        posicao (tuple)

    Returns:
        dict: prado
    """
    prado['animais'] += (animal,)
    prado['posicoes'] += (posicao,)

    return prado


def eh_prado(arg) -> bool:
    """Devolve True caso o seu argumento seja um TAD prado e False caso contrário.

    Args:
        arg 

    Returns:
        bool: é um TAD prado?
    """
    if not isinstance(arg, dict):
        return False
    if len(arg) != 4:
        return False
    if 'limite'not in arg.keys() or 'rochedos' not in arg.keys() or 'animais' not in arg.keys() or 'posicoes' not in arg.keys():
        return False
    if not validar_prado(arg["limite"], arg["rochedos"], arg["animais"], arg["posicoes"]):
        return False
    return True


def eh_posicao_animal(prado: dict, posicao_a_procurar: tuple) -> bool:
    """Devolve True apenas no caso da posição p do prado estar ocupada por um animal.

    Args:
        prado (dict)
        posicao_a_procurar (tuple)

    Returns:
        bool: é uma posição com animal?
    """
    for posicao in obter_posicao_animais(prado):
        if posicoes_iguais(posicao_a_procurar, posicao):
            return True

    return False


def eh_posicao_obstaculo(prado: dict, pos: tuple) -> bool:
    """devolve True apenas no caso da posição do prado corresponder a uma montanha ou rochedo.

    Args:
        prado (dict)
        pos (tuple)

    Returns:
        bool: é um obstáculo?
    """
    pos_x = obter_pos_x(pos)
    pos_y = obter_pos_y(pos)

    if pos_x == 0 or pos_x == obter_tamanho_x(prado) - 1:
        return True
    if pos_y == 0 or pos_y == obter_tamanho_y(prado) - 1:
        return True

    for p in prado['rochedos']:
        if posicoes_iguais(p, pos):
            return True

    return False


def eh_posicao_livre(prado: dict, pos: tuple) -> bool:
    """Devolve True apenas no caso da posição do prado corresponder a um espaço livre.

    Args:
        prado (dict)
        pos (tuple)

    Returns:
        bool: é um espaço livre?
    """
    return not eh_posicao_obstaculo(prado, pos) and not eh_posicao_animal(prado, pos)


def prados_iguais(p1: dict, p2: dict) -> bool:
    """Avalia se 2 prados são iguais.

    Args:
        p1 (dict): prado 1
        p2 (dict): prado 2

    Returns:
        bool: são iguais?
    """
    return p1 == p2


def prado_para_str(prado: dict) -> str:
    """Devolve uma cadeia de caracteres que representa o prado.

    Args:
        prado (dict)

    Returns:
        str: prado em str
    """
    largura = obter_tamanho_x(prado)
    comprimento = obter_tamanho_y(prado)

    representacao = "+" + ("-" * (largura - 2)) + "+" + "\n"

    for y in range(1, comprimento - 1):
        representacao += "|"

        for x in range(1, largura - 1):
            posicao = cria_posicao(x, y)

            if eh_posicao_animal(prado, posicao):
                representacao += animal_para_char(obter_animal(prado, posicao))
            elif eh_posicao_obstaculo(prado, posicao):
                representacao += "@"
            else:
                representacao += "."

        representacao += "|\n"

    return representacao + "+" + ("-" * (largura - 2)) + "+"


def obter_valor_numerico(prado: dict, posicao: tuple) -> int:
    """Devolve o valor numerico da posicao, correspondente à ordem de leitura do prado.

    Args:
        prado (dict)
        posicao (tuple)

    Returns:
        int: valor numerico
    """
    largura = obter_tamanho_x(prado)
    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)

    return x + largura * y


def pode_comer_animal(prado: dict, animal_comedor: dict, posicao_a_comer: tuple) -> bool:
    """Valida se um animal pode comer outro

    Args:
        prado (dict)
        animal_comedor (dict)
        posicao_a_comer (tuple)

    Returns:
        bool: pode comer'
    """
    animal_comido = obter_animal(prado, posicao_a_comer)
    return eh_predador(animal_comedor) and eh_presa(animal_comido)


def filtrar_posicoes_adjacentes(prado: dict, posicoes_adjacentes: tuple, animal: dict) -> tuple:
    """Filtra as posições adjacentes

    Args:
        prado (dict)
        posicoes_adjacentes (tuple)
        animal (dict)

    Returns:
        tuple: posições filtradas
    """
    posicoes_filtradas = []

    if eh_predador(animal):
        for posicao_a_mover in posicoes_adjacentes:
            if pode_comer_animal(prado, animal, posicao_a_mover):
                posicoes_filtradas.append(posicao_a_mover)

        if len(posicoes_filtradas) > 0:
            return posicoes_filtradas

    for posicao_a_mover in posicoes_adjacentes:
        if eh_posicao_livre(prado, posicao_a_mover):
            posicoes_filtradas.append(posicao_a_mover)

    return posicoes_filtradas


def obter_movimento(prado: dict, pos: tuple) -> tuple:
    """DEvolve a posição seguinte do animal com base na sua posição atual.

    Args:
        prado (dict)
        pos (tuple)

    Returns:
        tuple: posição seguinte
    """
    posicoes_adjacentes = obter_posicoes_adjacentes(pos)
    valor_posicao_atual = obter_valor_numerico(prado, pos)

    animal = obter_animal(prado, pos)

    posicoes_possiveis = filtrar_posicoes_adjacentes(prado, posicoes_adjacentes, animal)
    len_posicoes_possiveis = len(posicoes_possiveis)

    if len_posicoes_possiveis == 0:
        return pos

    index_posicao_escolhida = valor_posicao_atual % len_posicoes_possiveis
    return posicoes_possiveis[index_posicao_escolhida]


def iterar_animal(prado, animal, posicao_atual, posicao_destino) -> bool:
    """Retorna o que aconteceu ao animal durante esta iteração do prado.

    Args:
        prado 
        animal 
        posicao_atual 
        posicao_destino 

    Returns:
        bool: comeu presa?
    """
    aumenta_idade(animal)
    aumenta_fome(animal)

    comeu_presa = False

    if not posicoes_iguais(posicao_atual, posicao_destino):
        if pode_comer_animal(prado, animal, posicao_destino):
            eliminar_animal(prado, posicao_destino)
            reset_fome(animal)
            comeu_presa = True

        mover_animal(prado, posicao_atual, posicao_destino)

        if eh_animal_fertil(animal):
            filho = reproduz_animal(animal)
            inserir_animal(prado, filho, posicao_atual)

    if eh_animal_faminto(animal):
        eliminar_animal(prado, posicao_destino)

    return comeu_presa


def geracao(prado: dict) -> dict:
    """É a funçãao auxiliar que modifica o prado fornecido como argumento de acordo com a evolução correspondente a uma geração completa, 
    e devolve o próprio prado. Isto é, seguindo a ordem de leitura do prado, cada animal (vivo) realiza o seu turno de ação. 

    Args:
        prado (dict)

    Returns:
        dict: prado
    """
    posicoes_por_validar = list(obter_posicao_animais(prado))

    while len(posicoes_por_validar) > 0:
        posicao_atual = posicoes_por_validar.pop(0)

        animal_iterante = obter_animal(prado, posicao_atual)
        posicao_destino = obter_movimento(prado, posicao_atual)

        comeu_presa = iterar_animal(prado, animal_iterante, posicao_atual, posicao_destino)

        if comeu_presa:
            # se um predados, ao comer (elimina presa do prado),
            # move-se para uma posicao para a direita ou para baixo
            # será necessário remover essa posicao (onde estava uma presa por iterar) das posicoes a validar,
            # senão esse animal (que já não é uma presa, mas um predador),
            # iterava duas vezes o predador.
            index_posicao = procurar_indice_posicao(posicoes_por_validar, posicao_destino)

            if index_posicao != -1:
                posicoes_por_validar.pop(index_posicao)

    return prado


def prado_para_str_com_estatisticas(prado, nr_predadores, nr_presas, nr_geracao):
    """Transforma os dados do prado numa string

    Args:
        prado 
        nr_predadores 
        nr_presas 
        nr_geracao 

    Returns:
        str: string com os dados do prado 
    """
    estatisticas = f"Predadores: {nr_predadores} vs Presas: {nr_presas} (Gen. {nr_geracao})"
    return estatisticas + "\n" + prado_para_str(prado)


def simula_ecossistema(nome_ficheiro: str, nr_geracoes_a_simular: int, verboso: bool) -> tuple:
    """É a função principal que permite simular o ecossistema de um prado.
     A função recebe uma cadeia de caracteres, um valor inteiro e um valor booleano e devolve o tuplo de dois elementos correspondentes ao número de predadores e 
     presas no prado no fim da simulação. 


    Args:
        nome_ficheiro (str): [description]
        nr_geracoes_a_simular (int): [description]
        verboso (bool): [description]

    Returns:
        tuple: [description]
    """
    prado = None

    with open(nome_ficheiro, 'r') as fp:
        dimensoes = eval(fp.readline())
        obstaculos = eval(fp.readline())
        animais_e_posicoes_raw = map(eval, fp.readlines())

        animais = []
        posicoes = []

        for i in animais_e_posicoes_raw:
            animal_raw = i[:-1]
            animais.append(cria_animal(animal_raw[0], animal_raw[1], animal_raw[2]))

            posicao_raw = i[-1]
            posicoes.append(cria_posicao(posicao_raw[0], posicao_raw[1]))

        prado = cria_prado(dimensoes, obstaculos, tuple(animais), tuple(posicoes))

    nr_predadores = obter_numero_predadores(prado)
    nr_presas = obter_numero_presas(prado)
    print(prado_para_str_com_estatisticas(prado, nr_predadores, nr_presas, 0))

    for g in range(nr_geracoes_a_simular):
        nr_predadores_old = nr_predadores
        nr_presas_old = nr_presas

        prado = geracao(prado)

        nr_predadores = (prado)
        nr_presas = obter_numero_presas(prado)

        if verboso:
            houve_diff_predadores = nr_predadores_old != nr_predadores
            houve_diff_presas = nr_presas != nr_presas_old

            if houve_diff_predadores or houve_diff_presas:
                print(prado_para_str_com_estatisticas(prado, nr_predadores, nr_presas, g + 1))
        else:
            if g == nr_geracoes_a_simular - 1:  # se for a ultima geracao...
                print(prado_para_str_com_estatisticas(prado, nr_predadores, nr_presas, g + 1))

    return ((prado), obter_numero_presas(prado))

