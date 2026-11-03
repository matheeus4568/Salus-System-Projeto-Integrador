document.addEventListener("DOMContentLoaded", () => {

    // Elementos HTML
    const searchInput = document.getElementById("searchInput");
    const table = document.querySelector(".table");

    // Verifica se os elementos existem
    if (!searchInput || !table) {
        console.error("Elementos necessários para o filtro não encontrados.");
        return;
    }

    // Captura todas as linhas da tabela
    const rows = table.querySelectorAll("tbody tr");

    // Função de filtragem
    function filterTable() {
        const search = searchInput.value.toLowerCase().trim();

        rows.forEach(row => {
            const paciente = row.dataset.paciente || "";

            const matchesSearch = paciente.toLowerCase().includes(search);

            row.style.display = matchesSearch ? "" : "none";
        });
    }

    // Evento disparado enquanto o usuário digita
    searchInput.addEventListener("input", filterTable);

});