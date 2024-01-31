# Curs 1 Aplicatii Web cu ASP.NET Core - Razor Pages -

## ASP.NET Core
* ASP.NET -O unealtaMicrosoft C# pentrudezvoltareade aplicatiiweb
* Competitori: Java Spring,PHPLaravel, Node.js Express
* .NET Platformade dezvoltareMicrosoft din anul2001
* ASP –Active Server Pages-paginiweb dinamice, de celemaimulteoriconectatela o bazade date
* Core – open source, cross-platform
* Necesitatea ca ASP.NET si Entity Framework sa ruleze pe alte SO in afara de Windows
* Arhitectura care usureaza testarea
* Integrarea de framework-uri client-side – Blazor –creare de UIs utilizand C# in loc de JavaScript.
* Suporta instalarea de versiuni diferite ale .Net Core – side by side versioning

## Tehnologii Web
* HTML
* CSS
* JavaScript si TypeScript
* Librarii de scripting


## HTML si CSS
* Cascade Style Sheets - definesc felul in care arata pagina web
* HTML tagul pentru list item <li> definea modul in care este vizualizat,cerc,disc,patrat ->CSS
* Se pot utiliza template-uri Bootstrap - o colectie de conventii CSS si HTML care pot fi adaptate facil
* www.getbootstrap.com - documentatie si template-uri

## JavaScript si TypeScript
* Putem modifica dynamic elemente client-side
* ECMAScript – standard care defineste functionalitatile curente si vitoare pentru JavaScript.
* Implementarea Microsoft pentru JavaScript se numeste JScript.
* TypeScript similar cu JavaScript. Sintaxa TypeScript se bazeaza pe JavaScript, dar aduce noi functionalitati (ex. Cod puternic tipizat, adnotari)
* Documentatie la : www.typescriptlang.org.

## Librarii de scripting
* Pot fi utilizate server-side impreuna cu ASP.NET Core
* jQuery (http://www.jquery.org) –utilizata pentru a gestiona unitar modul in care diferite browsere gestioneaza evenimentele
* Angular (https://angular.io) librarie de la Google bazata pe patternul MVC creata pentru a simplifica dezvoltarea si testarea aplicatiilor web de tip single-page (Spre deosebire de ASP.NET MVC, Angular ofera patternul MVC in codul client-side)
* React (https://reactjs.org) librarie de la FaceBook care ofera functionalitati prin care se pot actualiza facil intefetele utilizator pe masura ce datele se modifica in background
* Visual Studio ofera template-uri pentru Angular si React

## Aplicatii Web cu ASP.NET Core
### De tip Server-side
* Razor Pages
* MVC

### De tip Client-side
* Blazor
* Angular
* React


# Curs 2 Pagini Razor și sintaxa

## Structura unei aplicatii Web – cu Razor

In directorul wwwroot regasim continut de tip client-side CSS, JavaScript, imagini, si orice alt continut non-programatic

Directorul Pages contine pagini Razor si fisiere suport. Fiecare pagina este o pereche a urmatoarelor fisiere:

* 	Un fisier _.cshtml_ care contine markup Razor, HTML si cod C#.
* 	Un fisier _.cshtml.cs_ care contine cod C# pentru a gestiona evenimentele la nivel de pagina.

Fisierele suport au nume care incepe cu “_”. Ex fisierul “_Layout.cshtml” configureaza elemente UI comune tuturor. Ex. acest fisier seteaza
navigation menu in partea de sus a paginii si informatia despre copyright in
partea de jos a paginii.

## Pagini Layout

* Majoritatea site-urilor prezintă același conținut pe fiecare pagină sau într-un număr mare de pagini (ex. antet, subsol, bara meniu de navigare, scripturile, css etc.)
* Adăugarea aceluiași continut încalcă principiul DRY (Don’t Repeat Yourself) => trebuie să modificați aspectul antetului, trebuie să editați fiecare pagină
* Pagina Layout - acționează ca un șablon pentru toate paginile care fac referire la aceasta.
* Paginile care fac referire la pagina de Layout se numesc pagini de conținut. Paginile de conținut nu sunt pagini web complete. Acestea conțin doar conținutul care variază de la o pagină la alta.

```
<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title></title>
		<link href="/css/site.css" rel="stylesheet" type="text/css" />
	</head>
	<body>
		@RenderBody()
	</body>
</html>
```

## Fisiere configurare aplicatii Web – cu Razor

**appSettings.json**

* Contine date de configurare, precum string-uri de conexiune

**Program.cs**

* Punctul de start al aplicatiei.


## Sintaxa Razor

* Razor este o sintaxa de tip markup pentru a incorpora cod de tip server-side in pagini web
* Sintaxa Razor consta in Razor markup, C#, si HTML
* Limbajul Razor implicit este HTML. Interpretarea HTML din markup-ul Razor este similara cu interpretarea HTML dintr-un fisier HTML.
* Pentru a trece la limbaj C# - simbolul @ - Razor evalueaza expresiile C# si le randeaza in output HTML
* Cand simbolul @ este urmat de un cuvant cheie Razor – tranzitia se face la markup specific Razor


## Expresii implicite/explicite Razor

### • Expresii implicite

```
<p>@DateTime.Now</p>
<p>Last week: @DateTime.Now -
TimeSpan.FromDays(7)</p>
```
Se afiseaza

```
<p>Last week: 7/7/2016 4:39:52 PM - TimeSpan.FromDays(7)</p>
```

### • Expresii explicite ()

```
<p>Last week this time: @(DateTime.Now - TimeSpan. FromDays(7)) </p>
```

Continutul @() este evaluat si afisat