document.addEventListener('DOMContentLoaded', function() {
    fetch("data.json")
        .then(response => response.json())
        .then(data => {
            const tabla = document.getElementById('tabla-viajeros').getElementsByTagName('tbody')[0];
            data.forEach(viajero => {
                const fila = document.createElement('tr');
                fila.innerHTML = `<td>${viajero['Trip ID']}</td>
                                  <td>${viajero['Traveller Name']}</td>
                                  <td>${viajero['Departure Date']}</td>
                                  <td>${viajero['Return Date']}</td>
                                  <td>${viajero['Departure City']}</td>
                                  <td>${viajero['Arrival City']}</td>`;
                tabla.appendChild(fila);
            });
        })
        .catch(error => {
            console.error('Error al cargar los datos:', error);
        });
});
