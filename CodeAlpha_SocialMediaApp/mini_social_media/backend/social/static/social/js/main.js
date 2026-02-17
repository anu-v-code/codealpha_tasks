document.querySelectorAll(".post-card").forEach(card => {
    card.addEventListener("mouseenter", () => {
        card.style.boxShadow = "0 15px 40px rgba(0,0,0,0.6)";
    });
    card.addEventListener("mouseleave", () => {
        card.style.boxShadow = "0 10px 25px rgba(0,0,0,0.4)";
    });
});
