using System;
using System.Collections.Generic;
using System.Text;

namespace KalkulatorWyplaty
{
    class Wyplata
    {
        public string Imie { get; set; }
        public string Nazwisko { get; set; }
        public string Pesel { get; set; }
        public double Brutto { get; set; }
        //Skladki 
        public double Emerytalna { get; set; }  // Brutto * 9,76%
        public double Rentowa { get; set; }    // Brutto * 1,50%
        public double Chorobowa { get; set; }   // Brutto * 2,45%
        /*Skladki na ubezpieczenie zdrowotne:
         Podstawa wymiaru skladek na ubezpieczenie zdrowotne: PodstawaZdr = Brutto - (Emerytalna + Rentowa + Chorobowa)
        */
        public double PodstawaZdr { get; set; }   // PodstawaZdr = Brutto - (Emerytalna + Rentowa + Chorobowa)
        public double ZdrowotnaPobr { get; set; } // Skladka zdr. pobrana: ZdrowotnaPobr = PodstawaZdr * 9.00%
        public double ZdrowotnaOdli { get; set; } // Skladka zdr. odliczona: ZrowotnaOdli = PodstawaZdr * 7.75%

        /*Koszt uzyskania przychodu: 
        miejsce pracy = miejsce zam. 111,25; 
        miej.prac != miej.zam 139.06*/
        public double KosztyPrzychodu { get; set; }
        //Podstawa Opodatkowania
        public double PodstawaOpod { get; set; }  // PodstawaOpod = Brutto - ZdrowotnaPobr - KosztyPrzychodu
        //Zaliczka na podatek dochodowy
        public double ZaliczkaDoch { get; set; }  // ZaliczkaDoch = PodstawaOpod * 18.00%
        //Pobrana Zaliczka na podatek dochowy
        public double PobranaZaliDoch { get; set; } // PobranaZaliDoch = ZaliczkaDoch - ZdrowotnaOdli
        //Wynagrodzenie Netto
        public double Netto { get; set; } // Netto = (Brutto - (Emerytalna + Rentowa + Chorobowa)
       
    }
}
