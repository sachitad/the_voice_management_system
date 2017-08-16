import 'rxjs/add/operator/switchMap';
import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, ParamMap} from '@angular/router';
import {Location} from '@angular/common';

import {TeamService} from './team.service';
import {Team} from './team';

@Component({
  templateUrl: './team-detail.component.html'
})
export class TeamDetailComponent implements OnInit {
  team: Team;

  constructor(private teamService: TeamService,
              private route: ActivatedRoute,
              private location: Location) {
  }

  ngOnInit(): void {
    this.route.paramMap
      .switchMap((params: ParamMap) => this.teamService.getTeam(+params.get('id')))
      .subscribe(team => this.team = team);
  }

  goBack(): void {
    this.location.back();
  }
}
