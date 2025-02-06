const wrapper = document.querySelector('.wrapper');
const registerLink = document.querySelector('.register-link');
const loginLink = document.querySelector('.login-link');
const API_URL = 'http://localhost:3000'; // URL do backend
let token = null; // Variável para armazenar o token JWT

// Alternar entre formulários de login e registro
registerLink.onclick = () => {
    wrapper.classList.add('active');
};

loginLink.onclick = () => {
    wrapper.classList.remove('active');
};

// Função para exibir mensagens na tela
function showMessage(message, isError = false) {
    const messageDiv = document.getElementById('message');
    messageDiv.textContent = message;
    messageDiv.style.color = isError ? 'red' : 'green';
    messageDiv.style.display = 'block';

    // Esconder a mensagem após 3 segundos
    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 3000);
}

// Registrar um novo usuário
document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('registerUsername').value;
    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;

    try {
        const response = await fetch(`${API_URL}/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }), // Adicione o email se necessário
        });

        const data = await response.json();
        if (response.ok) {
            showMessage('Usuário registrado com sucesso!');
            switchToLogin();
        } else {
            showMessage(data.message || 'Erro ao registrar usuário', true);
        }
    } catch (error) {
        showMessage('Erro ao conectar com o servidor', true);
    }
});

document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    try {
        const response = await fetch(`${API_URL}/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();
        if (response.ok) {
            token = data.token;
            showMessage('Login realizado com sucesso!');

            localStorage.setItem('token', token);
            localStorage.setItem('user', JSON.stringify(data.user));

            window.location.href = '/Curso_Video/frontend/Pages/Auth/Dash/UserDashboard.html';
            return;
        } else {
            showMessage(data.message || 'Credenciais inválidas', true);
        }
    } catch (error) {
        showMessage('Erro ao conectar com o servidor', true);
    }
});

function switchToLogin() {
    wrapper.classList.remove('active');
}

function switchToRegister() {
    wrapper.classList.add('active');
}
