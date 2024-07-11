import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { GalgalComponent } from './galgal/galgal.component';
import { ManoaComponent } from './manoa/manoa.component';
import { CarComponent } from './car/car.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'menni';
}
