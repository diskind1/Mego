import { Component } from '@angular/core';
import { Item } from '../../models/item';
import { CommonModule } from '@angular/common';
import { Item1Component } from '../item1/item1.component';

@Component({
  selector: 'app-item-list',
  standalone: true,
  imports: [CommonModule,Item1Component],
  templateUrl: './item-list.component.html',
  styleUrl: './item-list.component.css'
})
export class ItemListComponent {
  items: Item[] = [];

  constructor(){
    this.items.push({Makat: "re546", Name: "גיטרה", Category: "כלי נגינה",  Description:"גיטרה מיוחדת עם צליל מיתר נעים ומרגיע", Price:2000, Qty:15, Image:"./img/Gitar.jpg"})
    this.items.push({Makat: "erv584", Name: "כינור", Category: "כלי נגינה",  Description:"!הכינור שחלמתם עליו, פשוט להתרפק", Price:1200, Qty:25, Image:"./img/Cinor.jpg"})
    this.items.push({Makat: "erg264", Name: "קלידים", Category: "כלי נגינה",  Description:"הקלידנים! ועכשיו במחיר מבצע", Price:13000, Qty:7, Image:"./img/Klidim.jpg"})
    this.items.push({Makat: "ggg4359", Name: "קנטלה", Category: "כלי נגינה",  Description:"!למייבינים בלבד", Price:1750, Qty:9, Image:"./img/Cantele.jpg"})
    this.items.push({Makat: "ef485", Name: "קלרינט", Category: "כלי נגינה",  Description:"חיליפ של הדור הבא, עכשיו ברשתות", Price:2900, Qty:13, Image:"./img/Klarinet.jpg"})
  }

}
