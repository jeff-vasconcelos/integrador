
let sendEstoque = () => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-estoque/',
        data: {
            'csrfmiddlewaretoken': csrf
        },
        success: (response) => {
            let message = response.data
            log_register.innerHTML += `
                <p class="card-text-log"> >> ${message}</p>
            `
        },
        error: function (error) {
            console.log(error)
            log_register.innerHTML += `
                <p style="color: darkred" class="card-text-log"> >> Erro ao enviar estoque!</p>
            `
        }
    })
}

function clickSendEstoque () {
    log_register.innerHTML += `
        <p class="card-text-log"> >> Iniciando envio de estoque!</p>
    `
    sendEstoque()
}