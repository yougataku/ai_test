# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        form_data = request.POST
        name = form_data.get('name', '')

        # フォームデータの処理（例：バリデーション、データベース保存など）
        data = {
            'message': f'{name},フォームが正常に送信されました！',
            'status': 'success'
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'message': '無効なリクエスト', 'status': 'error'})