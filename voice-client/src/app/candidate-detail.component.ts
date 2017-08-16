import 'rxjs/add/operator/switchMap';
import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, ParamMap} from '@angular/router';
import {Location} from '@angular/common';

import {TeamService} from './team.service';
import {Candidate} from './candidate';

@Component({
  templateUrl: './candidate-detail.component.html'
})
export class CandidateDetailComponent implements OnInit {
  candidate: Candidate;

  constructor(private teamService: TeamService,
              private route: ActivatedRoute,
              private location: Location) {
  }

  ngOnInit(): void {
    this.route.paramMap
      .switchMap((params: ParamMap) => this.teamService.getCandidate(+params.get('id')))
      .subscribe(candidate => this.candidate = candidate);
  }

  goBack(): void {
    this.location.back();
  }
}
