async function fetchJson(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Erro ao acessar a API: ${response.statusText}`);
    }
    return response.json();
}

async function carregarOpcoesEdificacao() {
    try {
        const edificacoes = await fetchJson("/api/v1/edificacoes");
        const edificacaoInput = document.querySelector("input[name='edificacao']");

        edificacaoInput.innerHTML = "";

        edificacoes.items.forEach(edificacao => {
            let newOption = document.createElement("option");
            newOption.value = edificacao.codigo;
            document.getElementById("edificacao").appendChild(newOption);
        });

    } catch (error) {
        console.error('Erro ao carregar opções de edificação:', error);
    }
}

function carregarPonto() {
    let target = window.location.pathname.split("/ponto/")[1];
    target = target.replace(/\/$/, "");

    fetch("/api/v1/pontos/" + target, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => {
            if (!response.ok) {
                // window.location.href = "/ponto/";
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            document.getElementById("id").value = data.id;
            document.getElementById("ambiente").value = data.ambiente;
            document.getElementById("tipo").value = data.tipo;
            document.getElementById("tombo").value = data.tombo;
            
            // URL da imagem
            const imageUrl = data.imagem;

            // Exibir a imagem em um elemento <img>
            const imgElement = document.getElementById("imagePreview");
            imgElement.src = imageUrl;

            fetchJson(data.edificacao_url)
                .then((edificacao) => {
                    document.querySelector("input[name='edificacao']").value = edificacao.codigo;
                    console.log("Edificação carregada com sucesso!");
                });


            fetchJson(data.edificacao_url)
                .then((edificacao) => {
                    document.querySelector("input[name='edificacao']").value = edificacao.codigo;
                    console.log("Edificação carregada com sucesso!");
                });

            var formAction = "/api/v1/edificacoes/" + target;

            document.getElementById("edificacaoForm").action = formAction;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function atualizarPreview() {
    const inputFoto = document.getElementById("foto");
    const imgElement = document.getElementById("imagePreview");

    if (inputFoto.files && inputFoto.files[0]) {
        const reader = new FileReader();

        reader.onload = function(e) {
            imgElement.src = e.target.result;
        };

        reader.readAsDataURL(inputFoto.files[0]);
    }
}

async function atualizarPonto() {
    console.log("Atualizando Ponto de Coleta...");
    let target = window.location.pathname.split("/ponto/")[1];
    target = target.replace(/\/$/, "");

    var id = document.getElementById("id").value;
    var ambiente = document.getElementById("ambiente").value;
    var tipo = document.getElementById("tipo").value;
    var tombo = document.getElementById("tombo").value;
    var edificacao = document.getElementById("edificacao_value").value;
    
    var imagem = document.getElementById("foto");

    var json = {
        "ambiente": ambiente,
        "tipo": parseInt(tipo),
        "tombo": tombo,
        "codigo_edificacao": edificacao,
    };
    console.log(json)

    try {
        const responsePonto = await fetch("/api/v1/pontos/" + target, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(json),
        });

        if (!responsePonto.ok) {
            const errorResponse = await responsePonto.json(); // Adiciona esta linha
            throw new Error(`Erro ao atualizar o ponto: ${responsePonto.statusText}. Detalhes: ${JSON.stringify(errorResponse)}`);
        }

        console.log('Ponto atualizado com sucesso:', await responsePonto.json());
        
        let formData = new FormData();

        if (imagem.files.length > 0) {
            formData.append("imagem", imagem.files[0]);
        }

        const responseImagem = await fetch("/api/v1/pontos/" + target + "/imagem", {
            method: 'POST',
            body: formData,
        });

        if (!responseImagem.ok) {
            throw new Error('Erro ao enviar a imagem');
        }

        console.log('Imagem enviada com sucesso:', await responseImagem.json());
        window.location.href = "/ponto";

    } catch (error) {
        console.error('Erro durante a atualização:', error);
    }

}

function excluirEdificacao() {
    console.log("Excluindo edificação...");
    let target = window.location.pathname.split("/edificacao/")[1];
    target = target.replace(/\/$/, "");

    var json = {};

    fetch("/api/v1/edificacoes/" + target, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(json)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            window.location.href = "/edificacao";
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

carregarOpcoesEdificacao();
carregarPonto();
