import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BoregComponent } from './boreg.component';

describe('BoregComponent', () => {
  let component: BoregComponent;
  let fixture: ComponentFixture<BoregComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BoregComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BoregComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
