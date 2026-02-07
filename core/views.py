import json

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import RegistrationForm
import random

from .models import AdderGame, AdderQuestion, WordleGame, WordleGuess

WORDLE_ANSWERS = [
    "about","above","abuse","actor","acute","admit","adopt","adult","after","again",
    "agent","agree","ahead","alarm","album","alert","alien","align","alive","alley",
    "allow","alone","along","alter","among","angel","anger","angle","angry","anime",
    "ankle","annex","apart","apple","apply","arena","argue","arise","armor","array",
    "arrow","aside","asset","atlas","attic","audio","audit","avoid","awake","award",
    "aware","awful","bacon","badge","badly","bagel","baker","bases","basic","basin",
    "basis","batch","beach","beard","beast","begun","being","belly","below","bench",
    "berry","bible","birth","black","blade","blame","bland","blank","blast","blaze",
    "bleed","blend","bless","blind","blink","bliss","block","blood","bloom","blown",
    "blues","bluff","blunt","board","boast","bonus","boost","booth","bound","bowel",
    "boxer","brain","brand","brave","bread","break","breed","brick","bride","brief",
    "bring","broad","broke","brook","brown","brush","buddy","build","built","bunch",
    "burst","buyer","cabin","cable","camel","candy","cargo","carry","catch","cater",
    "cause","cedar","chain","chair","chalk","chaos","charm","chart","chase","cheap",
    "check","cheek","cheer","chess","chest","chief","child","china","chunk","churn",
    "civic","civil","claim","clash","class","clean","clear","clerk","click","cliff",
    "climb","cling","clock","clone","close","cloth","cloud","clown","coach","coast",
    "cobra","cocoa","color","comet","comic","coral","corps","couch","could","count",
    "court","cover","crack","craft","crane","crash","crazy","cream","crest","crime",
    "crisp","cross","crowd","crown","cruel","crush","curve","cycle","daily","dance",
    "datum","dealt","death","debug","debut","decal","decay","decor","decoy","delay",
    "delta","demon","dense","depot","depth","derby","deter","detox","devil","diary",
    "dirty","disco","ditch","dodge","donor","doubt","dough","draft","drain","drake",
    "drama","drank","drape","drawn","dread","dream","dress","dried","drift","drill",
    "drink","drive","droit","drone","drove","drown","drugs","drums","drunk","dryer",
    "dummy","dusty","dwarf","dwell","dying","eager","eagle","early","earth","easel",
    "eat","eight","elect","elite","embed","ember","emoji","empty","ended","enemy",
    "enjoy","enter","entry","equal","equip","error","essay","ethic","event","every",
    "evoke","exact","exams","excel","exile","exist","extra","fable","facet","facto",
    "faint","fairy","faith","fancy","fatal","fatty","fault","feast","fence","ferry",
    "fetch","fever","fiber","field","fiery","fifth","fifty","fight","filed","final",
    "first","fixed","flags","flame","flash","flask","flesh","flies","flies","float",
    "flock","flood","floor","flora","flour","fluid","flush","flute","focal","focus",
    "folly","force","forge","forth","forum","found","foxes","frame","frank","fraud",
    "fresh","front","frost","froze","fruit","fully","fungi","funny","gamma","gauge",
    "genre","ghost","giant","given","glare","glass","gleam","globe","gloom","glory",
    "gloss","glove","gonna","grace","grade","grain","grand","grant","grape","graph",
    "grasp","grass","grave","great","greed","green","greet","grief","grill","grind",
    "groan","groom","gross","group","grove","grown","guard","guess","guest","guide",
    "guild","guilt","guise","guitar","habit","handy","happy","harsh","haste","hasn",
    "haven","heads","heart","heavy","hedge","hefty","hello","hence","herbs","honey",
    "honor","hoped","horse","hotel","house","hover","human","humor","humid","hurry",
    "hyper","ideal","image","imply","inbox","index","indie","inner","input","intro",
    "ionic","irony","ivory","jewel","joker","jolly","judge","juice","juicy","jumbo",
    "jumps","jury","karma","kayak","keeps","khaki","kills","knack","kneel","knelt",
    "knife","knock","known","label","labor","lance","large","laser","latch","later",
    "laugh","layer","leads","lease","least","leave","legal","lemon","level","lever",
    "light","liked","limit","linen","liner","liter","lived","liven","liver","local",
    "lodge","logic","logo","lonely","loose","lords","lorry","lotus","lover","lower",
    "loyal","lucid","lucky","lunar","lunch","lying","lyric","macro","magic","major",
    "maker","manga","manor","maple","march","marry","marsh","mason","match","mayor",
    "meaty","medal","media","meets","melon","mercy","merge","merit","merry","messy",
    "metal","meter","midst","might","mills","miner","minor","minus","mirth","mixed",
    "model","modem","mogul","moist","money","month","moral","motif","motor","motto",
    "mound","mount","mourn","mouse","mouth","moved","mover","movie","muddy","multi",
    "mural","music","naive","named","nasty","naval","nerve","never","newly","niche",
    "night","noble","noise","north","notch","noted","novel","nurse","nylon","occur",
    "ocean","oddly","offer","often","olive","omega","onset","opera","opted","orbit",
    "order","organ","other","ought","outer","owned","owner","oxide","ozone","paced",
    "paint","panic","paper","parts","party","pasta","paste","patch","pause","peace",
    "peach","pearl","pedal","penny","perch","peril","phase","phone","photo","piano",
    "piece","pilot","pinch","pitch","pixel","pizza","place","plain","plane","plant",
    "plate","plead","pleas","pluck","plumb","plume","plump","plunge","point","polar",
    "polls","pooch","poppy","porch","poser","posit","pound","power","press","price",
    "pride","prime","prince","print","prior","prize","probe","prone","proof","prose",
    "proud","prove","proxy","psalm","pulse","pumps","punch","pupil","puppy","purse",
    "qualm","queen","query","quest","queue","quick","quiet","quirk","quota","quote",
    "rabbi","radar","radio","raids","rails","rainy","raise","rally","ranch","range",
    "rapid","ratio","raven","reach","reads","ready","realm","rebel","recap","refer",
    "reign","relax","relay","renal","renew","repay","reply","resin","retro","rider",
    "ridge","rifle","right","rigid","risky","rival","river","roads","robin","robot",
    "rocky","rogue","roots","rouge","rough","round","route","rover","royal","rugby",
    "ruler","rural","sadly","saint","salad","salon","salsa","sauce","saved","scale",
    "scare","scene","scent","scope","score","scout","scrap","screw","sedan","seize",
    "sense","serve","seven","shade","shaft","shake","shall","shame","shape","share",
    "shark","sharp","shear","sheep","sheer","sheet","shelf","shell","shift","shine",
    "shirt","shock","shoot","shore","short","shout","shown","sided","siege","sight",
    "sigma","since","sixth","sixty","sized","skill","skull","slate","slave","sleep",
    "slice","slide","slope","smart","smell","smile","smoke","snack","snake","solar",
    "solid","solve","sorry","south","space","spare","spark","spawn","speak","spear",
    "spell","spend","spent","spice","spill","spine","spite","split","spoke","spoon",
    "sport","spray","squad","stack","staff","stage","stain","stake","stall","stamp",
    "stand","stark","start","state","stays","steak","steal","steam","steel","steep",
    "steer","steps","stick","stiff","still","stock","stole","stone","stood","store",
    "storm","story","stout","stove","strap","straw","stray","strip","stuck","study",
    "stuff","style","sugar","suite","sunny","super","surge","swamp","swear","sweat",
    "sweep","sweet","swept","swift","swing","swirl","sword","swore","sworn","stuck",
    "syrup","table","taken","taste","taxes","teach","teeth","tempo","tense","tenth",
    "terms","theft","theme","thick","thief","thing","think","third","thorn","those",
    "three","threw","throw","thumb","tiger","tight","timer","tired","title","today",
    "token","topic","torch","total","touch","tough","towel","tower","toxic","trace",
    "track","trade","trail","train","trait","treat","trend","trial","tribe","trick",
    "tried","troop","truck","truly","trump","trunk","trust","truth","tumor","tuned",
    "tuner","turbo","tutor","twice","twist","tying","ultra","uncle","under","undue",
    "union","unity","until","upper","upset","urban","usage","usher","using","usual",
    "utter","vague","valid","value","valve","vapor","vault","venue","verge","verse",
    "video","vigor","vinyl","viola","viral","virus","visit","vista","vital","vivid",
    "vocal","vodka","voice","voter","vowel","vulgar","wages","wagon","waist","waste",
    "watch","water","waves","wears","weary","weave","wedge","weigh","weird","whale",
    "wheat","wheel","where","which","while","white","whole","whose","widen","widow",
    "width","wield","witch","woman","women","world","worry","worse","worst","worth",
    "would","wound","wrath","wrist","wrote","yacht","yield","young","youth","zebra",
]


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def level2(request):
    return render(request, 'level2.html')


@login_required
def towers(request):
    return render(request, 'towers.html')


@login_required
def adder(request):
    return render(request, 'adder.html')


@login_required
@require_POST
def adder_save(request):
    data = json.loads(request.body)
    game = AdderGame.objects.create(
        user=request.user,
        score=data['score'],
        total=data['total'],
    )
    for q in data['questions']:
        AdderQuestion.objects.create(
            game=game,
            num1=q['num1'],
            num2=q['num2'],
            user_answer=q['user_answer'],
            correct=q['correct'],
        )
    return JsonResponse({'status': 'ok', 'game_id': game.id})


@login_required
def adder_history(request):
    games = AdderGame.objects.filter(user=request.user).order_by('-played_at')
    return render(request, 'adder_history.html', {'games': games})


@login_required
def account_settings(request):
    return render(request, 'account_settings.html')


@login_required
def wordle(request):
    return render(request, 'wordle.html')


@login_required
def wordle_word(request):
    word = random.choice(WORDLE_ANSWERS)
    return JsonResponse({'word': word})


@login_required
@require_POST
def wordle_save(request):
    data = json.loads(request.body)
    game = WordleGame.objects.create(
        user=request.user,
        word=data['word'],
        won=data['won'],
        attempts=data['attempts'],
    )
    for g in data['guesses']:
        WordleGuess.objects.create(
            game=game,
            guess_number=g['guess_number'],
            word=g['word'],
        )
    return JsonResponse({'status': 'ok', 'game_id': game.id})


@login_required
def wordle_history(request):
    games = WordleGame.objects.filter(user=request.user).order_by('-played_at').prefetch_related('guesses')
    return render(request, 'wordle_history.html', {'games': games})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
