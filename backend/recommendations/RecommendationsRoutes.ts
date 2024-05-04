import { Router } from 'express';
import { RecommendationsController } from './RecommendationsController';
import { AgentClient } from './infrastructure/AgentClient';

const router = Router()
const client = new AgentClient(process.env.AGENT_HOST);
const controller = new RecommendationsController(client);

router.get('/', controller.getRecommendation);
//router.post('/', /*TODO*/() => {});

export default router;