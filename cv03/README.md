Cvičenie 3
==========

**Riešenie odovzdávajte podľa
[pokynov na konci tohoto zadania](#technické-detaily-riešenia)
do Nedele 16.3.  23:59:59.**

Vytvorte objektovú hierarchiu na reprezentáciu výrokovologických formúl.
Zadefinujte základnú triedu `Formula` a 6 od nej odvodených tried určených
na reprezentáciu jednotlivých druhov atomických a zložených formúl.

Všetky triedy naprogramujte ako knižnicu podľa
[pokynov na konci tohoto zadania](#technické-detaily-riešenia)
tak, aby tam uvedené príklady boli skompilovateľné (a vypísali
správny výsledok ;).

```
class Formula
	constructor()
	String toString()	// vrati textovu reprezentaciu formule
	Bool eval(Interpretation i)	// vrati true, ak je formula
					// pravdiva pri interpretacii i
	Array of Formula subf()	// vrati vsetky priame podformuly ako pole

class Variable(Formula)
	constructor(String name)
	String name()	// vrati meno premennej

class Negation(Formula)
	constructor(Formula originalFormula)
	Formula originalFormula()	// vrati povodnu formulu
					// (jedinu priamu podformulu)

class Implication(Formula)
	constructor(Formula leftSide, Formula rightSide)
	Formula leftSide()	// vrati lavu priamu podformulu
	Formula rightSide()	// vrati pravu priamu podformulu

class Disjunction(Formula)
	constructor(Array of Formula disjuncts)

class Conjunction(Formula)
	constructor(Array of Formula conjuncts)

class Equivalence(Formula)
	constructor Create(leftSide, rightSide)
	Formula leftSide()
	Formula rightSide()
```
Samozrejme použite syntax a základné typy jazyka ktorý používate (viď
príklady použitia knižnice na konci).

Funkcie `toString` a `eval` budú virtuálne funkcie predefinované v každej
podtriede tak, aby robil *správnu vec*<sup>TM</sup> pre dotyčný typ formuly.

Funkcia `toString` vráti textovú reprezentáciu formuly podľa nasledovných
pravidiel:
- `Variable`: reťazec `a`, kde `a` je meno premennej (môže byť
  viacpísmenkové)
- `Negation`: reťazez `-A`, kde `A` je reprezentácia podformuly
- `Conjunction`:  reťazec `(A&B&C....)`, kde `A`, `B`, `C`, ... sú
  reprezentácie podformúl (konjunktov)
- `Disjunction`:  reťazec `(A|B|C....)`, kde `A`, `B`, `C`, ... sú
  reprezentácie podformúl (disjunktov)
- `Implication`:  reťazec `(A=>B)`, kde `A` a `B` sú reprezentácie
  ľavej a pravej podformuly
- `Equivalence`: reťazec `(A<=>B)`, kde `A` a `B` sú reprezentácie
  ľavej a pravej podformuly
Teda napri

Funkcia `eval` vráti `True` alebo `False` podľa toho, či je formula pravdivá
pri danej interpretácii. Ak sa stane, že ohodnotenie neobsahuje nejakú
premennú, ktorá sa vyskytne vo formule, tak môžete buď vygenerovať chybu /
výnimku alebo ju považovať za False.

## Interpretácia
Interpretácia je mapa z reťazcov na Bool, použite správny typ podľa vášho
jazyka:

### C++
Vaša knižnica by mala definovať   nasledovný typedef:
```c++
typedef std::map<std::string, bool> Interpretation;
```
  príklad použitia:
```c++
Interpretation i;
i["a"] = true;
Formula *f = new Variable("a");
if (f->eval(i) != i["a"]) { /* nieco je zle */ }
```

### Python
Slovnik (`dict`, `{}`), v ktorom sú reťazce mapovane na `True` alebo `False`:
```python
i = { 'a':True, 'b':False }
f = Variable('a')
if f.eval(i) != i['a']:
	# nieco je zle
```

### Java:
**TODO**

## Technické detaily riešenia

Riešenie odovzdajte do vetvy `cv03` v adresári `cv03`.  Odovzdávajte súbor
`formula.h`/`formula.cpp`, `formula.py`, alebo `formula.java`.

Odovzdávanie riešení v iných jazykoch konzultujte s cvičiacimi.

### C++
Nasledovný program [`cv03.cpp`](cv03.cpp) musí byť skompilovateľný, keď sa k
nemu priloží vaša knižnica:
```c++
#include <iostream>

#include "formla.h"

int main()
{
	Formula *f = new Equivalence(
		new Conjunction(
			new Variable("alfa"),
			new Negation(new Variable("beta"))
		),
		new Disjunction(
			new Vriable("alfa"),
			new Implication(
				new Variable("beta"),
				new Variable("alfa")
			)
		)
	);
	// vypise ((alfa&-beta)<=>(alfa|(beta=>alfa)))
	std::cout << f->toString() << std::endl;
	Interpretation i;
	i["alfa"] = true;
	i["beta"] = false;
	if (f->eval(i))
		std::count << "pravdiva" << std::endl;
	else
		std::count << "nepravdiva" << std::endl;

	delete f;
	return 0;
}
```
Poznámka: formula vždy vlastní svoje podformuly. Príkaz `delete f` v
programe zmaže zároveň aj všetky podformuly.

### Python
Nasledovný program [`cv03.py`](cv03.py) musí korektne fungovať, keď sa k
nemu priloží vaša knižnica:
```python
from formula import Variable, Negation, Conjunction, Dijunction, Implication, Equivalence

f = Equivalence(
	Conjunction(
		Variable('alfa'),
		Negation(Variable('beta'))
	),
	Disjunction(
		Vriable('alfa'),
		Implication(
			Variable('beta'),
			Variable('alfa')
		)
	)
)
# vypise ((alfa&-beta)<=>(alfa|(beta=>alfa)))
print(f.toString())

i = {}
i['alfa'] = True;
i['beta'] = False;
if f.eval(i):
	print('pravdiva')
else:
	print('nepravdiva')
return 0;
```

Java:
