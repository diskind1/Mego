import { Component } from '@angular/core';
import { CarComponent } from '../car/car.component';

@Component({
  selector: 'app-moshavim',
  standalone: true,
  imports: [CarComponent, MoshavimComponent],
  templateUrl: './moshavim.component.html',
  styleUrl: './moshavim.component.css'
})
export class MoshavimComponent {

}
