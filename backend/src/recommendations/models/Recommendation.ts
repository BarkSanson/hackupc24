import { Relation } from "./Relation";

export type Recommendation = {
    text: string,
    relations: Relation[]
};