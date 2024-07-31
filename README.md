# Personal Finance Tracker - Ficker

[![Qodana](https://github.com/gonssalves/ficker-devops/actions/workflows/code_quality.yml/badge.svg)](https://github.com/gonssalves/ficker-devops/actions/workflows/code_quality.yml)

## Configuration
You should have Python and virtual environment (preferentially) on your machine.
* Use <em>pip install -r requirements.txt</em> to install the packages.
* After the packages are installed, activate the virtual environment with <em>. venv/bin/activate</em>
* While inside the venv, to run the server, use <em>flask --app app run --debug</em> or <em>export FLASK_APP=app</em> and then <em>flask run</em>.

Additionally, you can find our app URL in the 'about' section. Please be patient, though, as the service spins down due to inactivity, so it might take a while to load.

Feel free to contribute :)

## Relatório

<b>I. Codebase:</b>

Status de Implementação: ✅

A base de código da aplicação está hospedada em um repositório Git na plataforma de versionamento, acessível através do link https://github.com/gonssalves/ficker.

<b>II. Dependencies:</b>

Status de Implementação: ✅

Utilizamos a ferramenta Pipenv para declarar e gerenciar as dependências no código da aplicação, garantindo uma gestão eficiente e organizada.

<b>III. Configs:</b>

Status de Implementação: ✅

Implementamos a biblioteca Dotenv do Python para configurar diversas variáveis de ambiente da aplicação, facilitando a gestão e o controle das configurações através de arquivos .env.

<b>IV. Backing services:</b>

Status de Implementação: ✅

O código da aplicação foi desenvolvido para interoperar com sistemas similares sem a necessidade de modificações no código, apenas exigindo ajustes na configuração através de strings de conexão.


<b>V. Build, release, run</b>

Status de Implementação: ✅

Shell scripts foram utilizados para separar os estágios de execução da aplicação. O script de build, por exemplo, cria um ambiente virtual, ativa o ambiente e instala as dependências. 

<b>VI. Processes</b>

Status de Implementação: ✅

Foi utilizado o Servidor WSGI Gunicorn para executar a aplicação em produção com múltiplos workers, cada um sendo um processo separado que pode lidar com solicitações HTTP.

<b>VII. Port Binding:</b>

Status de Implementação: ✅

A aplicação está configurada para receber requisições na porta 8080 (postgres na porta 5432), garantindo a correta comunicação com outros sistemas.

<b>VIII. Concurrency:</b>

Status de Implementação: ✅

Foi usado o Celery para tarefas em segundo plano, permitindo que a aplicação distribua a carga de trabalho de forma eficiente, processando tarefas assíncronas em paralelo com solitações HTTP principais.

<b>IX. Disposability:</b>

Status de Implementação: ✅

Pelo fato da aplicação ser dockerizada, os containers podem ser iniciados, parados e substituídos rapidamente, conforme necessário.

<b>X. Dev/Prod Parity:</b>

Status de Implementação: ❌

Este fator não foi requisitado no contexto do projeto.

<b>XI. Logs:</b>

Status de Implementação: ✅

Utilizamos a ferramenta Sentry para capturar e tratar logs da aplicação, garantindo um monitoramento eficaz e a identificação de eventuais problemas.

<b>XII. Admin Processes:</b>

Status de Implementação: ✅

Incorporamos as rotinas administrativas, como migrações e outros processos, diretamente na base de código do sistema, simplificando e automatizando tarefas administrativas.


