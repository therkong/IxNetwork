from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Value(Base):
	"""The Value class encapsulates a required value node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Value property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'value'

	def __init__(self, parent):
		super(Value, self).__init__(parent)

	@property
	def Object(self):
		"""An instance of the Object class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object.Object)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.object import Object
		return Object(self)

	@property
	def Name(self):
		"""The name of the object

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	def GetMVPropertyCandidatesToSharePatternWith(self):
		"""Executes the getMVPropertyCandidatesToSharePatternWith operation on the server.

		Returns a list of MVProperties this pattern can be shared with.

		Args:
			Arg1 (str(None|/api/v1/sessions/1/ixnetwork/topology)): The method internally set Arg1 to the current href for this instance

		Returns:
			list(list[str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*]]): list of MVProperties this pattern can be shared with

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('GetMVPropertyCandidatesToSharePatternWith', payload=locals(), response_object=None)

	def GetSharedPatternCandidates(self):
		"""Executes the getSharedPatternCandidates operation on the server.

		Returns a list of shared pattern candidates.

		Args:
			Arg1 (str(None|/api/v1/sessions/1/ixnetwork/topology)): The method internally set Arg1 to the current href for this instance

		Returns:
			list(list[str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*]]): list of patterns may be shared

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		Arg1 = self.href
		return self._execute('GetSharedPatternCandidates', payload=locals(), response_object=None)
