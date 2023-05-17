import { Component } from '@angular/core';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent {
  buttonFlag:boolean = false;
  menuActiveFlag: boolean = false;

  buttonCliked() {
    this.buttonFlag = !this.buttonFlag;
    this.menuActiveFlag = !this.menuActiveFlag;
  }

  closeMenu() {
    this.buttonFlag = false;
    this.menuActiveFlag = false;
  }
}
