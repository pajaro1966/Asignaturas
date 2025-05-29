function activarKaraoke() {
  const audio = document.getElementById("audio");
  const lines = document.querySelectorAll(".karaoke-line");

  if (!audio || lines.length === 0) return;

  audio.addEventListener("timeupdate", () => {
    const currentTime = audio.currentTime;
    lines.forEach((line) => {
      const start = parseFloat(line.dataset.start);
      const end = parseFloat(line.dataset.end);
      if (currentTime >= start && currentTime < end) {
        line.classList.add("highlight");
      } else {
        line.classList.remove("highlight");
      }
    });
  });
}

// Activar tras cada carga de página en MkDocs Material
if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    activarKaraoke();
  });
} else {
  // fallback para HTML normal
  document.addEventListener("DOMContentLoaded", activarKaraoke);
}
