
let sendEstoque = (inicio, fim) => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-entradas/',
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
                <p style="color: darkred" class="card-text-log"> >> Erro ao enviar entradas!</p>
            `
        }
    })
}

function clickSendEstoque () {
    let date_start = document.getElementById('input-date-start-entradas').value
    let date_end = document.getElementById('input-date-end-entradas').value
    log_register.innerHTML += `
        <p class="card-text-log"> >> Iniciando envio de entradas!</p>
    `
    sendEstoque(date_start, date_end)
}