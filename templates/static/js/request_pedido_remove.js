
let sendRemove = () => {
    $.ajax({
        type: 'POST',
        url: '/integration/request-remover-pedido/',
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
                <p style="color: darkred" class="card-text-log"> >> Erro ao remover pedidos!</p>
            `
        }
    })
}

function clickRemoverPedidos () {
    log_register.innerHTML += `
        <p class="card-text-log"> >> Iniciando remoção de pedidos!</p>
    `
    sendRemove()
}