from bs4 import BeautifulSoup
import requests
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import DB_V3

class Login(object):
    def __init__(self, scan_name, user_name="CyberScope", password="Cy2er$cope", speed=0):
        super(Login, self).__init__()
        self.scan_name            = scan_name
        self.scan_id              = DB_V3.get_scan_id_by_name(self.scan_name)
        self.speed                = speed
        self.target               = DB_V3.get_target_by_scan_name(self.scan_name)
        self.user_name            = user_name
        self.password             = password
        self.forms                = DB_V3.get_all_forms_with_url(self.scan_id)
        self.login_form           = self.detect_login_form()
        self.method               = self.method_value(self.login_form[1])
        self.parameters           = self.extract_form_data(self.login_form[1])
        self.credentials          = dict(zip(self.parameters, [self.user_name, self.password]))
        self.action_path          = self.extract_form_action(self.login_form[1])[1]
        self.parameters_with_d_v  = self.extract_input_names_with_value(self.login_form[1])
        self.parameters_gived_d_v = self.extract_input_give_default_values(self.login_form[1])
        self.parameters_gived_d_v.update(self.parameters_with_d_v)


    def login(self):
        try:
            requests_path = self.target + self.action_path
            r = requests.post(requests_path, data=self.credentials, allow_redirects=True, timeout=15)
            if self.user_name in r.text:
                return True, r.cookies
            else:
                errorMessage = 'Login Faild!!'
                return False, errorMessage
        except Exception as e:
            errorMessage = 'Error in login function ' + str(e)
            print(errorMessage)
            return False, errorMessage

    def detect_login_form(self):
        common_login_form_names = ["loginform", "login-form", "signin-form", "signinform", "user-login", "user-login-form", "user-signin", "user-signin-form", "authentication-form", "auth-form"]
        login_action_methods = ["/login", "/user/login", "/signin", "/user/signin", "/auth/login", "/authenticate", "/user/authenticate", "/account/login", "/session/login", "/api/login", "/api/auth/login", "/login.php", "/signin.php", "/authenticate.php", "/process_login", "/user/login_process", "/do_login", "/validate_login", "/check_login", 'userinfo.php']
        try:
            for form in self.forms:
                is_name_extracted, errorMessage1 = self.extract_form_name(form[1])
                is_acrion_extracted, errorMessage2 = self.extract_form_action(form[1])
                if is_name_extracted or is_acrion_extracted:
                    if errorMessage1 in common_login_form_names or errorMessage2 in login_action_methods:
                        return (form[0],form[1])
        except Exception as e:
            errorMessage = 'Error in detect_login_form function ' + str(e)
            print(errorMessage1)
            return False

    def extract_form_data(self, form):
        soup = BeautifulSoup(form, 'html.parser')
        form_data = {}

        input_tags = soup.find_all('input', {'name': True})
        for tag in input_tags:
            name = tag.get('name')
            value = tag.get('value', '')
            if name:
                form_data[name] = value
        textarea_tags = soup.find_all('textarea', {'name': True})
        for tag in textarea_tags:
            name = tag.get('name')
            value = tag.text
            if name:
                form_data[name] = value

        select_tags = soup.find_all('select', {'name': True})
        for tag in select_tags:
            name = tag.get('name')
            selected_option = tag.find('option', {'selected': False})
            if selected_option:
                value = selected_option.get('value', selected_option.text)
                if name:
                    form_data[name] = value

        return form_data

    def extract_form_name(self, form):
        soup = BeautifulSoup(form, 'html.parser')
        form = soup.find('form')
        if form and form.get('name'):
            return True, form.get('name')
        else:
            errorMessage = "This form has no name"
            return False, errorMessage

    def extract_form_action(self, form):
        soup = BeautifulSoup(form, 'html.parser')
        form = soup.find('form')
        
        if form:
            action_value = form.get('action')
            return True, action_value
        else:
            errorMessage = 'This form has no action'
            return False, errorMessage

    def method_value(self, form):
        soup = BeautifulSoup(form, 'html.parser')
        form = soup.find('form')
        
        if form:
            method_value = form.get('method')
            return method_value
        else:
            return None

    def extract_input_names_with_value(self, form):
        soup = BeautifulSoup(form, 'html.parser')    
        input_tags = soup.find_all(['input', 'select'], {'name': True})    
        input_data = {}
        
        for tag in input_tags:
            name = tag.get('name')
            
            if tag.name == 'input':
                value = tag.get('value')
                if value:
                    input_data[name] = value if value else None
            elif tag.name == 'select':
                option = tag.find('option', selected=False)
                input_data[name] = option.get('value') if option else ''
        
        return input_data

    def extract_input_give_default_values(self, form):
        soup = BeautifulSoup(form, 'html.parser')
        
        input_tags = soup.find_all(['input', 'textarea', 'select'], {'name': True})
        
        input_values = {}
        for tag in input_tags:
            name = tag.get('name')
            tag_name = tag.name.lower()
            value = tag.get('value')
            
            if value is None or value.strip() == '':
                if tag_name == 'input':
                    input_type = tag.get('type', '').lower()
                    input_type = input_type.split()
                    if input_type == 'email' or any('email' in word for word in input_type):
                        input_values[name] = 'CyberScope@support.com'
                    elif input_type in ['tel', 'number'] or any('phone' in word for word in input_type):
                        input_values[name] = '+123456789'
                    else:
                        input_values[name] = 'CyberScope'
                elif tag_name == 'textarea':
                    input_values[name] = 'CyberScope'
                elif tag_name == 'select':
                    selected_option = tag.find('option', {'selected': False})
                    if selected_option:
                        input_values[name] = selected_option.get('value', selected_option.text)
        
        return input_values


# print(x.login_form[1])
# print(x.scan_name)