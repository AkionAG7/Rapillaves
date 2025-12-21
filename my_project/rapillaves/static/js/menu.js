function toggleMenu(){
    document.getElementById("menu").classList.toggle("active")
}

function openModal() {
  document.getElementById("Modal").classList.add("active");
}

function closeModal() {
  document.getElementById("Modal").classList.remove("active");
}

function open_especific_modal(target){
  document.getElementById(target).classList.add("active");
}

function close_specific_modal(target) {
  document.getElementById(target).classList.remove("active");
}