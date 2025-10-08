# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [2.0.0] - 2024-12-24

### Adicionado
- Interface gráfica completamente redesenhada com tema escuro profissional
- Sistema de histórico de scans com tabela detalhada
- Barra de progresso em tempo real durante os testes
- Skeleton loading animado e integrado ao tema
- Ícones nos botões do menu lateral
- Página inicial aprimorada com informações detalhadas
- Sistema de navegação por páginas (Home, Scan, Histórico)
- Resultados detalhados com status, severidade e descrições específicas
- Testes unitários atualizados para nova estrutura de dados
- Script de execução automatizado (run.sh)
- Arquivo de configuração setup.py
- Documentação completa e profissional

### Modificado
- Backend de testes completamente refatorado para outputs realistas
- Sistema de progresso com callback para atualização da UI
- Estrutura de dados dos resultados (status, severity, details)
- Layout da interface principal com melhor organização
- Tema escuro com cores mais elegantes e profissionais
- Testes unitários adaptados para nova estrutura
- README.md completamente reescrito com guia detalhado

### Corrigido
- Erro de sintaxe em f-strings
- Problemas de importação entre módulos
- Compatibilidade com diferentes ambientes Qt
- Tratamento de erros na interface
- Sincronização entre threads

### Removido
- Outputs simplificados do backend antigo
- Interface básica da versão anterior
- Dependências desnecessárias

## [1.0.0] - 2024-12-24

### Adicionado
- Implementação inicial da ferramenta
- Interface básica com PySide6
- Testes simulados de vulnerabilidades (DDoS, Backend, Rotas, XoS, Outros)
- Sistema básico de skeleton loading
- Testes unitários básicos
- Estrutura modular do projeto
- Documentação inicial

### Funcionalidades Iniciais
- Teste de DDoS simulado
- Teste de proteção de backend
- Teste de falhas de rotas
- Teste de ataques XoS
- Outros testes de vulnerabilidades
- Interface gráfica básica
- Sistema de threads para não bloquear UI

