document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".tags-input-container").forEach(container => {
        const input = container.querySelector(".tags-text-input");
        const hiddenInput = container.querySelector('input[type="hidden"]');
        const tagsList = container.querySelector(".tags-list");

        let tags = [];

        try {
            tags = JSON.parse(hiddenInput.value || "[]");
            if (!Array.isArray(tags)) tags = [];
        } catch {
            tags = [];
        }

        function updateInput() {
            hiddenInput.value = JSON.stringify(tags);
        }

        function renderTags() {
            tagsList.innerHTML = "";

            tags.forEach((tag, index) => {
                const tagElement = document.createElement("span");
                tagElement.classList.add("tag-item");

                const tagText = document.createElement("span");
                tagText.textContent = tag;

                const removeButton = document.createElement("button");
                removeButton.type = "button";
                removeButton.classList.add("tag-remove");
                removeButton.textContent = "×";
                removeButton.setAttribute("aria-label", `Remover ${tag}`);

                removeButton.addEventListener("click", () => {
                    tags.splice(index, 1);
                    renderTags();
                });

                tagElement.append(tagText, removeButton);
                tagsList.appendChild(tagElement);
            });

            updateInput();
        }

        function addTag(value) {
            const tag = value.trim();

            if (!tag || tags.some(item => item.toLowerCase() === tag.toLowerCase())) {
                return;
            }

            tags.push(tag);
            renderTags();
        }

        input.addEventListener("keydown", event => {
            if (event.key === "Enter" || event.key === ",") {
                event.preventDefault();

                addTag(input.value);
                input.value = "";
            }
        });

        input.addEventListener("blur", () => {
            if (input.value.trim()) {
                addTag(input.value);
                input.value = "";
            }
        });

        renderTags();
    });
});