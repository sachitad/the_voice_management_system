class Activities {
  constructor(public song_name: string,
              public date_of_performance: string) {
  }
}

export class Candidate {
  constructor(public pk: number,
              public name: string,
              public average_score: number,
              public team_average_score: number,
              public activities: Activities[]) {
  }
}
