# backend/main.py

"""
Ponto de entrada da API para a Render.

Reaproveita o app definido em backend/alunos.py,
onde estão todas as rotas (professor, academias, medalhas, ranking e alunos).
"""

from .alunos import app  # noqa: F401
