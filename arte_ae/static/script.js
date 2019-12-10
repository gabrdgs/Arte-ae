var nav = document.querySelector("nav");
var botaoNavMobile = document.querySelector(".toggle-menu");

// variaveis com relação a página cadastro-evento.html
let cep = document.querySelector("#id_cep");
let logradouro = document.querySelector("#id_logradouro");
let bairro = document.querySelector("#id_bairro");
let estado = document.querySelector("#id_localidade");
let uf = document.querySelector("#id_uf");
let modal = document.querySelector("#modal")

function checkPosition() {
    if (window.matchMedia('(max-width: 768px)').matches) {
        nav.classList.remove("desktop")
        nav.classList.add("mobile")
    } else {
        nav.classList.remove("mobile")
        nav.classList.add("desktop")
    }
}
checkPosition();

window.onload = checkPosition();

function toggleMenu(){
    nav.classList.toggle("mobile-toggle")
}

// Limpa valores do formulário de cep.
function limpa_formulário_cep() {
    cep.value = ''
    logradouro.value = ''
    bairro.value = ''
    estado.value = ''
    uf.value = ''
}

//Quando o campo cep perde o foco.
cep.addEventListener('blur', function(e) {
    e.preventDefault()
    let valueCep = e.target.value
    let validaCep = /^[0-9]{8}$/

    if (validaCep.test(valueCep)) {
      var URL = `https://viacep.com.br/ws/${valueCep}/json/`;
      var req = new XMLHttpRequest()
      req.open("GET", URL)
      req.responseType = "json"
      req.send()

      req.onload = function() {
        logradouro.value = req.response.logradouro
        bairro.value = req.response.bairro
        estado.value = req.response.localidade
        uf.value = req.response.uf
      };
    } else {
      alert("CEP Inválido")
      limpa_formulário_cep()
    }
  },
  true
)

function getEvento(id) {
  var URL = `/painel/evento/${id}`;
  var req = new XMLHttpRequest()
  req.open("GET", URL)
  req.responseType = "json"
  req.send()

  req.onload = function() {
    openModal(JSON.parse(req.response))
  }
}
function bodyModal(res) {
  let contentModal = ""
  console.log(res)
  document.querySelector("#shadow__modal").style.display = "block" 
  contentModal = `
    <div class="modal__container">
      <div class="modal__header">
      <div class="modal__close">
        <span onclick="closeModal()">X</span>
        <img src="../../media/${res.imagem}" width="500" heigth="100">
      </div>
      </div>
      <div class="modal__body">
        <div class="modal__title">
          <h2>${res.nome}</h2>
        </div>
        <div class="modal__more__information">
          <div class="modal__item">
            Local: ${res.logradouro}, ${res.numero} -
            ${res.bairro} - ${res.localidade} - ${res.uf}
          </div>
          <div class="modal__item">
            Data do evento: ${res.data}
          </div>
          <div class="modal__item">
            Horário do evento: ${res.horario}
          </div>
        </div>
      </div>
    </div>`
  return contentModal
}

function openModal(res) {
  modal.style.display = 'flex'
  window.scrollTo(0,0)
  modal.innerHTML = bodyModal(res[0].fields)
}
function closeModal() {
  modal.innerHTML = ""
  document.querySelector("#shadow__modal").style.display = "none" 
}
botaoNavMobile.onclick = toggleMenu;
