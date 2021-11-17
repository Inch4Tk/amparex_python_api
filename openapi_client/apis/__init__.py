
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.addresses_api import AddressesApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.addresses_api import AddressesApi
from openapi_client.api.application_types_api import ApplicationTypesApi
from openapi_client.api.appointment_planner_api import AppointmentPlannerApi
from openapi_client.api.appointment_templates_api import AppointmentTemplatesApi
from openapi_client.api.appointments_api import AppointmentsApi
from openapi_client.api.article_items_api import ArticleItemsApi
from openapi_client.api.article_variants_api import ArticleVariantsApi
from openapi_client.api.articles_api import ArticlesApi
from openapi_client.api.audiograms_api import AudiogramsApi
from openapi_client.api.availabilities_api import AvailabilitiesApi
from openapi_client.api.branches_api import BranchesApi
from openapi_client.api.brands_api import BrandsApi
from openapi_client.api.cash_desk_balances_api import CashDeskBalancesApi
from openapi_client.api.colors_api import ColorsApi
from openapi_client.api.comments_api import CommentsApi
from openapi_client.api.companies_api import CompaniesApi
from openapi_client.api.contact_lenses_api import ContactLensesApi
from openapi_client.api.customers_api import CustomersApi
from openapi_client.api.deliveries_api import DeliveriesApi
from openapi_client.api.doctors_api import DoctorsApi
from openapi_client.api.document_templates_api import DocumentTemplatesApi
from openapi_client.api.documents_api import DocumentsApi
from openapi_client.api.glasses_api import GlassesApi
from openapi_client.api.health_insurance_api import HealthInsuranceApi
from openapi_client.api.hearing_cares_api import HearingCaresApi
from openapi_client.api.invoices_api import InvoicesApi
from openapi_client.api.lenses_api import LensesApi
from openapi_client.api.login_api import LoginApi
from openapi_client.api.main_versions_api import MainVersionsApi
from openapi_client.api.marketing_actions_api import MarketingActionsApi
from openapi_client.api.marketing_campaigns_api import MarketingCampaignsApi
from openapi_client.api.marketing_contacts_api import MarketingContactsApi
from openapi_client.api.orders_api import OrdersApi
from openapi_client.api.principals_api import PrincipalsApi
from openapi_client.api.programs_api import ProgramsApi
from openapi_client.api.properties_api import PropertiesApi
from openapi_client.api.resources_api import ResourcesApi
from openapi_client.api.servers_api import ServersApi
from openapi_client.api.service_contracts_api import ServiceContractsApi
from openapi_client.api.staffs_api import StaffsApi
from openapi_client.api.survey_templates_api import SurveyTemplatesApi
from openapi_client.api.surveys_api import SurveysApi
from openapi_client.api.treatments_api import TreatmentsApi
from openapi_client.api.versions_api import VersionsApi
from openapi_client.api.views_api import ViewsApi
