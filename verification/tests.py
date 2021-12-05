"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            'input': ('aaaatctwtkdn', 'dawn'), 
            'answer': 'attackatdawn',
            'explanation': 'diameter = 4'
        },
        {
            'input': ('hdoeerlallrdow', 'world'),
            'answer': 'hellodearworld',
            'explanation': 'diameter = 3'
        },
        {
            'input': ('totetshpmeecisendysescwticsriasraytlaegphet', 'sicret'),
            'answer': None,
            'explanation': 'crib is not in plaintext'
        },
        {
            'input': ('aaaatctwtkdn', 'at'), 
            'answer': None,
            'explanation': 'more than one possible key, inconclusive'
        }
    ],
    "Extra": [
        {
            'input': ('atcadwtaktan', 'attackatdawn'), 
            'answer': 'attackatdawn'
        },
        {
            'input': ('horredwlleodla', 'world'), 
            'answer': 'hellodearworld'
        },
        {
            'input': ('mtieanetttihmoeeneaevtletenhvieensng', 'eleven'),
            'answer': 'meetmeatthestationelevenintheevening'
        },
        {
            'input': ('mheheeleeseettvvmaeeetnnaiiitonntntg', 'eleven'),
            'answer': 'meetmeatthestationelevenintheevening'
        },
        {
            'input': ('mtieeehonveenietsennmtltieaehnatvegt', 'eleven'),
            'answer': 'meetmeatthestationelevenintheevening'
        },
        {
            'input': ('mateneetaltnettvhithieenmeonegesniv', 'eleven'),
            'answer': None
        },
        {
            'input': ('mtieanetttihmoeeneaevtletenhvieensng', 'eve'),
            'answer': None
        },
        {
            'input': ('tpsyhhsspsieatcscgeyiredtseewaatniltmcteoer', 'secret'),
            'answer': 'thisisatopsecretmessageencryptedwithscytale'
        },
        {
            'input': ('solnacaeyacndcpenessyeerhsckpftosyiuisaaaftpcsenrrltktdenataehnoedtmasieogvbgenbsowriyrlsc',
                      'scytale'),
            'answer': 'scytaleisoneoftheoldestknowncryptographicdevicesusedbyancientgreeksnamelyspartansasfarasbc'
        },
        {
            'input': ('ttrscdchoearwyiptgyitssmeptaieeethlscsnesea', 'scytale'),
            'answer': 'thisisatopsecretmessageencryptedwithscytale'
        },
        {
            'input': ('seeathtsetsassesheaeshaleeptlaelptlaelnlesslnsstlstsstspssheehshleaese', 'stale'),
            'answer': None
        },
        {
            'input': ('seeathtsetsassesheaeshaleeptlaelptlaelnlesslnsstlstsstspssheehshleaese', 'sell'),
            'answer': None
        },
        {
            'input': ('seeathtsetsassesheaeshaleeptlaelptlaelnlesslnsstlstsstspssheehshleaese', 'sells'),
            'answer': 'statesshesellspleasantseashellsatsaleshehelpstestsetsseeshellsheepants'
        }
    ],
    "Long": [
        {
            'input': ('tttttttteetseeeeeeeettsstssssssssetteettttttttsettssesesesetsettesesesesstsetttttttt',
                      'testesttestset'),
            'answer': 'testesttestsettestesttestsettestesttestsettestesttestsettestesttestsettestesttestset'
        },
        {
            'input': ('ienhrnnnbteedttahfutlhsernhyiesecetsdeqhhhcusuaiehpyengiaosnghrpntceeotaeidrredmeboirissurgwf\
eotdiefaftenlecthraorhheploelecopkneiollattnnyatitdsgiadeitrnnerviatuaritpemteduhxbotuestetaanafrhiltrroonlleefssees\
qceitteuittttpephseeanhaorrrcetwssairwnooteseiffesyhdttdasaehhartvneeneeetmdddmmieicesetsgoswtysrnthsaaasriongpeocfd\
ehqyhasssuearoaaedrit', 'identity'),
            'answer': 'inthischapterwelookatanumberofciphersystemswhicharebaseduponadifferentideatothosethatwehaveme\
tsofarinthesesystemseachletterretainsitsownidentityandsothefrequenciesoftheindividuallettersofthemessagesareunchange\
dbuttheconstituentlettersofthedigraphsandthehigherorderpolygraphsareseparatedandconsequentlytheiroriginalplaintextfr\
equenciesaredestroyed'
        },
        {
            'input': ('ihatdorenivsunditceoaserhhmwltroiaenliprsrtietoicesdtulghboeteyiaafnengnpsatrtraterislaledito\
epprunyfthlwptattsaeohnheailnederrnoassmsetodeoeosekistsfexafyhstpttfseahafaetfgerrnreredaeuemesitqmnsqageubteurrdee\
iaeeaanrdcnupncoehcnhdifalicscecteehaosiotsannapttondsrhhefgteeeortehqdrsrhdeueseeebhesyttiuintshantgtrtaidthloetnih\
eyymwsverteseiicohdwh', 'its'),
            'answer': None
        },
        {
            'input': ('rhpinotisucfsuisanupfmoeolaloutpbmwlefrlstmfeiuatiuuataotwltmhorstgepsthuualoutpbmumgunrilvgr\
mrstptiolenarhseeeitcotteseoirrsvwlrlerlwiscyoeiestintnhrttnhlrhibheofalitiuioettwlrlerlinbusdeseinofmieraouyaglimaq\
nonrtnhomtrrndtoeefmadoeelpipbmnrohrpsdeopsdegimleetdtnanhntntopsefmadoesaioapceanoooinretngskag',
                      'algorithm'),
            'answer': 'roughlyspeakinganalgorithmisasequenceofinstructionsthatonemustperforminordertosolveawellformu\
latedproblemwewillspecifyproblemsintermsoftheirinputsandtheiroutputsandthealgorithmwillbethemethodoftranslatingthein\
putsintotheoutputsawellformulatedproblemisunambiguousandpreciseleavingnoroomformisinterpretation'
        },
        {
            'input': ('rltoehumegwihenlwpyiusltplsesiapnketiconitgfhayenpoarulotgbpoluretimstsahiwmneitlselarfs\
moesrqomufuetlnhaceteieordfipinrnposubttlrseuamcnitdsituohnneasimtrbhoiaugttuoponuuetsmsauansndtdpptreherecfaio\
lsrgemolireniaotvrhidmnewgrintloolrsbooeoltmvhfeeoamrwemetilhsloifdnootrfemtrurplaranetsteladatptirioonnbg',
                      'the'),
            'answer': None
        },
        {
            'input': ('tiacnibspclyrinagsyoiviistacrioeiapstrdeoreamecsbugrchesttaiswspshiecsysbsaeolicnibsswrl\
foahlscaleenhasdekodioanoatseayhvoglhdooiviishowknalowagteasyeteonwtnspeoaorrottelaeyrnaeeatiilaksaloatslerelar\
rpaooiviekobistteeautypstecatyeuesnkgttlslbaieuoseefgteanyogosanouacnibsasmirrhwhkoodanmronhsryudoionwrsascbsea\
mettlsolemelgputngteaseueeshtyscrerretftnhswrcimishierilcesra', 'psychology'),
            'answer': 'theideaofcognitivebiasinpsychologyworksinananalogouswayacognitivebiasisasystematicerrori\
nhowwethinkasopposedtoarandomerrororonethatsmerelycausedbyourignorancewhereasstatisticalbiasskewsasamplesothati\
tlesscloselyresemblesalargerpopulationcognitivebiasesskewourbeliefssothattheylessaccuratelyrepresentthefactsand\
theyskewourdecisionmakingsothatitlessreliablyachievesourgoals'
        },
        {
            'input': ('tiacnibspclyrinagsyoiviistacrioeiapstrdeoreamecsbugrchesttaiswspshiecsysbsaeolicnibsswrl\
foahlscaleenhasdekodioanoatseayhvoglhdooiviishowknalowagteasyeteonwtnspeoaorrottelaeyrnaeeatiilaksaloatslerelar\
rpaooiviekobistteeautypstecatyeuesnkgttlslbaieuoseefgteanyogosanouacnibsasmirrhwhkoodanmronhsryudoionwrsascbsea\
mettlsolemelgputngteaseueeshtyscrerretftnhswrcimishierilcesra', 'attack'),
            'answer': None
        }
    ]
}
