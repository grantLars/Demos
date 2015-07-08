from fabric.api import local, lcd
#to be added to
def prepare_deployment(branch_name):
	local('python manage.py test django_project')
	local('git add -p && git commit')

def deploy():
	with lcd('/home/grant/Demos-git/django_project')
	#not done