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

class CreateIpSetsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'CreateIpSets','gaplus')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_AcceleratorId(self):
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self,AcceleratorId):
		self.add_query_param('AcceleratorId',AcceleratorId)

	def get_AccelerateRegions(self):
		return self.get_query_params().get('AccelerateRegion')

	def set_AccelerateRegions(self, AccelerateRegions):
		for depth1 in range(len(AccelerateRegions)):
			if AccelerateRegions[depth1].get('AccelerateRegionId') is not None:
				self.add_query_param('AccelerateRegion.' + str(depth1 + 1) + '.AccelerateRegionId', AccelerateRegions[depth1].get('AccelerateRegionId'))
			if AccelerateRegions[depth1].get('IpVersion') is not None:
				self.add_query_param('AccelerateRegion.' + str(depth1 + 1) + '.IpVersion', AccelerateRegions[depth1].get('IpVersion'))
			if AccelerateRegions[depth1].get('Bandwidth') is not None:
				self.add_query_param('AccelerateRegion.' + str(depth1 + 1) + '.Bandwidth', AccelerateRegions[depth1].get('Bandwidth'))