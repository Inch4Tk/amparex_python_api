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
from amparex.model.list_result_wrapper_marketing_action import ListResultWrapperMarketingAction
from amparex.model.marketing_action import MarketingAction
from amparex.model.marketing_action_search_query import MarketingActionSearchQuery


class MarketingActionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_marketing_action_order_by_fields_using_get_endpoint = _Endpoint(
            settings={
                'response_type': ([str],),
                'auth': [
                    'security_token'
                ],
                'endpoint_path': '/alias/{alias}/protected/marketingactions/orderbyfields',
                'operation_id': 'get_marketing_action_order_by_fields_using_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'alias',
                ],
                'required': [
                    'alias',
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
                },
                'attribute_map': {
                    'alias': 'alias',
                },
                'location_map': {
                    'alias': 'path',
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
        self.get_marketing_action_using_get_endpoint = _Endpoint(
            settings={
                'response_type': (MarketingAction,),
                'auth': [
                    'security_token'
                ],
                'endpoint_path': '/alias/{alias}/protected/marketingactions/{id}',
                'operation_id': 'get_marketing_action_using_get',
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
        self.search_marketing_actions_using_post_endpoint = _Endpoint(
            settings={
                'response_type': (ListResultWrapperMarketingAction,),
                'auth': [
                    'security_token'
                ],
                'endpoint_path': '/alias/{alias}/protected/marketingactions/search',
                'operation_id': 'search_marketing_actions_using_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'alias',
                    'marketingaction_search_query',
                ],
                'required': [
                    'alias',
                    'marketingaction_search_query',
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
                    'marketingaction_search_query':
                        (MarketingActionSearchQuery,),
                },
                'attribute_map': {
                    'alias': 'alias',
                },
                'location_map': {
                    'alias': 'path',
                    'marketingaction_search_query': 'body',
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

    def get_marketing_action_order_by_fields_using_get(
        self,
        alias,
        **kwargs
    ):
        """Get possible fields for orderby of marketingaction fields  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_marketing_action_order_by_fields_using_get(alias, async_req=True)
        >>> result = thread.get()

        Args:
            alias (str): alias

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
            [str]
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
        return self.get_marketing_action_order_by_fields_using_get_endpoint.call_with_http_info(**kwargs)

    def get_marketing_action_using_get(
        self,
        alias,
        id,
        **kwargs
    ):
        """Get one specific marketingaction by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_marketing_action_using_get(alias, id, async_req=True)
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
            MarketingAction
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
        return self.get_marketing_action_using_get_endpoint.call_with_http_info(**kwargs)

    def search_marketing_actions_using_post(
        self,
        alias,
        marketingaction_search_query,
        **kwargs
    ):
        """Get a list of marketingactions  # noqa: E501

        Get a list of marketingactions  by a search query, paging is used, specify limit and page; Model Type: MarketingAction is returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_marketing_actions_using_post(alias, marketingaction_search_query, async_req=True)
        >>> result = thread.get()

        Args:
            alias (str): alias
            marketingaction_search_query (MarketingActionSearchQuery): marketingactionSearchQuery

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
            ListResultWrapperMarketingAction
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
        kwargs['marketingaction_search_query'] = \
            marketingaction_search_query
        return self.search_marketing_actions_using_post_endpoint.call_with_http_info(**kwargs)

