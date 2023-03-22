import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { ScheduleDataService, ScheduleDay } from '../schedule.service';

@Component({
  selector: 'schedule',
  templateUrl: './schedule.component.html',
  styleUrls: ['./schedule.component.css'],
})
export class ScheduleComponent {
  show_schedule: boolean = false;
  schedule: ScheduleDay[] = [];

  todaysDataTime = '';
  today: number = Date.now();

  getData() {
    this.schedule = [];
    this.show_schedule = false;
    this.scheduleService.getData().subscribe((enteringData) =>
      enteringData.forEach((day) => {
        console.log(day);
        this.schedule.push(day);
      })
    );
    this.show_schedule = true;
  }

  constructor(private scheduleService: ScheduleDataService) {
    setInterval(() => {
      this.today = Date.now();
    }, 1);
  }
}
