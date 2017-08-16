import {Component} from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-root',
  template: `
    <h1 class="text-center text-success">{{title}}</h1>
    <hr>
    <router-outlet></router-outlet>
  `,
})

export class AppComponent {
  constructor(private router: Router) {
  }
  title = 'The Voice';

}
