async function Login(evento){
    evento.preventDefault();

    const nome = document.getElementById('nome').value
    const senha = document.getElementById('senha').value
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value

    const resposta = await apiFetch('/api/login/', "POST", {nome:nome, senha:senha}, {"X-CSRFToken":csrf})


    console.log(resposta)
    
}

document.getElementById('loginForm').addEventListener("submit", Login)