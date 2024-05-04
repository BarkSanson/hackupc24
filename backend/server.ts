import express, { Express, Request, Response } from "express";

class Server {
    constructor(
        private app, 
        private host, 
        private port,
        private readonly recommendationsController,
        private readonly commentsController,
    ) {
        this.app = express()
        this.config();
        this.routes();
    }

    private config() {
        this.app.use(express.json());
        this.app.use(express.urlencoded({extended: true}));
    }

    private routes() {
        this.app.get('/recommendations')
    }

    start() {
        this.app.listen(this.port, () => {
        console.log(`[server]: Server is running at http://${this.host}:${this.port}`);
        });
    }

}