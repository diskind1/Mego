import { Component } from '@angular/core';
import { CarComponent } from '../car/car.component';


@Component({
  selector: 'app-michsemanoa',
  standalone: true,
  imports: [CarComponent, MichsemanoaComponent],
  templateUrl: './michsemanoa.component.html',
  styleUrl: './michsemanoa.component.css'
})
export class MichsemanoaComponent {

}
