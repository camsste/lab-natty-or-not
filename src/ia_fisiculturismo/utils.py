import random
from typing import List

def formatar_titulo(texto: str, simbolo: str = "=") -> str:
    """Formata um título com símbolos"""
    return f"\n{simbolo * 40}\n{texto}\n{simbolo * 40}"

def selecionar_aleatorio(lista: List, quantidade: int = 1):
    """Seleciona itens aleatórios de uma lista"""
    if quantidade == 1:
        return random.choice(lista)
    return random.sample(lista, quantidade)

def validar_entrada_usuario(entrada: str, opcoes_validas: List[str]) -> bool:
    """Valida a entrada do usuário"""
    return entrada.strip() in opcoes_validas