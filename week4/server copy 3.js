//import express 和 ws 套件
const express = require('express')
const cors = require('cors')
const app = express()
const server = require('http').createServer(app)
const SocketServer = require('ws')
const bodyParser = require('body-parser')
const router = express.Router()
router.use(bodyParser.urlencoded({ extended: false }))
router.use(bodyParser.json())
app.use(cors())
app.use(router)
//將 express 交給 SocketServer 開啟 WebSocket 的服務
const wss = new SocketServer.Server({ server: server })

let users = { type: 'count', count: 0 }
let usersname = {
    type: 'usersname',
    list: [
    ],
}

router.get('/about', function (req, res) {
    res.send('about page!')
})

router.post('/login', function (req, res) {
    let isExist = usersname.list.some((name) => {
        return name === req.body.name
    })
    res.send(isExist)
})

//當 WebSocket 從外部連結時執行
wss.on('connection', (ws, req) => {
    users.count += 1
    ws.on('message', (data) => {
        let messageData = JSON.parse(data)
        if (messageData.type === 'come') {
            console.log('1')
            ws.name = messageData.name
            usersname.list.push(ws.name)
        }
        let clients = wss.clients
        //做迴圈，發送訊息至每個 client
        clients.forEach((client) => {
            if (client.room !== ws.room) return
            if (client != ws) {
                client.send(data)
            }
            client.send(JSON.stringify(users))
            client.send(JSON.stringify(usersname))
        })
    })

    ws.on('close', () => {
        let clients = wss.clients
        usersname.list = usersname.list.filter((name) => {
            return name !== ws.name
        })
        console.log(usersname)
        users.count -= 1
        //做迴圈，發送訊息至每個 client
        clients.forEach((client) => {
            if (client.room !== ws.room) return
            if (client != ws) {
                let data = {
                    type: 'leave',
                    message: ws.name + '離開',
                }
                client.send(JSON.stringify(data))
            }

            client.send(JSON.stringify(users))
            client.send(JSON.stringify(usersname))
        })
    })
})

//創建 express 的物件，並綁定及監聽 3000 port ，且設定開啟後在 console 中提示
server.listen(3000, () => console.log(`Listening on ${3000}`))
