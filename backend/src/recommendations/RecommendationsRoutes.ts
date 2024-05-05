import { Router } from 'express';
import { RecommendationsController } from './RecommendationsController';
import { AgentClient } from './infrastructure/AgentClient';

const router = Router()
const client = new AgentClient(process.env.AI_HOST, process.env.AI_PORT);
const controller = new RecommendationsController(client);

router.get('/', controller.getRecommendation);

export default router;