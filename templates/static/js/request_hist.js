
let sendHistorico = (inicio, fim) => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-historico/',
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
                <p style="color: darkred" class="card-text-log"> >> Erro ao enviar histórico!</p>
            `
        }
    })
}

function clickSendHistorico () {
    let date_start = document.getElementById('input-date-start-historico').value
    let date_end = document.getElementById('input-date-end-historico').value
    log_register.innerHTML += `
        <p class="card-text-log"> >> Iniciando envio de histórico!</p>
    `
    sendHistorico(date_start, date_end)
}