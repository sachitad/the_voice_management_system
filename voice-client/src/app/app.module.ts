import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {AppRoutingModule} from './app-routing.module';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {HttpClientModule} from '@angular/common/http';
import {AppComponent} from './app.component';
import {LoginComponent} from './login.component';
import {TeamsComponent} from './teams.component';
import {TeamService} from './team.service';
import {CandidateDetailComponent} from './candidate-detail.component';
import {TeamDetailComponent} from './team-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    TeamsComponent,
    CandidateDetailComponent,
    TeamDetailComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    HttpModule,
    HttpClientModule,
  ],
  providers: [TeamService],
  bootstrap: [AppComponent]
})
export class AppModule {
}

