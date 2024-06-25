import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { BoregComponent } from '../boreg/boreg.component';
import { CarComponent } from '../car/car.component';

@Component({
  selector: 'app-galgal',
  standalone: true,
  imports: [CommonModule, GalgalComponent, BoregComponent, CarComponent],
  templateUrl: './galgal.component.html',
  styleUrl: './galgal.component.css'
})
export class GalgalComponent {

}
