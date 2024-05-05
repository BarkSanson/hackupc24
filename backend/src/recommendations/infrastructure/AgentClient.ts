import { Recommendation } from "../models/Recommendation";
import { TravelProposal } from "../models/TravelProposal";
import { IAgentClient } from "./IAgentClient";

export class AgentClient implements IAgentClient {
    constructor(private host, private port) {}

    public async sendTravelProposal(proposal: TravelProposal): Promise<Recommendation> {
        const proposalJson = JSON.stringify(proposal);

        const response = await fetch(`http://${this.host}:${this.port}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(proposalJson)
        });
        const responseJson = await response.json();

        const r = JSON.parse(responseJson) as Recommendation;

        return r;
    }
}