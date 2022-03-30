import vk_api
import time
import forismatic


def get_quote():
    quote = f.get_Quote('ru')
    if not quote[1]:
        quote = f'"{quote[0][:-1]}"'
    else:
        quote = f'"{quote[0]}"\n/{quote[1]}/'
    return quote


def set_status():
    text = get_quote()
    vk.status.set(text=text)
    print('changed')


def dead_inside_status():
    num = 1000
    while True:
        num = 1000 if num - 7 < 0 else num - 7
        vk.status.set(text=f'{num}-7 = {num - 7}')


def quote_status():
    while True:
        set_status()
        minutes_30 = 30 * 60
        time.sleep(minutes_30)


token = 'b8d88010e41c948691b0844af7dfde48fa0d6ea2f0a67e69604d8c99fffb7377764e07014eb2f55b1adad'
vk = vk_api.VkApi(token=token).get_api()
f = forismatic.ForismaticPy()

quote_status()
# dead_inside_status()
