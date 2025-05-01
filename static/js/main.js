function updateGuest(type, change) {
    const input = document.getElementById(`guest-${type}`);
    let value = parseInt(input.value, 10);
    if (isNaN(value)) value = 0;
    value += change;
    if (value < 0) value = 0;
    input.value = value;
}