import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MichsemanoaComponent } from './michsemanoa.component';

describe('MichsemanoaComponent', () => {
  let component: MichsemanoaComponent;
  let fixture: ComponentFixture<MichsemanoaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MichsemanoaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MichsemanoaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
