# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from amparex.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from amparex.model.address import Address
from amparex.model.address_search_query import AddressSearchQuery
from amparex.model.address_to_save import AddressToSave
from amparex.model.api_article_item_overview import ApiArticleItemOverview
from amparex.model.api_cash_desk_balance import ApiCashDeskBalance
from amparex.model.api_cash_desk_balance_search_query import ApiCashDeskBalanceSearchQuery
from amparex.model.api_company_customer_number import ApiCompanyCustomerNumber
from amparex.model.api_service_contract_interval import ApiServiceContractInterval
from amparex.model.application_type import ApplicationType
from amparex.model.appointment import Appointment
from amparex.model.appointment_free_busy_search_query import AppointmentFreeBusySearchQuery
from amparex.model.appointment_planner import AppointmentPlanner
from amparex.model.appointment_search_query import AppointmentSearchQuery
from amparex.model.appointment_sync import AppointmentSync
from amparex.model.appointment_template import AppointmentTemplate
from amparex.model.appointment_template_search_query import AppointmentTemplateSearchQuery
from amparex.model.appointment_to_save import AppointmentToSave
from amparex.model.article_detail import ArticleDetail
from amparex.model.article_item import ArticleItem
from amparex.model.article_item_search_query import ArticleItemSearchQuery
from amparex.model.article_overview import ArticleOverview
from amparex.model.article_properties_meta import ArticlePropertiesMeta
from amparex.model.article_property import ArticleProperty
from amparex.model.article_search_query import ArticleSearchQuery
from amparex.model.article_type import ArticleType
from amparex.model.article_type_reduced import ArticleTypeReduced
from amparex.model.article_type_search_query import ArticleTypeSearchQuery
from amparex.model.article_variant import ArticleVariant
from amparex.model.article_variant_search_query import ArticleVariantSearchQuery
from amparex.model.audiogram import Audiogram
from amparex.model.audiogram_search_query import AudiogramSearchQuery
from amparex.model.availability import Availability
from amparex.model.availability_search_query import AvailabilitySearchQuery
from amparex.model.availability_to_save import AvailabilityToSave
from amparex.model.bank_account import BankAccount
from amparex.model.book_appointment_by_template import BookAppointmentByTemplate
from amparex.model.branch import Branch
from amparex.model.branch_reduced import BranchReduced
from amparex.model.branch_search_query import BranchSearchQuery
from amparex.model.brand import Brand
from amparex.model.brand_search_query import BrandSearchQuery
from amparex.model.color import Color
from amparex.model.color_search_query import ColorSearchQuery
from amparex.model.comment import Comment
from amparex.model.comment_search_query import CommentSearchQuery
from amparex.model.comment_to_save import CommentToSave
from amparex.model.company import Company
from amparex.model.company_search_query import CompanySearchQuery
from amparex.model.complaint import Complaint
from amparex.model.contact_lense import ContactLense
from amparex.model.contact_lense_detail import ContactLenseDetail
from amparex.model.contact_lense_search_query import ContactLenseSearchQuery
from amparex.model.contact_lense_to_save import ContactLenseToSave
from amparex.model.creation_response import CreationResponse
from amparex.model.customer import Customer
from amparex.model.customer_reduced import CustomerReduced
from amparex.model.customer_reduced_with_email import CustomerReducedWithEmail
from amparex.model.customer_search_query import CustomerSearchQuery
from amparex.model.customer_to_save import CustomerToSave
from amparex.model.delivery import Delivery
from amparex.model.delivery_position import DeliveryPosition
from amparex.model.delivery_search_query import DeliverySearchQuery
from amparex.model.doctor import Doctor
from amparex.model.doctor_property import DoctorProperty
from amparex.model.doctor_reduced import DoctorReduced
from amparex.model.doctor_search_query import DoctorSearchQuery
from amparex.model.document import Document
from amparex.model.document_search_query import DocumentSearchQuery
from amparex.model.document_template import DocumentTemplate
from amparex.model.document_template_search_query import DocumentTemplateSearchQuery
from amparex.model.document_to_save import DocumentToSave
from amparex.model.free_busy_appointment import FreeBusyAppointment
from amparex.model.glasses_care import GlassesCare
from amparex.model.glasses_configuration import GlassesConfiguration
from amparex.model.glasses_search_query import GlassesSearchQuery
from amparex.model.health_insurance import HealthInsurance
from amparex.model.health_insurance_reduced import HealthInsuranceReduced
from amparex.model.health_insurance_search_query import HealthInsuranceSearchQuery
from amparex.model.hearing_care import HearingCare
from amparex.model.hearing_care_search_query import HearingCareSearchQuery
from amparex.model.image import Image
from amparex.model.invoice import Invoice
from amparex.model.invoice_position import InvoicePosition
from amparex.model.invoice_position_to_save import InvoicePositionToSave
from amparex.model.invoice_search_query import InvoiceSearchQuery
from amparex.model.item_ref import ItemRef
from amparex.model.items_to_transfer import ItemsToTransfer
from amparex.model.lense_option_search_query import LenseOptionSearchQuery
from amparex.model.lense_options import LenseOptions
from amparex.model.lense_type import LenseType
from amparex.model.lense_type_search_query import LenseTypeSearchQuery
from amparex.model.list_result_wrapper_address import ListResultWrapperAddress
from amparex.model.list_result_wrapper_api_cash_desk_balance import ListResultWrapperApiCashDeskBalance
from amparex.model.list_result_wrapper_appointment import ListResultWrapperAppointment
from amparex.model.list_result_wrapper_appointment_template import ListResultWrapperAppointmentTemplate
from amparex.model.list_result_wrapper_article_detail import ListResultWrapperArticleDetail
from amparex.model.list_result_wrapper_article_item import ListResultWrapperArticleItem
from amparex.model.list_result_wrapper_article_overview import ListResultWrapperArticleOverview
from amparex.model.list_result_wrapper_article_variant import ListResultWrapperArticleVariant
from amparex.model.list_result_wrapper_audiogram import ListResultWrapperAudiogram
from amparex.model.list_result_wrapper_availability import ListResultWrapperAvailability
from amparex.model.list_result_wrapper_branch import ListResultWrapperBranch
from amparex.model.list_result_wrapper_brand import ListResultWrapperBrand
from amparex.model.list_result_wrapper_color import ListResultWrapperColor
from amparex.model.list_result_wrapper_comment import ListResultWrapperComment
from amparex.model.list_result_wrapper_company import ListResultWrapperCompany
from amparex.model.list_result_wrapper_contact_lense import ListResultWrapperContactLense
from amparex.model.list_result_wrapper_customer import ListResultWrapperCustomer
from amparex.model.list_result_wrapper_delivery import ListResultWrapperDelivery
from amparex.model.list_result_wrapper_doctor import ListResultWrapperDoctor
from amparex.model.list_result_wrapper_document import ListResultWrapperDocument
from amparex.model.list_result_wrapper_document_template import ListResultWrapperDocumentTemplate
from amparex.model.list_result_wrapper_glasses_care import ListResultWrapperGlassesCare
from amparex.model.list_result_wrapper_health_insurance import ListResultWrapperHealthInsurance
from amparex.model.list_result_wrapper_hearing_care import ListResultWrapperHearingCare
from amparex.model.list_result_wrapper_invoice import ListResultWrapperInvoice
from amparex.model.list_result_wrapper_lense_options import ListResultWrapperLenseOptions
from amparex.model.list_result_wrapper_lense_type import ListResultWrapperLenseType
from amparex.model.list_result_wrapper_main_version import ListResultWrapperMainVersion
from amparex.model.list_result_wrapper_marketing_action import ListResultWrapperMarketingAction
from amparex.model.list_result_wrapper_marketing_campaign import ListResultWrapperMarketingCampaign
from amparex.model.list_result_wrapper_marketing_contact import ListResultWrapperMarketingContact
from amparex.model.list_result_wrapper_order import ListResultWrapperOrder
from amparex.model.list_result_wrapper_predefined_property import ListResultWrapperPredefinedProperty
from amparex.model.list_result_wrapper_principal import ListResultWrapperPrincipal
from amparex.model.list_result_wrapper_program_move import ListResultWrapperProgramMove
from amparex.model.list_result_wrapper_property_type import ListResultWrapperPropertyType
from amparex.model.list_result_wrapper_resource import ListResultWrapperResource
from amparex.model.list_result_wrapper_sales_price import ListResultWrapperSalesPrice
from amparex.model.list_result_wrapper_server import ListResultWrapperServer
from amparex.model.list_result_wrapper_service_contract import ListResultWrapperServiceContract
from amparex.model.list_result_wrapper_staff import ListResultWrapperStaff
from amparex.model.list_result_wrapper_stock_amount import ListResultWrapperStockAmount
from amparex.model.list_result_wrapper_survey import ListResultWrapperSurvey
from amparex.model.list_result_wrapper_survey_template import ListResultWrapperSurveyTemplate
from amparex.model.list_result_wrapper_treatment import ListResultWrapperTreatment
from amparex.model.list_result_wrapper_version import ListResultWrapperVersion
from amparex.model.list_result_wrapper_view import ListResultWrapperView
from amparex.model.main_version import MainVersion
from amparex.model.main_version_search_query import MainVersionSearchQuery
from amparex.model.mapstringstring import Mapstringstring
from amparex.model.marketing_action import MarketingAction
from amparex.model.marketing_action_search_query import MarketingActionSearchQuery
from amparex.model.marketing_campaign import MarketingCampaign
from amparex.model.marketing_campaign_reduced import MarketingCampaignReduced
from amparex.model.marketing_campaign_search_query import MarketingCampaignSearchQuery
from amparex.model.marketing_contact import MarketingContact
from amparex.model.marketing_contact_search_query import MarketingContactSearchQuery
from amparex.model.optional_mapstringstring import OptionalMapstringstring
from amparex.model.optionalboolean import Optionalboolean
from amparex.model.optionalstring import Optionalstring
from amparex.model.order import Order
from amparex.model.order_by import OrderBy
from amparex.model.order_position import OrderPosition
from amparex.model.order_search_query import OrderSearchQuery
from amparex.model.predefined_property import PredefinedProperty
from amparex.model.predefined_property_reduced import PredefinedPropertyReduced
from amparex.model.predefined_property_search_query import PredefinedPropertySearchQuery
from amparex.model.predefined_property_simple import PredefinedPropertySimple
from amparex.model.principal import Principal
from amparex.model.principal_search_query import PrincipalSearchQuery
from amparex.model.principal_to_save import PrincipalToSave
from amparex.model.procurement import Procurement
from amparex.model.program_move import ProgramMove
from amparex.model.program_move_search_query import ProgramMoveSearchQuery
from amparex.model.property_type import PropertyType
from amparex.model.property_type_search_query import PropertyTypeSearchQuery
from amparex.model.refraction_report import RefractionReport
from amparex.model.request_for_synchronization import RequestForSynchronization
from amparex.model.resource import Resource
from amparex.model.resource_reduced import ResourceReduced
from amparex.model.resource_search_query import ResourceSearchQuery
from amparex.model.resource_to_save import ResourceToSave
from amparex.model.result_meta_data import ResultMetaData
from amparex.model.result_of_synchronization import ResultOfSynchronization
from amparex.model.sales_price import SalesPrice
from amparex.model.sales_price_search_query import SalesPriceSearchQuery
from amparex.model.sales_treatment_to_create import SalesTreatmentToCreate
from amparex.model.search_property_entry import SearchPropertyEntry
from amparex.model.search_query_meta_data import SearchQueryMetaData
from amparex.model.security_token import SecurityToken
from amparex.model.server import Server
from amparex.model.server_search_query import ServerSearchQuery
from amparex.model.service_contract import ServiceContract
from amparex.model.service_contract_search_query import ServiceContractSearchQuery
from amparex.model.staff import Staff
from amparex.model.staff_reduced import StaffReduced
from amparex.model.staff_search_query import StaffSearchQuery
from amparex.model.staff_to_save import StaffToSave
from amparex.model.stock_amount import StockAmount
from amparex.model.stock_amount_search_query import StockAmountSearchQuery
from amparex.model.stock_availability import StockAvailability
from amparex.model.survey import Survey
from amparex.model.survey_answer import SurveyAnswer
from amparex.model.survey_search_query import SurveySearchQuery
from amparex.model.survey_template import SurveyTemplate
from amparex.model.survey_template_answer import SurveyTemplateAnswer
from amparex.model.survey_template_category import SurveyTemplateCategory
from amparex.model.survey_template_group import SurveyTemplateGroup
from amparex.model.survey_template_question import SurveyTemplateQuestion
from amparex.model.survey_template_search_query import SurveyTemplateSearchQuery
from amparex.model.therapeutics_treatment import TherapeuticsTreatment
from amparex.model.timestamp import Timestamp
from amparex.model.translated_string import TranslatedString
from amparex.model.treatment import Treatment
from amparex.model.treatment_creation_response import TreatmentCreationResponse
from amparex.model.treatment_position import TreatmentPosition
from amparex.model.treatment_search_query import TreatmentSearchQuery
from amparex.model.version import Version
from amparex.model.version_search_query import VersionSearchQuery
from amparex.model.version_to_save import VersionToSave
from amparex.model.view import View
from amparex.model.view_resource import ViewResource
from amparex.model.view_resource_to_save import ViewResourceToSave
from amparex.model.view_search_query import ViewSearchQuery
from amparex.model.view_to_save import ViewToSave
from amparex.model.who_am_i import WhoAmI
