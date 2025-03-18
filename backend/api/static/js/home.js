document.addEventListener('DOMContentLoaded', function () {
    async function GetUserLogado() {
        const resposta = await apiFetch('/api/GetDadosUsuarioLogado')
        
        const div = document.getElementById('nomeUsuario')
        div.innerHTML = resposta.username
    }
    GetUserLogado()

});