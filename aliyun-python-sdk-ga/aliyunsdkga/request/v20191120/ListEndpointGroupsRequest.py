# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkga.endpoint import endpoint_data

class ListEndpointGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'ListEndpointGroups','gaplus')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_PageNumber(self):
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self,PageNumber):
		self.add_query_param('PageNumber',PageNumber)

	def get_ListenerId(self):
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self,ListenerId):
		self.add_query_param('ListenerId',ListenerId)

	def get_EndpointGroupType(self):
		return self.get_query_params().get('EndpointGroupType')

	def set_EndpointGroupType(self,EndpointGroupType):
		self.add_query_param('EndpointGroupType',EndpointGroupType)

	def get_AccessLogSwitch(self):
		return self.get_query_params().get('AccessLogSwitch')

	def set_AccessLogSwitch(self,AccessLogSwitch):
		self.add_query_param('AccessLogSwitch',AccessLogSwitch)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_AcceleratorId(self):
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self,AcceleratorId):
		self.add_query_param('AcceleratorId',AcceleratorId)

	def get_EndpointGroupId(self):
		return self.get_query_params().get('EndpointGroupId')

	def set_EndpointGroupId(self,EndpointGroupId):
		self.add_query_param('EndpointGroupId',EndpointGroupId)