"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yy*0p-_ym9fromve=r0hsj02%o4dbja&g@mttmowx##4=@)r)('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [“thankq.pythonanywhere.com",]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

"""
django에서 template을 찾을 때 INSTALLED_APPS에 나온 경로와
(예를 들면 내가 blog등록 해놨으니깐 blog/templates를 검색), Templates dirs에서
등록해놓은 경로를 순서대로 검색함
"""

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
"""
STATICFILES_DIRS은 개발 단계에서 사용하는 정적 파일이 위치한 경로들을
지정하는 설정 항목입니다. 특정 Django App2에만 사용하는 정적 파일이
있거나 혹은 정적 파일을 관리하기 용이하게 하기 위해 여러 경로(path)에
정적 파일을 배치하였다면, 이 경로들을 Python의 list나 tuple로 담으면
됩니다.
 """
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),

)


#웹 페이지에서 사용할 정적 파일의 최상위 url 경로
# 실제 파일이나 디렉토리가 아닌 url로만 존재
STATIC_URL = '/static/'


#Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아놓는 경로
#한 곳에 모으는 기능은 collectstatic 명령어로 수행
#개발과정에선 settings.py에 Debug가 true 로 되어 있으면 작용하지 않음.
#실 서비스 환경을 위한 설정 항목.
STATIC_ROOT=os.path.join(BASE_DIR,'collected_statics')


# STATIC_URL과 같이 url 경로를 설정해주는 항목.
MEDIA_URL = '/uploads/'

# MEDIA_ROOT는 업로드가 끝난 파일을 배치할 최상위 경로를 지정하는 설정 항목
MEDIA_ROOT = os.path.join(BASE_DIR, 'static_files')
# categories setting
