import { Component } from '@angular/core';
import { GalgalComponent } from '../galgal/galgal.component';
import { ManoaComponent } from '../manoa/manoa.component';
import { MichsemanoaComponent } from '../michsemanoa/michsemanoa.component';
import { HegeComponent } from '../hege/hege.component';
import { MoshavimComponent } from '../moshavim/moshavim.component';
import { BaggageComponent } from '../baggage/baggage.component';
import { BoregComponent } from '../boreg/boreg.component';


@Component({
  selector: 'app-car',
  standalone: true,
  imports: [CarComponent, ManoaComponent, MichsemanoaComponent, HegeComponent,MoshavimComponent,BaggageComponent, GalgalComponent, BoregComponent],
  templateUrl: './car.component.html',
  styleUrl: './car.component.css'
})
export class CarComponent {

}
