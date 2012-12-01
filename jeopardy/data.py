import subprocess
questions = {}
q =  questions

VS = []
GS = []
WS = []
AS = []
UC = []
BL = []
PP = []
TST= []

TST.append(("""
    <Br>
A psychosomatic illness that causes rapid heartbeat, dizziness, fainting,
confusion and even hallucinations when an individual is exposed to art...

    """,
    """Stendhal's syndrome, hyperkulturemia, or Florence syndrome
<font size=-3><br>
<img height="200px" src="media/Transverselline1923.jpg">
<br>

... usually when the art is particularly beautiful or a large amount of art is in
a single place. 
<br>
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

Former Secretary of Defense Robert McNamara attended Berkeley at
the beginning of the Great Depression and it only cost him (per semester)
<font size=-3><br>
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
    <Br><br><Br>

    This CIA run program ran from 1953-1973 and included experiments
    involving administration of LSD surreptitiously to, among others,
    unwitting members of the general public, some of whom were lured into
    would-be brothels in San
    Francisco.


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
Ted "The Unabomber" Kaczynski was a test subject for MK-ULTRA


<br>
</font>
    """
    ))


TST.append(("""
    <Br><br><Br>
    Name the James Bond movies with "eye" in the titles...
    """,
    """
    <Br><br><Br>
For Your Eyes Only and GoldenEye

<img height="50%" src="media/for-your-eyes-only.jpeg">
<img height="200px" src="media/ge.jpg">

<font size=-3><br>

<br>
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
    <br><Br>
What interesting ocular feature makes one of these animals different from the
rest<br>

<br>Human
<br>Ostrich
<br>Whale
<br>Tiger
    """,
    """
    <Br><br><Br>
    The Ostritch
<font size=-3><br>
It's the only animal on the list whose eyeballs are bigger than its brain

<br>
</font>
    """))
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
Which of these famous people was not an ophthalmologist?
<font size=-3><br>
<br>Sir Arthur Conan Doyle : inventor of Sherlock Holmes
<br>Thomas Young: say no more
<br>Rand Paul, Republican Senate Nominee in Kentucky
<br>Roberta Bondar, Astronaut
<br>Socrates: Brazilian Football Star
</font>
    """,
    """
    Rand Paul
    </center>
<font color='white' size=-3><br>
Over the weekend, the Courier-Journal in Louisville reported that Dr. Rand
Paul, the Republican Senate nominee in Kentucky, is not a "board-certified"
ophthalmologist according to the national clearinghouse for such
certifications. 

<br><br>Now Paul is explaining his decision to let his recognized certification lapse
as resulting from "the kind of hypocritical power play that I despise and have
always fought against."

<br><br>First some background: Paul's claim that he is a "board-certified" ophthalmologist is tied to his certification by the National Board of Ophthalmology. 

<br><br>Yet that's a group that Paul himself founded in 1999; he also serves as its head. 

<br><br>The organization that works with the American Medical Association to approve specialty boards of this nature, as the Courier-Journal notes, is called the American Board of Medical Specialties. And it does not recognize Paul's group

<br>
</font>
    <center>
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
<img src="media/someting.png">
</font>
    """))
WS.append(("""
    <Br><br><Br>
Near-sighted model, Grace Robin was the first to show off what optical aid in 1930.

    """,
    """
    <Br><br><Br>
Contact lenses 
<font size=-3><br>$25 a piece<br> ($50 a pair - the equivalent of $647 today) 

<br>
<img src="media/contactlenses1930.png">
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
<img src="media/someting.png">
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

UC.append(("""
What is the oldest building on the Berkeley Campus?
<br>
<ol>
<li>South Hall
<li>The Campanile
<li>Senior Mens Hall (the log cabin)
<li>Hearst Mining Building
</ol>
    
    ""","""
    South Hall
    <br>

<img src="media/southhall.png">
<br>
<font color='white' size=-2>
Built in 1873, South Hall is one of the few original buildings still standing
on the Berkeley campus 
<br>
<table>
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
    """))

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
UC.append(("""
     <font size=-2>Which of these characters was never a regular on the Berkeley Campus?
     </font>

     <table>
     <tr>
     <td>
     <center>
    <img src="media/stoneyburke.png"> <br>
    </center>
    </td>
    <td>
     <center>
    <img src="media/notberkeley.png"> <br>
    </center>
    </td>
    </tr>
    <tr>
    <td>
     <center>
    <img src="media/pinkguy.png"> <br>
    </center>
    </td>
    <td>
    <center>
    <img src="media/nakedguy.png"> <br>
    </center>
    </td>
    </tr>
    </table>
     
    """,

    """
    <br><br><br>
    <img src="media/notberkeley.png"> <br>

    """
    ))

UC.append(("""
    How tall is the Sather Tower, aka the Campanile, and how does it rank among
    other bell towers in the world?

<ol>
<li>507 ft; #1
<li>450 ft; #5
<li>307 ft; #3
<li>298 ft; #2
</ol>
    """,
    """
<table>
<tr>
<td>
<img width=500% height=800% src="media/campanilesmall.png">
</td>
<td>
<br><br>
Sather tower<br>
Designed by John Galen Howard<br>
309 ft<br>
3rd tallest bell tower in the world<br>
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
<img src="media/someting.png">
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
BL.append(("""What do these local eateries have in common?
<font color='white' size=-1>
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


BL.append(("""
    <Br><br><Br>
For a student, what's the cheapest way to get to San Francisco from campus using public transportation?

    """,
    """
    <Br><br><Br>
AC Transit  F route (free with Class-Pass sticker)
<font size=-3><br>

<br>
<img src="media/someting.png">
</font>
    """))
BL.append(( """
        Where is it considered fashionable to wait in line for 20 minutes to buy a slice of pizza and enjoy it with a hefty side of exhaust fumes?

   """,
   """
   Cheeseboard Pizza<br><br>(it's worth it)

   """
   
   ))

BL.append(("""
    <Br><br><Br>
Caffe Med is known as the birthplace of what popular coffee drink? 

    """,
    """
    <Br><br><Br>Caffe Latte
<font size=-3><br>

<br>
</font>
    """))

BL.append(("""
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
<img src="media/someting.png">
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
<img src="media/someting.png">
</font>
    """))

WS.append(("""
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
WS.append(("""
    <Br><br><Br>
The first VS degree was awarded to Elwin Marg in 1950. Who was the first female to graduate with a VS PhD degree* from UC Berkeley? 
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

    JEOPARDY!


    """,
    """
    <Br><br><Br>
    Correct!
<font size=-3><br>
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
<img src="media/someting.png">
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
<img src="media/someting.png">
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
<img src="media/someting.png">
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
<img src="media/someting.png">
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


PP.append(("""
    <Br><br><Br>
"Gentlemen, you can't fight in here! This is the War Room!" 
    Name the movie 

    """,
    """
    <Br><br><Br>
Dr. Strangelove
<font size=-3><br>

<br>
<img src="media/someting.png">
</font>
    """))



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
<img src="media/someting.png">
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
<img src="media/someting.png">
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
<img src="media/someting.png">
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
<img src="media/someting.png">
</font>
    """))

PP.append(("""
    <Br><br><Br>

In the Bay Area, what has a 63% chance of occuring before 2036 - be specific?
    """,
    """
Magnitude 6.7+ earthquake
    <Br><br><Br>
<font size=-3><br>

<br>
<img src="media/someting.png">
</font>
    """))
q["Vision Science"]=VS
q["Women in Science"]=WS
q[ "General Science"]=GS
q[ "'Almost' Science"]=AS
q[ "UC Berkeley"]=UC
q[ "Berkeley Life"]=BL
q[ "Potpourri!"]=PP
q[ "Potpourri!"]=TST

# the dictionary's not ordered, so we'll just rearrange how we want things here
catnames =  ["Vision Science","Women in Science", "General Science", 
         "'Almost' Science","UC Berkeley", "Berkeley Life", "Potpourri!",]

catnames =  [ 'Potpourri!' ]
         



questions[''] = ["no category specified"]

if __name__ == '__main__':
    #import wxevents
    pass
