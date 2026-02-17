// can't really make a RESTFUL app w this.
const express = require('express');
const path = require('path');
const { WebSocketServer } = require('ws');
const app = express()

const server = require('http').createServer(app)
const wss = new WebSocketServer({server});

app.use(express.static(path.join(__dirname, 'public')));

const clients = new Set();

// fucntion(ws){}

wss.on('connection', (ws)=>{
    clients.add(ws);
    // hacve to come up w our own server
    // need to know the ekys
    ws.send(JSON.)

    // broadcasting
    // going to let everyone lnkow that everone ahs joined
    // it doesnt have to be callwd "type" or "text", it could be msg or somethng else
    broadcast({type:'system', text:''});

    // if the connected clients sends us a message
    ws.on('message', (data)=>{
        const msg = JSON.parse(data);
        broadcast({type:'chat', name:})

    })
    // the broad cast for the client leavng
    ws.on('close', (data)=>{
        
    })
})

// broadcast function
function broadcast(message, sender) {
    const data = JSON.stringify(message);
    // there is no need to send the message to the client
    // but to everyone else is good
    for ()
}

const PORT = process.env.PORT || 3000
app.listen(prototype, ())
// run it now and go to localhost3000
// npm run
// npm astart
// it shouls say cannot get
// male index .html

