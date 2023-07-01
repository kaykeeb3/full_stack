<h1 align="center">FULL-STACK</h1>

<p align="center">Aplicação desenvolvida para um chat de estudos usando uma API implementada de uma base de dados, usuário faz a determinada pergunta a API retorna a resposta.

<br>

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

### Front-end 
- Go

### Back-end 
- Python
- OpenAi
- API Chat-bot
  

## 💻 Projeto

#### Back-end
Substitua "YOUR_OPENAI_API_KEY" pela sua chave de API do OpenAI.
<br/>

Este código define um aplicativo Flask que possui uma rota /question que aceita requisições POST. Ele espera um payload JSON com um campo prompt contendo a pergunta. A função handle_question() extrai a pergunta da requisição, chama a função get_openai_response() para obter a resposta do OpenAI e retorna a resposta como JSON.
<br/>

A função get_openai_response() envia uma requisição POST para a API do OpenAI com o prompt fornecido, usando a biblioteca requests. Ela inclui os cabeçalhos e a chave de API necessários. Se a requisição for bem-sucedida, ela extrai as opções de resposta da resposta e retorna uma instância da classe OpenAIResponse
<br/>

#### Fron-end 
Este código Go define um servidor HTTP que lida com duas rotas. A rota / lida com as requisições GET e serve o arquivo index.html. A rota / lida com as requisições POST, obtém a mensagem do corpo da requisição e chama a função getChatResponse() para obter a resposta do backend em Python.
<br/>

A função getChatResponse() envia uma requisição POST para o endpoint /question do backend Python, passando a mensagem fornecida como payload. Ele recebe a resposta do backend e a decodifica em uma estrutura ChatResponse antes de retorná-la.
<br/>

Certifique-se de substituir a URL "http://localhost:5000/question" no trecho http.NewRequest no método getChatResponse() pelo URL correto do seu backend Python.
<br/>

Certifique-se de ter os pacotes html/template e encoding/json importados

- [Visite o projeto online](https://chat-gpt-bot-rouge.vercel.app/)
  
