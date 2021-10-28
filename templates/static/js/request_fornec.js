let csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

let sendFornec = (inicio, fim) => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-fornecedores/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'dt_inicio': inicio,
            'dt_fim': fim
        },
        success: (response) => {
            let message = response.data
        },
        error: function (error) {
            console.log(error)
        }
    })
}

function clickSendFornec () {
    let date_start = document.getElementById('input-date-start-fornec')
    let date_end = document.getElementById('input-date-end-fornec')
    sendFornec(date_start, date_end)
}