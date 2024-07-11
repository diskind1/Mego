import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MoshavimComponent } from './moshavim.component';

describe('MoshavimComponent', () => {
  let component: MoshavimComponent;
  let fixture: ComponentFixture<MoshavimComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MoshavimComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MoshavimComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
