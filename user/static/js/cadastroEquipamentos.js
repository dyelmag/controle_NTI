$(document).ready(function () {
    preencheSelectMarca(0);
});

var marcaSelecionada = 0;

function preencheSelectMarca(id) {
    var select = document.getElementById("marca");
    var length = select.options.length;
    for (i = length - 1; i >= 1; i--) {
        select.options[i] = null;
    }
    $.get("/equipamento/marcas/", function (data, status) {
        for (d of data) {
            var x = document.getElementById("marca");
            var option = document.createElement("option");
            option.text = d.nome;
            option.value = d.id;
            x.add(option);
        }
        document.getElementById("marca").value = id;
        if (id > 0) {
            document.getElementById("bt_addModelo").disabled = false;
            document.getElementById("modelo").disabled = false;
        }
    });
}

function cadastraMarca() {
    var csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0]
        .value;
    var nome = document.getElementById("nomeMarca").value;
    var obs = document.getElementById("obsMarca").value;
    if (nome.length < 2) {
        document.getElementById("marcaErro2").hidden = false;
    } else {
        document.getElementById("marcaErro2").hidden = true;
        $.ajax({
            method: "POST",
            url: "/equipamento/marcas/",
            data: { csrfmiddlewaretoken: csrfmiddlewaretoken, nome: nome, obs: obs },
        })
            .done(function (msg) {
                if (msg.evento_id === 1) {
                    $("#modalMarca").modal("hide");
                    document.getElementById("nomeMarca").value = "";
                    document.getElementById("obsMarca").value = "";
                } else {
                    document.getElementById("marcaErro").hidden = false;
                }
                console.log(msg);
                preencheSelectMarca(msg.id_marca);
            })
            .fail(function (jqXHR, textStatus, msg) {
                alert(msg);
            });
    }
}

function marcaChange(event) {
    if (event.target.value > 0) {
        document.getElementById("bt_addModelo").disabled = false;
        document.getElementById("modelo").disabled = false;
        marcaSelecionada = event.target.value;
        listaModeloByMarca(0);
    } else {
        document.getElementById("bt_addModelo").disabled = true;
        document.getElementById("modelo").disabled = true;
    }
    selectModelo();
}

function teste(v) {
    document.getElementById("marca").value = v;
}


/*Scripts Modelos */

function listaModeloByMarca(id) {
    var select = document.getElementById("modelo");
    var length = select.options.length;
    for (i = length - 1; i >= 1; i--) {
        select.options[i] = null;
    }
    $.get("/equipamento/modelo/" + marcaSelecionada + "/", function (data, status) {
        for (d of data) {
            var x = document.getElementById("modelo");
            var option = document.createElement("option");
            option.text = d.nome;
            option.value = d.id;
            x.add(option);
        }
        document.getElementById("modelo").value = id;
    });
}

function CadastraModelo() {
    var csrfmiddlewaretoken = document.getElementsByName("csrfmiddlewaretoken")[0]
        .value;
    var nome = document.getElementById("nomeModelo").value;
    var tipo = document.getElementById("tipo").value;
    var desc = document.getElementById("descricaoModelo").value;
    var obs = document.getElementById("obsModelo").value;

    if (nome.length < 2) {
        document.getElementById("modeloErro2").hidden = false;
    } else {
        document.getElementById("modeloErro2").hidden = true;
        $.ajax({
            method: "POST",
            url: "/equipamento/modelo/" + marcaSelecionada + "/",
            data: {
                csrfmiddlewaretoken: csrfmiddlewaretoken,
                nome: nome,
                tipo: tipo,
                desc: desc,
                obs: obs
            },
        })
            .done(function (msg) {
                if (msg.evento_id === 1) {
                    $("#modalModelo").modal("hide");
                    document.getElementById("nomeModelo").value = "";
                    document.getElementById("descricaoModelo").value = "";
                    document.getElementById("obsModelo").value = "";
                } else {
                    document.getElementById("modeloErro").hidden = false;
                }
                console.log(msg);
                listaModeloByMarca(msg.id_modelo);
            })
            .fail(function (jqXHR, textStatus, msg) {
                alert(msg);
            });
    }

}

function selectModelo() {

    if ((document.getElementById('marca').value > 0) && (document.getElementById('modelo').value > 0)) {
        document.getElementById("nextBtn").disabled = false;
    } else {
        document.getElementById("nextBtn").disabled = true;
    }

}