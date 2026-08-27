# Mi aproximación (Qatium)

Created By: Álvaro Bautista Pino
Last Edited: November 8, 2023 9:46 AM

Sobre testing, no sabría recoger todas mis opiniones o principios al respecto pero he recogido una serie de puntos que se me han ocurrido más o menos inconexos. He parado por que me podría tirar horas.

- La Calidad es responsabilidad de todos y cada uno de los miembros del equipo. El testing es una parte fundamental.
- Balance: Me gusta tener guías como la pirámide clásica o algunas
versiones más "modernas", pero de ninguna manera creo que se deban
seguir a rajatabla. Propongo siempre pensar y sopesar el valor obtenido
vs la inversión. Ante todo intento tener presente la confianza que me
aporta tener un test, independientemente de a qué nivel. Si un test no
contribuye a darme confianza me planteo borrarlo.
- Intento no plantear una estructura muy fija al principio para ir viendo qué voy necesitando.
- Siempre intento probar lo que voy a hacer con un test automático, si resulta que es muy difícil o no vale la pena el coste entonces reculo
pero lo intento. Así contengo mis peores deseos de "tira palante y ya
veremos".
- Intento hacer TDD siempre que pueda aunque hay veces que no encaja y entonces declarada y explícitamente dejo el test para luego o incluso
prescindo de él. En estos casos me dejo muy claro el riesgo asociado y
cómo y cuándo me podría morder. A veces esto me hace replantearme la
decisión.
- Invierto mucho en la forma en que escribo los tests, sobretodo
cuanto más funcionales más me gusta que se lean como un texto escrito.
También tengo en cuenta el balance aquí pues hemos de ser conscientes de que las abstracciones se pagan.
- Mi aproximación siempre es hacia testear behaviour (rollo BDD),
incluso si un componente es técnico sus pruebas las escribo por lo que
ofrece y no por cómo lo hace.
- Los tests se refactorizan y se cuidan como el resto del código.
- Las suites de tests (suite = fichero con tests o varios ficheros
agrupados y testeando lo mismo al mismo nivel) intento que sean lo más
independiente posibles, si bien llegado el momento en que hay
duplicación de concepto entonces hago por compartir artefactos
transversales (helpers, fixtures y demás) pero con mucho ojo.
- Tiendo a hacer outside-in, desde aceptación hasta unitarios. Aunque
es mi preferencia no considero que sea ni lo mejor ni lo deseable. Esto
me ayuda a enfocarme en el valor entregado y a no dejarme huecos entre
las distintas capas que pueda/quiera testear.
- No necesariamente uso mocks para que los tests vayan rápido. Sí o sí los uso para aislarme de dependencias que no puedo o es muy costoso
tener en los tests (servicios de terceros por ejemplo).
- Si la funcionalidad es muy sencilla puedo incluso dejar solo tests
de alto nivel (aceptación o integración/integrados), mientras considere
necesario, prescindiendo de tests en capas más bajas (integración,
unitarios...). Muchas veces no sabemos cómo aproximar el testeo de una
funcionalidad/módulo o componente hasta que le hemos metido varias
pasadas y entonces vemos a qué niveles testear mejor. Esto vs tener una
estructura fija e inamovible. NOTA: hago esto porque considero los tests tan cambiables como el resto del código y por supuesto atiendo y asumo
que tenemos tiempo y recursos para ir adaptándolos. Si creo que hay un
riesgo de que se queden como están si puedo proponer forzar una
estructura.
    - Muchas veces la primera versión de la suite de tests es integrada,
    por ejemplo yendo hasta la db. Por distintas razones, como que los tests van muy lentos igual introduzco algún doble de test para ese componente lento, eso sí entonces me planteo que ese component esté testeado en
    integración (si es posible) y que haya algún test que mínimamente cubra
    el desenganche que he hecho.
    - A veces esto deriva en aplicar ports&adapters si hemos visto que de forma generalizada queremos tener dobles de test para las hojas del
    árbol de dependencias (repositorios, gateways o whatever que ataca a
    otros servicios)
- Suelo hacer pruebas manuales antes de subir un cambio (cambio =
conjunto de commits a pushear). Sobretodo si afecta a nivel usuario o a
muchas partes del sistema. Aprovecho para intentar hacer pruebas
exploratorias (no soy tester/qa y no tengo muchas tablas pero algo
intento). No tanto porque no me fie de los tests automatizados si no
porque me gusta experimentar el cambio en mis propias carnes. Y sí,
también porque ya me ha explotado muchas veces no hacer pruebas manuales y por que ya he visto muchos fallos más o menos tontos por no probar
mínimamente los cambios. El ingeniero interior se suele fiar de que
hemos hecho pequeños cambios aislados y que todos encajan a la
perfección, muchas veces nos hemos dejado algo.
- Al hilo del anterior, si dispongo de un entorno "realista" (lo más
similar a producción) también pruebo algunos cambios ahí. Según
distintos criterios: partes afectadas, incertidumbre en cuanto a
dependencias reales, etc.
- Unidad != clase/función/artefacto. Si bien según la arquitectura hay artefactos que por defecto se llevan un test. Pasa por ejemplo con las
acciones (interactors de IDD...)
- TDD de manual por defecto. Si yo (y mi pareja/mob si es el caso)
estamos sueltos con lo que estamos haciendo relajamos, damos pasos más
grandes, nos saltamos el ciclo. Eso sí en el momento en que nos explota o atascamos reculamos y volvemos a un modo más riguroso.
    - De normal suelo esforzarme mucho en que el cambio no rompa nada haciendolos en paralelo y demás.
    - Estreso la independencia de los tests, si veo que al hacer un solo
    cambio se rompe muchos tests me planteo si están bien planteados los
    casos, etc.
- Tirar los tests con muchísima frecuencia, del palo cambio una línea
los tiro. Esto a mi personalmente me ayuda a no perder foco y a hacer
baby steps. Asegura que buscamos tests rápidos al hacer TDD.

Update: A todo esto añadiría que creo que no por más testear 
pre-deploy vamos a asegurar la calidad, hay que contemplar también 
pruebas en producción. Creo que no hay mejor prueba que poner una 
funcionalidad a disposición de los usuarios. Por ello a día de hoy 
prefiero explorar el favorecer feature toggles y hacer pruebas en prod 
vs entornos de pruebas o staging. Si acaso esto para otro capítulo 
futuro.