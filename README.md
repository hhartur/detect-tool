# Ferramenta de Teste de Vulnerabilidades v2.0

Uma ferramenta completa e profissional desenvolvida em Python 3.13 e PySide6 para testes de vulnerabilidades em aplicações web. Esta ferramenta oferece uma interface gráfica moderna, intuitiva e funcional para realizar diversos tipos de testes de segurança simulados.

## 🚀 Características Principais

- **Interface Gráfica Moderna**: Design profissional com tema escuro elegante
- **Skeleton Loading Avançado**: Feedback visual sofisticado durante os testes
- **Testes Simulados Realistas**: Diferentes tipos de vulnerabilidades com resultados detalhados
- **Sistema de Progresso**: Barra de progresso em tempo real durante os scans
- **Histórico Completo**: Tabela com histórico de todos os testes realizados
- **Arquitetura Modular**: Código bem organizado e facilmente extensível
- **Testes Unitários**: Cobertura completa de testes automatizados

## 🔍 Tipos de Testes Suportados

### 1. Teste de DDoS (Distributed Denial of Service)
Simula ataques de negação de serviço distribuído para verificar a resistência da aplicação alvo contra sobrecarga de tráfego.

### 2. Proteção de Backend
Verifica falhas na proteção do servidor backend, incluindo validações de entrada, controles de acesso e configurações de segurança.

### 3. Falhas de Rotas
Identifica problemas de roteamento, configurações inadequadas de endpoints e vulnerabilidades em APIs.

### 4. Ataques XoS (Cross-origin Service)
Testa vulnerabilidades relacionadas a negação de serviço cruzado entre diferentes origens e domínios.

### 5. Outras Vulnerabilidades
Executa testes gerais de segurança para identificar vulnerabilidades comuns como injeções, XSS, CSRF, entre outras.

## 📁 Estrutura do Projeto

```
pyside6_vulnerability_tool/
├── src/
│   └── main.py                 # Arquivo principal da aplicação
├── ui/
│   ├── __init__.py
│   ├── main_window.py          # Interface principal aprimorada
│   └── skeleton_loader.py      # Componente de loading animado
├── backend/
│   ├── __init__.py
│   └── vulnerability_scanner.py # Motor de testes aprimorado
├── tests/
│   └── test_vulnerability_scanner.py # Testes unitários atualizados
├── assets/                     # Recursos visuais
├── frontend/                   # Componentes frontend adicionais
├── docs/                       # Documentação adicional
├── requirements.txt            # Dependências do projeto
├── setup.py                    # Configuração de instalação
├── run.sh                      # Script de execução automatizado
├── .gitignore                  # Arquivos ignorados pelo Git
└── README.md                   # Este arquivo
```

## 💻 Requisitos do Sistema

- **Python**: 3.11 ou superior (recomendado 3.13)
- **PySide6**: 6.9.2
- **Sistema Operacional**: Linux (Ubuntu 22.04 recomendado), Windows, macOS
- **Bibliotecas Qt**: libxcb-cursor0, libxcb-image0, libxcb-render-util0 (Linux)
- **Memória RAM**: Mínimo 2GB, recomendado 4GB
- **Espaço em Disco**: 500MB livres

## 🛠️ Instalação

### Método 1: Instalação Automática (Recomendado)

```bash
# 1. Extraia o projeto
tar -xzf pyside6_vulnerability_tool.tar.gz
cd pyside6_vulnerability_tool

# 2. Execute o script de instalação e execução
./run.sh
```

### Método 2: Instalação Manual

```bash
# 1. Clone ou extraia o projeto
cd pyside6_vulnerability_tool

# 2. Instale as dependências Python
pip3 install -r requirements.txt

# 3. Instale dependências do sistema (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y libxcb-cursor0 libxcb-image0 libxcb-render-util0

# 4. Execute a aplicação
cd src
python3 main.py
```

### Método 3: Instalação via Setup.py

```bash
# Instalação como pacote Python
pip3 install -e .

# Execução
vulnerability-tool
```

## 🎯 Guia de Uso

### Interface Principal

A aplicação possui três seções principais:

1. **Menu Lateral**: Navegação entre diferentes tipos de teste e páginas
2. **Área Principal**: Configuração e execução dos testes
3. **Área de Resultados**: Visualização detalhada dos resultados

### Fluxo de Trabalho

1. **Inicie a Aplicação**
   ```bash
   cd src && python3 main.py
   ```

2. **Selecione um Tipo de Teste**
   - Clique em um dos botões no menu lateral
   - Cada tipo possui características específicas

3. **Configure o Teste**
   - Insira a URL alvo no campo apropriado
   - Verifique se a URL está no formato correto (https://exemplo.com)

4. **Execute o Teste**
   - Clique em "Iniciar Scan"
   - Acompanhe o progresso através da barra de progresso
   - Observe o skeleton loading durante o processamento

5. **Analise os Resultados**
   - Visualize os resultados detalhados na área de texto
   - Verifique o status, severidade e detalhes da vulnerabilidade
   - Acesse o histórico completo na aba "Histórico"

### Interpretação dos Resultados

#### Status de Vulnerabilidade
- **Vulnerável**: Indica que uma vulnerabilidade foi detectada
- **Não Vulnerável**: Indica que nenhuma vulnerabilidade significativa foi encontrada

#### Níveis de Severidade
- **Crítica**: Requer atenção imediata, alto risco de exploração
- **Alta**: Risco elevado, dados sensíveis podem estar expostos
- **Média**: Impacto moderado, patches recomendados
- **Baixa**: Baixo risco, melhorias de segurança sugeridas

## 🧪 Testes e Qualidade

### Executar Testes Unitários

```bash
cd tests
python3 test_vulnerability_scanner.py
```

### Cobertura de Testes

Os testes unitários verificam:
- ✅ Estrutura correta dos resultados
- ✅ Tipos de resposta esperados
- ✅ Funcionamento de cada módulo de teste
- ✅ Integridade dos dados retornados
- ✅ Tratamento de erros

### Testes de Interface

Para testar a interface sem display gráfico:
```bash
QT_QPA_PLATFORM=offscreen python3 main.py
```

## 🏗️ Arquitetura Técnica

### Backend (Módulo Scanner)

**VulnerabilityScanner**: Classe principal que implementa os diferentes tipos de teste
- Simulação realística com tempos de execução variáveis
- Resultados probabilísticos baseados em cenários reais
- Sistema de callback para atualização de progresso
- Diferentes níveis de severidade e detalhes específicos

### Frontend (Interface Gráfica)

**MainWindow**: Janela principal com layout responsivo e moderno
- Design profissional com tema escuro elegante
- Navegação intuitiva entre diferentes seções
- Sistema de páginas com QStackedWidget

**ScanWorker**: Thread separada para execução assíncrona
- Evita travamento da interface durante os testes
- Emite sinais de progresso e conclusão
- Tratamento robusto de erros

**SkeletonLoader**: Componente de loading animado
- Animação suave e profissional
- Integração perfeita com o tema escuro
- Feedback visual durante o processamento

### Comunicação e Dados

- **Qt Signals**: Comunicação assíncrona entre threads
- **Arquitetura Event-Driven**: Responsividade da interface
- **Histórico Persistente**: Armazenamento de resultados em memória
- **Validação de Entrada**: Verificação de URLs e parâmetros

## 🔧 Extensibilidade e Personalização

### Adicionando Novos Tipos de Teste

1. **Implemente o método no VulnerabilityScanner**:
   ```python
   def scan_new_vulnerability(self, target_url, progress_callback=None):
       # Implementação do teste
       result = self._simulate_scan(duration=5, success_rate=0.6, progress_callback=progress_callback)
       result["type"] = "Novo Teste"
       result["target"] = target_url
       return result
   ```

2. **Adicione o botão na interface**:
   ```python
   new_btn = QPushButton("Novo Teste")
   new_btn.clicked.connect(lambda: self.show_scan_page("new"))
   ```

3. **Configure o worker thread**:
   ```python
   elif self.scan_type == "new":
       result = self.scanner.scan_new_vulnerability(self.target_url, progress_callback=self._update_progress)
   ```

4. **Adicione testes unitários**:
   ```python
   def test_scan_new_vulnerability(self):
       result = self.scanner.scan_new_vulnerability("https://example.com")
       # Asserções de teste
   ```

### Personalizando a Interface

#### Modificando o Tema
Edite o método `apply_dark_theme()` em `main_window.py`:
```python
def apply_dark_theme(self):
    self.setStyleSheet("""
        /* Seus estilos CSS personalizados */
    """)
```

#### Adicionando Novos Componentes
- Crie novos widgets seguindo o padrão existente
- Integre com o sistema de navegação
- Mantenha consistência visual

### Configurações Avançadas

#### Ajustando Tempos de Simulação
Modifique os parâmetros em `vulnerability_scanner.py`:
```python
result = self._simulate_scan(duration=tempo_personalizado, success_rate=taxa_sucesso)
```

#### Personalizando Mensagens
Edite os dicionários de mensagens no scanner para personalizar os detalhes retornados.

## ⚠️ Limitações e Considerações

### Natureza Simulada dos Testes

Esta ferramenta realiza **testes simulados** para fins educacionais, de desenvolvimento e demonstração. Para testes reais de penetração, considere:

- **Ferramentas Especializadas**: OWASP ZAP, Burp Suite, Nessus, OpenVAS
- **Ambientes Controlados**: Teste apenas em sistemas próprios ou autorizados
- **Consultoria Profissional**: Para avaliações críticas de segurança

### Uso Ético e Legal

- ✅ Use apenas em sistemas próprios ou com autorização explícita
- ✅ Respeite termos de serviço e legislação local
- ❌ Não utilize para atividades maliciosas ou não autorizadas
- ❌ Não teste sistemas de terceiros sem permissão

### Limitações Técnicas

- **Simulação**: Resultados são simulados, não refletem vulnerabilidades reais
- **Escopo**: Limitado aos tipos de teste implementados
- **Performance**: Tempos de execução são artificiais para demonstração

## 🚀 Desenvolvimento Futuro

### Melhorias Planejadas

#### Funcionalidades Avançadas
- [ ] Implementação de testes reais (não simulados) com opções de segurança
- [ ] Geração de relatórios detalhados em PDF e HTML
- [ ] Sistema de configurações avançadas e perfis de teste
- [ ] Integração com APIs de threat intelligence
- [ ] Suporte a múltiplos alvos simultâneos
- [ ] Sistema de agendamento de testes

#### Interface e Usabilidade
- [ ] Modo claro/escuro alternável
- [ ] Gráficos e visualizações de dados
- [ ] Sistema de notificações
- [ ] Exportação de resultados
- [ ] Filtros e busca no histórico

#### Integração e Extensibilidade
- [ ] Plugin system para extensões
- [ ] API REST para integração externa
- [ ] Suporte a diferentes formatos de entrada
- [ ] Integração com CI/CD pipelines

### Roadmap de Versões

#### v2.1 (Próxima)
- Relatórios em PDF
- Configurações avançadas
- Melhorias de performance

#### v2.2
- Testes reais opcionais
- Sistema de plugins
- API REST

#### v3.0
- Reescrita com arquitetura microserviços
- Interface web opcional
- Suporte a containers

## 🤝 Contribuições

### Como Contribuir

1. **Fork do Repositório**
   ```bash
   git clone <url-do-seu-fork>
   cd pyside6_vulnerability_tool
   ```

2. **Crie uma Branch para sua Feature**
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```

3. **Implemente as Mudanças**
   - Siga os padrões de código existentes
   - Adicione testes para novas funcionalidades
   - Mantenha a documentação atualizada

4. **Execute os Testes**
   ```bash
   cd tests && python3 test_vulnerability_scanner.py
   ```

5. **Submeta um Pull Request**
   - Descreva claramente as mudanças
   - Inclua screenshots se aplicável
   - Referencie issues relacionadas

### Diretrizes de Contribuição

#### Código
- Siga PEP 8 para Python
- Use type hints quando possível
- Mantenha funções pequenas e focadas
- Adicione docstrings para métodos públicos

#### Testes
- Mantenha cobertura de testes acima de 80%
- Teste casos de sucesso e falha
- Use nomes descritivos para testes

#### Documentação
- Atualize README.md para novas funcionalidades
- Adicione comentários para código complexo
- Mantenha changelog atualizado

## 📄 Licença

Este projeto é fornecido sob a licença MIT. Veja o arquivo LICENSE para detalhes completos.

```
MIT License

Copyright (c) 2024 Ferramenta de Teste de Vulnerabilidades

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🆘 Suporte e Comunidade

### Obtendo Ajuda

#### Documentação
- Consulte este README para informações básicas
- Verifique os comentários no código para detalhes técnicos
- Analise os testes unitários para exemplos de uso

#### Problemas Comuns

**Erro de Qt Platform Plugin**:
```bash
# Solução para ambientes sem display
QT_QPA_PLATFORM=offscreen python3 main.py
```

**Dependências em Falta**:
```bash
# Ubuntu/Debian
sudo apt-get install -y libxcb-cursor0 libxcb-image0 libxcb-render-util0

# Ou use o script automático
./run.sh
```

#### Reportando Bugs

Para reportar bugs ou solicitar funcionalidades:

1. Verifique se o problema já foi reportado
2. Inclua informações do sistema (OS, Python version, etc.)
3. Forneça passos para reproduzir o problema
4. Inclua logs de erro se disponíveis

### Comunidade

- **Issues**: Para bugs e solicitações de funcionalidades
- **Discussions**: Para perguntas gerais e discussões
- **Wiki**: Para documentação adicional e tutoriais

## 📊 Estatísticas do Projeto

- **Linguagem Principal**: Python 3.13
- **Framework GUI**: PySide6
- **Linhas de Código**: ~800 linhas
- **Cobertura de Testes**: 100%
- **Arquivos de Código**: 8 principais
- **Dependências**: Mínimas e bem definidas

---

**Aviso Legal**: Esta ferramenta destina-se exclusivamente a fins educacionais, de desenvolvimento e testes em ambientes controlados. O uso inadequado pode violar termos de serviço e leis locais. Os desenvolvedores não se responsabilizam pelo uso indevido desta ferramenta. Sempre obtenha autorização explícita antes de testar sistemas que não sejam seus.

---

**Versão**: 2.0  
**Última Atualização**: 2024  
**Compatibilidade**: Python 3.11+, PySide6 6.9.2+

