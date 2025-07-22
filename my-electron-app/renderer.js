const { execFile } = require('child_process');
const path = require('path');

window.runPython = function () {
  const pythonPath = 'python3'; // or 'python' — try both if needed
  const scriptPath = path.join(__dirname, 'spin.py');

  execFile(pythonPath, [scriptPath], (error, stdout, stderr) => {
    const msgElement = document.getElementById('msg');

    if (error) {
      console.error('Exec error:', error);
      msgElement.innerText = "⚠ Error running Python!";
      return;
    }

    msgElement.innerText = stdout.trim();
  });
};
