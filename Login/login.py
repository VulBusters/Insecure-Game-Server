import azure.functions as func
from PlayFabUtil.authen import AUTHEN
from HttpMessageHandling import request_validation, response_handler

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    json_data, kid = request_validation.validate_encrypted_params(req, context)
    request_validation.validate_decrypted_params(json_data.items())
    email = json_data.get('Email')
    passwd = json_data.get('Password')
    playfab_auth_req = {
        'Email': email,
        'Password': passwd
    }
    playfab_auth = AUTHEN()
    playfab_auth.login_with_email(playfab_auth_req)
    return response_handler.send_response(kid, playfab_auth)
