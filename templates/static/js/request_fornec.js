
let sendFornec = () => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-fornecedores/',
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
                <p style="color: darkred" class="card-text-log"> >> Erro ao enviar fornecedores!</p>
            `
        }
    })
}

function clickSendFornec() {
    log_register.innerHTML += `
        <p class="card-text-log"> >> Iniciando envio de fornecedores!</p>
    `
    sendFornec()
}