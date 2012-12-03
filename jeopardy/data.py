# -*- coding: utf8 -*-
import subprocess
questions = {}
q =  questions

VS = []
GS = []
GS.append(("""
    <Br><br><Br>

    JEOPARDY!


    """,
    """
    <Br><br><Br>
    Correct!
<font size=-3><br>
</font>
    """))
WS = []
AS = []
UC = []
BL = []
PP = []
TST= []
BA = []


TST.append(("""
    <Br>
Why is Alex Trebek so cool?
<br><br>Because he’s Canadian
<br>Because he rocks his moustache




    """,
    """
    <Br><br><Br>
Because he’s Canadian

<font size=-3><br>
<img height="200px" src="pictures/Bliss.jpg">
<br>
</font>
    """
    ))



UC.append(("""
    What do you call the line that runs perpendicular to the 50 yard line at
    California’s Memorial Stadium?








    """,
    """
    <Br>
    The Hayward Fault line

<font size=-3><br>
<img height="200px" src="pictures/HaywardFault.jpg">
<br>
</font>
    """
    ))

BA.append(("""
Which of the following American Viticultural Areas (AVA) is not
within Napa county?
<font size=-3>
<br>Rutherford
<br>Suisun
<br>Napa
<br>Oakville
<br>Yountville
<br>St Helena
</font><br>


    """,
    """
    <Br><br><Br>
Answer: Suisun Valley
is in Solano County


<font size=-3><br>
<br>
</font>
    """
    ))

BA.append(("""

What do all these names have in common?
<br><br>Hefeweizen
<br>Apricot
<br>ThunderHead
<br>Outburst
<br>Wheaten IPA


    """,
    """
    <Br><br><Br>
Answer: They’re all from Pyramid Breweries 

<font size=-3><br>
<br>
</font>
    """
    ))


BA.append(("""
   

Which African animal was the SF 49er’s unofficial mascot in 2011
<br>
<br>Wildebeest
<br>Meerkat
<br>Rhinoceros
<br>Honeybadger


    """,
    """
    <Br><br><Br>
The Honeybadger

<font size=-3><br>
<br>
</font>
    """
    ))


GS.append(("""
What is the common name for this molecule?
<font size=-3><br>
<img height="200px" src="pictures/Caffiene.jpg">
<br>
<br>A) Caffeine
<br>B) Nicotine
<br>C) Tetrahydrocannabinol
<br>D) Methamphetamine
</font>



    """,
    """
    <Br><br><Br>


Answer: Caffeine

<font size=-3><br>
<img height="200px" src="pictures/Caffiene.jpg">
<br>
</font>

    """
    ))
GS.append(("""
    <Br><br><Br>

    How many neurons are there in the average adult human brain? 
<br>    
    (+/- 10
    billion is OK)


    """,
    """

    <Br><br><Br>
    ~ 86 Billion: 
    <br>
<font size=-3><br>
    Herculano-Houzel, S., Lent, R. "Isotropic fractionator: A simple, rapid
    method for the quantification of total cell and neuron numbers in the
    brain" J.Neuroscience. 25, 2518-2521. (2005).


<br>
</font>
    """
    ))
GS.append(("""
    <Br><br><Br>
How many bones are there in the adult human body?


    """,
    """
    <Br><br><Br>
Answer: 206

<font size=-3><br>
<br>
</font>
    """
    ))

GS.append(("""
    <Br><br><Br>
What was the first neurotransmitter ever discovered?

    """,
    """
    <Br><br><Br>
    Acytelcholine (ACh)

<font size=-3><br>

(thanks, Sahar!)
<br>
</font>
    """
    ))



BA.append(("""

What do these buildings have in common?
<img height="200px" src="pictures/BerkeleyCityClub.jpg">
<img height="200px" src="pictures/HearstGym.jpg">
<img height="200px" src="pictures/HearstCastle.jpg">
<img height="200px" src="pictures/JuliaMorganHouse.jpg">








    """,
    """
    <Br><br><Br>
All were designed by Julia Morga

<font size=-3><br>
<br>
</font>
    """
    ))


BL.append(("""
What do these 6 local eateries all have in common?
<font size=-3><br>
<br>La Trattoria Siciliana 2993 College Ave
<br>Cream 2993 College Ave
<br>Jayakarta 2026 University Ave
<br>Emilia’s Pizzeria 2995 Shattuck
<br>Plearn Thai Kitchen 2283 Shattuck Ave
</font>

    """,
    """
    <Br><br><Br>

They only take cash $$$$$
<font size=-3><br>
<br>
</font>
    """
    ))



BA.append(("""
    <Br>
What is the color of the Golden Gate Bridge?
<img height="200px" src="media/ggb.jpg">

    """,
    """
    <Br><br><Br>
International Orange
<img height="200px" src="media/ggb.jpg">

<font size=-3><br>
<br>
</font>
    """
    ))


BA.append(("""
<img height="200px" src="pictures/Bliss.jpg">
Where was this picture taken and what is it used for?

    """,
    """
    <Br><br><Br>
Bliss, the default Windows XP wallpaper taken in Napa county, in 1996
<font size=-3><br>


</font>
    """
    ))

BA.append(("""
<img height="200px" src="pictures/Bliss.jpg">
What is the name of this background in the Netherlands version of Microsoft office?
<font size=-3><br>


<br>Gelukzaligheid
<br>Ireland
<br>Groene Heuvel
<br>California Dreaming

</font>

    """,
    """
    <Br><br><Br>
Ireland
<font size=-3><br>
<br>
</font>
    """
    ))

BA.append(("""
<img height="200px" src="pictures/Bliss.jpg">
    If you took the picture today, what would the hills be covered with?
<font size=-3><br>
    <br>Grapevines
    <br>Houses
    <br>Sheep
    <br>Parking lot
<br>
</font>


    """,
    """
<img height="200px" src="pictures/PostBliss.jpg">
<font size=-3><br>
<br>
</font>
    """
    ))


PP.append(("""
    <Br>
What do these three school names have in common?
<br><br>Trent
<br>Queens
<br>York

    """,
    """
    <Br><br><Br>
There are the names of Universities in Canada <i>AND</i> the UK. 
<font size=-3><br>
<br>
<br>

</font>
    """
    ))

PP.append(("""
What animal is responsible for the most human deaths per year?
<br>
<br>Mosquito
<br>Shark
<br>Tse-tse Fly
<br>Killer Bunny

    """,
    """
    <Br><br><Br>
Mosquito

<font size=-3><br>
<br>
<br>

<br>


<br>
</font>
    """
    ))

PP.append(("""
What percentage of the total number of humans that ever lived on this earth is
alive right now? 
<font size=-3>
<br>0.1%
<br>1%
<br>5%
<br>10%
<br>20%
</font>

    """,
    """
    <Br><br><Br>
<font size=+3><br>
10%
<br>


<br>
</font>
    """
    ))


GS.append(("""
<font size=-1><br>
What is the fraction of microbial cells in a human body to those that contain
human DNA?<br>
<br>0.02
<br>2
<br>20
<br>200
</font>
    """,
    """
    <Br><br><Br>
    20

<font size=-3><br>
    There are more microbial cells in your body than cells that have your own
    DNA. As NPR's Robert Krulwich reported in 2006, the human body has 20
    times more microbes than cells! I guess that pretty well justifies the
    “Imperial We.”
<br>
<br>

<br>


<br>
</font>
    """
    ))

TST.append(("""
    <Br><br><Br>
What is 123 in hexidecimal form?





    """,
    """
    <Br><br><Br>
Answer: 0x7B

<font size=-3><br>
<br>
</font>
    """
    ))


TST.append(("""
What is the price of a non-fat double cappuccino refill at Strada?
<font size=-1><br>
<br>$3.90
<br>$2.75
<br>$4.25
<br>$3.25
</font>


    """,
    """
    <Br><br><Br>
Answer: $3.25
<font size=-3><br>
<br>
<br>

<br>


<br>
</font>
    """
    ))


VS.append(("""
    <Br><br>
An overflow of tears, usually caused by insufficient drainage of the tear film
from the eye.

    """,
    """
    <Br><br><Br>
Epiphora
<font size=-3><br>

(go cry about it, if you didn't get this one!)
<br>
<br>

<br>


<br>
</font>
    """
    ))

TST.append(("""
    <Br>
Double vision: name the only US President with consecutive double letters in
both his first and last name. (e.g., Harry Potter)







    """,
    """

Answer: Millard Fillmore, 13th POTUS and namesake of Fillmore Street in SF
<font size=-3><br>
<img height="200px" src="pictures/Fillmore.jpg">
<br>
</font>
    """
    ))

TST.append(("""
    <Br>
A psychosomatic illness that causes rapid heartbeat, dizziness, fainting,
confusion and even hallucinations when an individual is exposed to art...

    """,
    """Stendhal's syndrome
<font size=-3><br>
<img height="200px" src="media/Transverselline1923.jpg">
<br>
(A.K.A. hyperkulturemia, or Florence syndrome)
<br>
... usually when the art is particularly beautiful or a large amount of art is in
a single place. 
</font>
    """
    ))

TST.append(("""
    <Br><br><Br>
Rare metal used to make <br>Wonder Woman's bracelets

    """,
    """
    <Br><br><Br>
Feminum!
<font size=-3><br>
<img height="200px" src="media/metal_feminum.jpg">
<br>
<br>

<br>


<br>
</font>
    """
    ))

TST.append(("""

<font size=-3>
Former Secretary of Defense Robert McNamara attended Berkeley at
the beginning of the Great Depression and it only cost him (per semester)
<br>
A) $   26
<br>B) $   52
<br>C) $  104
<br>D) $  260
<br>E) $  520
<br>F) $ 1040
</font>
    """,
    """
    <Br><br><Br>

    $52!!!
<font size=-3><br>
<br>
<br>

<br>


<br>
</font>
    """
    ))

TST.append(("""
<font size=-3>
<br>
    This CIA run program ran from 1953-1973 and included experiments
    involving administration of LSD surreptitiously to, among others,
    unwitting members of the general public, some of whom were lured into
    would-be brothels in San
    Francisco.

</font>
    """,
    """
    <Br><br><Br>
MK-ULTRA.

<font size=-3><br>
From the "can't make this stuff up" department, the SF-based research
involving brothels was called "Operation Midnight Climax".
<br>
<br>

    bonus Berkeley connection:
<br>
Ted "The Unabomber" Kaczynski was a test subject for MK-ULTRA during his days
at Harvard.


<br>
</font>
    """
    ))


TST.append(("""
    <Br><br><Br>
    Name the James Bond movies with "eye" in the titles...
    """,
    """
<img height="50%" src="media/for-your-eyes-only.jpeg">
<img height="200px" src="media/ge.jpg">

<font size=-3><br>
</font>
    """
   
    """<Br>
bonus puns:
<br>"D<i>ie</i>monds Are Forever" 
<br>"Live and Let D<i>ie</i>"                                                                                          
<br>"Tomorrow Never D<i>ie</i>s" 
<br>"D<i>ie</i> Another Day" 
<br>"Sk<i>y</i>fall"   
<font size=-3><br>

<br>
</font>
"""
    ))

VS.append(("""
    <Br><br><Br>
The average number of times that the eye blinks per day is:<br>
<br>

115,000<br>
11,500<br>
1,500<br>
150<br>
    """,
    """
    <Br><br><Br>
11,500
<font size=-3><br>

<br>
</font>
    """))
VS.append(("""
    <Br><br><Br>
    Whose seminal work coined the term "Physiological Optics", which was also
    the name of the degree that was the precursor to the "Vision Science"
    degree? 

    """,
    """
Hermann von Helmholtz
    <Br><br><Br>
<font size=-2><br>
"Treatise on Physiological Optics", contained everything known about vision at the time. Published in German in 1896 and translated to English in 1924. 
<br>
</font>
    """))

VS.append(("""
    <Br><br><Br>
What time is it on Will Tuten’s clock in the Viral Sensation Vision Science
video?

    """,
    """
    <Br>
11:02
<font size=-3><br>
<img height="200px" src="pictures/TutenClock.jpg">
<br>
</font>
    """
    ))

VS.append(("""
    <Br><br><Br>

<font size=-3><br>
When centered on the fovea, a disk XX degrees in diameter will encompass roughly 47 percent of all cone photoreceptors in the human retina.
<br>A) 5
<br>B) 15
<br>C) 35
<br>D) 75

</font>


    """,
    """
    <Br><br><Br>
Answer: D, see Figure 8 in Curcio et al, 1990
<img src="pictures/47Percent.jpg">

<br>
</font>
    """
    ))


VS.append(("""
    <Br>

Name  five current VS faculty who used to work at the University of Houston College of Optometry

    """,
    """
    <Br>
<br>Gerald Westheimer
<br>Stan Klein
<br>Dennis Levi
<br>Austin Roorda
<br>Susana Chung
<font size=-3><br>
<br>
</font>
    """
    ))


VS.append(("""
    <Br><br><Br>

    Helmholtz is the inventor of what instrument widely used in optometry?

    """,
    """
    <Br><br><Br>
    Direct Opthalmascope
    <br><Br>
<font size=-3><br>
invented in 1851
<br>
<img src="media/opthamlascope.png">
<img src="media/helmholtz.png"><br>
</font>
    """))

VS.append(("""
    <Br><br><Br>
    What Year did the Berkeley Vision Science* program start?
<br><br>
<font size=-3><br>
* The degree was called Physiological Optics at that time
</font>
    """,
    """
    <Br><br><Br>
    1946
<font size=-3><br>

<br>
</font>
    """))
VS.pop()

VS.append(("""
    <Br><br><Br>
Where will the ARVO annual meeting be held in the next four years? 


    """,
    """
    <Br><br><Br>
Seattle (2013), Orlando (2014), Denver (2015), Seattle (2016)

<font size=-3><br>
<br>
</font>
    """
    ))


VS.append(("""
    <Br><br><Br>
Name the former Berkeley Vision Science Professor who was the great grandson of Charles Darwin

    """,
    """
    <Br><br><Br>
    Horace Barlow
<font size=-3><br>

<br>
<img src="media/barlow.png">
</font>
    """))
VS.append(("""
<br>
What is the pixels per degree of the IPad4 ‘retina display’ when held at 38 cm viewing distance?
<font size=-3><br>
Hint: screen resolution is 105 pix/cm
</font>


    """,
    """
    <Br><br><Br>
 69.5

<br>
    """
    ))


VS.append(("""
What interesting ocular feature makes one of these animals different from the
rest<br>

<font size=-3>
<br>Human
<br>Ostrich
<br>Whale
<br>Tiger
</font>
    """,
    """
    <Br><br><Br>
    The Ostritch
<font size=-3><br>
It's the only animal on the list whose eyeballs are bigger than its brain

<br>
</font>
    """))

VS.pop()

VS.append(("""
<font size=-3><br>
Known for their role in regulating the body’s circadian rhythm, these cells make up about “1 percent” of the total number of ganglion cells in the retina.
<br>

<img height="200px" src="pictures/1Percent.jpg">


<br>
</font>
    """,
    """
<img height="200px" src="pictures/1Percent.jpg">
<br>



Intrinsically photosensitive retinal ganglion cells 
<br>
<font size=-3><br>
(ipRGCs, AKA melanopsin-containing ganglion cells)


<br>
</font>
    """
    ))



VS.append(("""
    <Br><br><Br>
Which nonextinct animal has the largest eyeballs?
    """,
    """
<font size=-3><br>

<br>
<img src="media/squid.png">
</font>
    """))


VS.append(("""
    <Br><br><Br>
Where does the word "camera" come from (for photo camera)

    """,
    """
    <Br><br><Br>
    Camera Obscura - 
<font size=-3><br>

    The camera obscura <br>(Latin; "camera" is a "vaulted chamber/room" + "obscura" means "dark"= "darkened chamber/room")
<br>
</font>
    """))





VS.append(("""
    <Br><br><Br>
How many PhD graduates total (VS + Opthalmic Optics)

    """,
    """
    <Br><br><Br>
    156
<font size=-3><br>

<br>
</font>
    """))
VS.pop()


VS.append(("""
    <Br><br><Br>
Near-sighted model, Grace Robin was the first to show off what optical aid in 1930.

    """,
    """
    <Br><br><Br>
Contact lenses 
<font size=-3><br>$25 a piece<br> ($50 a pair - the equivalent of $647 in 2010) 

<br>
<img src="media/contactlenses1930.jpg">
</font>
    """))

WS.append(("""
    <Br><br><Br>

Who was the first computer programmer?
    """,
    """
    <Br><br><Br>
Ada Lovelace - Augusta Ada King, Countess of Lovelace 

<font size=-3><br>

(10 December 1815 - 27 November 1852), born Augusta Ada Byron, was an English writer chiefly known for her work on Charles Babbage's early mechanical general-purpose computer, the analytical engine. Her notes on the engine include what is recognised as the first algorithm intended to be processed by a machine; as such she is regarded as the world's first computer programmer.
<br>
</font>
    """))
VS.append(("""
    <Br><br><Br>

Name the current VS faculty who got their PhD in the Vision Science program?

    """,
    """
    <Br><br><Br>
    Ralph Freeman
<br>Gunilla Hagestrom-Portnoy
<br>Cliff Schor
<font size=-3><br>

<br>
</font>
    """))
VS.append(("""
    <br><Br>
    Luis Alvarez, UCB Professor and 1968 winner of the Nobel Prize in Physics
    "for contributions to elementary particle physics...", 
    also made a major contribution for ophthalmic instrumentation. 
    <br>
    <br>

    What was it?

    """,
    """
    <Br>
The Alvarez Lens, which was used in the Humphrey Vision Analyzer.
<font size=-3><br>

<br>
<img src="media/alvarez.png">
</font>
    """))

VS.pop()

BL.append(( 
"""
    What was recently spotted and shot by police in the Gourmet Ghetto?
    ""","Mountain Lion"))

BL.append(( """What is the price of a large Mocha Bianca at Caffe Strada?
        <br>
        </font>
<font color='white' size=-1>
<br>a) $3.25
<br>b) $2.90
<br>c) $2.75
<br>d) $4.50
""","""<br><br><br>

<table><tr align='center'><td valign='middle'>a) $3.25</td></tr></table>

"""))
BL.append(("""What does BAM/PFA stand for?""","""Berkeley Art Museum <br> Pacific Film
    Archives"""))

UC.append((
""" 

In the 1982 Big Game: Who was Stanford's Quarterback?

<font color='white' size=-2>
<table>
<tr>
<td>
<ol>
<li>John Elway
<li>Joe Montana
<li>Dan Marino
<li>Archie Manning
</ol>
</td>
<td>
<br><img src="media/theplay.png"><br>
</td>
</tr>
</table>
</font>
""",
""" 
John Elway
<br>
<br>
<font color='white' size=-1>
Went on to be a Hall of Fame Quarterback for the Denver Broncos
<br>
<img src="media/elway1.png">
<img src="media/elway2.png">
</font>


"""))

"""What is the oldest building on the Berkeley Campus?
<br>
<ol>
<li>South Hall
<li>The Campanile
<li>Senior Mens Hall (the log cabin)
<li>Hearst Mining Building
</ol>
"""

UC.append(("""
Which building in this picture is still standing, and what is its name? 
    
<img src="pictures/SouthHall.jpg">
    ""","""
    South Hall
    <br>

<img src="media/southhall.png">
<br>
<font color='white' size=-2>
Built in 1873, South Hall is one of the few original buildings still standing
on the Berkeley campus 
<br>
    """))

"""<table>
<tr>
<td>
<center>
<img src="media/seniorhall.png">
<br>
Senior Hall<br> 1906
</center>
</td>
<td>
<center>
<img width=100 src="media/hearsmining.png">
<br>
Hearst Mining<br> 1907
</center>
</td>
<td>
<center>
<img width=100% height=100% src="media/campanilesmall.png">
<br>
Capanile<br>1914
</center>
</td>
</tr>
</table>
</font>
"""
UC.append(("""
        Who does the UC Basketball player with the biggest feet give his shoes
        to every year?

        """,
        """
        OSKI Bear, Cal mascot
        <br><br>

    <img src="media/oski.png"> <br>
        """
        ))

UC.append(("""<br><br>
    Who was the highest paid UC Employee in 2009, and estimate his/her salary
    to within $500,000?

    """
    ,
    """
    $2,338,409.39 <br><br>

    Jeff Tedford <br><br>
    UC Berkeley FOOTBALL COACH

    """
    ))

UC.pop() # exclude question
UC.append(("""
     <font size=-2>Which of these characters was never a regular on the Berkeley Campus?
     </font>

     <table>
     <tr>
     <td>
     <center>
    <img src="pictures/HappyHappyHappyGuy.jpg"> <br>
    </center>
    </td>
    <td>
     <center>
    <img src="pictures/HateMan.jpg"> <br>
    </center>
    </td>
    </tr>
    <tr>
    <td>
     <center>
    <img src="pictures/OneManBandGuy.jpg"> <br>
    </center>
    </td>
    <td>
    <center>
    <img src="pictures/Yoshua.jpg"> <br>
    </center>
    </td>
    </tr>
    </table>
     
    """,

    """
    <br>One Man Band Guy:
        is often seen on Harvard Campus<br>
    <img src="pictures/OneManBandGuy.jpg"> <br>

    """
    ))
UC.append(("""
    <Br>
 What two Berkeley students (one graduated in 2005, one signed in 2012)
together have 17 olympic medals to their credit?

    """,
    """
    <Br><br><Br>
Answer: Natalie Coughlin (12) and Missy Franklin (5)
<font size=-3><br>
<br>
</font>
    """
    ))

UC.append(("""
    <Br><br><Br>
What was Cal Football’s overall win-loss record in 2012?

    """,
    """
    <Br><br><Br>
    3-9

<font size=-3><br>
<br>
</font>
    """
    ))

UC.append(("""

Which one of these do not belong to this list (and why)?
<font size=-3><br>
<br>Julia Morgan
<br>Bernard Maybeck
<br>John Galen Howard
<br>William Wurster
<br>Frank Gehry
</font>

    """,
    """
    <Br><br><Br>
Gehry is the only architect who did not design a building on UC Berkeley Campus

    """
    ))


UC.append(("""
    <Br><br><Br>

Name the last three Berkeley Nobel Laureates

    """,
    """
<font size=-3><br>
<br>2011 - Saul Perlmutter (Physics) 
<br>2009 - Oliver E. Williamson (Economics) 
<br>2006 - George F. Smoot (Physics)

<br>
</font>
    """
    ))

UC.append(("""
    How tall is the Sather Tower, aka the Campanile, and how does it rank among
    other bell towers in the world?
 <font size=-3>
<ol>
<li>507 ft; #1
<li>450 ft; #5
<li>309 ft; #3
<li>298 ft; #2
</ol>
 </font>
    """,
    """
<table>
<tr>
<td>
<img width=500% height=800% src="media/campanilesmall.png">
</td>
<td>
<br><br>
<font size=-3><br>
Sather tower<br>
Designed by John Galen Howard<br>
309 ft<br>
3rd tallest bell tower in the world<br>
</font><br>
</td>
</tr>
</table>
    """
    ))


UC.append(("""
    <Br><br><Br>
Right before he died*"Samuel Langhorne Clemens"* better know by his pen                                                                                     name, -------------------, stipulated that  his autobiography (kept in a                                                                                    vault in Bancroft) should be published only 100 years after he died.  


    """,
    """
    <Br><br><Br>Mark                                                                                 Twain
<font size=-3><br>

<br>
</font>
    """))
UC.append(("""
    Which one on this list is NOT among the UC Berkeley Alumni?
<font color='white' size=-2>
    <ol>
    <li>Alice Waters: owner of Chez Panisse, founder of slow food movement, USA
    <li>Philip K. Dick: science fiction writer
    <li>Ted Kaczynski: a.k.a the Unabomber
    <li>Gregory Peck: Actor
    <li>Scott Adams: creator of Dilbert
    <li>Johnny Mosely: Olympic Gold Medallist Skier
    <li>Gordon Moore: founder of Intel
    <li>Timothy Leary: psychologist and advocate of psychadelic drugs
    </ol>
</font>


    """,
    """

    <font color='white' size=-1>
    Ted Kaczynski, not an alum, but a professor <br>

    
    <img src="media/unabomber.png"> <br>
    <font color='white' size=-2>

    In the fall of 1967, Kaczynski became an assistant professor of mathematics
    at the University of California, Berkeley, where he taught undergraduate
    courses in geometry and calculus. He was also noted as the youngest
    professor ever hired by the university. This position proved short-lived,
    however, as Kaczynski received numerous complaints and low ratings from the
    undergraduates he taught... Without explanation, he resigned from his
    position in 1969, at age 26. 
    </font>

    """
    ))

BA.append(("""What do these local eateries have in common?
<font color='white' size=-3>

<ol>
<li> Jojos
<li>Pizzaiolo
<li>Quince
<li>Foreign Cinema
<li>Eccolo
<li>Bakesale Betty
</ol>
</font>
""" ,"""They are all spinoffs of Chez Panisse
<br>
<img src="media/chezpanisse.png">""")
)




BL.append(( """
   Which local drinkery has the following home brews?
   </font>
   <font color='white' size=-1>
<table>
<tr><td>
    <ol>
    <li> Hefeweizen 
    <li>Pale Ale 
    <li>Sunspot Gold 
    <li>Honey Wheat 
    <li>Pilsner 
    <li>India Pale Ale 
    </ol>
</td>
<td>
<ol>
<li>Amber 
<li>Red Spot 
<li>Quasar (Double IPA) 
<li>Porter 
<li>Dry Stout 
<li>Summer Solstice 
</ol>
</td>
</tr>
</table>
   """,
"""
<img src="media/jupiterlogo.gif">
2181 Shattuck St
<img src="media/jupiterlogo.gif">
<br><br>
<img src="media/jupiterbg.jpg">

   """))
UC.append(   
 ("""
        Who is giving this speech and in what context?

    <Br><br><Br>
        <br><br>(Paul, press 'p')

   """,
   """Mario Savio
   <br><br>
  Key member of the Berkeley Free Speech Movement.  
   """,
   {112:lambda:
       subprocess.call(["mplayer","media/savio.mp4"])}
   ))


BA.append(("""
    <Br>
For a student, what's the cheapest way to get to San Francisco from campus using public transportation?

    """,
    """
    <Br><br><Br>
AC Transit  F route (free with Class-Pass sticker)
<font size=-3><br>

<br>
</font>
    """))
BA.append(( """
        Where is it considered fashionable to wait in line for 20 minutes to buy a slice of pizza and enjoy it with a hefty side of exhaust fumes?

   """,
   """
   Cheeseboard Pizza<br><br>(it's worth it)

   """
   
   ))

BA.append(("""
    <Br><br><Br>
Caffe Med is known as the birthplace of what popular coffee drink? 

    """,
    """
    <Br><br><Br>Caffe Latte
<font size=-3><br>

<br>
</font>
    """))

BA.append(("""
    <Br>

Which of these bands did not start out at 924 Gilman (which was founded in 1986 as an all-ages, non-profit, collectively organized music club)  
<br>
<br>                Green Day, 
<br>                 Rancid
<br>                 Tiger Army 
<br>                 AFI 
<br>                 Bad Religion  
    """,
    """
    <Br><br><Br>
               Bad Religion
<font size=-3><br>

<br>
</font>
    """))

WS.append(("""
    <Br><br><Br>
Which female has won two Nobel prizes?

    """,
    """
   <br><Br>
    Marie Currie
<font size=-3><br>
<br>1903 in Physics
<br>1911 in Chemistry
<br><br>Madame Curie loved Pierre,
<br>And together found elements rare,
<br>But they stood way to close,
<br>And got quite a dose,
<br>And suffered from falling of hair.
</font>
    """))

WS.append(("""
    <Br><br><Br>
Of the ten UC Campuses, how many have a woman as the chancellor?

    """,
    """
   <img src="media/img34.png"

    """))
WS.append(("""
    <Br><br><Br>
Who was an instrumental figure in discovering the structure of DNA, but did not live receive the Nobel Prize?

    """,
    """
    <Br>
Rosalind Franklin
<font size=-3><br>

Her data, according to Francis Crick, was "the data we actually used"[1] to formulate Crick and Watson's 1953 hypothesis regarding the structure of DNA.[2]
<br>
<img src="media/Rosalind_Franklin.jpg">
</font>
    """))
WS.append(("""
    <Br><br><Br>
    According to a recent report by the Washington-based Council of Graduate
    Schools, what did women receive more of then men in 2008-2009?

    """,
    """
    PhDs
<font size=-3><br>
<ul>
<li>Women received just over half of all doctorates in the 2008-2009 school year, based on data from more than 500 universities. 
<li>Not included in the report were professional degrees in law, business and medicine. 
<li>According to a new analysis of 2,000 communities in 147 out of 150 of the biggest cities in the U.S., the median full-time salaries of young women are 8% higher than those of the guys in their peer group. In two cities, Atlanta and Memphis, those women are making about 20% more. 
</ul>
<br>
</font>
    """))

UC.append(("""
    <Br><br><Br>
    Name four elements on the periodic table that were discovered by UC
    Berkeley or LBL Scientists

    """,
    """
    Berkelium<br>
    Seaborgium<br>
    Lawrencium<br>
    Californium<br>
    <Br><br><Br>
<font size=-3><br>

<br>
</font>
    """))

GS.append(("""
    <Br><br><Br>
The ratio of male:female Nobel Prize winners from inception to 2009 is:
<br>a) 36  : 1
<br>b) 18  : 1 
<br>c) 	9    : 1
<br>d) 	4 : 1
    """,
    """
    <Br><br><Br>
 b) 18.7  : 1 
<font size=-3><br>

<br>
</font>
    """))
WS.append(("""
    <Br><br><Br>
The ACM (Association for Computing Machinery) award for Outstanding Young Computer Professionals is named after whom?

    """,
    """
    <Br><br><Br>
Rear Admiral Grace Murray Hopper (December 9, 1906 - January 1, 1992) 
<font size=-3><br>
<img src="media/Grace_Hopper.jpg">
<img src="media/bug.jpg">

<br>
</font>
    """))

VS.append(("""
    <Br><br><Br>
The first Vision Science* PhD degree recipient 
<font size=-3><br>
(double points if you can tell me the year)<br><br>
* The degree was called Physiological Optics at that time
</font>
    """,
    """
    <Br><br><Br>
Elwin Marg in 1950.
   <br>
    """))
VS.pop()

VS.append(("""
Who was the first female to graduate with a VS PhD degree* from UC Berkeley? 
<font size=-3><br>
(double points if you can tell me the year)<br><br>
* The degree was called Physiological Optics at that time
</font>
    """,
    """
    <Br><br><Br>
Ellen
Takahashi
   <br>

<font size=-2>
Year: 1968<br><br>
Effects of flanking contours on visual resolution at foveal and
near-foveal loci<br>
<br>
Degree Awarded: PhD<br>
Chair: Flom
    </font>

    """))
VS.pop()

WS.append(("""
    <Br><br><Br>
Name the female astronaut who just returned from the International Space Station?
    """,
    """
    <Br><br><Br>
   Tracy Caldwell Dyson, Ph.D.
   <br>
   <br>

<font size=-2>
    Received B.S. in Chemistry from the California State University at
    Fullerton (1993) and Ph.D. in Chemistry from the University of California, Davis (1997). 
    <br>
   <br>
    <img src="media/caldwell.png">
    </font>

    """))

GS.append(("""
    <Br><br><Br>
    Who's the author of this widely repeated quote: "If I have seen
    further it is by standing on the shoulders of Giants."


    """,
    """
    <Br><br><Br>
    Isaac Newton (1642-1727)<br> 
<font size=-3><br>
in: Letter to Robert Hooke, February 5, 1675/1676
<br>
</font>
    """))


GS.append(("""
    <Br><br><Br>

-40 degrees Fahrenheit corresponds to how many degrees Celsius?

    """,
    """
    <Br><br><Br>
-40 degrees Celsius 
<font size=-3><br>
(exactly the same)
<br>
</font>
    """))

GS.append(("""
    <Br><br><Br>
What two pairs of digits satisfy the relationship <br>
XY Celsius = YX Farhenheit <br>

    """,
    """
    <Br><br><Br>

<br>16 C = 61 F
<br>28 C = 82 F
<font size=-3><br>

<br>
</font>
    """))

GS.append(("""
    <Br><br><Br>

Name the animal whose tusk, protruding from its upper jaw, can equal 75% of                                                                                 its body length. 
    """,
    """
    <Br><br><Br>Narhwal, 3 meter tusk 4 meter body.
<font size=-3><br>

<br>
</font>
    """))

GS.append(("""
    <Br><br><Br>
What is the name of the elite group of scientists which advises the United
States Government on matters of science and technology?
    """,
    """
    <Br><br><Br>
JASONS
    """))

GS.append(("""
    <Br><br><Br>
Who *really* invented the radio?

    """,
    """
    <Br><br><Br>
Nikola Tesla
<font size=-3><br>

<br>
</font>
    """))
AS.append(("""
    <Br><br><Br>
In the Back to the Future trilogy, what speed must be reached in order to activate the flux capacitor?

    """,
    """
    <Br><br><Br>
88 mph
<font size=-3><br>

<br>
<img src="media/back-to-the-future.jpg">
</font>
    """))


AS.append(("""
<br><br><br>
What major discovery by Martin Fleischmann and Stanley Pons in 1989 was met
first by enthusiasm, then skepticism when noone could replicate the results. 
    """,
    """
    <Br><br><Br>
    Cold Fusion

    """))


AS.append(("""
    <Br><br><Br>
    This 1985 film featured Val Kilmer as a slacker grad student working
    with a 15-year-old wiz-kid on Light Amplification by Stimulated Emission of Radiation.


    """,
    """
    Real Genius
<font size=-3><br>
<img src="media/real-genius-cover.jpg">
<img src="media/real-genius-poster.jpg">
</font>
    """))

AS.append(("""
    <Br><br><Br>

 What scifi movie starring Ethan Hawke and Uma Thurman, explores the ethical aspects of genetic screening?
    """,
    """
    <br><Br>
GATTACA
<font size=-3><br>

<img src="media/gattaca.jpg">
</font>
    """))
AS.append(("""
    <Br><br><Br>

In the Back to the Future trilogy, how much power is required by the flux capacitor?
    """,
    """
    <Br><br><Br>
1.21 "jiga"watts (gigawatts)
<font size=-3><br>

<br>
<img src="media/back-to-the-future-doc-marti.jpg">
</font>
    """))
AS.append(("""
<br><br><br>
What important number is encoded into this quote? 
<Br><br>

<font size=-3>
"May I have a large container of coffee?"  "Thank You"
</font>
    """,
   """
<br><br><br>
Pi 
<br><br>
<font size=-3>
   <tt>
"May I have a large container of coffee?"  "Thank You"<br>
__3__1___4__1____5______9______2___6__________5____3_
 </tt>
 </font>
    """))

AS.append(("""
    <Br><br><Br>
What is the tragus?
    """,
    """
    Targus
    <Br><br>

    The little lump of flesh in front of the ear canal.
    <Br><br>
    <img src="media/targus.png">

    """))


AS.append(("""
    <Br>
Name the source of the indisputable inverse relationship between the number
of pirates in the world and the global tempurature.  
<br><img src="media/pirates.png">
    """,
    """
    FSM
<font size=-3><br>
The Church of the Flying Spaghetti Monster
<br>
<img src="media/FSM.jpg">
</font>
    """))


AS.append(("""
    <Br><br><Br>

 What member of the band Queen completed his PhD more than 30 years after
 starting his research? 

    """,
    """
    <Br><br><Br> *Brian May
<font size=-3><br>
 astrophysicist <br>
 Thesis: "A Survey of Radial Velocities in the Zodiacal Dust Cloud" 
<br>
<img src="media/queen.png">
</font>
    """))
PP.append(("""
To what movie franchise does this refer:
"Team Jacob or Team Edward"?
    """,
    """Twilight
    <br>
    <img src="media/twilight.png">

    """))


TST.append(("""
    <Br><br><Br>
"Gentlemen, you can't fight in here! This is the War Room!" 
    Name the movie 

    """,
    """
    <Br><br><Br>
Dr. Strangelove
<font size=-3><br>

<br>
</font>
    """))

VS.append(("""
    <Br>
<font size=-3><br>
Complex and vivid hallucinations, often taking human form, are a hallmark of
what condition in patients with visual loss?<br>
</font>

<img height="200px" src="pictures/Eastwood.jpg">





    """,
    """
    <Br><br><Br>
Answer: Charles Bonnet Syndrome

    """
    ))


PP.append(("""
    Which of the following American Viticultural Areas (AVA) is not within Napa
    county? 

    <ol>
    <li>Rutherford
    <li>Napa
    <li>Oakville
    <li>Yountville
    <li>Suisun
    <li>St Helena

    </ol>
    
    """,
    """
    Suisun Valley

    <br><Br>
    is in Solano County

    """
    ))


PP.append(("""
    <Br><br><Br>
7. Mario Savio, one of the leaders of FSM, "Bodies upon the gears" speech was
plagarized by a character playing a union head in what scifi show?

    """,
    """
    <Br><br><Br>Battlestart Gallactica
<font size=-3><br>
("Lay Down Your                                                                                
Burdens, Part II")

<br>
</font>
    """))


PP.append(("""
    <Br><br><Br>
What is the third brightest object in the sky, after the sun and moon?

    """,
    """
    <Br><br><Br>
Venus.
<font size=-3><br>

<br>
</font>
    """))

PP.append(("""
    <Br><br><Br>
What current television show claims you can reconstruct image the optic nerve
    """,
    """
    <Br><br><Br>
    Fringe
<font size=-3><br>

<br>
</font>
    """))



PP.append(("""
    <Br><br><Br>

Where is this quote from, "Strange women lying in ponds distributing swords                                                                                is no basis for a system of government."? 
    """,
    """
    <Br><br><Br>Monty Python and the Holy Grail
<font size=-3><br>

<br>
</font>
    """))

BA.append(("""
    <Br><br><Br>

In the Bay Area, what has a 63% chance of occuring before 2036 - be specific?
    """,
    """
Magnitude 6.7+ earthquake
    <Br><br><Br>
<font size=-3><br>

<br>
</font>
    """))
TST.append(("""
    <Br><br><Br>
Convert the binary number 1111011 to decimal



    """,
    """
    <Br><br><Br>
Answer: 123

<font size=-3><br>
<br>
</font>
    """
    ))

TST.append(("""
What number is represented here on this Japanese Abacus?
<br><img height="200px" src="pictures/Abacus.jpg">








    """,
    """
    <Br><br><Br>

Answer: 851,531
<font size=-3><br>
<img height="200px" src="pictures/Abacus.jpg">
<br>
</font>
    """
    ))

q["Vision Science"]=VS
q["Women in Science"]=WS
q[ "General Science"]=GS
q[ "'Almost' Science"]=AS
q[ "UC Berkeley"]=UC
q[ "Berkeley Life"]=BL
q[ "Bay Area"]=BA
q[ "Potpourri!"]=PP
q[ "Potpourri!"]=TST

# the dictionary's not ordered, so we'll just rearrange how we want things here
catnames =  ["Vision Science","Women in Science", "General Science", 
         "'Almost' Science","UC Berkeley", "Berkeley Life", "Potpourri!",]

catnames =  [ 'Potpourri!' , "Bay Area", "UC Berkeley", "General Science",
"Vision Science"]
catnames.reverse()
         



questions[''] = ["no category specified"]

if __name__ == '__main__':
    #import wxevents
    pass
