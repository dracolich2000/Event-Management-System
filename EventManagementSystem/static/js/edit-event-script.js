const errorMessage = document.getElementById('error-message');
        if (errorMessage.innerText.trim() !== '') {
            errorMessage.style.display = 'block';
            errorMessage.style.textAlign = 'center';
            errorMessage.style.color = 'red';
        }

const successMessage = document.getElementById('success-message');
        if (successMessage.innerText.trim() !== '') {
            successMessage.style.display = 'block';
            successMessage.style.textAlign = 'center';
            successMessage.style.color = 'green';
        }