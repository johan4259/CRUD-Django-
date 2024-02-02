document.getElementById('registerForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
    };
    fetch('http://localhost:8000/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Registro fallido');
        }
    })
    .then(data => {
        console.log('Registro exitoso:', data);
        return fetch('http://localhost:8000/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({username: formData.username, password: formData.password}),
        });
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error obteniendo token');
        }
    })
    .then(data => {
        console.log('Token obtenido:', data);
        localStorage.setItem('accessToken', data.access);
        alert('Usuario registrado y token almacenado');
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

function createClient(clientData) {
    const accessToken = localStorage.getItem('accessToken');

    if (!accessToken) {
        console.error('No se encontró el token de acceso. Asegúrate de estar autenticado.');
        return;
    }
    fetch('http://localhost:8000/clients/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`
        },
        body: JSON.stringify(clientData),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Solicitud no autorizada. Asegúrate de que el token sea válido y esté activo.');
        }
    })
    .then(data => {
        console.log('Cliente creado con éxito:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
