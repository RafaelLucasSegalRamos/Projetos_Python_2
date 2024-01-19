from playwright.sync_api import Playwright, sync_playwright
from time import sleep

with sync_playwright() as p:
    def escreve_URL(url):
        print(page.title())
        sleep(2)


    browser = p.chromium.launch(
        headless=False)  # O headless é para não abrir o navegador, no caso ele vem por padrão como True

    iphone = p.devices[
        'Pixel 7']  # O devices é para mudar o dispositivo que o navegador vai abrir, no caso ele vem por padrão como desktop
    # for i in p.devices:
    #     print(i)

    context = browser.new_context(
        color_scheme='dark')  # O color_scheme é para mudar o tema do navegador, no caso ele vem por padrão como light

    page = context.new_page()
    page.goto(
        "https://www.youtube.com")  # O goto é para ir para o site que você quer, no caso o youtube
    page.on("load", escreve_URL)  # O on é para executar uma função quando algo acontecer, no caso quando a URL mudar
    # page.screenshot(path="example.png", full_page=True)  # O screenshot é para tirar um print da tela
    # page.pdf(path="example.pdf")  # O pdf é para tirar um print da tela em pdf

    page.goto("https://www.google.com")
    page.fill(selector="id=APjFqb", value="Eduardo Mendes live de python #222")
    page.press(selector="id=APjFqb", key="Enter")
    sleep(5)
    # sleep(2)
    #
    # page.go_back()
    #
    # sleep(2)
    #
    # page.go_forward()

    context.close()
