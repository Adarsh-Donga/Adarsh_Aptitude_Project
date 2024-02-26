# Adarsh_Project

This projct is helpfull to get user information from the different social media account. Here, we have use Django framework to build this project. If you want to setup on your local machine please follow below steps.

>**_NOTE:_**  - Before start, You should have installed  Python and git on your machine.
---

## Clone this repository

```
git clone https://github.com/Adarsh-Donga/Adarsh_Aptitude_Project.git
```

Then, you have to clone this 3 repo in git folder.

```
git clone https://github.com/soxoj/maigret.git
```
```
git clone https://github.com/daprofiler/DaProfiler.git
```
```
git clone https://github.com/0x0be/yesitsme.git
```

## Create new virtual environment in your system
```
python -m venv path_of_env/venv_name
```

## Activate venv
- Windows 
```path_of_venv\Scripts\activate.bat```
- MAC/Ubuntu 
```source path_of_venv/bin/activate```

After that, you have to install all dependency using
```
pip install -r requirements.txt
```

## Error Solution
### 'geckodriver' is not recognized as an internal or external command, operable program or batch file OR
### ValueError: Timeout value

 - In windows platform you have to download 'geckodriver' from below link.
   - https://github.com/mozilla/geckodriver/releases
 - Then update your soundcloud.py & Wattpad_search.py with below code.

 ```
 geckodriver_path = 'path_of_geckodriver.exe'
 options = webdriver.FirefoxOptions()
 options.headless = True
 timeout_value = 10
 service = Service(geckodriver_path, connect_timeout=timeout_value) 
 driver = webdriver.Firefox(executable_path=geckodriver_path, options=options, service=service)
```


Make sure to replace placeholders like `path_of_env`, `env_name`, `YOUR_E-MAIL-ID`, `YOUR_LINKEDIN_PASS`, `YOUR_INSTA_SESSION` and `path_of_geckodriver` with the actual values.
