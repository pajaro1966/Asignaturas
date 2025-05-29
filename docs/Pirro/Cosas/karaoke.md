# Karaoke con sincronización

<audio id="audio" controls>
  <source src="karaoke.mp3" type="audio/mpeg">
  Tu navegador no soporta el audio.
</audio>

<div id="karaoke">
  <div class="karaoke-line" data-start="0" data-end="3">🎵 Esta es la primera línea del karaoke</div>
  <div class="karaoke-line" data-start="3" data-end="6">🎶 Aquí va la segunda frase con ritmo</div>
  <div class="karaoke-line" data-start="6" data-end="9">🎤 Y esta es la tercera línea musical</div>
</div>

<style>
  .karaoke-line {
    transition: background-color 0.3s;
    padding: 5px;
  }
  .highlight {
    background-color: yellow;
  }
</style>

<script>
  const audio = document.getElementById('audio');
  const lines = document.querySelectorAll('.karaoke-line');

  audio.addEventListener('timeupdate', () => {
    const currentTime = audio.currentTime;
    lines.forEach(line => {
      const start = parseFloat(line.dataset.start);
      const end = parseFloat(line.dataset.end);
      if (currentTime >= start && currentTime < end) {
        line.classList.add('highlight');
      } else {
        line.classList.remove('highlight');
      }
    });
  });
</script>
