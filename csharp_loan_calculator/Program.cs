using System;

namespace KalkulatorWyplaty
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("################Kalkulator Wyplaty###################");
            Console.Write("Wprowadz ilosc pracownikow: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Wyplata[] wyp = new Wyplata[n];

            for (int i = 0; i < n; i++)
            {
                wyp[i] = new Wyplata();
                Console.WriteLine("ID Pracownika: ", i + 1);

                Console.Write("Imie: ");
                wyp[i].Imie = Console.ReadLine();

                Console.Write("Nazwisko: ");
                wyp[i].Nazwisko = Console.ReadLine();

                Console.Write("PESEL: ");
                wyp[i].Pesel = Console.ReadLine();

                Console.Write("Miejsce pracy jest miesjcem zamieszkania? (tak / nie): ");
                if (Console.ReadLine() == "tak")
                {
                    wyp[i].KosztyPrzychodu = 111.25;
                }
                else
                {
                    wyp[i].KosztyPrzychodu = 139.06;
                }

                Console.Write("Brutto: ");
                wyp[i].Brutto = Convert.ToDouble(Console.ReadLine());
                //Emerytalna = Brutto * 9,76%
                wyp[i].Emerytalna = wyp[i].Brutto * .0976;
                //Rentowa = Brutto * 1,50%
                wyp[i].Rentowa = wyp[i].Brutto * .015;
                //Chorobowa = Brutto * 2,45%
                wyp[i].Chorobowa = wyp[i].Brutto * .0245 ;
                //PodstawaZdr = Brutto - (Emerytalna + Rentowa + Chorobowa)
                wyp[i].PodstawaZdr = (wyp[i].Brutto - (wyp[i].Emerytalna + wyp[i].Rentowa + wyp[i].Chorobowa));
                // Skladka zdr. pobrana: ZdrowotnaPobr = PodstawaZdr * 9.00%
                wyp[i].ZdrowotnaPobr = wyp[i].PodstawaZdr * .090;
                // Skladka zdr. odliczona: ZrowotnaOdli = PodstawaZdr * 7.75%
                wyp[i].ZdrowotnaOdli = wyp[i].PodstawaZdr * .0775;
                //PodstawaOpod = Brutto - ZdrowotnaPobr - KosztyPrzychodu
                wyp[i].PodstawaOpod = (wyp[i].Brutto - (wyp[i].Emerytalna + wyp[i].Rentowa + wyp[i].Chorobowa)-wyp[i].KosztyPrzychodu);
                //ZaliczkaDoch = PodstawaOpod * 18.00 %
                wyp[i].ZaliczkaDoch = wyp[i].PodstawaOpod * .18;
                // PobranaZaliDoch = ZaliczkaDoch - ZdrowotnaOdli - 46.30
                wyp[i].PobranaZaliDoch = (wyp[i].ZaliczkaDoch  - wyp[i].ZdrowotnaOdli - 46.30 );
                // Netto = (Brutto - (Emerytalna + Rentowa + Chorobowa)
                wyp[i].Netto = (wyp[i].Brutto - (wyp[i].Emerytalna + wyp[i].Rentowa + wyp[i].Chorobowa) - wyp[i].ZdrowotnaPobr -  wyp[i].PobranaZaliDoch);
            }
            for (int i = 0; i < n; i++)
            {
                Console.WriteLine(
                    "----------------DANE PODSTAWOWE-----------------\n\n" +
                    "ID Pracownika:...............................{0}\n" +
                    "Imie:........................................{1}\n" +
                    "Nazwisko:....................................{2}\n" +
                    "PESEL:.......................................{3}\n" +
                    "Wynagrodzenie Brutto:........................{4}\n\n" +
                    "---------------------SKLADKI--------------------\n\n" +
                    "Skladka Emerytalna:..........................{5}\n" +
                    "Skladka Rentowa:.............................{6}\n" +
                    "Skladka Chorobowa:...........................{7}\n\n" +
                    "-------------UBEZPIECZENIE ZDROWOTNE-----------\n\n" +
                    "Podstawa wymiaru skladek ubez. zdrow:........{8}\n" +
                    "Skladka zdrow. pobrana.......................{9}\n" +
                    "Skladka zdrow. odliczona.....................{10}\n" +
                    "Koszty uzyskania przychodu...................{11}\n" +
                    "Podstawa odpodatkowania......................{12}\n" +
                    "Zaliczka na podatek dochodowy................{13}\n" +
                    "Pobrana zaliczka na podatek dochodowy........{14}\n" +
                    "Wynagrodzenie Netto..........................{15}\n"

                      ,i + 1,
                      wyp[i].Imie,                               //1  Imie
                      wyp[i].Nazwisko,                           //2  Nazwisko
                      wyp[i].Pesel,                              //3  PESEL
                      wyp[i].Brutto,                             //4  Brutto
                      Math.Round(wyp[i].Emerytalna),             //5  Emerytalna
                      wyp[i].Rentowa,                            //6  Rentowa
                      wyp[i].Chorobowa,                          //7  Chorobowa
                      wyp[i].PodstawaZdr,                        //8  Podstawa wymiaru na zdrowotne
                      wyp[i].ZdrowotnaPobr,                      //9  Zdrowotna pobrana
                      wyp[i].ZdrowotnaOdli,                      //10 Zdrowotna odliczona
                      wyp[i].KosztyPrzychodu,                    //11 Koszty uzyskania przychodu
                      wyp[i].PodstawaOpod,                       //12 Podstawa odpodatkowania
                      wyp[i].ZaliczkaDoch,                       //13 Zaliczka na podatek dochodowy
                      wyp[i].PobranaZaliDoch,                    //14 Pobrana zaliczka na podatek dochodowy
                      wyp[i].Netto);                             //15 Netto

            }
        }

    }
}