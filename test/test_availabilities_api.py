"""
    AMPAREX Rest API Documentation

    This is the description of the AMPAREX Rest API. All REST calls plus the corresponding data model are described in this documentation. Direct calls to the server are possible over this page.&lt;br/&gt;Following steps are needed to use the API:&lt;br/&gt;&lt;br/&gt;1. Get the alias identifier of your login account from AMPAREX Software (Branch office administration) -&gt; Service accounts -&gt; your service account -&gt; copy alias token)&lt;br/&gt;2. Please use the login URL /alias/{alias}/login under section \"Login\" below with your credentials to get a valid bearer token.&lt;br/&gt;3. Copy bearer token from login response&lt;br/&gt;3. Then click \"Authorize\" on the top of this page&lt;br/&gt;4. Insert into the field \"value\": \"Bearer {Your Bearer token}\" (without {}) for example \"Bearer 334d34d3dgh5tz5h5h\"&lt;br/&gt;4. Click Authorize&lt;br/&gt;5. Bearer token will be automatically used in the header for every following API call.&lt;br/&gt;6. Now you are ready to use the API&lt;br/&gt;&lt;br/&gt;See also [documentation](https://manual.amparex.com/display/HAN/AMPAREX+API) for help&lt;br/&gt;&lt;br/&gt;Documentation of all the used fields and objects is at the bottom of this page called \"Models\"  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import amparex
from amparex.api.availabilities_api import AvailabilitiesApi  # noqa: E501


class TestAvailabilitiesApi(unittest.TestCase):
    """AvailabilitiesApi unit test stubs"""

    def setUp(self):
        self.api = AvailabilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_availability_using_post(self):
        """Test case for create_availability_using_post

        Create a new availability  # noqa: E501
        """
        pass

    def test_delete_availability_using_delete1(self):
        """Test case for delete_availability_using_delete1

        Delete an availability with given id  # noqa: E501
        """
        pass

    def test_get_availability_order_by_fields_using_get(self):
        """Test case for get_availability_order_by_fields_using_get

        Get possible fields for orderby of availability fields  # noqa: E501
        """
        pass

    def test_get_availability_using_get(self):
        """Test case for get_availability_using_get

        Get one specific availability by id  # noqa: E501
        """
        pass

    def test_search_availabilities_using_post(self):
        """Test case for search_availabilities_using_post

        Get a list of availabilities  # noqa: E501
        """
        pass

    def test_update_availability_using_patch(self):
        """Test case for update_availability_using_patch

        Update availability with given id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
