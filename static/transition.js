document.addEventListener("DOMContentLoaded", function () {
    const overlay = document.getElementById("transition-overlay");
    const music = document.getElementById("bg-music");
    const sparklesContainer = document.getElementById("sparkles-container");

    // Fade-in scény (rozsvícení)
    setTimeout(() => {
        overlay.style.opacity = "0";
    }, 50);

    // Hudba: spustí se po prvním kliknutí
    const startMusic = () => {
        if (music.paused) {
            music.volume = 0;
            music.play();

            // fade-in hudby
            let vol = 0;
            const fadeAudio = setInterval(() => {
                if (vol < 0.4) {
                    vol += 0.02;
                    music.volume = vol;
                } else {
                    clearInterval(fadeAudio);
                }
            }, 200);
        }
    };
    document.body.addEventListener("click", startMusic, { once: true });

    // Blikající světélka
    function createSparkle() {
        const sparkle = document.createElement("div");
        sparkle.classList.add("sparkle");
        sparkle.style.top = Math.random() * 100 + "%";
        sparkle.style.left = Math.random() * 100 + "%";
        sparkle.style.animationDuration = 1 + Math.random() * 2 + "s";
        sparklesContainer.appendChild(sparkle);

        setTimeout(() => sparkle.remove(), 3000);
    }

    // Generuj světélka stále
    setInterval(createSparkle, 300);
});
