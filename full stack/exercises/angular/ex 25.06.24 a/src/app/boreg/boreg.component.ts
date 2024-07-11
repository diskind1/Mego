import { Component } from '@angular/core';
import { CarComponent } from '../car/car.component';
import { GalgalComponent } from '../galgal/galgal.component';

@Component({
  selector: 'app-boreg',
  standalone: true,
  imports: [CarComponent, GalgalComponent],
  templateUrl: './boreg.component.html',
  styleUrl: './boreg.component.css'
})
export class BoregComponent {

}
