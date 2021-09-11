import { HttpClient, HttpHeaders } from '@angular/common/http';
import { getInterpolationArgsLength } from '@angular/compiler/src/render3/view/util';
import { Observable } from 'rxjs';

export interface FormInfo {
    console: boolean;
    alcohol_referene: boolean;
    animated_blood: boolean;
    blood: boolean;
    blood_and_gore: boolean;
    cartoon_violence: boolean;
    drug_reference: boolean;
    fantasy_violence: boolean;
    intense_violence: boolean; 
    mature_humor: boolean; 
    mild_fantasy_violence: boolean; 
    mild_lyrics: boolean;
    mild_suggestive_themes: boolean;
    sexual_content: boolean;
    sexual_themes: boolean;
    simulated_gambling: boolean;
    strong_janguage: boolean;
    strong_sexual_content: boolean; 
    suggestive_themes: boolean;
    use_of_drugs_and_alcohol: boolean;
}

export class RatingFormService {
    endpoint = 'http://localhost:3000';

    constructor(private httpClient: HttpClient) { }

    httpHeader = {
        headers: new HttpHeaders({
            'Content-Type': 'application/json'
        })
    }

    getRatingResults(data): Observable<FormInfo> {
        return this.httpClient.post<FormInfo>(this.endpoint + '/results', JSON.stringify(data), this.httpHeader)
        .pipe(
            retry(1)
        )
    }
}