class LoginPage:
    def __init__(self, page): #Initiate the class and expects the page object
        self.page = page
        self.username_input = page.locator("#username") #username input id="username"
        self.password_input = page.locator("#password") #password input id="password"
        self.login_button = page.locator("#submit") #submit input id="submit"

    def navigate(self, url: str): #This opens the given URL in the browser using Playwright's goto() method.
        self.page.goto(url) #This goto() method only opens the URL

    def login(self, username: str, password: str):
        self.username_input.fill(username) # Using the fill method the value of username and password are filled
        self.password_input.fill(password)
        self.login_button.click() # Using the click method the submit button is clicked.
