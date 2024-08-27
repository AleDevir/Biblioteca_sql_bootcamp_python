'''
Módulo com fluxo principal do programa Biblioteca.
  
'''

from src.app_biblioteca import biblioteca_db

if __name__ == "__main__":
    biblioteca_db()

from src.db.conexao_db import encontrar_livros_emprestados
