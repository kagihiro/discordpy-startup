import requests

url = "https://docs.google.com/forms/d/e/1FAIpQLScwuK8YoZsGFxVOuaQPa1rawwdBhEflgwomgd1-K7Pkwn_bYA/formResponse"
# 2107036936 = u_name
# 1837347428 = t_name
# 823897192 = d_main
# 923874105 = d_sub
# 524364112 = ken
# 70018937 = bp


def to_entry_id(params_id):
    return f"entry.{params_id}"


def send_form(params):
    r = requests.get(url, params=params)
    return r
