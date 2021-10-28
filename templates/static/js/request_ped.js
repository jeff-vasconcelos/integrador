
let sendPedidos = (inicio, fim) => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-pedidos/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'dt_inicio': inicio,
            'dt_fim': fim
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
                <p style="color: darkred" class="card-text-log"> >> Erro ao enviar pedidos!</p>
            `
        }
    })
}

function clickSendPedidos () {
    let date_start = document.getElementById('input-date-start-pedidos').value
    let date_end = document.getElementById('input-date-end-pedidos').value
    log_register.innerHTML += `
        <p class="card-text-log"> >> Iniciando envio de pedidos!</p>
    `
    sendPedidos(date_start, date_end)
}