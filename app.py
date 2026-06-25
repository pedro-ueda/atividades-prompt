import streamlit as st
import nltk
from collections import Counter
from nltk.corpus import stopwords

st.title("Atividade 1")


st.title("Tokenizador")

# Garante o download do recurso necessário para a tokenização
nltk.download("punkt", quiet=True)

# Texto de exemplo simulando a mensagem de um cliente
texto_cliente = st.text_input('Insira seu texto')

if st.button('Clique para tokenizar'):
    # Executa a tokenização real do texto em palavras e pontuações
    tokens = nltk.word_tokenize(texto_cliente)

    st.text("\nTokens Gerados:")
    st.success(tokens)


st.title("Atividade 2")


st.title("Contador de palavras")

# Avaliações de exemplo combinadas em um único texto
avaliacoes = st.text_input('Insira seu texto', key="avaliacoes")

if st.button('Clique para contar'):

    st.text(avaliacoes)

    # Tokeniza o texto e padroniza para letras minúsculas
    tokens = nltk.word_tokenize(avaliacoes.lower())

    # Filtra para manter apenas palavras, removendo pontuações
    palavras = [token for token in tokens if token.isalnum()]

    # Conta a frequência de cada palavra
    contagem = Counter(palavras)

    # Exibe as palavras mais comuns e suas respectivas frequências
    st.text("Frequência das palavras:")

    for palavra, freq in contagem.most_common():
        st.success(f"{palavra}: {freq}")


st.title("Atividade 3")

# Interface simples com Streamlit
st.title("Detector de Mensagens Negativas")
mensagem = st.text_input("Digite a mensagem do cliente:", "O serviço foi ruim.")

# Botão para executar a análise
if st.button("Analisar Mensagem"):
    # Tokeniza e padroniza o texto para minúsculas
    tokens = nltk.word_tokenize(mensagem.lower())

    # Lista de gatilhos negativos
    palavras_negativas = {"ruim", "péssimo", "erro", "pessimo"}

    # Verifica a interseção entre os tokens e as palavras negativas
    intersecao = palavras_negativas.intersection(tokens)

    # Exibe o resultado condicional na tela do Streamlit
    if intersecao:
        st.error(f"Alerta: Mensagem negativa detectada! Palavras: {intersecao}")
    else:
        st.success("Mensagem limpa. Sem termos negativos identificados.")


st.title("Atividade 4")

# Garante o download dos recursos necessários do NLTK
nltk.download("stopwords", quiet=True)

st.title("Removedor de Stopwords")
texto = st.text_input("Texto:", "O produto é bom, mas a entrega para o Brasil atrasou.")

if st.button("Remover Stopwords"):
    # Tokeniza o texto e carrega a lista de stopwords em português
    tokens = nltk.word_tokenize(texto.lower())
    palavras_irrelevantes = set(stopwords.words("portuguese"))

    # Filtra os tokens mantendo apenas o que não for stopword e for alfanumérico
    filtrado = [t for t in tokens if t not in palavras_irrelevantes and t.isalnum()]

    # Exibe o resultado formatado como string na tela
    st.write("**Texto Original:**", texto)
    st.success(f"**Resultado Filtrado:** {' '.join(filtrado)}")


st.title("Atividade 5")

st.title("Classificador de Sentimento Simples")
comentario = st.text_input("Comentário do cliente:", "O atendimento foi ótimo, mas o prazo foi ruim.")

if st.button("Classificar Sentimento"):
    tokens = set(nltk.word_tokenize(comentario.lower()))

    # Listas de palavras-chave para a pontuação
    positivas = {"bom", "ótimo", "otimo", "excelente", "maravilhoso", "rápido", "gostei"}
    negativas = {"ruim", "péssimo", "pessimo", "lento", "atrasou", "odiei", "caro"}

    # Calcula o score baseado na interseção de palavras
    score = len(tokens.intersection(positivas)) - len(tokens.intersection(negativas))

    # Classifica e exibe o resultado com base no score
    if score > 0:
        st.success(f"Sentimento: **Positivo** (Score: {score})")
    elif score < 0:
        st.error(f"Sentimento: **Negativo** (Score: {score})")
    else:
        st.warning(f"Sentimento: **Neutro** (Score: {score})")

        

st.title("Atividade 6")

st.title("Roteador de Chatbot por Palavras-Chave")
mensagem = st.text_input("Mensagem do cliente:", "Tive um erro no processamento do pagamento.")

if st.button("Direcionar Atendimento"):
    tokens = set(nltk.word_tokenize(mensagem.lower()))

    # Mapeamento de palavras-chave para seus respectivos setores
    setores = {"cancelar": "Retenção", "erro": "Suporte Técnico", "pagamento": "Financeiro"}

    # Identifica as palavras mapeadas que estão presentes na mensagem
    chaves_encontradas = tokens.intersection(setores.keys())

    # Exibe o direcionamento na tela do Streamlit
    if chaves_encontradas:
        for chave in chaves_encontradas:
            st.info(f"Setor identificado por '{chave}': **{setores[chave]}**")
    else:
        st.warning("Nenhuma palavra-chave identificada. Encaminhando para a triagem geral.")

        

st.title("Atividade 7")

st.title("Analisador de Palavras Frequentes")
reclamacao = st.text_area("Reclamação do cliente:", "O aplicativo trava muito. O aplicativo é lento e o suporte não responde. Que aplicativo ruim!")

if st.button("Analisar Frequência"):
    # Tokeniza, padroniza para minúsculas e filtra apenas caracteres alfanuméricos
    tokens = nltk.word_tokenize(reclamacao.lower())
    palavras = [t for t in tokens if t.isalnum()]

    # Conta a frequência e extrai as mais comuns
    contagem = Counter(palavras).most_common()

    # Exibe o resultado na tela do Streamlit
    st.write("**Resultado da Contagem:**")
    for palavra, freq in contagem:
        st.write(f"- **{palavra}**: aparece {freq} vez(es)")

        

st.title("Atividade 8")

st.title("Classificador de Departamento")
mensagem = st.text_input("Mensagem do cliente:", "Preciso de ajuda com o boleto.")

if st.button("Classificar Mensagem"):
    tokens = set(nltk.word_tokenize(mensagem.lower()))

    # Palavras-chave de cada departamento
    tecnico = {"erro", "bug", "senha", "sistema", "login", "travo", "app"}
    financeiro = {"boleto", "pagamento", "fatura", "cobrança", "reembolso", "preço"}

    # Classificação baseada na interseção de palavras
    if tokens.intersection(tecnico) and not tokens.intersection(financeiro):
        st.info("Departamento: **Suporte Técnico**")
    elif tokens.intersection(financeiro) and not tokens.intersection(tecnico):
        st.success("Departamento: **Financeiro**")
    else:
        st.warning("Departamento: **Encaminhar para Triagem Geral**")

        

st.title("Atividade 9")

st.title("Limpador e Normalizador de Texto")
texto_usuario = st.text_area("Texto original:", "Olá! O produto chegou? Sim, chegou perfeitamente.")

if st.button("Limpar Texto"):
    # Tokeniza o texto convertido para minúsculas
    tokens = nltk.word_tokenize(texto_usuario.lower())

    # Mantém apenas os tokens que são puramente alfanuméricos (remove pontuações)
    tokens_limpos = [token for token in tokens if token.isalnum()]

    # Junta os tokens limpos de volta em uma string para exibição
    texto_limpo = " ".join(tokens_limpos)

    # Exibe os resultados na tela
    st.write("**Tokens limpos (Lista):**", tokens_limpos)
    st.success(f"**Texto normalizado:** {texto_limpo}")

        

st.title("Atividade 10")

st.title("Análise de Sentimento de Avaliações")
avaliacao = st.text_input("Avaliação do produto:", "Amei o produto, muito bom e entrega rápida!")

if st.button("Analisar Satisfação"):
    # Tokeniza e padroniza o texto para minúsculas
    tokens = set(nltk.word_tokenize(avaliacao.lower()))

    # Léxico simples de termos positivos e negativos
    positivos = {"bom", "amei", "gostei", "excelente", "maravilhoso", "recomendo", "rápida"}
    negativos = {"ruim", "péssimo", "pessimo", "odiei", "defeito", "atrasou", "quebrado"}

    # Avalia a presença das palavras-chave no texto
    tem_positivo = bool(tokens.intersection(positivos))
    tem_negativo = bool(tokens.intersection(negativos))

    # Determina o estado de satisfação por regras condicionais
    if tem_positivo and not tem_negativo:
        st.success("Cliente Satisfeito 😊")
    elif tem_negativo and not tem_positivo:
        st.error("Cliente Insatisfeito 😡")
    else:
        st.warning("Resultado Inconclusivo / Neutro 😐")