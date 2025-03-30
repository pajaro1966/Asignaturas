document.addEventListener("DOMContentLoaded", function () {
    const audioPlayers = document.querySelectorAll(".fragmented-audio");
  
    audioPlayers.forEach((audio) => {
      let segmentEnd = null;
      let activeButton = null;
  
      const container = audio.closest(".audio-block");
      if (!container) return;
  
      const buttons = container.querySelectorAll("button[data-segment]");
  
      buttons.forEach((btn) => {
        btn.addEventListener("click", () => {
          const segment = btn.getAttribute("data-segment");
          const [startStr, endStr] = segment.split("-");
          const start = parseFloat(startStr);
          const end = parseFloat(endStr);
  
          if (isNaN(start) || isNaN(end)) return;
  
          // Quitar clase activa anterior
          if (activeButton) {
            activeButton.classList.remove("active-segment");
          }
  
          audio.currentTime = start;
          segmentEnd = end;
          activeButton = btn;
          btn.classList.add("active-segment");
          audio.play();
        });
      });
  
      audio.addEventListener("timeupdate", () => {
        if (segmentEnd !== null && audio.currentTime >= segmentEnd) {
          audio.pause();
          segmentEnd = null;
  
          if (activeButton) {
            activeButton.classList.remove("active-segment");
            activeButton = null;
          }
        }
      });
  
      audio.addEventListener("pause", () => {
        if (activeButton) {
          activeButton.classList.remove("active-segment");
          activeButton = null;
        }
      });
    });
  });
  