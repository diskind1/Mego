import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HegeComponent } from './hege.component';

describe('HegeComponent', () => {
  let component: HegeComponent;
  let fixture: ComponentFixture<HegeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HegeComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HegeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
