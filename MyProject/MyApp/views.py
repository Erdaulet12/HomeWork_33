from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.signing import Signer, TimestampSigner, BadSignature

# Create your views here.


def notify_user(request):
    messages.success(request, 'Вы успешно вошли в систему!')
    messages.warning(request, 'Внимание: проверьте свой профиль!')
    return redirect('home')


def sign_data(request):
	signer = Signer()

	signed_data = signer.sign("Секретные данные")

	try:
		original_data = signer.unsign(signed_data)
	except BadSignature:
		original_data = "Ошибка проверки подписи"

	return render(request, 'sign_data.html', {'signed_data': signed_data, 'original_data': original_data})
