// Tomasz Waszczewski; Egzamin cpp 2019
#include <iostream>
#include <string>
using namespace std;
//Zadanie 1. 
/*(Zadanie 1.) Niech dana b�dzie klasa abstrakcyjna: 
class Shape { 
public: 
  virtual ~Shape() {} 
  virtual float area() = 0; 
}; 
Napisz klas� dziedzicz�c� po Shape i reprezentuj�c�: 
dla X = 2: Kwadrat 
Klasa pochodna powinna posiada�: 
-prywatne pola potrzebne do reprezentowania okre�lonego kszta�tu, 
-publiczny konstruktor inicjuj�cy pola klasy, ka�de pole powinno posiada� warto�� domy�ln� r�wn� zero, 
-publiczne metody ustawiaj�ce i zwracaj�ce pola klasy, 
-przeci��on� metod� area
-publiczny operator por�wnuj�cy pole obiektu: dla X = 2: operator wi�kszo�ci (>); 

*/
//klasa abstrakcyjna
class Shape {
	public: 
		virtual ~Shape() {}
		virtual float area()=0;
};
//klasa Kwadrat dziedziczaca po klasie shape 
class Kwadrat:public Shape{
	
private:
	float bok; //prywatne pole bok 
	
public: 
//publiczny konstruktor inicjuj�cy pola klasy, ka�de pole powinno posiada� warto�� domy�ln� r�wn� zero,
	Kwadrat(float bok=0) {  
	this->bok=bok;	
	} 
	
	float area(){
		return bok*bok;
	}
//publiczne metody ustawiaj�ce i zwracaj�ce pola klasy, 
	void setBok(float bok){
		this->bok=bok;  //aby zidentyfikowac 'data members' i odroznic od zmiennych lokalnych, uzywamy wskaznika - this->bok=bok lub (*this).bok=bok  ; Taka koniecznosc zachodzi jezeli mamy takie same nazwy. Kompilator daje 
	}					// pierwszenstwo zmiennym lokalnym i nie przypisuje wartosci do 'data members' bo ich nie rozroznia, te maja rozne miesca w pamieci, zatem, 
						// bez uzycia this-> i wskazania co jest 'data member' otrzymalibysmy tzw. 'garbage values'; 

	float getBok(){
		return bok;
	}
			
	float drukujSzczegoly(){
		cout<<"Bok:    "<<getBok()<<endl;
		cout<<"Pole:   "<<area()<<endl;
		cout<<"#########################################################################################################"<<endl;	
	}
//publiczny operator por�wnuj�cy pole obiektu: dla X = 2: operator wi�kszo�ci (>); 	
    float operator > (Kwadrat &other) {
    if (area() > other.area()) {
        return 1.0;
		} 
			else 
    			return 0.0;
    }
};

/*Zadanie 2.
Napisz klase ShapeList reprezentujaca tablice obiektow (dla X=2 kwadraty) 
W klasie zdefiniuj: 
-prywatne pole typu wska�nik na typ zaprogramowanej klasy; 
-prywatne pole size typu size_t

 reprezentuj�ce rozmiar tablicy; 
-publiczny jedno-parametrowy konstruktor alokuj�cy pami�� dynamiczn� (tablic�) dla 
wska�nika klasy o rozmiarze przekazanym w parametrze; 
-publiczn� metod� zwracaj�c� rozmiar tablicy; 
-publiczny konstruktor kopiuj�cy; 
-publiczny destruktor; 
-publiczny operator przypisania (=); 
-publiczny operator [] zwracaj�cy referencj� do elementu tablicy (obiektu typu 
zaprogramowanej klasy), je�li indeks przekracza zakres tablicy zachowanie powinno 
by� nieokre�lone -- nie nale�y obs�ugiwa� takiej sytuacji. 
*/

//Napisz klase ShapeList reprezentujaca tablice obiektow (dla X=2 kwadraty) 
class ShapeList {
private:
    Kwadrat *wskaznik; //deklaracja zmiennej wskaznikowej na typ klasy, ta zmienna utworzona na - stack, bedzie przechowywala adres komorki pamieci zaalokowanej dynamicznie na - heap, przy pomocy operatora new. 
    size_t size; //zmienna size typu size_t; 

public:
    ShapeList(size_t size=0){			//publiczny konstruktor jedno parametrowy ustawiajacy wartosc poczatkowa na 0 
    this->size=size; 					//przypisanie wartosci do zmiennej size - uzycie wskaznika - this - powoduje, ze wskazujemy bezposrednio na adres gdzie przechowywana jest zmienna size. 
	wskaznik = new Kwadrat[size]; 		//przypisanie adresu pamieci zaalokowanej na - heap - do wkaznika -wskaznik- przechowywanego na - stack.    
	} 									//Zaalokowanie pamieci na - heap - przy uzyciu operatora -new- dla tablicy, typu Kwadrat, ktorej rozmiar jest przekazany w paramentrze -size

   ShapeList(const ShapeList &other) {  //konstruktor kopiujacy - parametr typu klasa oraz parametr typu referencynego; kiedy jest wywolany przekazuje dane z obiektu &other do nowego obiektu - stad konstruktor kopiujacy
   size=other.size; 					//przypisanie danych obiektu -other- do zmiennej -size-, zatem dane z obiektu other sa kopiowane do obiektu size. 
   wskaznik=new Kwadrat[other.size];	//przypisanie adresu pamieci zaalokowanej na - heap - do wkaznika -wskaznik- przechowywanego na - stack; 
   										//Zaalokowanie pamieci na - heap - przy uzyciu operatora -new- dla tablicy, typu Kwadrat, ktorej rozmiar jest przekazany w paramentrze -other.size;
		for(size_t i=0; i < this->size; i++) this->wskaznik[i] = other.wskaznik[i];
	}
	
~ShapeList() {delete[] wskaznik;} //-publiczny destruktor; Zwalnia uprzednio zaalokowana pamiec przy pomocy operatora -new;
/* w materialach jest tak;
Array & Array::operator=(const Array & a) {
if (this != &a) {
delete [] t;
this->size = a.size;
this->t = new int[a.size];
for (size_t i = 0; i < this->size; i++)
this->t[i] = a.t[i];
}
return *this;
}
*/
ShapeList & operator=(const ShapeList & other) { //klasa ShapeList - operator przypisania
	if(this != &other) {
        delete [] wskaznik;
        this->size = other.size;
        this->wskaznik = new Kwadrat[other.size];
        for(size_t i=0; i < this->size; i++) 
		   this->wskaznik[i] = other.wskaznik[i];
	    }
		return *this;
	}
//-publiczny operator [] zwracaj�cy referencj� do elementu tablicy (obiektu typu zaprogramowanej klasy)
	Kwadrat & operator[](int index) const
	{
		return wskaznik[index];
	}
	inline size_t rozmiar() const { return size; }
};
/*Zadanie 3. 
Napisz funkcj� main gdzie stworzysz obiekt typu ShapeList oraz przypiszesz dowolne obiekty (wi�cej ni� 2) do tablicy przechowywanej przez obiekt (za pomoc� 
operatora []). Nast�pnie oblicz i wy�wietl na ekran obiekt o najwi�kszym polu, do znalezienia 
tego obiektu wykorzystaj przeci��ony operator. 
*/
//Napisz funkcj� main
int main (){  
//test klasy class Kwadrat:public Shape i przeciazonego operatora porownania
Kwadrat k1,k2;
k1.setBok(172.6);
cout<<"Kwadrat: "<<endl;
cout<<k1.drukujSzczegoly()<<endl;

k2.setBok(22.6);
cout<<"Kwadrat: "<<endl;
cout<<k2.drukujSzczegoly()<<endl;
if ((k1.area())>(k2.area()))
	cout << "Pole kwadratu k1 jest wieksze od kwadratu k2; "<< " k1: "<<k1.area()<<" > "<<" k2: "<<k2.area()<< endl;
		else
			cout << "Pole kwadratu k2 jest wieksze lub rowne polu kwadratu k1; "<< " k1: "<<k1.area()<<" < lub = "<<" k2: "<<k2.area()<< endl;

//gdzie stworzysz obiekt typu ShapeList oraz przypiszesz dowolne obiekty (wi�cej ni� 2)do tablicy przechowywanej przez obiekt (za pomoc� operatora []).
ShapeList sl(3); 
    cout << "#########################################################################################################"<<endl;
    cout << "Przypisanie dowolnych obiektow do tablicy"<<endl;
    cout << "#########################################################################################################"<<endl;
    sl[0]=Kwadrat (7.43);
    sl[1]=Kwadrat (4.3);
    sl[2]=Kwadrat (122.2);
    for (int i=0; i<3; i++){
    	sl[i].drukujSzczegoly();
	}
//Nast�pnie oblicz i wy�wietl na ekran obiekt o najwi�kszym polu,   
    float najwiekszePole = sl[0].area();
    	for(int i=1; i<3; i++)
    		if (sl[i].area() > najwiekszePole)
    			najwiekszePole = sl[i].area();
    			
    			cout << "Kwadrat o najwiekszym polu to:  "<< najwiekszePole << endl; 
}
