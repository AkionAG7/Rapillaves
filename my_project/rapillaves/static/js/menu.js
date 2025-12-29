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

function openStatusInventoryModal(productId, productName) {
  const form = document.getElementById("statusForm");
  const title = document.getElementById("modal_title");
  const text = document.getElementById("modal_text");

  form.action = `/rapillaves/inventario/change_status/${productId}`;

  title.textContent = `¿Cambiar estado de ${productName}?`;
  text.textContent = "Esta acción activará o desactivará el producto.";

  open_especific_modal("modal_inventory_status");
}

function openStatusProveedorModal(proveedorId, proveedorName) {
  const formProveedor = document.getElementById("statusFormProveedor");
  const titleProveedor = document.getElementById("modal_title");
  const textProveedor = document.getElementById("modal_text");

  formProveedor.action = `/rapillaves/proveedores/change_status/${proveedorId}/`;

  titleProveedor.textContent = `¿Cambiar estado de ${proveedorName}?`;
  textProveedor.textContent = "Esta acción activará o desactivará el proveedor.";

  open_especific_modal("modal_proveedor_status");
}

