import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GalgalComponent } from './galgal.component';

describe('GalgalComponent', () => {
  let component: GalgalComponent;
  let fixture: ComponentFixture<GalgalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GalgalComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GalgalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
