from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *


def send_otp_code(phone_number, code):
	try:
		api = KavenegarAPI('74647A4D73415778346D56504B48755148326B764735672F5A596A704E69434E6273546E41787833706C303D')
		params = {
			'sender': '',
			'receptor': phone_number,
			'message': f'{code} کد تایید شما '
		}
		response = api.sms_send(params)
		print(response)
	except APIException as e:
		print(e)
	except HTTPException as e:
		print(e)


class IsAdminUserMixin(UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_authenticated and self.request.user.is_admin

