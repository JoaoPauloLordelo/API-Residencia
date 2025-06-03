from transformers import pipeline

# Carrega o modelo uma única vez quando o módulo é importado
analisador = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analisar_sentimento_texto(mensagem: str):
    """Analisa o sentimento do texto usando o modelo pré-carregado."""
    if not mensagem:
        return None # Ou algum valor padrão/erro
    try:
        resultado = analisador(mensagem)
        # Extrai apenas a label do sentimento (ex: '5 stars', '1 star')
        # A estrutura exata de 'resultado' pode variar, ajuste se necessário
        if resultado and isinstance(resultado, list):
            return resultado[0].get('label', 'Erro na análise') 
        else:
            return 'Erro na análise'
    except Exception as e:
        print(f"Erro durante a análise de sentimento: {e}")
        return 'Erro na análise'


