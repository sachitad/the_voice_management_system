import {Component} from '@angular/core';
import {OnInit} from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Router} from '@angular/router';


@Component({
  selector: 'app-login-form',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})


export class LoginComponent implements OnInit {
  loginForm: FormGroup;
  error: string;
  usernameError: string;
  passwordError: string;

  constructor(private http: HttpClient, private router: Router) {
  }

  ngOnInit() {
    this.loginForm = new FormGroup({
      username: new FormControl(),
      password: new FormControl()
    });
  };

  onSubmit() {
    const url = 'http://localhost:8000/api/v1/login/';
    this.http.post(url, this.loginForm.value).subscribe(
      res => {
        this.getuserInfo(res);
      },
      // msg => this.error = `${msg.error.non_field_errors}`
      msg => this.handleError(msg.error)
    );
  }

  getuserInfo(res) {
    localStorage.setItem('token', res['key']);
    const url = 'http://localhost:8000/api/v1/user/';
    this.http.get(url, {
      headers: new HttpHeaders().set('Authorization', 'Token' + ' ' + localStorage.getItem('token')),
    }).subscribe(
      res => {
          this.router.navigate(['teams']);
      },
      msg => console.log(msg)
    );
  };

  private handleError(error: any) {
    this.usernameError = '';
    this.passwordError = '';
    if (error.username && error.password) {
      this.usernameError = error.username;
      this.passwordError = error.username;
    }
    else if (error.username) {
      this.usernameError = error.username;
    }
    else if (error.password) {
      this.passwordError = error.password;
    }
    else {
      this.error = error.non_field_errors;
    }
  }
}
