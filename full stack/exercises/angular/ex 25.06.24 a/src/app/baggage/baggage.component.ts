import { Component } from '@angular/core';
import { CarComponent } from '../car/car.component';


@Component({
  selector: 'app-baggage',
  standalone: true,
  imports: [CarComponent, BaggageComponent],
  templateUrl: './baggage.component.html',
  styleUrl: './baggage.component.css'
})
export class BaggageComponent {

}
