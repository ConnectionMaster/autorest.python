# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class PagingOperations(object):
    """PagingOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def get_single_pages(
            self, custom_headers=None, raw=False, **operation_config):
        """A paging operation that finishes on the first call without a nextlink.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/single'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_multiple_pages(
            self, client_request_id=None, paging_get_multiple_pages_options=None, custom_headers=None, raw=False, **operation_config):
        """A paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param paging_get_multiple_pages_options: Additional parameters for
         the operation
        :type paging_get_multiple_pages_options:
         ~paging.models.PagingGetMultiplePagesOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        maxresults = None
        if paging_get_multiple_pages_options is not None:
            maxresults = paging_get_multiple_pages_options.maxresults
        timeout = None
        if paging_get_multiple_pages_options is not None:
            timeout = paging_get_multiple_pages_options.timeout

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_odata_multiple_pages(
            self, client_request_id=None, paging_get_odata_multiple_pages_options=None, custom_headers=None, raw=False, **operation_config):
        """A paging operation that includes a nextLink in odata format that has 10
        pages.

        :param client_request_id:
        :type client_request_id: str
        :param paging_get_odata_multiple_pages_options: Additional parameters
         for the operation
        :type paging_get_odata_multiple_pages_options:
         ~paging.models.PagingGetOdataMultiplePagesOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged1[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        maxresults = None
        if paging_get_odata_multiple_pages_options is not None:
            maxresults = paging_get_odata_multiple_pages_options.maxresults
        timeout = None
        if paging_get_odata_multiple_pages_options is not None:
            timeout = paging_get_odata_multiple_pages_options.timeout

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple/odata'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged1(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged1(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_multiple_pages_with_offset(
            self, paging_get_multiple_pages_with_offset_options, client_request_id=None, custom_headers=None, raw=False, **operation_config):
        """A paging operation that includes a nextLink that has 10 pages.

        :param paging_get_multiple_pages_with_offset_options: Additional
         parameters for the operation
        :type paging_get_multiple_pages_with_offset_options:
         ~paging.models.PagingGetMultiplePagesWithOffsetOptions
        :param client_request_id:
        :type client_request_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        maxresults = None
        if paging_get_multiple_pages_with_offset_options is not None:
            maxresults = paging_get_multiple_pages_with_offset_options.maxresults
        offset = None
        if paging_get_multiple_pages_with_offset_options is not None:
            offset = paging_get_multiple_pages_with_offset_options.offset
        timeout = None
        if paging_get_multiple_pages_with_offset_options is not None:
            timeout = paging_get_multiple_pages_with_offset_options.timeout

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple/withpath/{offset}'
                path_format_arguments = {
                    'offset': self._serialize.url("offset", offset, 'int')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if client_request_id is not None:
                header_parameters['client-request-id'] = self._serialize.header("client_request_id", client_request_id, 'str')
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if maxresults is not None:
                header_parameters['maxresults'] = self._serialize.header("maxresults", maxresults, 'int')
            if timeout is not None:
                header_parameters['timeout'] = self._serialize.header("timeout", timeout, 'int')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_multiple_pages_retry_first(
            self, custom_headers=None, raw=False, **operation_config):
        """A paging operation that fails on the first call with 500 and then
        retries and then get a response including a nextLink that has 10 pages.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple/retryfirst'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_multiple_pages_retry_second(
            self, custom_headers=None, raw=False, **operation_config):
        """A paging operation that includes a nextLink that has 10 pages, of which
        the 2nd call fails first with 500. The client should retry and finish
        all 10 pages eventually.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple/retrysecond'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_single_pages_failure(
            self, custom_headers=None, raw=False, **operation_config):
        """A paging operation that receives a 400 on the first call.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/single/failure'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_multiple_pages_failure(
            self, custom_headers=None, raw=False, **operation_config):
        """A paging operation that receives a 400 on the second call.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple/failure'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_multiple_pages_failure_uri(
            self, custom_headers=None, raw=False, **operation_config):
        """A paging operation that receives an invalid nextLink.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple/failureuri'

                # Construct parameters
                query_parameters = {}

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_multiple_pages_fragment_next_link(
            self, api_version, tenant, custom_headers=None, raw=False, **operation_config):
        """A paging operation that doesn't return a full URL, just a fragment.

        :param api_version: Sets the api version to use.
        :type api_version: str
        :param tenant: Sets the tenant to use.
        :type tenant: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged1[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple/fragment/{tenant}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = '/paging/multiple/fragment/{tenant}/{nextLink}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str'),
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True)
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged1(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged1(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized

    def get_multiple_pages_fragment_with_grouping_next_link(
            self, custom_parameter_group, custom_headers=None, raw=False, **operation_config):
        """A paging operation that doesn't return a full URL, just a fragment with
        parameters grouped.

        :param custom_parameter_group: Additional parameters for the operation
        :type custom_parameter_group: ~paging.models.CustomParameterGroup
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Product
        :rtype: ~paging.models.ProductPaged1[~paging.models.Product]
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        api_version = None
        if custom_parameter_group is not None:
            api_version = custom_parameter_group.api_version
        tenant = None
        if custom_parameter_group is not None:
            tenant = custom_parameter_group.tenant

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = '/paging/multiple/fragmentwithgrouping/{tenant}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = '/paging/multiple/fragmentwithgrouping/{tenant}/{nextLink}'
                path_format_arguments = {
                    'tenant': self._serialize.url("tenant", tenant, 'str'),
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True)
                }
                url = self._client.format_url(url, **path_format_arguments)
                query_parameters = {}
                query_parameters['api_version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                exp = CloudError(response)
                exp.request_id = response.headers.get('x-ms-request-id')
                raise exp

            return response

        # Deserialize response
        deserialized = models.ProductPaged1(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductPaged1(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
