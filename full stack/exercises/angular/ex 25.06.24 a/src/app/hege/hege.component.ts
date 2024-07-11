import { Component } from '@angular/core';
import { CarComponent } from '../car/car.component';


@Component({
  selector: 'app-hege',
  standalone: true,
  imports: [CarComponent, HegeComponent],
  templateUrl: './hege.component.html',
  styleUrl: './hege.component.css'
})
export class HegeComponent {

}
