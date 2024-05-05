import { Recommendation } from "../models/Recommendation";
import { TravelProposal } from "../models/TravelProposal";

export interface IAgentClient {
    sendTravelProposal(proposal: TravelProposal): Promise<Recommendation>;
}