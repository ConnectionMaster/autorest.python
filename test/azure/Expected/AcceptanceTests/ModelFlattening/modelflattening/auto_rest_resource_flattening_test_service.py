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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
import uuid
from . import models


class AutoRestResourceFlatteningTestServiceConfiguration(AzureConfiguration):
    """Configuration for AutoRestResourceFlatteningTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestResourceFlatteningTestServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestresourceflatteningtestservice/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class AutoRestResourceFlatteningTestService(SDKClient):
    """Resource Flattening for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestResourceFlatteningTestServiceConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = AutoRestResourceFlatteningTestServiceConfiguration(credentials, base_url)
        super(AutoRestResourceFlatteningTestService, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def put_array(
            self, resource_array=None, custom_headers=None, raw=False, **operation_config):
        """Put External Resource as an Array.

        :param resource_array: External Resource as an Array to put
        :type resource_array: list[~modelflattening.models.Resource]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_array.metadata['url']

        # Construct parameters
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

        # Construct body
        if resource_array is not None:
            body_content = self._serialize.body(resource_array, '[Resource]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_array.metadata = {'url': '/model-flatten/array'}

    def get_array(
            self, custom_headers=None, raw=False, **operation_config):
        """Get External Resource as an Array.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~modelflattening.models.FlattenedProduct] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.get_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[FlattenedProduct]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_array.metadata = {'url': '/model-flatten/array'}

    def put_wrapped_array(
            self, resource_array=None, custom_headers=None, raw=False, **operation_config):
        """No need to have a route in Express server for this operation. Used to
        verify the type flattened is not removed if it's referenced in an
        array.

        :param resource_array: External Resource as an Array to put
        :type resource_array: list[~modelflattening.models.WrappedProduct]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_wrapped_array.metadata['url']

        # Construct parameters
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

        # Construct body
        if resource_array is not None:
            body_content = self._serialize.body(resource_array, '[WrappedProduct]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}

    def get_wrapped_array(
            self, custom_headers=None, raw=False, **operation_config):
        """No need to have a route in Express server for this operation. Used to
        verify the type flattened is not removed if it's referenced in an
        array.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~modelflattening.models.ProductWrapper] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.get_wrapped_array.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[ProductWrapper]', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_wrapped_array.metadata = {'url': '/model-flatten/wrappedarray'}

    def put_dictionary(
            self, resource_dictionary=None, custom_headers=None, raw=False, **operation_config):
        """Put External Resource as a Dictionary.

        :param resource_dictionary: External Resource as a Dictionary to put
        :type resource_dictionary: dict[str,
         ~modelflattening.models.FlattenedProduct]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_dictionary.metadata['url']

        # Construct parameters
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

        # Construct body
        if resource_dictionary is not None:
            body_content = self._serialize.body(resource_dictionary, '{FlattenedProduct}')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_dictionary.metadata = {'url': '/model-flatten/dictionary'}

    def get_dictionary(
            self, custom_headers=None, raw=False, **operation_config):
        """Get External Resource as a Dictionary.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: dict or ClientRawResponse if raw=true
        :rtype: dict[str, ~modelflattening.models.FlattenedProduct] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.get_dictionary.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('{FlattenedProduct}', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_dictionary.metadata = {'url': '/model-flatten/dictionary'}

    def put_resource_collection(
            self, resource_complex_object=None, custom_headers=None, raw=False, **operation_config):
        """Put External Resource as a ResourceCollection.

        :param resource_complex_object: External Resource as a
         ResourceCollection to put
        :type resource_complex_object:
         ~modelflattening.models.ResourceCollection
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_resource_collection.metadata['url']

        # Construct parameters
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

        # Construct body
        if resource_complex_object is not None:
            body_content = self._serialize.body(resource_complex_object, 'ResourceCollection')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}

    def get_resource_collection(
            self, custom_headers=None, raw=False, **operation_config):
        """Get External Resource as a ResourceCollection.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ResourceCollection or ClientRawResponse if raw=true
        :rtype: ~modelflattening.models.ResourceCollection or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.get_resource_collection.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ResourceCollection', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_resource_collection.metadata = {'url': '/model-flatten/resourcecollection'}

    def put_simple_product(
            self, simple_body_product=None, custom_headers=None, raw=False, **operation_config):
        """Put Simple Product with client flattening true on the model.

        :param simple_body_product: Simple body product to put
        :type simple_body_product: ~modelflattening.models.SimpleProduct
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SimpleProduct or ClientRawResponse if raw=true
        :rtype: ~modelflattening.models.SimpleProduct or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        # Construct URL
        url = self.put_simple_product.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SimpleProduct', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    put_simple_product.metadata = {'url': '/model-flatten/customFlattening'}

    def post_flattened_simple_product(
            self, product_id, max_product_display_name, description=None, generic_value=None, odatavalue=None, custom_headers=None, raw=False, **operation_config):
        """Put Flattened Simple Product with client flattening true on the
        parameter.

        :param product_id: Unique identifier representing a specific product
         for a given latitude & longitude. For example, uberX in San Francisco
         will have a different product_id than uberX in Los Angeles.
        :type product_id: str
        :param max_product_display_name: Display name of product.
        :type max_product_display_name: str
        :param description: Description of product.
        :type description: str
        :param generic_value: Generic URL value.
        :type generic_value: str
        :param odatavalue: URL value.
        :type odatavalue: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SimpleProduct or ClientRawResponse if raw=true
        :rtype: ~modelflattening.models.SimpleProduct or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        simple_body_product = None
        if product_id is not None or description is not None or max_product_display_name is not None or generic_value is not None or odatavalue is not None:
            simple_body_product = models.SimpleProduct(product_id=product_id, description=description, max_product_display_name=max_product_display_name, generic_value=generic_value, odatavalue=odatavalue)

        # Construct URL
        url = self.post_flattened_simple_product.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SimpleProduct', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    post_flattened_simple_product.metadata = {'url': '/model-flatten/customFlattening'}

    def put_simple_product_with_grouping(
            self, flatten_parameter_group, custom_headers=None, raw=False, **operation_config):
        """Put Simple Product with client flattening true on the model.

        :param flatten_parameter_group: Additional parameters for the
         operation
        :type flatten_parameter_group:
         ~modelflattening.models.FlattenParameterGroup
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: SimpleProduct or ClientRawResponse if raw=true
        :rtype: ~modelflattening.models.SimpleProduct or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<modelflattening.models.ErrorException>`
        """
        name = None
        if flatten_parameter_group is not None:
            name = flatten_parameter_group.name
        product_id = None
        if flatten_parameter_group is not None:
            product_id = flatten_parameter_group.product_id
        description = None
        if flatten_parameter_group is not None:
            description = flatten_parameter_group.description
        max_product_display_name = None
        if flatten_parameter_group is not None:
            max_product_display_name = flatten_parameter_group.max_product_display_name
        generic_value = None
        if flatten_parameter_group is not None:
            generic_value = flatten_parameter_group.generic_value
        odatavalue = None
        if flatten_parameter_group is not None:
            odatavalue = flatten_parameter_group.odatavalue
        simple_body_product = None
        if product_id is not None or description is not None or max_product_display_name is not None or generic_value is not None or odatavalue is not None:
            simple_body_product = models.SimpleProduct(product_id=product_id, description=description, max_product_display_name=max_product_display_name, generic_value=generic_value, odatavalue=odatavalue)

        # Construct URL
        url = self.put_simple_product_with_grouping.metadata['url']
        path_format_arguments = {
            'name': self._serialize.url("name", name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        if simple_body_product is not None:
            body_content = self._serialize.body(simple_body_product, 'SimpleProduct')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('SimpleProduct', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    put_simple_product_with_grouping.metadata = {'url': '/model-flatten/customFlattening/parametergrouping/{name}/'}
