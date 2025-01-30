document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.guess-form');
    const input = document.querySelector('.guess-input');
    const message = document.querySelector('.message');

    form.addEventListener('submit', function() {
        const button = document.querySelector('.guess-button');
        button.style.transform = 'scale(0.95)';
        setTimeout(() => button.style.transform = 'scale(1)', 100);
    });

    input.addEventListener('input', function() {
        if (this.value < 1 || this.value > 100) {
            this.style.borderColor = '#e74c3c';
        } else {
            this.style.borderColor = '#3498db';
        }
    });

    if (message) {
        message.style.display = 'none';
        setTimeout(() => {
            message.style.display = 'block';
        }, 100);
    }
});