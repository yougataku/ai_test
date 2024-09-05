from django import forms

class SampleForm(forms.Form):
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'メールアドレスは必須です。',
            'invalid': '有効なメールアドレスを入力してください。'
        }
    )
    name = forms.CharField(
        required=True,
        max_length=100,
        error_messages={
            'required': '名前は必須です。',
            'max_length': '名前は100文字以内で入力してください。'
        }
    )