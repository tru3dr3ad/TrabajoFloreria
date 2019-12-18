function confirmarEliminacion(id) {
    Swal.fire({
        title: '¿Estas Seguro?',
        text: "No podrás revertir esto!",
        icon: 'Peligro!',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Borralo!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.value) {
            window.location.href = "/eliminar-flores/" + id;
        }
    })
}