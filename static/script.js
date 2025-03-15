document.addEventListener("DOMContentLoaded",function()
{
    const checkboxes=document.querySelectorAll(".keyword-checkbox");
    const suggestedcontainer=document.getElementById("suggested-keywords");

    checkboxes.forEach(checkbox=>
        {
            checkbox.addEventListener("change",()=>
            {
                updateRelatedKeywords();
            });
        });

        function updateRelatedKeywords()
        {
            const selectedKeywords=Array.from(checkboxes).filter(checkbox=>checkbox.checked).map(checkbox=>checkbox.value);
            console.log("selectedkeywords: ",selectedKeywords);
            fetch("/related_keywords",{
                method:"POST",headers:{"Content-Type":"application/json"}, 
                body:JSON.stringify({selected_keywords:selectedKeywords})
            })
            .then(response=>response.json())
            .then(data=>
                {
                    suggestedcontainer.innerHTML="";
                    data.forEach(keyword=>
                        {
                            const keywordElement=document.createElement("span");
                            keywordElement.textContent=keyword;
                            keywordElement.style.marginRight="10px";
                            suggestedcontainer.appendChild(keywordElement);
                        });
                })
            .catch(error=> console.error("Fetch error: ",error));
        }
});