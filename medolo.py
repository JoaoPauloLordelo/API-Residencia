from transformers import pipeline

def analisadorSentimento(mensagem :str):
    analisador = pipeline("sentiment-analysis",model="nlptown/bert-base-multilingual-uncased-sentiment")
    resultado = analisador(mensagem)
    return resultado
