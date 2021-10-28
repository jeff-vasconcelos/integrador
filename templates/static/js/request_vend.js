
let sendVendas = (inicio, fim) => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-vendas/',
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
                <p style="color: darkred" class="card-text-log"> >> Erro ao enviar vendas!</p>
            `
        }
    })
}

function clickSendVendas () {
    let date_start = document.getElementById('input-date-start-vendas').value
    let date_end = document.getElementById('input-date-end-vendas').value
    log_register.innerHTML += `
        <p class="card-text-log"> >> Iniciando envio de vendas!</p>
    `
    sendVendas(date_start, date_end)
}