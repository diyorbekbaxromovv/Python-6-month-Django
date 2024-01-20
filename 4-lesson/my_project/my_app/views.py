from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def index(request):
    names = {
    "Murodjon":{"surname":"Tohirov", "age":26, "profession":"Mentor", "about":"И́лон Рив Маск[* 1] (англ. Elon Reeve Musk, МФА: [ˈiːlɒn 'mʌsk]; род. 28 июня 1971[1][2][…], Претория, ЮАР) — американский предприниматель, инженер[5] и миллиардер. Основатель, генеральный директор и главный инженер компании SpaceX; инвестор, генеральный директор и архитектор продукта компании Tesla; основатель The Boring Company; соучредитель Neuralink и OpenAI; владелец Twitter (X)."},
    "Diyorbek":{"surname":"Bahromov", "age":16, "profession":"Developer", "about":"William Henry Gates III (born October 28, 1955) is an American businessman, investor, philanthropist, and writer best known for co-founding the software giant Microsoft, along with his childhood friend Paul Allen. During his career at Microsoft, Gates held the positions of chairman, chief executive officer (CEO)"},
    "Javohir":{"surname":"Hoshimov", "age":19, "profession":"Teacher", "about":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book"},
    "Ikromjon":{"surname":"Odiljonov", "age":23, "profession":"Teacher", "about":"Геродо́т Галикарна́сский (др.-греч. Ἡρόδοτος Ἁλικαρνᾱσσεύς, около 484 г до н. э. — около 425 г до н. э.) — древнегреческий историк и географ[1][2], по крылатому выражению Цицерона, «отец истории» — автор первого[3][4] сохранившегося значительного трактата «История», описывающего греко-персидские войны и обычаи многих современных ему народов."},
    
    }
    return render(request, 'my_app/index.html', context={"names":names})



def main(request):
    return render(request, "my_app/main.html")