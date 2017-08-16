import {Injectable} from '@angular/core';
import {Headers, Http} from '@angular/http';

import 'rxjs/add/operator/toPromise';

import {Team} from './team';
import {Candidate} from './candidate';

@Injectable()
export class TeamService {

  private headers = new Headers({'Content-Type': 'application/json', 'Authorization': 'Token ' + localStorage.getItem('token')});
  private teamUrl = 'http://localhost:8000/api/v1/teams';  // URL to web api
  private candidateDetailUrl = 'http://localhost:8000/api/v1/candidate';
  constructor(private http: Http) {
  }

  getTeams(): Promise<Team[]> {
    return this.http.get(this.teamUrl, {headers: this.headers})
      .toPromise()
      .then(response => response.json() as Team[])
      .catch(this.handleError);
  }

  getAllTeams(): Promise<Team[]> {
    return this.http.get(this.teamUrl, {headers: this.headers})
      .toPromise()
      .then(response => response.json() as Team[])
      .catch(this.handleError);
  }

  getCandidate(id: number): Promise<Candidate> {
    const url = `${this.candidateDetailUrl}/${id}`;
    return this.http.get(url, {headers: this.headers})
      .toPromise()
      .then(response => response.json() as Candidate)
      .catch(this.handleError);
  }

  getTeam(id: number): Promise<Team> {
    const url = `${this.teamUrl}/${id}`;
    return this.http.get(url, {headers: this.headers})
      .toPromise()
      .then(response => response.json() as Team)
      .catch(this.handleError);
  }


  private handleError(error: any): Promise<any> {
    console.error(error['status']);
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}

