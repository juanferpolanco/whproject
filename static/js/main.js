function updateGuest(type, change) {
    const input = document.getElementById(`guest-${type}`);
    let value = parseInt(input.value, 10);
    if (isNaN(value)) value = 0;
    value += change;
    if (value < 0) value = 0;
    input.value = value;
}

// {% comment %} function setCiudad(value) {
//     document.getElementById('inputCiudad').value = value;
//     document.getElementById('ciudadDropdown').textContent = value;
//   } {% endcomment %}

// function setCiudad(value) {
//     document.getElementById('inputCiudad').value = value;
//     document.getElementById('ciudadDropdown').textContent = value;

//     document.getElementById('inputDistrito').value = '';
//     document.getElementById('distritoDropdown').textContent = 'Distrito';

//     const distritoDropdown = document.getElementById('distritoDropdown');
//     const distritoMenu = distritoDropdown.nextElementSibling;
//     distritoMenu.innerHTML = '<li><span class="dropdown-item">Loading...</span></li>';

//     fetch(`/api/neighborhoods/?city=${encodeURIComponent(value)}`)
//         .then(response => response.json())
//         .then(data => {
//             distritoMenu.innerHTML = '';  

//             if (data.neighborhoods.length > 0) {
//                 data.neighborhoods.forEach(neighborhood => {
//                     const li = document.createElement('li');
//                     const a = document.createElement('a');
//                     a.className = 'dropdown-item';
//                     a.href = '#';
//                     a.onclick = function() { setDistrito(neighborhood); };
//                     a.textContent = neighborhood;
//                     li.appendChild(a);
//                     distritoMenu.appendChild(li);
//                 });
//             } else {
//                 const li = document.createElement('li');
//                 li.innerHTML = '<span class="dropdown-item">No neighborhoods</span>';
//                 distritoMenu.appendChild(li);
//             }
//         })
//         .catch(error => {
//             console.error('Error fetching neighborhoods:', error);
//             distritoMenu.innerHTML = '<li><span class="dropdown-item text-danger">Error loading</span></li>';
//         });
// } 

function setCiudad(cityId, cityName) {
    document.getElementById('inputCiudad').value = cityName; // used in the URL
    document.getElementById('ciudadDropdown').textContent = cityName;

    // Reset district
    document.getElementById('inputDistrito').value = '';
    document.getElementById('distritoDropdown').textContent = 'Distrito';

    const distritoDropdown = document.getElementById('distritoDropdown');
    const distritoMenu = distritoDropdown.nextElementSibling;
    distritoMenu.innerHTML = '<li><span class="dropdown-item">Loading...</span></li>';

    // Use city ID in API call
    fetch(`/api/neighborhoods/?city_id=${encodeURIComponent(cityId)}`)
        .then(response => response.json())
        .then(data => {
            distritoMenu.innerHTML = '';

            if (data.neighborhoods.length > 0) {
                data.neighborhoods.forEach(neighborhood => {
                    const li = document.createElement('li');
                    const a = document.createElement('a');
                    a.className = 'dropdown-item';
                    a.href = '#';
                    a.onclick = function () { setDistrito(neighborhood); };
                    a.textContent = neighborhood;
                    li.appendChild(a);
                    distritoMenu.appendChild(li);
                });
            } else {
                distritoMenu.innerHTML = '<li><span class="dropdown-item">No neighborhoods</span></li>';
            }
        })
        .catch(error => {
            console.error('Error fetching neighborhoods:', error);
            distritoMenu.innerHTML = '<li><span class="dropdown-item text-danger">Error loading</span></li>';
        });
}

function setDistrito(value) {
    document.getElementById('inputDistrito').value = value;
    document.getElementById('distritoDropdown').textContent = value;
}

function changeCount(id, delta, event) {
    event.stopPropagation();

    let input = document.getElementById(id);
    let hiddenInput = document.getElementById('input' + capitalize(id));
    let value = parseInt(input.value) || 0;
    value = Math.max(0, value + delta);
    input.value = value;
    hiddenInput.value = value;
}

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

document.addEventListener('DOMContentLoaded', function() {
    const today = new Date();
    const tomorrow = new Date();
    tomorrow.setDate(today.getDate() + 1);

    flatpickr("#dateRange", {
        mode: "range",
        //dateFormat: "d M Y",
        dateFormat: "Y-m-d",
        minDate: "today",
        defaultDate: [today, tomorrow],
        onReady: function(selectedDates, dateStr, instance) {
        // Set the initial value once flatpickr is ready
        document.getElementById('inputFechaRango').value = dateStr;
        },
        onChange: function(selectedDates, dateStr) {
            document.getElementById('inputFechaRango').value = dateStr;
        }
    });
});