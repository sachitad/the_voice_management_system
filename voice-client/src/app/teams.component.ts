import {Component, OnInit} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Team} from './team';
import {TeamService} from './team.service';

@Component({
  selector: 'app-teams',
  templateUrl: './teams.component.html'
})

export class TeamsComponent implements OnInit {
  candidate: String;
  mentor: Boolean;
  admin: Boolean;
  teams: Team[];

  constructor(private http: HttpClient,
              private TeamService: TeamService) {
  }

  getMentorTeams(): void {
    this.TeamService
      .getTeams()
      .then(teams => this.teams = teams);
  }

  getTeams(userType) {
    if (userType === 'C') {
      this.candidate = 'System for candidate is in progress. Please check in later.';
    }
    else if (userType === 'M') {
      this.mentor = true;
      this.getMentorTeams();
    }
    else {
      this.admin = true;
      this.getMentorTeams();
    }
  }

  ngOnInit() {
    const url = 'http://localhost:8000/api/v1/user/';
    this.http.get(url, {
      headers: new HttpHeaders().set('Authorization', 'Token' + ' ' + localStorage.getItem('token')),
    }).subscribe(
      res => this.getTeams(res['user_type']),
      msg => console.log(msg)
    );
  };
}


