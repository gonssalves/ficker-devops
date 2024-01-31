#!/bin/bash

# Criação de ambiente virtual
python -m venv venv

# Ativação do ambiente virtual
source venv/bin/activate

# Instalação de dependências
pip install -r requirements.txt
