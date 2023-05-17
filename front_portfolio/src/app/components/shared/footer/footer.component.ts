import { Component } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent {
  public year: number;
  public user: string;


  constructor() {
    this.year = new Date().getFullYear();
    this.user = 'Sergio Vargas';
  }
}
