#!/bin/bash

echo "Iniciando Ferramenta de Teste de Vulnerabilidades..."

if ! command -v python3 &> /dev/null; then
    echo "Python 3 não encontrado. Por favor, instale Python 3.11 ou superior."
    exit 1
fi

if ! python3 -c "import PySide6" 2>/dev/null; then
    echo "PySide6 não encontrado. Instalando dependências..."
    pip3 install -r requirements.txt
fi

echo "Verificando dependências do sistema..."
if ! dpkg -l | grep -q libxcb-cursor0; then
    echo "Instalando dependências do Qt..."
    sudo apt-get update
    sudo apt-get install -y libxcb-cursor0 libxcb-image0 libxcb-render-util0
fi

echo "Executando aplicação..."
cd src
python3 main.py

