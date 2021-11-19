"""
    AMPAREX Rest API Documentation

    This is the description of the AMPAREX Rest API. All REST calls plus the corresponding data model are described in this documentation. Direct calls to the server are possible over this page.&lt;br/&gt;Following steps are needed to use the API:&lt;br/&gt;&lt;br/&gt;1. Get the alias identifier of your login account from AMPAREX Software (Branch office administration) -&gt; Service accounts -&gt; your service account -&gt; copy alias token)&lt;br/&gt;2. Please use the login URL /alias/{alias}/login under section \"Login\" below with your credentials to get a valid bearer token.&lt;br/&gt;3. Copy bearer token from login response&lt;br/&gt;3. Then click \"Authorize\" on the top of this page&lt;br/&gt;4. Insert into the field \"value\": \"Bearer {Your Bearer token}\" (without {}) for example \"Bearer 334d34d3dgh5tz5h5h\"&lt;br/&gt;4. Click Authorize&lt;br/&gt;5. Bearer token will be automatically used in the header for every following API call.&lt;br/&gt;6. Now you are ready to use the API&lt;br/&gt;&lt;br/&gt;See also [documentation](https://manual.amparex.com/display/HAN/AMPAREX+API) for help&lt;br/&gt;&lt;br/&gt;Documentation of all the used fields and objects is at the bottom of this page called \"Models\"  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from amparex.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from amparex.exceptions import ApiAttributeError


def lazy_import():
    from amparex.model.address_to_save import AddressToSave
    globals()['AddressToSave'] = AddressToSave


class CustomerToSave(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'address': (AddressToSave,),  # noqa: E501
            'advertising_flags': (int,),  # noqa: E501
            'birthdate': (str,),  # noqa: E501
            'customer_nr_extern': (str,),  # noqa: E501
            'customer_since': (str,),  # noqa: E501
            'dominant_eye': (str,),  # noqa: E501
            'dominant_hand': (str,),  # noqa: E501
            'extension_name': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_visit': (str,),  # noqa: E501
            'privacy_statement': (bool,),  # noqa: E501
            'privacy_statement_date': (str,),  # noqa: E501
            'resp_branch_id': (str,),  # noqa: E501
            'resp_staff_id': (str,),  # noqa: E501
            'restricted_view': (bool,),  # noqa: E501
            'salutation': (str,),  # noqa: E501
            'status_id': (str,),  # noqa: E501
            'surname': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'address': 'address',  # noqa: E501
        'advertising_flags': 'advertisingFlags',  # noqa: E501
        'birthdate': 'birthdate',  # noqa: E501
        'customer_nr_extern': 'customerNrExtern',  # noqa: E501
        'customer_since': 'customerSince',  # noqa: E501
        'dominant_eye': 'dominantEye',  # noqa: E501
        'dominant_hand': 'dominantHand',  # noqa: E501
        'extension_name': 'extensionName',  # noqa: E501
        'first_name': 'firstName',  # noqa: E501
        'last_visit': 'lastVisit',  # noqa: E501
        'privacy_statement': 'privacyStatement',  # noqa: E501
        'privacy_statement_date': 'privacyStatementDate',  # noqa: E501
        'resp_branch_id': 'respBranchID',  # noqa: E501
        'resp_staff_id': 'respStaffID',  # noqa: E501
        'restricted_view': 'restrictedView',  # noqa: E501
        'salutation': 'salutation',  # noqa: E501
        'status_id': 'statusID',  # noqa: E501
        'surname': 'surname',  # noqa: E501
        'title': 'title',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CustomerToSave - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            address (AddressToSave): [optional]  # noqa: E501
            advertising_flags (int): flags for accepted advertising channels (1=Letter 2=E-Mail 4=Phone 8=SMS) / Example: Letter + E-Mail + SMS = 1+2+8 = 11. [optional]  # noqa: E501
            birthdate (str): Customers birthdate. [optional]  # noqa: E501
            customer_nr_extern (str): External identifier of customer. [optional]  # noqa: E501
            customer_since (str): Customer in our shop since. [optional]  # noqa: E501
            dominant_eye (str): The dominant eye (side_right,side_left). [optional]  # noqa: E501
            dominant_hand (str): The dominant hand (side_right,side_left). [optional]  # noqa: E501
            extension_name (str): Depending on country: Name extension (von, zu) customers middle name (F.) or secondary surname e.g. for spanish names (García). [optional]  # noqa: E501
            first_name (str): Customers first name. [optional]  # noqa: E501
            last_visit (str): The date when the customer has last visited the shop. [optional]  # noqa: E501
            privacy_statement (bool): Does the customer have already accepted/signed the shops privacy statement? (true=accepted, null=not yet, false=declined). [optional]  # noqa: E501
            privacy_statement_date (str): The date of acceptance/signature of privacy statement. [optional]  # noqa: E501
            resp_branch_id (str): The ID of the branch that is responsible for this customer. [optional]  # noqa: E501
            resp_staff_id (str): The ID of the staff member responsible for this customer. [optional]  # noqa: E501
            restricted_view (bool): TRUE if access to this customer data is restricted to the responsible staff member only. (May be used for VIP persons). [optional]  # noqa: E501
            salutation (str): Customers gender (salutation_missis/salutation_mister/salutation_diverse). [optional]  # noqa: E501
            status_id (str): The ID of the customers status. Use /alias/{alias}/protected/properties/propertytypes/search with name=\"propertytype_customer_status\" to get the type-id and then /alias/{alias}/protected/properties/predefinedproperties/search with propertyTypeIDs=[\"type-id\"] to get all possible ids and its meaning. [optional]  # noqa: E501
            surname (str): Customers last name. [optional]  # noqa: E501
            title (str): Customers academic title. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """CustomerToSave - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            address (AddressToSave): [optional]  # noqa: E501
            advertising_flags (int): flags for accepted advertising channels (1=Letter 2=E-Mail 4=Phone 8=SMS) / Example: Letter + E-Mail + SMS = 1+2+8 = 11. [optional]  # noqa: E501
            birthdate (str): Customers birthdate. [optional]  # noqa: E501
            customer_nr_extern (str): External identifier of customer. [optional]  # noqa: E501
            customer_since (str): Customer in our shop since. [optional]  # noqa: E501
            dominant_eye (str): The dominant eye (side_right,side_left). [optional]  # noqa: E501
            dominant_hand (str): The dominant hand (side_right,side_left). [optional]  # noqa: E501
            extension_name (str): Depending on country: Name extension (von, zu) customers middle name (F.) or secondary surname e.g. for spanish names (García). [optional]  # noqa: E501
            first_name (str): Customers first name. [optional]  # noqa: E501
            last_visit (str): The date when the customer has last visited the shop. [optional]  # noqa: E501
            privacy_statement (bool): Does the customer have already accepted/signed the shops privacy statement? (true=accepted, null=not yet, false=declined). [optional]  # noqa: E501
            privacy_statement_date (str): The date of acceptance/signature of privacy statement. [optional]  # noqa: E501
            resp_branch_id (str): The ID of the branch that is responsible for this customer. [optional]  # noqa: E501
            resp_staff_id (str): The ID of the staff member responsible for this customer. [optional]  # noqa: E501
            restricted_view (bool): TRUE if access to this customer data is restricted to the responsible staff member only. (May be used for VIP persons). [optional]  # noqa: E501
            salutation (str): Customers gender (salutation_missis/salutation_mister/salutation_diverse). [optional]  # noqa: E501
            status_id (str): The ID of the customers status. Use /alias/{alias}/protected/properties/propertytypes/search with name=\"propertytype_customer_status\" to get the type-id and then /alias/{alias}/protected/properties/predefinedproperties/search with propertyTypeIDs=[\"type-id\"] to get all possible ids and its meaning. [optional]  # noqa: E501
            surname (str): Customers last name. [optional]  # noqa: E501
            title (str): Customers academic title. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
