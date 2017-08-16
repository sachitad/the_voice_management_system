import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {LoginComponent} from './login.component';
import {TeamsComponent} from './teams.component';
import {CandidateDetailComponent} from './candidate-detail.component';
import {TeamDetailComponent} from './team-detail.component';

const routes: Routes = [
  {path: '', redirectTo: '/login', pathMatch: 'full'},
  {path: 'login', component: LoginComponent},
  {path: 'teams', component: TeamsComponent},
  {path: 'candidate/:id', component: CandidateDetailComponent},
  {path: 'team/:id', component: TeamDetailComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule {
}
