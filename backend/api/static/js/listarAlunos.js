
async function deletar(id){
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
    const resposta = await apiFetch(`/api/user/${id}`, "DELETE", null, {"X-CSRFToken":csrf})

    if(resposta.status === 200){
        var linhaAluno = document.getElementById(`usuarios-${id}`)
        linhaAluno.remove()
    }

}
