# Task Manager

## Sobre
Simples aplicação web para gerenciamento de tarefas com os seguintes recursos:
 <ol>
    <li>Cadastro de tarefas;</li>
    <li>Lista de tarefas;</li>
    <li>Detalhar tarefas;</li>
    <li>Sistema de login e logout</li>
    <li>Um usuário pode assumir uma tarefa de criado por um outro usuário</li>
    <li>Paginaçāo</li>
    <li>Casdastro de acões tomadas para realizar a tarefa</li>
    <li>Funcionalides habilitadas somente se cumpridas algumas condiçoes</li>
 </ol>

## Ferramentas utilizadas
 Para criaçao desta aplicação, foi utilizado a linguagem python com seu framework django o banco de dados postgresql para a criaçao da estrutura do sistema. Para estilização foi utilizado o bootstrap e o fontawesome para alguns ícones.

 
## Como usar
 *OBS: Para que a aplicação funcione é necessário ter instalado e configurado na maquina o Postgreasql e o Python, recomendo  o tutorial abaixo: </br>
  https://blog.nextideatech.com/how-to-create-a-django-app-and-connect-it-to-a-database/ </br>
  Fazer as alteraçoes de configuraçõs de acordo com os dados da aplicação: </br>
     --> nome do banco de dados: tasksdb </br>
     --> nome de usuário do banco de dados: davi </br>
     --> senha de usuário do banco de dados: davilucca </br>
     
## 1- clonar o projeto computador
`````````````````````````
git clone https://github.com/shelsonx/simple_task_manager.git && cd simple_task_manager
`````````````````````````
## 2 - ativar a ambiente virtual

      -> . env/bin/activate

    2.1 entrar no diretório webApplication
       --> cd webApplication/
       
    2.2 criar um usuario para acesso ao sistema
       --> python3 manage.py createsuperuser
       * inserir nome e senha de sua preferência.
        
    2.3 iniciar o servidor
       --> python3 manage.py runserver
       
   
## 3 - abrir o navegador e acessar o o link
    --> http://127.0.0.1:8080/tasks/
   
<img src="https://github.com/shelsonx/simple_task_manager/blob/master/image/task_manager.gif"/>
  
  
