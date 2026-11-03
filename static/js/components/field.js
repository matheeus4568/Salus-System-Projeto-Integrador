document.addEventListener('DOMContentLoaded', function() {
    
    const fileContainers = document.querySelectorAll('.file-upload-container');
    
    fileContainers.forEach(container => {
        const fileInput = container.querySelector('input[type="file"]');
        const btnUpload = container.querySelector('#btn-upload');
        const fileNameDisplay = container.querySelector('#file-name-display');

        if (fileInput && btnUpload) {
            btnUpload.addEventListener('click', function(event) {
                event.preventDefault(); 
                fileInput.click();
            });

            fileInput.addEventListener('change', function() {
                if (this.files && this.files.length > 0) {
                    fileNameDisplay.textContent = this.files[0].name;
                } else {
                    fileNameDisplay.textContent = "Nenhum arquivo selecionado";
                }
            });
        }
    });

    const dateContainers = document.querySelectorAll('.field-container:has(input[type="date"])');
    dateContainers.forEach(container => {
        const input = container.querySelector('input[type="date"]');
        container.addEventListener('click', function(event) {
            const rect = container.getBoundingClientRect();
            const clickX = event.clientX - rect.left;
            if (clickX > (rect.width - 40)) {
                if (input.showPicker) {
                    input.showPicker();
                }
            }
        });
    });
});