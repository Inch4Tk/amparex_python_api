"""
    AMPAREX Rest API Documentation

    This is the description of the AMPAREX Rest API. All REST calls plus the corresponding data model are described in this documentation. Direct calls to the server are possible over this page.&lt;br/&gt;Following steps are needed to use the API:&lt;br/&gt;&lt;br/&gt;1. Get the alias identifier of your login account from AMPAREX Software (Branch office administration) -&gt; Service accounts -&gt; your service account -&gt; copy alias token)&lt;br/&gt;2. Please use the login URL /alias/{alias}/login under section \"Login\" below with your credentials to get a valid bearer token.&lt;br/&gt;3. Copy bearer token from login response&lt;br/&gt;3. Then click \"Authorize\" on the top of this page&lt;br/&gt;4. Insert into the field \"value\": \"Bearer {Your Bearer token}\" (without {}) for example \"Bearer 334d34d3dgh5tz5h5h\"&lt;br/&gt;4. Click Authorize&lt;br/&gt;5. Bearer token will be automatically used in the header for every following API call.&lt;br/&gt;6. Now you are ready to use the API&lt;br/&gt;&lt;br/&gt;See also [documentation](https://manual.amparex.com/display/HAN/AMPAREX+API) for help&lt;br/&gt;&lt;br/&gt;Documentation of all the used fields and objects is at the bottom of this page called \"Models\"  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "amparex"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="AMPAREX Rest API Documentation",
    author="AMPAREX",
    author_email="nobody@email.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "AMPAREX Rest API Documentation"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    This is the description of the AMPAREX Rest API. All REST calls plus the corresponding data model are described in this documentation. Direct calls to the server are possible over this page.&amp;lt;br/&amp;gt;Following steps are needed to use the API:&amp;lt;br/&amp;gt;&amp;lt;br/&amp;gt;1. Get the alias identifier of your login account from AMPAREX Software (Branch office administration) -&amp;gt; Service accounts -&amp;gt; your service account -&amp;gt; copy alias token)&amp;lt;br/&amp;gt;2. Please use the login URL /alias/{alias}/login under section \&quot;Login\&quot; below with your credentials to get a valid bearer token.&amp;lt;br/&amp;gt;3. Copy bearer token from login response&amp;lt;br/&amp;gt;3. Then click \&quot;Authorize\&quot; on the top of this page&amp;lt;br/&amp;gt;4. Insert into the field \&quot;value\&quot;: \&quot;Bearer {Your Bearer token}\&quot; (without {}) for example \&quot;Bearer 334d34d3dgh5tz5h5h\&quot;&amp;lt;br/&amp;gt;4. Click Authorize&amp;lt;br/&amp;gt;5. Bearer token will be automatically used in the header for every following API call.&amp;lt;br/&amp;gt;6. Now you are ready to use the API&amp;lt;br/&amp;gt;&amp;lt;br/&amp;gt;See also [documentation](https://manual.amparex.com/display/HAN/AMPAREX+API) for help&amp;lt;br/&amp;gt;&amp;lt;br/&amp;gt;Documentation of all the used fields and objects is at the bottom of this page called \&quot;Models\&quot;  # noqa: E501
    """
)
