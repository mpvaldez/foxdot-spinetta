Root.default = "C"
Scale.default.set("major", tuning=Tuning.ET12)
Clock.bpm = 110

dur_riff_bass1 = [1/2]*4 + [1] + [1/2]*2
dur_riff_bass2 = [4]*2 +[2]*4 + [6]
dur_riff = [1/2]*4 + [1]*2 + [1/2]*4 + [3/4]*2 + [1/2]
melo_riff = Pattern([_,0,2,0,-1,1]*2 + [4])
melo_riff_bass1 = Pattern([[5,_],5,7,5,2,4,5])
melo_riff_bass2 = Pattern([3,4,0,2,5,8,11])
melo_acom = Pattern([3,4,0,2,5,8,11])

## Momento 1

p1 >> play("-{[-][----]}", amp=0.2, sample=6)

bass1 = jbass(melo_riff_bass1, amp=[0.2, 0.1], dur=dur_riff_bass1, oct=4, vib=4) 
b1 >> bass1
p2 >> play("pS", amp=0.1)
p3 >> play("S", dur=1)


## Momento 2
bass2 = sawbass(melo_riff_bass1, amp=[0.6, 0.3], dur=dur_riff_bass1, slidedelay=250, oct=5)
b2 >> bass2
p4 >> play("X-( o)-{ o}({-[----][--]})( o)(-[-o])", amp=0.4, sample=2)
b1.amp = 0.08
p2.amp = 0.2
p3.stop()

    
## Momento 3
p4.stop(1)
p5 >> play("OI", amp=[0.7,0.5], sample=5)
p1.amp=0.3
b1.stop(1)
b2.stop(1)
b3 >> jbass(melo_riff_bass2, amp=[0.4, 0.2], dur=dur_riff_bass2, oct=4, vib=4)
b4 >> sawbass(melo_riff_bass2, amp=[0.6, 0.3], dur=dur_riff_bass2, slidedelay=250, chop=8, room=4)
a1 >> blip(melo_acom + [0, 2, 3, 4, 7, 9], dur=1/4, amp=0.4, oct=4)
a2 >> spark(melo_acom, dur=dur_riff_bass2, amp=0.8, oct=4) + (0,4,8)
a3 >> keys(melo_acom, dur=dur_riff_bass2) + (0,4,8)
Group(a4, a5, p6, m1, m2, m3).stop()


## Momento 4

Group(a1, a2, a3, a6, q1, q2).stop()
p5 >> play("u", amp=0.6)

Group(a1, b3, b4).stop()
p6 >> play("X-O-", sample=3)
b1 >> bass1
b2 >> bass2
melo1 = marimba(melo_riff, dur=dur_riff, amp=4, oct=6)
melo2 = razz(melo_riff, dur=dur_riff, fmod=-2, oct=7)
melo3 = nylon(melo_riff, dur=dur_riff, amp=0.6, oct=4)
m1 >> melo1
m2 >> melo2
m3 >> melo3

y3 >> play("#", dur=8).stop(3) 

Group(m1, m2, m3, m4).stop()

melo4 = sitar(melo_riff, dur=dur_riff, amp=0.8, fmod=2, oct=6)
m4 >> melo4


## Momento 5
Group(a1, a2, a3).stop()

Group(b3, b4, p1, p2, p3, p4, p5, m1, m2, m3, m4).stop()
b1 >> bass1
b2 >> bass2
p6 >> play("Xr( oP)-{lot}{kmNv}{pano}(-[-o])", amp=0.4, sample=3)
y1 >> play("S", dur=1)
y2 >> play("E", sample=1, dur=8).stop(3)
y3 >> play("E", sample=0, amp=0.4, dur=8).stop(3)
a4 >> marimba(P[7,6,5,4,5,5,6,6].stutter(12), amp=1.5, dur=1/6)
a5 >> marimba(P[7,6,5,4,5,5,6,6].stutter(12), amp=1.5, dur=1/6, oct=4)

## Momento 6
Group(a1, a2, a3, b3, b4, p1, p2, p3, p4, p5, m1, m2, m3, m4).stop()
q1 >> play("{m|m1||m2||m3||m4||m5||m6|pano}", dur=[1/4, 1/2])
q2 >> play("{#|#1||#2||#3|E|E1||E2|}", dur=1/2)
y4 >> play("U", sample=2, dur=8).stop(3)
a6 >> prophet(melo_acom, dur=4, amp=0.8, oct=5) + (0,2,4)


Group(m1, m2, m3, m4).solo()

# En esta obra condenso varias de mis pasiones y habitus
# 	Mas que programacion, la algoritmia euclideana
# 	Mi amor por la musica que no se reconoce en la valorizacion ni en jerarquizacion de sus generos:
# 		La obra, siempre refrescante, de spinetta
# 			(En este caso, justo cuando Spinetta deja un poco de lado sus incursiones jazzeras para meterse en el tecno de la epoca y el uso de sintetizadores)
# 	La sonificacion y la creacion sonora a nivel elemental de ondas y patrones
# 	Mi pasado como dj
# 	El software siempre libre en pos del conocimiento tambien libre. Nunca con privatizaciones
# 	Mis ganas, siempre vitales, de pensar que la division establecida entre arte y ciencia no solo a veces es futil y difusa sino que tambien puede llevar a discusiones sin sentido


#c = Buffer.read(s, "/home/anopa/Documentos/FoxDot/2020-09-30 19:07:49.wav");

#c.play