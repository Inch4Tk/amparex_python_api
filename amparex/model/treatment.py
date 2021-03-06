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
    from amparex.model.application_type import ApplicationType
    from amparex.model.complaint import Complaint
    from amparex.model.customer_reduced import CustomerReduced
    from amparex.model.hearing_care import HearingCare
    from amparex.model.invoice import Invoice
    from amparex.model.refraction_report import RefractionReport
    from amparex.model.staff_reduced import StaffReduced
    from amparex.model.translated_string import TranslatedString
    from amparex.model.treatment_position import TreatmentPosition
    globals()['ApplicationType'] = ApplicationType
    globals()['Complaint'] = Complaint
    globals()['CustomerReduced'] = CustomerReduced
    globals()['HearingCare'] = HearingCare
    globals()['Invoice'] = Invoice
    globals()['RefractionReport'] = RefractionReport
    globals()['StaffReduced'] = StaffReduced
    globals()['TranslatedString'] = TranslatedString
    globals()['TreatmentPosition'] = TreatmentPosition


class Treatment(ModelNormal):
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
            'application_type': (ApplicationType,),  # noqa: E501
            'article_set_name': (str,),  # noqa: E501
            'avoid_collective_invoice': (bool,),  # noqa: E501
            'branch_id': (str,),  # noqa: E501
            'causation_date': (date,),  # noqa: E501
            'check_mandatory': (str,),  # noqa: E501
            'company_id': (str,),  # noqa: E501
            'complaints': ([Complaint],),  # noqa: E501
            'convert_reason_property_id': (str,),  # noqa: E501
            'coverage_treatment_extension': (str,),  # noqa: E501
            'customer': (CustomerReduced,),  # noqa: E501
            'data_checked': (bool,),  # noqa: E501
            'delivery_address_id': (str,),  # noqa: E501
            'demo_hearing_cares': ([HearingCare],),  # noqa: E501
            'doctor_id': (str,),  # noqa: E501
            'end_date': (date,),  # noqa: E501
            'exempt_from_extra_payment_amount': (int,),  # noqa: E501
            'exempt_from_extra_payment_status': (TranslatedString,),  # noqa: E501
            'extra_staff': (StaffReduced,),  # noqa: E501
            'hi_membership2_id': (str,),  # noqa: E501
            'hi_membership_id': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'import_date': (datetime,),  # noqa: E501
            'invoices': ([Invoice],),  # noqa: E501
            'is_working': (str,),  # noqa: E501
            'kind': (TranslatedString,),  # noqa: E501
            'marketing_contact_id': (str,),  # noqa: E501
            'modified': (datetime,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'payed_prepayment': (float,),  # noqa: E501
            'prescription_date': (date,),  # noqa: E501
            'prescription_number': (str,),  # noqa: E501
            'prescription_type': (TranslatedString,),  # noqa: E501
            'reference_number': (str,),  # noqa: E501
            'refraction_reports': ([RefractionReport],),  # noqa: E501
            'related_to_id': (str,),  # noqa: E501
            'repetition_index': (int,),  # noqa: E501
            'repetition_type': (TranslatedString,),  # noqa: E501
            'side': (TranslatedString,),  # noqa: E501
            'staff': (StaffReduced,),  # noqa: E501
            'start_date': (date,),  # noqa: E501
            'state': (TranslatedString,),  # noqa: E501
            'tariff_indicator': (str,),  # noqa: E501
            'treatment_nr': (str,),  # noqa: E501
            'treatment_positions': ([TreatmentPosition],),  # noqa: E501
            'use_start_date_for_pricing': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'acceptance_date': 'acceptanceDate',  # noqa: E501
        'acceptance_nr': 'acceptanceNr',  # noqa: E501
        'application_type': 'applicationType',  # noqa: E501
        'article_set_name': 'articleSetName',  # noqa: E501
        'avoid_collective_invoice': 'avoidCollectiveInvoice',  # noqa: E501
        'branch_id': 'branchID',  # noqa: E501
        'causation_date': 'causationDate',  # noqa: E501
        'check_mandatory': 'checkMandatory',  # noqa: E501
        'company_id': 'companyID',  # noqa: E501
        'complaints': 'complaints',  # noqa: E501
        'convert_reason_property_id': 'convertReasonPropertyID',  # noqa: E501
        'coverage_treatment_extension': 'coverageTreatmentExtension',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'data_checked': 'dataChecked',  # noqa: E501
        'delivery_address_id': 'deliveryAddressID',  # noqa: E501
        'demo_hearing_cares': 'demoHearingCares',  # noqa: E501
        'doctor_id': 'doctorID',  # noqa: E501
        'end_date': 'endDate',  # noqa: E501
        'exempt_from_extra_payment_amount': 'exemptFromExtraPaymentAmount',  # noqa: E501
        'exempt_from_extra_payment_status': 'exemptFromExtraPaymentStatus',  # noqa: E501
        'extra_staff': 'extraStaff',  # noqa: E501
        'hi_membership2_id': 'hiMembership2ID',  # noqa: E501
        'hi_membership_id': 'hiMembershipID',  # noqa: E501
        'id': 'id',  # noqa: E501
        'import_date': 'importDate',  # noqa: E501
        'invoices': 'invoices',  # noqa: E501
        'is_working': 'isWorking',  # noqa: E501
        'kind': 'kind',  # noqa: E501
        'marketing_contact_id': 'marketingContactID',  # noqa: E501
        'modified': 'modified',  # noqa: E501
        'name': 'name',  # noqa: E501
        'payed_prepayment': 'payedPrepayment',  # noqa: E501
        'prescription_date': 'prescriptionDate',  # noqa: E501
        'prescription_number': 'prescriptionNumber',  # noqa: E501
        'prescription_type': 'prescriptionType',  # noqa: E501
        'reference_number': 'referenceNumber',  # noqa: E501
        'refraction_reports': 'refractionReports',  # noqa: E501
        'related_to_id': 'relatedToID',  # noqa: E501
        'repetition_index': 'repetitionIndex',  # noqa: E501
        'repetition_type': 'repetitionType',  # noqa: E501
        'side': 'side',  # noqa: E501
        'staff': 'staff',  # noqa: E501
        'start_date': 'startDate',  # noqa: E501
        'state': 'state',  # noqa: E501
        'tariff_indicator': 'tariffIndicator',  # noqa: E501
        'treatment_nr': 'treatmentNr',  # noqa: E501
        'treatment_positions': 'treatmentPositions',  # noqa: E501
        'use_start_date_for_pricing': 'useStartDateForPricing',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Treatment - a model defined in OpenAPI

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
            application_type (ApplicationType): [optional]  # noqa: E501
            article_set_name (str): [optional]  # noqa: E501
            avoid_collective_invoice (bool): [optional]  # noqa: E501
            branch_id (str): [optional]  # noqa: E501
            causation_date (date): [optional]  # noqa: E501
            check_mandatory (str): [optional]  # noqa: E501
            company_id (str): [optional]  # noqa: E501
            complaints ([Complaint]): [optional]  # noqa: E501
            convert_reason_property_id (str): [optional]  # noqa: E501
            coverage_treatment_extension (str): [optional]  # noqa: E501
            customer (CustomerReduced): [optional]  # noqa: E501
            data_checked (bool): [optional]  # noqa: E501
            delivery_address_id (str): [optional]  # noqa: E501
            demo_hearing_cares ([HearingCare]): [optional]  # noqa: E501
            doctor_id (str): [optional]  # noqa: E501
            end_date (date): [optional]  # noqa: E501
            exempt_from_extra_payment_amount (int): [optional]  # noqa: E501
            exempt_from_extra_payment_status (TranslatedString): [optional]  # noqa: E501
            extra_staff (StaffReduced): [optional]  # noqa: E501
            hi_membership2_id (str): [optional]  # noqa: E501
            hi_membership_id (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            import_date (datetime): [optional]  # noqa: E501
            invoices ([Invoice]): [optional]  # noqa: E501
            is_working (str): [optional]  # noqa: E501
            kind (TranslatedString): [optional]  # noqa: E501
            marketing_contact_id (str): [optional]  # noqa: E501
            modified (datetime): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            payed_prepayment (float): [optional]  # noqa: E501
            prescription_date (date): [optional]  # noqa: E501
            prescription_number (str): [optional]  # noqa: E501
            prescription_type (TranslatedString): [optional]  # noqa: E501
            reference_number (str): [optional]  # noqa: E501
            refraction_reports ([RefractionReport]): [optional]  # noqa: E501
            related_to_id (str): A link to a previous, related treatment. [optional]  # noqa: E501
            repetition_index (int): [optional]  # noqa: E501
            repetition_type (TranslatedString): [optional]  # noqa: E501
            side (TranslatedString): [optional]  # noqa: E501
            staff (StaffReduced): [optional]  # noqa: E501
            start_date (date): [optional]  # noqa: E501
            state (TranslatedString): [optional]  # noqa: E501
            tariff_indicator (str): [optional]  # noqa: E501
            treatment_nr (str): [optional]  # noqa: E501
            treatment_positions ([TreatmentPosition]): [optional]  # noqa: E501
            use_start_date_for_pricing (bool): [optional]  # noqa: E501
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
        """Treatment - a model defined in OpenAPI

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
            application_type (ApplicationType): [optional]  # noqa: E501
            article_set_name (str): [optional]  # noqa: E501
            avoid_collective_invoice (bool): [optional]  # noqa: E501
            branch_id (str): [optional]  # noqa: E501
            causation_date (date): [optional]  # noqa: E501
            check_mandatory (str): [optional]  # noqa: E501
            company_id (str): [optional]  # noqa: E501
            complaints ([Complaint]): [optional]  # noqa: E501
            convert_reason_property_id (str): [optional]  # noqa: E501
            coverage_treatment_extension (str): [optional]  # noqa: E501
            customer (CustomerReduced): [optional]  # noqa: E501
            data_checked (bool): [optional]  # noqa: E501
            delivery_address_id (str): [optional]  # noqa: E501
            demo_hearing_cares ([HearingCare]): [optional]  # noqa: E501
            doctor_id (str): [optional]  # noqa: E501
            end_date (date): [optional]  # noqa: E501
            exempt_from_extra_payment_amount (int): [optional]  # noqa: E501
            exempt_from_extra_payment_status (TranslatedString): [optional]  # noqa: E501
            extra_staff (StaffReduced): [optional]  # noqa: E501
            hi_membership2_id (str): [optional]  # noqa: E501
            hi_membership_id (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            import_date (datetime): [optional]  # noqa: E501
            invoices ([Invoice]): [optional]  # noqa: E501
            is_working (str): [optional]  # noqa: E501
            kind (TranslatedString): [optional]  # noqa: E501
            marketing_contact_id (str): [optional]  # noqa: E501
            modified (datetime): [optional]  # noqa: E501
            name (str): [optional]  # noqa: E501
            payed_prepayment (float): [optional]  # noqa: E501
            prescription_date (date): [optional]  # noqa: E501
            prescription_number (str): [optional]  # noqa: E501
            prescription_type (TranslatedString): [optional]  # noqa: E501
            reference_number (str): [optional]  # noqa: E501
            refraction_reports ([RefractionReport]): [optional]  # noqa: E501
            related_to_id (str): A link to a previous, related treatment. [optional]  # noqa: E501
            repetition_index (int): [optional]  # noqa: E501
            repetition_type (TranslatedString): [optional]  # noqa: E501
            side (TranslatedString): [optional]  # noqa: E501
            staff (StaffReduced): [optional]  # noqa: E501
            start_date (date): [optional]  # noqa: E501
            state (TranslatedString): [optional]  # noqa: E501
            tariff_indicator (str): [optional]  # noqa: E501
            treatment_nr (str): [optional]  # noqa: E501
            treatment_positions ([TreatmentPosition]): [optional]  # noqa: E501
            use_start_date_for_pricing (bool): [optional]  # noqa: E501
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
