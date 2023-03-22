import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, throwError } from 'rxjs';

export interface ScheduleDay {
  id: number;
  name: string;
  datetime_start: Date;
  datetime_end: Date;
}

@Injectable({
  providedIn: 'root',
})
export class ScheduleDataService {
  constructor(private http: HttpClient) {}
  baseURL = 'http://localhost:8000';

  getData(): Observable<ScheduleDay[]> {
    return this.http
      .get<ScheduleDay[]>(this.baseURL.concat('/schedule/get_all_subjects'))
      .pipe(catchError(this.handleError));
  }

  private handleError(error: HttpErrorResponse) {
    if (error.status === 0) {
      // A client-side or network error occurred. Handle it accordingly.
      console.error('An error occurred:', error.error);
    } else {
      // The backend returned an unsuccessful response code.
      // The response body may contain clues as to what went wrong.
      console.error(
        `Backend returned code ${error.status}, body was: `,
        error.error
      );
    }
    // Return an observable with a user-facing error message.
    return throwError(() => new Error('Сервер не доступен. Попробуйте позже.'));
  }
}
