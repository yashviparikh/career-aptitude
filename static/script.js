document.addEventListener("DOMContentLoaded",function()
{
    const suggestedContainer=document.getElementById("suggested-skills");
    const preferencesContainer=document.getElementById("user-preferences");
    updatePreferenceSection();
    document.addEventListener("change",function(event)
    {
        if (event.target.classList.contains("skill-checkbox"))
        {
            updateRelatedSkills();
        }
    });


    function updateRelatedSkills()
    {
        const selectedSkills=Array.from(
            document.querySelectorAll(".skill-checkbox"))
            .filter(checkbox=>checkbox.checked)
            .map(checkbox=>checkbox.value);   
        console.log("selected skills: ",selectedSkills);
        if (selectedSkills.length === 0) {
            console.error("No skills selected. Skipping fetch request.");
            return; 
        }
        fetch("/related_keywords",
        {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({selected_skills:selectedSkills})
        })
        .then(response=>response.json())
        .then(data=>
            {
                console.log("API Response: ", data);
                suggestedContainer.innerHTML="";
                preferencesContainer.innerHTML="";
                data.forEach(skill=>
                    {
                        const label=document.createElement("label");
                        label.style.marginRight="10px";

                        const checkbox = document.createElement("input");
                        checkbox.type = "checkbox";
                        checkbox.name = "skills";
                        checkbox.value = skill;
                        checkbox.classList.add("skill-checkbox");

                        label.appendChild(checkbox);
                        label.appendChild(document.createTextNode(" " + skill));
                        suggestedContainer.appendChild(label);
                            });
            })
            .catch(error=> console.error("Fetch error: ",error));
    }
function updatePreferenceSection()
{
    const preferences=["coding-based","managerial-based","remote","in-office", "teamwork", "alone"];
    preferencesContainer.innerHTML="";
    preferences.forEach(pref=>
        {
            const label=document.createElement("label");
            label.style.marginRight="10px";

            const checkbox=document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.name = "preferences";
            checkbox.value = pref;
            checkbox.classList.add("preference-checkbox");

            label.appendChild(checkbox);
            label.appendChild(document.createTextNode(" " + pref));
            preferencesContainer.appendChild(label);
        });
}
});