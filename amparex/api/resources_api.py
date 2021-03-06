"""
    AMPAREX Rest API Documentation

    This is the description of the AMPAREX Rest API. All REST calls plus the corresponding data model are described in this documentation. Direct calls to the server are possible over this page.&lt;br/&gt;Following steps are needed to use the API:&lt;br/&gt;&lt;br/&gt;1. Get the alias identifier of your login account from AMPAREX Software (Branch office administration) -&gt; Service accounts -&gt; your service account -&gt; copy alias token)&lt;br/&gt;2. Please use the login URL /alias/{alias}/login under section \"Login\" below with your credentials to get a valid bearer token.&lt;br/&gt;3. Copy bearer token from login response&lt;br/&gt;3. Then click \"Authorize\" on the top of this page&lt;br/&gt;4. Insert into the field \"value\": \"Bearer {Your Bearer token}\" (without {}) for example \"Bearer 334d34d3dgh5tz5h5h\"&lt;br/&gt;4. Click Authorize&lt;br/&gt;5. Bearer token will be automatically used in the header for every following API call.&lt;br/&gt;6. Now you are ready to use the API&lt;br/&gt;&lt;br/&gt;See also [documentation](https://manual.amparex.com/display/HAN/AMPAREX+API) for help&lt;br/&gt;&lt;br/&gt;Documentation of all the used fields and objects is at the bottom of this page called \"Models\"  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from amparex.api_client import ApiClient, Endpoint as _Endpoint
from amparex.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from amparex.model.creation_response import CreationResponse
from amparex.model.list_result_wrapper_resource import ListResultWrapperResource
from amparex.model.resource import Resource
from amparex.model.resource_search_query import ResourceSearchQuery
from amparex.model.resource_to_save import ResourceToSave


class ResourcesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_resource_using_post_endpoint = _Endpoint(
            settings={
                'response_type': (CreationResponse,),
                'auth': [
                    'security_token'
                ],
                'endpoint_path': '/alias/{alias}/protected/resources',
                'operation_id': 'create_resource_using_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'alias',
                    'to_save',
                ],
                'required': [
                    'alias',
                    'to_save',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alias':
                        (str,),
                    'to_save':
                        (ResourceToSave,),
                },
                'attribute_map': {
                    'alias': 'alias',
                },
                'location_map': {
                    'alias': 'path',
                    'to_save': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_resource_using_delete_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'security_token'
                ],
                'endpoint_path': '/alias/{alias}/protected/resources/{id}',
                'operation_id': 'delete_resource_using_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'alias',
                    'id',
                ],
                'required': [
                    'alias',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alias':
                        (str,),
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'alias': 'alias',
                    'id': 'id',
                },
                'location_map': {
                    'alias': 'path',
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_resource_using_get_endpoint = _Endpoint(
            settings={
                'response_type': (Resource,),
                'auth': [
                    'security_token'
                ],
                'endpoint_path': '/alias/{alias}/protected/resources/{id}',
                'operation_id': 'get_resource_using_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'alias',
                    'id',
                ],
                'required': [
                    'alias',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alias':
                        (str,),
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'alias': 'alias',
                    'id': 'id',
                },
                'location_map': {
                    'alias': 'path',
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.search_resources_using_post_endpoint = _Endpoint(
            settings={
                'response_type': (ListResultWrapperResource,),
                'auth': [
                    'security_token'
                ],
                'endpoint_path': '/alias/{alias}/protected/resources/search',
                'operation_id': 'search_resources_using_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'alias',
                    'resource_search_query',
                ],
                'required': [
                    'alias',
                    'resource_search_query',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alias':
                        (str,),
                    'resource_search_query':
                        (ResourceSearchQuery,),
                },
                'attribute_map': {
                    'alias': 'alias',
                },
                'location_map': {
                    'alias': 'path',
                    'resource_search_query': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_resource_using_patch_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'security_token'
                ],
                'endpoint_path': '/alias/{alias}/protected/resources/{id}',
                'operation_id': 'update_resource_using_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'alias',
                    'id',
                    'to_update',
                ],
                'required': [
                    'alias',
                    'id',
                    'to_update',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'alias':
                        (str,),
                    'id':
                        (str,),
                    'to_update':
                        (ResourceToSave,),
                },
                'attribute_map': {
                    'alias': 'alias',
                    'id': 'id',
                },
                'location_map': {
                    'alias': 'path',
                    'id': 'path',
                    'to_update': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create_resource_using_post(
        self,
        alias,
        to_save,
        **kwargs
    ):
        """Create a new resource  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_resource_using_post(alias, to_save, async_req=True)
        >>> result = thread.get()

        Args:
            alias (str): alias
            to_save (ResourceToSave): toSave

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            CreationResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alias'] = \
            alias
        kwargs['to_save'] = \
            to_save
        return self.create_resource_using_post_endpoint.call_with_http_info(**kwargs)

    def delete_resource_using_delete(
        self,
        alias,
        id,
        **kwargs
    ):
        """Delete a resource with given id, only resources which have no future appointments could be deleted  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_resource_using_delete(alias, id, async_req=True)
        >>> result = thread.get()

        Args:
            alias (str): alias
            id (str): id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alias'] = \
            alias
        kwargs['id'] = \
            id
        return self.delete_resource_using_delete_endpoint.call_with_http_info(**kwargs)

    def get_resource_using_get(
        self,
        alias,
        id,
        **kwargs
    ):
        """Get one specific resource by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_resource_using_get(alias, id, async_req=True)
        >>> result = thread.get()

        Args:
            alias (str): alias
            id (str): id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Resource
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alias'] = \
            alias
        kwargs['id'] = \
            id
        return self.get_resource_using_get_endpoint.call_with_http_info(**kwargs)

    def search_resources_using_post(
        self,
        alias,
        resource_search_query,
        **kwargs
    ):
        """Get a list of resources  # noqa: E501

        Get a list of resources  by a search query, paging is used, specify limit and page; Model Type: Resource is returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_resources_using_post(alias, resource_search_query, async_req=True)
        >>> result = thread.get()

        Args:
            alias (str): alias
            resource_search_query (ResourceSearchQuery): resourceSearchQuery

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ListResultWrapperResource
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alias'] = \
            alias
        kwargs['resource_search_query'] = \
            resource_search_query
        return self.search_resources_using_post_endpoint.call_with_http_info(**kwargs)

    def update_resource_using_patch(
        self,
        alias,
        id,
        to_update,
        **kwargs
    ):
        """Update resource with given id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_resource_using_patch(alias, id, to_update, async_req=True)
        >>> result = thread.get()

        Args:
            alias (str): alias
            id (str): id
            to_update (ResourceToSave): toUpdate

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['alias'] = \
            alias
        kwargs['id'] = \
            id
        kwargs['to_update'] = \
            to_update
        return self.update_resource_using_patch_endpoint.call_with_http_info(**kwargs)

