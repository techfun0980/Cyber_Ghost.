const input = document.getElementById('cmdInput');
const output = document.getElementById('output');

input.addEventListener('keypress', async (e) => {
    if (e.key === 'Enter') {
        const cmd = input.value;
        output.innerHTML += `<div style="color:#fff; margin-top:10px;">> ${cmd}</div>`;
        
        const res = await fetch('/execute', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({command: cmd})
        });
        
        const data = await res.json();
        output.innerHTML += `<div>${data.output}</div>`;
        input.value = '';
        output.scrollTop = output.scrollHeight;
    }
});
