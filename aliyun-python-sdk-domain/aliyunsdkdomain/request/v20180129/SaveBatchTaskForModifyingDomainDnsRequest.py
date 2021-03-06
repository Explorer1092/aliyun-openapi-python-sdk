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
from aliyunsdkdomain.endpoint import endpoint_data

class SaveBatchTaskForModifyingDomainDnsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Domain', '2018-01-29', 'SaveBatchTaskForModifyingDomainDns','domain')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_DomainNames(self):
		return self.get_query_params().get('DomainName')

	def set_DomainNames(self, DomainNames):
		for depth1 in range(len(DomainNames)):
			if DomainNames[depth1] is not None:
				self.add_query_param('DomainName.' + str(depth1 + 1) , DomainNames[depth1])

	def get_AliyunDns(self):
		return self.get_query_params().get('AliyunDns')

	def set_AliyunDns(self,AliyunDns):
		self.add_query_param('AliyunDns',AliyunDns)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_DomainNameServers(self):
		return self.get_query_params().get('DomainNameServer')

	def set_DomainNameServers(self, DomainNameServers):
		for depth1 in range(len(DomainNameServers)):
			if DomainNameServers[depth1] is not None:
				self.add_query_param('DomainNameServer.' + str(depth1 + 1) , DomainNameServers[depth1])

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)