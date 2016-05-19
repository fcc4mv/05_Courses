from system.core.controller import *

class Courses(Controller):
	def __init__(self, action):
		super(Courses, self).__init__(action)
		self.load_model('Course')

	def index(self):
		courses = self.models['Course'].show()
		return self.load_view('index.html', courses=courses)

	def add(self):
		course_details = {
			'name': request.form['name'],
			'description': request.form['description']
			}

		if len(request.form['name']) < 15:
			flash ("Name field cannot be empty and less than 15 characters!!!")
			return redirect('/')
		else:
			pass

		self.models['Course'].add_course(course_details)
		return redirect ('/')

	def remove(self, id):
		course=self.models['Course'].remove(id)
		return self.load_view('delete.html', course=course[0])

	def delete(self, id):
		self.models['Course'].delete(id)
		return redirect ('/')