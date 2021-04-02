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

let users = []

router.post('/login', function (req, res) {
    let isExist = users.some((data) => {
        return data.name === req.body.name
    })
    res.send(isExist)
})

//當 WebSocket 從外部連結時執行
wss.on('connection', (ws, req) => {
    users.count += 1
    ws.on('message', (data) => {
        // console.log(data)
        let userData = JSON.parse(data)
        ws.user = userData
        if (userData.type === 'come') {
            users.push(userData)
        }
        let clients = wss.clients
        //做迴圈，發送訊息至每個 client
        console.log(data)
        if (userData.type == 'come') {
            clients.forEach((client) => {
                if(client.user.room !== userData.room) return
                client.send(JSON.stringify(users))
            })
            
            clients.forEach((client) => {
                if(ws !== client){
                    client.send(JSON.stringify(userData))
                }
            })
        }

        if (userData.type === 'changeIn') {
            users.forEach(user=>{
                if(user.name == userData.name){
                    user.room = userData.room
                }
            })
            clients.forEach((client) => {
                client.send(JSON.stringify(users))
                if(client.user.room !== userData.room) return
                if(ws !== client){
                    client.send(JSON.stringify(userData))
                }
            })
        }
        
        if (userData.type === 'changeOut') {
            clients.forEach((client) => {
                if(client.user.room !== userData.room) return
                client.send(JSON.stringify(users))
                if(ws !== client){
                    client.send(JSON.stringify(userData))
                }
            })
        }

        if(userData.type == 'message'){
            clients.forEach((client) => {
                if(client.user.room !== userData.room) return
                if(client !== ws){
                    client.send(JSON.stringify(userData))
                }
            })
        }
    })

    ws.on('close', () => {
        let clients = wss.clients
        users = users.filter((user) => {
            console.log(ws.user.name)
            console.log(user)
            return user.name !== ws.user.name
        })
        console.log(users)
        //做迴圈，發送訊息至每個 client
        clients.forEach((client) => {
            if (client != ws && client.user.room === ws.user.room) {
                let data = {
                    type: 'leave',
                    message: ws.user.name + '下線',
                }
                client.send(JSON.stringify(data))
            }
            client.send(JSON.stringify(users))
        })
    })
})

//創建 express 的物件，並綁定及監聽 3000 port ，且設定開啟後在 console 中提示
server.listen(3000, () => console.log(`Listening on ${3000}`))
