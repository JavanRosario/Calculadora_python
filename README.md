# Calculadora PySide6

Uma calculadora desktop desenvolvida em Python usando PySide6, com interface personalizada, operações básicas, exponenciação e sinais customizados para teclado. Possui display customizado para entrada de números, label de informações intermediárias, validação de entradas e tratamento de erros como divisão por zero ou overflow.

Funcionalidades: suporta operações `+`, `-`, `*`, `/` e `^`, interface com tema escuro, atalhos de teclado (Enter para calcular, Backspace/Delete para apagar, Esc para limpar, operadores via teclado), validação de números e ponto decimal, e mensagens de erro exibidas na interface.

Estrutura do projeto: a pasta `layout/` contém a janela principal (`main_window.py`), widgets (`dysplays.py`), botões e grade (`buttons.py`) e configuração de estilos (`styles.py`). A pasta `scripts/` contém constantes e variáveis de estilo (`variables.py`) e funções auxiliares (`utils.py`). O arquivo `main.py` inicia a aplicação. O projeto inclui este README.md com instruções completas.

Requisitos: Python 3.10+ e PySide6. Instalação de dependências: `pip install PySide6`. Para executar, rode `python main.py`.

Uso: digite números no display ou use o teclado, clique nos operadores ou use os atalhos, pressione `=` ou Enter para calcular, e use `C` ou Esc para limpar. O display e os botões são conectados a sinais personalizados que gerenciam entradas, operadores, backspace, clear e execução de cálculos. Erros como divisão por zero ou overflow são tratados e exibidos no label de informações.

Exemplo de código de inicialização da aplicação:

```python
from layout.main_window import MainWindow
from layout.dysplays import Dysplay, Infos
from layout.buttons import Grid
from PySide6.QtWidgets import QApplication

app = QApplication([])
window = MainWindow()
info = Infos("Sua conta")
window.add_widget(info)
dysplay = Dysplay()
window.add_widget(dysplay)
grid = Grid(dysplay, info, window)
window.window_layout.addLayout(grid)
window.show()
app.exec()
