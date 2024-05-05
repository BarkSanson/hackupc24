import express, { Express, Request, Response } from "express";
import dotenv from "dotenv";

import { Server } from './Server';

dotenv.config();

const app: Express = express();
const port = process.env.PORT || 3000;
const host = process.env.HOST || "localhost";

const server = new Server(app, host, port);

server.start();