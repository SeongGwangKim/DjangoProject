from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # AccountUpdateForm == UserCreationForm인데 초기화 이후에 username의 칸을 비활성화 시킨다.
        self.fields['username'].disabled = True
