# -*- coding: utf-8 -*-


class Meta(type):
	def __init__(cls, name, bases, attrs):
		for k, v in attrs.iteritems():
			if v is not None and '_name' in k:
				pass
				# if '_name' in k and 'main' in v:
				# 	if not isinstance(v, (list, tuple)):
				# 		v = [v]
				# 		print len(v)
					# if len(v) > 1:
						# raise ValueError("Just required a main window for run the app")
					# TODO: get current main
					# print v
			if '_type' in k:
				if 'window' in v:
					print "Value", v
				elif 'form' in v:
					print "Value", v
			if '_fields' in k:
				if v:
					print cls.__name__


class BaseWindows(object):
	__metaclass__ = Meta

	_name = None
	_type = []
	_fields = []
	_center = False

	@classmethod
	def _load_class(cls):
		print "Loading class ", cls.__name__



AbstractWindows = BaseWindows

class Windows(AbstractWindows):
	pass
