import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ManoaComponent } from './manoa.component';

describe('ManoaComponent', () => {
  let component: ManoaComponent;
  let fixture: ComponentFixture<ManoaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ManoaComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ManoaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
