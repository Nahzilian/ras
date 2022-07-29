import express, { Express, Request, Response } from 'express'

const app: Express = express()
const port: number = 8000

app.get('/', (_: Request, res: Response) => {
    res.send('From typescript backend')
})

app.listen(port, () => {
    console.log(`Running on port ${port}`)
})