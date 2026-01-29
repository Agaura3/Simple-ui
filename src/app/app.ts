import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { UserService } from './user.service';
import { environment } from '../environments/environment'; // ✅ ADD

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App {

  // 🔹 Number comparison
  num1!: number;
  num2!: number;
  message = '';

  // 🔹 Users list
  users: any[] = [];

  constructor(
    private http: HttpClient,
    private userService: UserService
  ) {}

  // ✅ FIXED: /check using SAME backend (environment)
  checkResult() {
    this.http.get<any>(
      `${environment.apiUrl}/check?num1=${this.num1}&num2=${this.num2}`
    ).subscribe({
      next: (res) => {
        if (res.status === 'greater') {
          this.message = 'First number is greater than second number';
        } else if (res.status === 'less') {
          this.message = 'Second number is greater than First number';
        } else {
          this.message = 'Both numbers are equal';
        }
      },
      error: () => {
        this.message = 'Backend error / Render sleeping';
      }
    });
  }

  // ✅ Users from PostgreSQL
  loadUsers() {
    this.userService.getUsers().subscribe({
      next: (res) => {
        this.users = res;
      },
      error: () => {
        alert('Backend not running / Render sleeping');
      }
    });
  }
}
