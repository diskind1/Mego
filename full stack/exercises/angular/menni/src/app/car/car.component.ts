import { Component } from '@angular/core';
import { GalgalComponent } from '../galgal/galgal.component';
import { ManoaComponent } from '../manoa/manoa.component';


@Component({
  selector: 'app-car',
  standalone: true,
  imports: [GalgalComponent ,CarComponent,ManoaComponent],
  templateUrl: './car.component.html',
  styleUrl: './car.component.css'
})
export class CarComponent {

}
