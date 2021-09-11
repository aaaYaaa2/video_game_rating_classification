import { Component } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {MatPseudoCheckboxModule, ThemePalette} from '@angular/material/core';
import { Observable } from 'rxjs';
// import { nextTick } from 'process';

export interface RatingData {
  console: boolean
  alcohol_referene: boolean
  animated_blood: boolean
  blood: boolean
  blood_and_gore: boolean
  cartoon_violence: boolean
  drug_reference: boolean
  fantasy_violence: boolean
  intense_violence: boolean 
  mature_humor: boolean 
  mild_fantasy_violence: boolean 
  mild_lyrics: boolean
  mild_suggestive_themes: boolean 
  sexual_content: boolean
  sexual_themes: boolean
  simulated_gambling: boolean 
  strong_janguage: boolean 
  strong_sexual_content: boolean 
  suggestive_themes: boolean 
  use_of_drugs_and_alcohol: boolean 
}

@Component({
  selector: 'app-rating-form',
  templateUrl: './rating-form.component.html',
  styleUrls: ['./rating-form.component.css']
})

export class RatingFormComponent {

  constructor(private httpClient: HttpClient) { }

  httpHeader = {
    headers: new HttpHeaders({
        'Content-Type': 'application/json; charset=UTF-8;',
        'Access-Control-Allow-Origin': '*',
    })
  }

  endpoint = 'http://127.0.0.1:5000';
  
  ratingForm = new FormGroup({
    console: new FormControl(false),
    alcoholReference: new FormControl(false),
    animatedBlood: new FormControl(false),
    blood: new FormControl(false),
    bloodAndGore: new FormControl(false),
    cartoonViolence: new FormControl(false),
    drugReference: new FormControl(false),
    fantasyViolence: new FormControl(false),
    intenseViolence: new FormControl(false),
    matureHumor: new FormControl(false),
    mildFantasyViolence: new FormControl(false),
    mildLyrics: new FormControl(false),
    mildSuggestiveThemes: new FormControl(false),
    sexualContent: new FormControl(false),
    sexualThemes: new FormControl(false),
    simulatedGambling: new FormControl(false),
    strongJanguage: new FormControl(false),
    strongSexualContent: new FormControl(false),
    suggestiveThemes: new FormControl(false),
    useOfDrugsAndAlcohol: new FormControl(false),
    predResult: new FormControl('unknown')
  });


  submitForm() {

    let databody = {
      console: false,
      alcohol_reference: false,
      animated_blood: false,
      blood: false,
      blood_and_gore: false,
      cartoon_violence: false,
      drug_reference: false,
      fantasy_violence: false,
      intense_violence: false, 
      mature_humor: false, 
      mild_fantasy_violence: false, 
      mild_lyrics: false,
      mild_suggestive_themes: false,
      sexual_content: false,
      sexual_themes: false,
      simulated_gambling: false, 
      strong_janguage: false,
      strong_sexual_content: false, 
      suggestive_themes: false, 
      use_of_drugs_and_alcohol: false,
      pred_result: 'unknown'
    };

    databody.console = this.ratingForm.value.console;
    databody.alcohol_reference = this.ratingForm.value.alcoholReference;
    databody.animated_blood = this.ratingForm.value.animatedBlood;
    databody.blood = this.ratingForm.value.blood;
    databody.blood_and_gore = this.ratingForm.value.bloodAndGore;
    databody.cartoon_violence = this.ratingForm.value.cartoonViolence;
    databody.drug_reference = this.ratingForm.value.drugReference;
    databody.fantasy_violence = this.ratingForm.value.fantasyViolence;
    databody.intense_violence = this.ratingForm.value.intenseViolence;
    databody.mature_humor = this.ratingForm.value.matureHumor;
    databody.mild_fantasy_violence = this.ratingForm.value.mildFantasyViolence;
    databody.mild_lyrics = this.ratingForm.value.mildLyrics;
    databody.mild_suggestive_themes = this.ratingForm.value.mildSuggestiveThemes;
    databody.sexual_content = this.ratingForm.value.sexualContent;
    databody.sexual_themes = this.ratingForm.value.sexualThemes;
    databody.simulated_gambling = this.ratingForm.value.simulatedGambling;
    databody.strong_janguage = this.ratingForm.value.strongJanguage;
    databody.strong_sexual_content = this.ratingForm.value.strongSexualContent;
    databody.suggestive_themes = this.ratingForm.value.suggestiveThemes;
    databody.use_of_drugs_and_alcohol = this.ratingForm.value.useOfDrugsAndAlcohol;
    
    const jsonData = {
      form: databody
    }

    this.httpClient.post<any>(this.endpoint + '/predict', JSON.stringify(jsonData))
      .toPromise()
      .then((result) => {
        console.log(result.result)
        let rating;
        switch(result.result) {
          case '0':
            rating = 'E'
            break
          case '1':
            rating = 'ET'
            break
          case '2':
            rating = 'T'
            break
          case '3':
            rating = 'M'
            break
          default:
            rating = 'UNKNOWN'
        }
        this.ratingForm.controls.predResult.setValue(rating)
      })
  }
}

