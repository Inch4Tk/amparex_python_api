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
    from amparex.model.document import Document
    from amparex.model.invoice_position import InvoicePosition
    globals()['Document'] = Document
    globals()['InvoicePosition'] = InvoicePosition


class Invoice(ModelNormal):
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
            'acceptance_date': (date,),  # noqa: E501
            'acceptance_nr': (str,),  # noqa: E501
            'acceptance_state': (str,),  # noqa: E501
            'accounting_state': (str,),  # noqa: E501
            'address_id': (str,),  # noqa: E501
            'alternative_cost_center': (str,),  # noqa: E501
            'application_type': (int,),  # noqa: E501
            'cash_discount_days': (int,),  # noqa: E501
            'cash_discount_granted': (bool,),  # noqa: E501
            'cash_discount_percentage': (int,),  # noqa: E501
            'contribution_free': (bool,),  # noqa: E501
            'cost_center_branch_id': (str,),  # noqa: E501
            'cost_coverage1': (float,),  # noqa: E501
            'cost_coverage2': (float,),  # noqa: E501
            'cost_coverage_percent1': (float,),  # noqa: E501
            'cost_coverage_percent2': (float,),  # noqa: E501
            'customer_id': (str,),  # noqa: E501
            'delivery_date': (date,),  # noqa: E501
            'discount': (float,),  # noqa: E501
            'documents': ([Document],),  # noqa: E501
            'dunning_level': (int,),  # noqa: E501
            'extra_payment': (float,),  # noqa: E501
            'gross': (bool,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'invoice_date': (date,),  # noqa: E501
            'invoice_kind': (str,),  # noqa: E501
            'invoice_nr': (str,),  # noqa: E501
            'invoice_state': (str,),  # noqa: E501
            'invoice_type': (str,),  # noqa: E501
            'is_vat_exempt': (bool,),  # noqa: E501
            'list_price': (float,),  # noqa: E501
            'modified': (datetime,),  # noqa: E501
            'payed': (float,),  # noqa: E501
            'payed_reminder_due': (float,),  # noqa: E501
            'payment_method_id': (str,),  # noqa: E501
            'payment_reference': (str,),  # noqa: E501
            'payment_target': (date,),  # noqa: E501
            'position_number': (int,),  # noqa: E501
            'positions': ([InvoicePosition],),  # noqa: E501
            'price': (float,),  # noqa: E501
            'related_to_id': (str,),  # noqa: E501
            'remark1': (str,),  # noqa: E501
            'remark2': (str,),  # noqa: E501
            'remark_intern': (str,),  # noqa: E501
            'sponsor_id': (str,),  # noqa: E501
            'sponsor_index': (int,),  # noqa: E501
            'staff_id': (str,),  # noqa: E501
            'total_gross': (float,),  # noqa: E501
            'total_net': (float,),  # noqa: E501
            'treatment_head_id': (str,),  # noqa: E501
            'turnover_date': (date,),  # noqa: E501
            'vat_exemption_reason': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'acceptance_date': 'acceptanceDate',  # noqa: E501
        'acceptance_nr': 'acceptanceNr',  # noqa: E501
        'acceptance_state': 'acceptanceState',  # noqa: E501
        'accounting_state': 'accountingState',  # noqa: E501
        'address_id': 'addressID',  # noqa: E501
        'alternative_cost_center': 'alternativeCostCenter',  # noqa: E501
        'application_type': 'applicationType',  # noqa: E501
        'cash_discount_days': 'cashDiscountDays',  # noqa: E501
        'cash_discount_granted': 'cashDiscountGranted',  # noqa: E501
        'cash_discount_percentage': 'cashDiscountPercentage',  # noqa: E501
        'contribution_free': 'contributionFree',  # noqa: E501
        'cost_center_branch_id': 'costCenterBranchID',  # noqa: E501
        'cost_coverage1': 'costCoverage1',  # noqa: E501
        'cost_coverage2': 'costCoverage2',  # noqa: E501
        'cost_coverage_percent1': 'costCoveragePercent1',  # noqa: E501
        'cost_coverage_percent2': 'costCoveragePercent2',  # noqa: E501
        'customer_id': 'customerID',  # noqa: E501
        'delivery_date': 'deliveryDate',  # noqa: E501
        'discount': 'discount',  # noqa: E501
        'documents': 'documents',  # noqa: E501
        'dunning_level': 'dunningLevel',  # noqa: E501
        'extra_payment': 'extraPayment',  # noqa: E501
        'gross': 'gross',  # noqa: E501
        'id': 'id',  # noqa: E501
        'invoice_date': 'invoiceDate',  # noqa: E501
        'invoice_kind': 'invoiceKind',  # noqa: E501
        'invoice_nr': 'invoiceNr',  # noqa: E501
        'invoice_state': 'invoiceState',  # noqa: E501
        'invoice_type': 'invoiceType',  # noqa: E501
        'is_vat_exempt': 'isVatExempt',  # noqa: E501
        'list_price': 'listPrice',  # noqa: E501
        'modified': 'modified',  # noqa: E501
        'payed': 'payed',  # noqa: E501
        'payed_reminder_due': 'payedReminderDue',  # noqa: E501
        'payment_method_id': 'paymentMethodID',  # noqa: E501
        'payment_reference': 'paymentReference',  # noqa: E501
        'payment_target': 'paymentTarget',  # noqa: E501
        'position_number': 'positionNumber',  # noqa: E501
        'positions': 'positions',  # noqa: E501
        'price': 'price',  # noqa: E501
        'related_to_id': 'relatedToID',  # noqa: E501
        'remark1': 'remark1',  # noqa: E501
        'remark2': 'remark2',  # noqa: E501
        'remark_intern': 'remarkIntern',  # noqa: E501
        'sponsor_id': 'sponsorID',  # noqa: E501
        'sponsor_index': 'sponsorIndex',  # noqa: E501
        'staff_id': 'staffID',  # noqa: E501
        'total_gross': 'totalGross',  # noqa: E501
        'total_net': 'totalNet',  # noqa: E501
        'treatment_head_id': 'treatmentHeadID',  # noqa: E501
        'turnover_date': 'turnoverDate',  # noqa: E501
        'vat_exemption_reason': 'vatExemptionReason',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Invoice - a model defined in OpenAPI

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
            acceptance_date (date): [optional]  # noqa: E501
            acceptance_nr (str): [optional]  # noqa: E501
            acceptance_state (str): [optional]  # noqa: E501
            accounting_state (str): [optional]  # noqa: E501
            address_id (str): [optional]  # noqa: E501
            alternative_cost_center (str): [optional]  # noqa: E501
            application_type (int): [optional]  # noqa: E501
            cash_discount_days (int): [optional]  # noqa: E501
            cash_discount_granted (bool): [optional]  # noqa: E501
            cash_discount_percentage (int): [optional]  # noqa: E501
            contribution_free (bool): [optional]  # noqa: E501
            cost_center_branch_id (str): [optional]  # noqa: E501
            cost_coverage1 (float): [optional]  # noqa: E501
            cost_coverage2 (float): [optional]  # noqa: E501
            cost_coverage_percent1 (float): [optional]  # noqa: E501
            cost_coverage_percent2 (float): [optional]  # noqa: E501
            customer_id (str): [optional]  # noqa: E501
            delivery_date (date): [optional]  # noqa: E501
            discount (float): [optional]  # noqa: E501
            documents ([Document]): [optional]  # noqa: E501
            dunning_level (int): [optional]  # noqa: E501
            extra_payment (float): [optional]  # noqa: E501
            gross (bool): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            invoice_date (date): [optional]  # noqa: E501
            invoice_kind (str): [optional]  # noqa: E501
            invoice_nr (str): [optional]  # noqa: E501
            invoice_state (str): [optional]  # noqa: E501
            invoice_type (str): [optional]  # noqa: E501
            is_vat_exempt (bool): [optional]  # noqa: E501
            list_price (float): [optional]  # noqa: E501
            modified (datetime): [optional]  # noqa: E501
            payed (float): [optional]  # noqa: E501
            payed_reminder_due (float): [optional]  # noqa: E501
            payment_method_id (str): [optional]  # noqa: E501
            payment_reference (str): [optional]  # noqa: E501
            payment_target (date): [optional]  # noqa: E501
            position_number (int): [optional]  # noqa: E501
            positions ([InvoicePosition]): [optional]  # noqa: E501
            price (float): [optional]  # noqa: E501
            related_to_id (str): [optional]  # noqa: E501
            remark1 (str): [optional]  # noqa: E501
            remark2 (str): [optional]  # noqa: E501
            remark_intern (str): [optional]  # noqa: E501
            sponsor_id (str): [optional]  # noqa: E501
            sponsor_index (int): [optional]  # noqa: E501
            staff_id (str): [optional]  # noqa: E501
            total_gross (float): [optional]  # noqa: E501
            total_net (float): [optional]  # noqa: E501
            treatment_head_id (str): [optional]  # noqa: E501
            turnover_date (date): [optional]  # noqa: E501
            vat_exemption_reason (str): [optional]  # noqa: E501
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
        """Invoice - a model defined in OpenAPI

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
            acceptance_date (date): [optional]  # noqa: E501
            acceptance_nr (str): [optional]  # noqa: E501
            acceptance_state (str): [optional]  # noqa: E501
            accounting_state (str): [optional]  # noqa: E501
            address_id (str): [optional]  # noqa: E501
            alternative_cost_center (str): [optional]  # noqa: E501
            application_type (int): [optional]  # noqa: E501
            cash_discount_days (int): [optional]  # noqa: E501
            cash_discount_granted (bool): [optional]  # noqa: E501
            cash_discount_percentage (int): [optional]  # noqa: E501
            contribution_free (bool): [optional]  # noqa: E501
            cost_center_branch_id (str): [optional]  # noqa: E501
            cost_coverage1 (float): [optional]  # noqa: E501
            cost_coverage2 (float): [optional]  # noqa: E501
            cost_coverage_percent1 (float): [optional]  # noqa: E501
            cost_coverage_percent2 (float): [optional]  # noqa: E501
            customer_id (str): [optional]  # noqa: E501
            delivery_date (date): [optional]  # noqa: E501
            discount (float): [optional]  # noqa: E501
            documents ([Document]): [optional]  # noqa: E501
            dunning_level (int): [optional]  # noqa: E501
            extra_payment (float): [optional]  # noqa: E501
            gross (bool): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            invoice_date (date): [optional]  # noqa: E501
            invoice_kind (str): [optional]  # noqa: E501
            invoice_nr (str): [optional]  # noqa: E501
            invoice_state (str): [optional]  # noqa: E501
            invoice_type (str): [optional]  # noqa: E501
            is_vat_exempt (bool): [optional]  # noqa: E501
            list_price (float): [optional]  # noqa: E501
            modified (datetime): [optional]  # noqa: E501
            payed (float): [optional]  # noqa: E501
            payed_reminder_due (float): [optional]  # noqa: E501
            payment_method_id (str): [optional]  # noqa: E501
            payment_reference (str): [optional]  # noqa: E501
            payment_target (date): [optional]  # noqa: E501
            position_number (int): [optional]  # noqa: E501
            positions ([InvoicePosition]): [optional]  # noqa: E501
            price (float): [optional]  # noqa: E501
            related_to_id (str): [optional]  # noqa: E501
            remark1 (str): [optional]  # noqa: E501
            remark2 (str): [optional]  # noqa: E501
            remark_intern (str): [optional]  # noqa: E501
            sponsor_id (str): [optional]  # noqa: E501
            sponsor_index (int): [optional]  # noqa: E501
            staff_id (str): [optional]  # noqa: E501
            total_gross (float): [optional]  # noqa: E501
            total_net (float): [optional]  # noqa: E501
            treatment_head_id (str): [optional]  # noqa: E501
            turnover_date (date): [optional]  # noqa: E501
            vat_exemption_reason (str): [optional]  # noqa: E501
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
