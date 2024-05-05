import { TravelProposal } from "./models/TravelProposal";
import { Recommendation } from "./models/Recommendation";
import { IAgentClient } from "./infrastructure/IAgentClient"

export class RecommendationsController {
    constructor(private readonly client: IAgentClient) {}

    public async getRecommendation(proposal: TravelProposal): Promise<Recommendation> {
        const response = await this.client.sendTravelProposal(proposal);

        return response;
    }
}