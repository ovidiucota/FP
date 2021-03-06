from domain import *

class Controller:
	def __init__(self, person_repository, activity_repository):
		self._person_repository = person_repository
		self._activity_repository = activity_repository
	
	def add_person(self, ID, name, phone, address, activities):
		pers = Person(ID, name, phone, address, activities)
		self._person_repository.add(pers)

	def add_activity(self, ID, date, time, description):
		act = Activity(ID, date, time, description)
		self._activity_repository.add(act)

	def search_activity_of(self, activity_id, activities):
		for act in activities:
			if (act.ID == activity_id):
				return (True)
		return (False)

	def search_person(self, person_id):
		persons = self.getPersons()
		for pers in persons:
			if (person_id == pers.ID):
				return (True)
		return (False)

	def get_activity(self, activity_id):
		activities = self._activity_repository.getAll()
		for act in activities:
			if (act.ID == activity_id):
				return (act)
		return (False)

	def get_person(self, person_id):
		persons = self._person_repository.getAll()
		for pers in persons:
			if (pers.ID == person_id):
				return (pers)
		return (False)

	def getActivities(self):
		return (self._activity_repository.getAll())

	def getPersons(self):
		return (self._person_repository.getAll())

	def search_activity(self, activity_id):
		activities = self._activity_repository.getAll()
		for act in activities:
			if (act.ID == activity_id):
				return (True)
		return (False)

	def exist_activities(self):
		activities = self._activity_repository.getAll()
		if (len(activities) == 0):
			return (False)
		else:
			return (True)

	def exist_year(self, year):
		activities = self._activity_repository.getAll()
		for act in activities:
			if (act.date == year):
				return (True)
		return (False)

	def exist_persons(self):
		persons = self._person_repository.getAll()
		if (len(persons) == 0):
			return (False)
		else:
			return (True)

	def remove_activity(self, activity_id):
		self._activity_repository.remove(activity_id)
		self._person_repository.remove_person_activities(activity_id)

	def remove_person(self, person_id):
		self._person_repository.remove(person_id)

	def update_date(self, activity_id, new_date):
		self._activity_repository.update_date(activity_id, new_date)

	def update_time(self, activity_id, new_time):
		self._activity_repository.update_time(activity_id, new_time)

	def update_description(self, activity_id, new_description):
		self._activity_repository.update_description(activity_id, new_description)

	def update_name(self, person_id, new_name):
		self._person_repository.update_name(person_id, new_name)

	def update_phone(self, person_id, new_phone):
		self._person_repository.update_phone(person_id, new_phone)

	def update_address(self, person_id, new_address):
		self._person_repository.update_address(person_id, new_address)

	def update_activities(self, person_id, new_activities):
		all_activities = self.getActivities()
		self._person_repository.update_activities(person_id, new_activities, all_activities)

	def sort1(self, person_id):
			persons = self._person_repository.getAll()
			activities = []
			for pers in persons:
				if (pers.ID == person_id):
					the_person = pers
			for act in the_person.activities:
				activities.append(act)
			activities.sort(key = lambda act: act.description)
			return (activities)

	def sort2(self, person_id):
			persons = self._person_repository.getAll()
			activities = []
			for pers in persons:
				if (pers.ID == person_id):
					the_person = pers
			for act in the_person.activities:
				activities.append(act)
			activities.sort(key = lambda act: act.date)
			return (activities)

	def sort3(self, date1, date2):
		persons = self._person_repository.getAll()
		new_persons = []
		for pers in persons:
			ok = 0
			for act in pers.activities:
				if (act.date <= date2 and act.date >= date1):
					ok = 1
			if (ok):
				new_persons.append(pers.name)
		return (new_persons)

	def sort4(self, date):
		copy_activities = []
		activities = self._activity_repository.getAll()
		for act in activities:
			if (act.date == date):
				copy_activities.append(act)
		copy_activities.sort(key = lambda act: act.description)
		return (copy_activities)

	def undo(self):
		self._person_repository.undo()
		self._activity_repository.undo()
