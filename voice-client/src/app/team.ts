import {Candidate} from './candidate';

export class Team {

  constructor(public pk: number,
              public team_name: string,
              public team_average_score: number,
              public candidates: Candidate[]) {
  }

}
