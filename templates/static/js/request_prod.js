
let sendProd = () => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-produtos/',
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
                <p style="color: darkred" class="card-text-log"> >> Erro ao enviar produtos!</p>
            `
        }})
}

function clickSendProd() {
    log_register.innerHTML += `
        <p class="card-text-log"> >> Iniciando envio de produtos!</p>
    `
    sendProd()
}