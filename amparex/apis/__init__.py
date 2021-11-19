
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
from amparex.api.addresses_api import AddressesApi
from amparex.api.application_types_api import ApplicationTypesApi
from amparex.api.appointment_planner_api import AppointmentPlannerApi
from amparex.api.appointment_templates_api import AppointmentTemplatesApi
from amparex.api.appointments_api import AppointmentsApi
from amparex.api.article_items_api import ArticleItemsApi
from amparex.api.article_variants_api import ArticleVariantsApi
from amparex.api.articles_api import ArticlesApi
from amparex.api.audiograms_api import AudiogramsApi
from amparex.api.availabilities_api import AvailabilitiesApi
from amparex.api.branches_api import BranchesApi
from amparex.api.brands_api import BrandsApi
from amparex.api.cash_desk_balances_api import CashDeskBalancesApi
from amparex.api.colors_api import ColorsApi
from amparex.api.comments_api import CommentsApi
from amparex.api.companies_api import CompaniesApi
from amparex.api.contact_lenses_api import ContactLensesApi
from amparex.api.customers_api import CustomersApi
from amparex.api.deliveries_api import DeliveriesApi
from amparex.api.doctors_api import DoctorsApi
from amparex.api.document_templates_api import DocumentTemplatesApi
from amparex.api.documents_api import DocumentsApi
from amparex.api.glasses_api import GlassesApi
from amparex.api.health_insurance_api import HealthInsuranceApi
from amparex.api.hearing_cares_api import HearingCaresApi
from amparex.api.invoices_api import InvoicesApi
from amparex.api.lenses_api import LensesApi
from amparex.api.login_api import LoginApi
from amparex.api.main_versions_api import MainVersionsApi
from amparex.api.marketing_actions_api import MarketingActionsApi
from amparex.api.marketing_campaigns_api import MarketingCampaignsApi
from amparex.api.marketing_contacts_api import MarketingContactsApi
from amparex.api.orders_api import OrdersApi
from amparex.api.principals_api import PrincipalsApi
from amparex.api.programs_api import ProgramsApi
from amparex.api.properties_api import PropertiesApi
from amparex.api.resources_api import ResourcesApi
from amparex.api.servers_api import ServersApi
from amparex.api.service_contracts_api import ServiceContractsApi
from amparex.api.staffs_api import StaffsApi
from amparex.api.survey_templates_api import SurveyTemplatesApi
from amparex.api.surveys_api import SurveysApi
from amparex.api.treatments_api import TreatmentsApi
from amparex.api.versions_api import VersionsApi
from amparex.api.views_api import ViewsApi
