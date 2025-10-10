// Función para abrir modal con vuelo recién creado
function abrirModalConfirmacionNueva(vueloId, vueloData, confirmacionData) {
    // Buscar información completa de aeronave y piloto
    var aeronave = aeronaves.find(function(a) { return a.aeronave_id === vueloData.aeronave_id; });
    var piloto = pilotos.find(function(p) { return p.piloto_id === vueloData.piloto_id; });
    var copiloto = vueloData.copiloto_id ? pilotos.find(function(p) { return p.piloto_id === vueloData.copiloto_id; }) : null;
    
    document.getElementById('vuelo_id_confirmar').value = vueloId;
    document.getElementById('vueloInfo').innerHTML = 
        '<div class="alert alert-success mb-3">' +
        '<i class="fas fa-check-circle me-2"></i>' +
        '<strong>¡Vuelo creado exitosamente!</strong> Revise y actualice la confirmación si es necesario.' +
        '</div>' +
        '<div class="row">' +
        '<div class="col-md-6"><strong>Número de Vuelo:</strong><br>' + vueloData.numero_vuelo + '</div>' +
        '<div class="col-md-6"><strong>Ruta:</strong><br>' + vueloData.origen + ' → ' + vueloData.destino + '</div>' +
        '</div>' +
        '<div class="row mt-2">' +
        '<div class="col-md-6"><strong>Fecha Salida:</strong><br>' + new Date(vueloData.fecha_salida).toLocaleString() + '</div>' +
        '<div class="col-md-6"><strong>Fecha Llegada:</strong><br>' + (vueloData.fecha_llegada ? new Date(vueloData.fecha_llegada).toLocaleString() : 'No programada') + '</div>' +
        '</div>' +
        '<div class="row mt-2">' +
        '<div class="col-md-6"><strong>Aeronave:</strong><br>' + (aeronave ? aeronave.matricula + ' - ' + aeronave.modelo : 'N/A') + '</div>' +
        '<div class="col-md-6"><strong>Piloto:</strong><br>' + (piloto ? piloto.nombre + ' (' + piloto.licencia + ')' : 'N/A') + '</div>' +
        '</div>' +
        (copiloto ? '<div class="row mt-2"><div class="col-md-6"><strong>Copiloto:</strong><br>' + copiloto.nombre + ' (' + copiloto.licencia + ')' + '</div></div>' : '') +
        '<div class="row mt-3">' +
        '<div class="col-12"><hr><strong>Confirmación creada:</strong><br>' +
        '<small class="text-muted">ID: ' + confirmacionData.id + ' | Fecha: ' + new Date().toLocaleString() + '</small></div>' +
        '</div>';
    
    // Establecer valores por defecto de la confirmación
    document.getElementById('estado_confirmacion').value = 'Pendiente';
    document.getElementById('notas_confirmacion').value = 'Confirmación creada automáticamente';
    
    // Guardar el ID de confirmación para actualizar en lugar de crear
    document.getElementById('vuelo_id_confirmar').setAttribute('data-confirmacion-id', confirmacionData.id);
    
    // Mostrar modal
    var modal = new bootstrap.Modal(document.getElementById('confirmarVueloModal'));
    modal.show();
}

// Función para crear confirmación automáticamente después de crear un vuelo
function crearConfirmacionAutomatica(vueloId, vueloData) {
    var confirmacionPayload = {
        vuelo_id: vueloId,
        estado: 'Pendiente',
        notas: 'Confirmación creada automáticamente'
    };
    
    return fetch('/api/confirmaciones', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(confirmacionPayload)
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(text => { throw new Error(text) });
        }
        return response.json();
    })
    .then(confirmacionData => {
        // Ocultar formulario y refrescar tabla
        hideForm();
        fetchVuelos();
        
        // Mostrar mensaje de éxito
        showMessage('Vuelo y confirmación creados exitosamente', 'success');
        
        // Abrir modal de confirmación para que el usuario pueda revisar/editar
        abrirModalConfirmacionNueva(vueloId, vueloData, confirmacionData);
    })
    .catch(error => {
        // Si falla la confirmación, mostrar advertencia pero el vuelo ya fue creado
        showMessage('Vuelo creado, pero hubo un error al crear la confirmación: ' + error.message, 'warning');
        hideForm();
        fetchVuelos();
    });
}
