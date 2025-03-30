document.addEventListener("DOMContentLoaded", function () {
    const audio = document.getElementById("audio");
    let segmentEnd = null;
  
    window.playSegment = function (start, end) {
      if (!audio) return;
      audio.currentTime = start;
      segmentEnd = end;
      audio.play();
    };
  
    if (audio) {
      audio.addEventListener("timeupdate", () => {
        if (segmentEnd !== null && audio.currentTime >= segmentEnd) {
          audio.pause();
          segmentEnd = null;
        }
      });
    }
  });
  