import { Component } from '@angular/core';
import axios from 'axios';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'angularstripe';
  card = '';
  cvc = '';
  doe = '';

  postCharge = async () => {
    if (this.cvc !== '' && this.card !== '' && this.doe !== '') {
      const url = 'http://127.0.0.1:8000/pay';
      const body = {
        card: this.card,
        doe: this.doe,
        cvc: this.cvc,
      };
      console.log(body);
      await axios
        .post(url, body)
        .then((res) => {
          console.log(res);
        })
        .catch((error) => console.log(error));
    }
  };
}
