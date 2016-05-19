from system.core.model import Model

class Course(Model):
	def __init__(self):
		super(Course, self).__init__()

	def show(self):
		query = 'SELECT * FROM course ORDER BY created_at DESC'
		return self.db.query_db(query)

	def add_course(self, course_details):
		query = 'INSERT INTO course (name, description, created_at) VALUES(:name, :description, NOW())'
		data = {
			'name': course_details['name'],
			'description': course_details['description']
			}
		return self.db.query_db(query, data)

	def remove(self, id):
		query = 'SELECT * FROM course WHERE id = :id'
		data = {
			'id': id
			}
		return self.db.query_db(query, data)

	def delete(self, id):
		query = 'DELETE FROM course WHERE id = :id'
		data = {
			'id': id
			}
		return self.db.query_db(query, data)