import { Component } from '@angular/core';
import { CarComponent } from '../car/car.component';



@Component({
  selector: 'app-manoa',
  standalone: true,
  imports: [CarComponent,],
  templateUrl: './manoa.component.html',
  styleUrl: './manoa.component.css'
})
export class ManoaComponent {

}
