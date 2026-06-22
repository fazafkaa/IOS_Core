console.log("Workspace Loaded");

document.addEventListener("DOMContentLoaded", () => {

    const trigger = document.getElementById("lightbox-trigger");

    const lightbox = document.getElementById("lightbox");

    const closeBtn = document.getElementById("close-lightbox");

    if(trigger){

        trigger.addEventListener("click", () => {

            lightbox.style.display = "flex";

        });

        closeBtn.addEventListener("click", () => {

            lightbox.style.display = "none";

        });

        lightbox.addEventListener("click", (e) => {

            if(e.target === lightbox){

                lightbox.style.display = "none";

            }

        });

    }
    
    

});

