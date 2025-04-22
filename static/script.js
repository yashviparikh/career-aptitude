let hasScrolledToPreferences = false;
let selectedSkillsSet = new Set();

document.addEventListener("DOMContentLoaded", function () {
    const suggestedContainer = document.getElementById("suggested-skills");
    const preferencesContainer = document.getElementById("user-preferences");
    const selectedSuggestions = document.getElementById("selected-suggestions");

    updatePreferenceSection();

    // Handle checkbox changes
    document.addEventListener("change", function (event) {
        if (event.target.classList.contains("skill-checkbox")) {
            handleSkillSelection(event.target);
        } else if (event.target.classList.contains("preference-checkbox")) {
            toggleSelection(event.target);
        }
    });

    function handleSkillSelection(checkbox) {
        if (checkbox.checked) {
            selectedSkillsSet.add(checkbox.value);
        } else {
            selectedSkillsSet.delete(checkbox.value);
        }
        toggleSelection(checkbox);
        updateRelatedSkills();
        updateSelectedSkillsDisplay();
    }

    function toggleSelection(checkbox) {
        const label = checkbox.parentElement;
        if (checkbox.checked) {
            label.style.background = "rgba(0, 0, 128, 1)";
            label.style.color = "white";
            label.style.border = "2px solid rgba(0, 0, 128, 1)";
        } else {
            label.style.background = "rgba(0, 123, 255, 0.2)";
            label.style.color = "#0056b3";
            label.style.border = "2px solid rgba(0, 123, 255, 0.4)";
        }
    }

    function updateRelatedSkills() {
        if (selectedSkillsSet.size === 0) {
            suggestedContainer.innerHTML = "";
            return;
        }

        if (!hasScrolledToPreferences) {
            const preferencesSection = document.getElementById("user-preferences");
            if (preferencesSection) {
                preferencesSection.scrollIntoView({ behavior: "smooth" });
                hasScrolledToPreferences = true;
            }
        }

        fetch("/related_keywords", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ selected_skills: Array.from(selectedSkillsSet) })
        })
        .then(response => response.json())
        .then(data => {
            // Store current suggestions before clearing
            const currentSuggestions = new Set(
                Array.from(suggestedContainer.querySelectorAll(".skill-checkbox"))
                    .filter(checkbox => checkbox.checked)
                    .map(checkbox => checkbox.value)
            );

            suggestedContainer.innerHTML = "";
            
            data.forEach(skill => {
                if (!selectedSkillsSet.has(skill)) {
                    const label = document.createElement("label");
                    label.style.marginRight = "10px";

                    const checkbox = document.createElement("input");
                    checkbox.type = "checkbox";
                    checkbox.name = "skills";
                    checkbox.value = skill;
                    checkbox.classList.add("skill-checkbox");
                    
                    // Restore checked state if it was previously selected
                    if (currentSuggestions.has(skill)) {
                        checkbox.checked = true;
                        selectedSkillsSet.add(skill);
                    }

                    label.appendChild(checkbox);
                    label.appendChild(document.createTextNode(" " + skill));
                    suggestedContainer.appendChild(label);

                    // Apply initial styling if checked
                    if (checkbox.checked) {
                        toggleSelection(checkbox);
                    }

                    checkbox.addEventListener("change", function () {
                        handleSkillSelection(checkbox);
                    });
                }
            });
        })
        .catch(error => {
            console.error("Fetch error: ", error);
            suggestedContainer.innerHTML = "<p class='error'>Error loading suggestions. Please try again.</p>";
        });
    }

    function updateSelectedSkillsDisplay() {
        selectedSuggestions.innerHTML = "";
        
        // Sort skills alphabetically
        const sortedSkills = Array.from(selectedSkillsSet).sort();
        
        sortedSkills.forEach(skill => {
            const skillElement = document.createElement("div");
            skillElement.className = "selected-skill";
            
            // Add remove button
            const removeButton = document.createElement("span");
            removeButton.className = "remove-skill";
            removeButton.innerHTML = "&times;";
            removeButton.onclick = function() {
                const checkbox = document.querySelector(`.skill-checkbox[value="${skill}"]`);
                if (checkbox) {
                    checkbox.checked = false;
                    handleSkillSelection(checkbox);
                }
            };
            
            skillElement.appendChild(document.createTextNode(skill));
            skillElement.appendChild(removeButton);
            selectedSuggestions.appendChild(skillElement);
        });
    }

    function updatePreferenceSection() {
        const preferences = ["Coding-based", "Leadership", "Remote", "In-office", "Team-based", "Solo"];
        preferencesContainer.innerHTML = "";
        preferences.forEach(pref => {
            const label = document.createElement("label");
            label.style.marginRight = "10px";

            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.name = "preferences";
            checkbox.value = pref;
            checkbox.classList.add("preference-checkbox");

            label.appendChild(checkbox);
            label.appendChild(document.createTextNode(" " + pref));
            preferencesContainer.appendChild(label);

            checkbox.addEventListener("change", function () {
                toggleSelection(checkbox);
            });
        });
    }
});
