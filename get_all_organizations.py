# Generated by ariadne-codegen
# Source: queries.gql

from typing import Annotated, List, Literal, Optional, Union

from pydantic import Field

from .base_model import BaseModel
from .enums import CardProductVertical, CardUsage, ComputeRegion, IntegrationEnvironment


class GetAllOrganizations(BaseModel):
    organizations: Optional[List["GetAllOrganizationsOrganizations"]]


class GetAllOrganizationsOrganizations(BaseModel):
    id: str
    profile: "GetAllOrganizationsOrganizationsProfile"
    card_products: Optional["GetAllOrganizationsOrganizationsCardProducts"] = Field(
        alias="cardProducts"
    )


class GetAllOrganizationsOrganizationsProfile(BaseModel):
    display_name: Optional[str] = Field(alias="displayName")
    environment: Optional[IntegrationEnvironment]
    region: Optional[ComputeRegion]


class GetAllOrganizationsOrganizationsCardProducts(BaseModel):
    edges: Optional[List["GetAllOrganizationsOrganizationsCardProductsEdges"]]
    page_info: "GetAllOrganizationsOrganizationsCardProductsPageInfo" = Field(
        alias="pageInfo"
    )


class GetAllOrganizationsOrganizationsCardProductsEdges(BaseModel):
    cursor: str
    node: Optional["GetAllOrganizationsOrganizationsCardProductsEdgesNode"]


class GetAllOrganizationsOrganizationsCardProductsEdgesNode(BaseModel):
    typename__: Literal["CardProduct"] = Field(alias="__typename")
    id: str
    name: Optional[str]
    usage: Optional[CardUsage]
    vertical: Optional[CardProductVertical]
    accounts: Optional["GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccounts"]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccounts(BaseModel):
    edges: Optional[
        List["GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdges"]
    ]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdges(BaseModel):
    node: Optional[
        "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNode"
    ]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNode(BaseModel):
    id: str
    name: Optional[str]
    features: Optional[
        List[
            Annotated[
                Union[
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesAchCapableFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesCardFundingFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesCommercialCreditPayInFullCardAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesCreditPaymentCardFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesDebitPaymentCardFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesDirectDepositFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesFleetCardAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesJustInTimeFundingFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesNegativeBalanceReserveFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesNonVerifiedFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesPayrollAdvanceFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesPayrollEmployerAdvanceFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesPointRewardFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesPrePaidPaymentCardFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesProductFundingFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesProductReserveFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesSecuredCreditPaymentCardFinancialAccountFeature",
                    "GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesVendorProvidedBankFinancialAccountFeature",
                ],
                Field(discriminator="typename__"),
            ]
        ]
    ]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesFinancialAccountFeature(
    BaseModel
):
    typename__: Literal[
        "CreditCardAccountFeature",
        "FinancialAccountFeature",
        "IncomeAccountFinancialAccountFeature",
        "MerchantSettlementFinancialAccountFeature",
        "OnDemandFundingFinancialAccountFeature",
        "PartialFundingFinancialAccountFeature",
        "PreprintedCardFinancialAccountFeature",
        "ProductSecuredDepositFinancialAccountFeature",
        "RepaymentFinancialAccountFeature",
        "SecuredDepositFinancialAccountFeature",
    ] = Field(alias="__typename")


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesAchCapableFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["AchCapableFinancialAccountFeature"] = Field(alias="__typename")
    typename__: Literal["AchCapableFinancialAccountFeature"] = Field(alias="__typename")
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesCardFundingFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["CardFundingFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["CardFundingFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesCommercialCreditPayInFullCardAccountFeature(
    BaseModel
):
    typename__: Literal["CommercialCreditPayInFullCardAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["CommercialCreditPayInFullCardAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesCreditPaymentCardFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["CreditPaymentCardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["CreditPaymentCardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesDebitPaymentCardFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["DebitPaymentCardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["DebitPaymentCardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesDirectDepositFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["DirectDepositFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["DirectDepositFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesFleetCardAccountFeature(
    BaseModel
):
    typename__: Literal["FleetCardAccountFeature"] = Field(alias="__typename")
    typename__: Literal["FleetCardAccountFeature"] = Field(alias="__typename")
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesJustInTimeFundingFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["JustInTimeFundingFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["JustInTimeFundingFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesNegativeBalanceReserveFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["NegativeBalanceReserveFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["NegativeBalanceReserveFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesNonVerifiedFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["NonVerifiedFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["NonVerifiedFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesPayrollAdvanceFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["PayrollAdvanceFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["PayrollAdvanceFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesPayrollEmployerAdvanceFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["PayrollEmployerAdvanceFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["PayrollEmployerAdvanceFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesPointRewardFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["PointRewardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["PointRewardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesPrePaidPaymentCardFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["PrePaidPaymentCardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["PrePaidPaymentCardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesProductFundingFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["ProductFundingFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesProductReserveFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["ProductReserveFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["ProductReserveFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesSecuredCreditPaymentCardFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["SecuredCreditPaymentCardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["SecuredCreditPaymentCardFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNodeFeaturesVendorProvidedBankFinancialAccountFeature(
    BaseModel
):
    typename__: Literal["VendorProvidedBankFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    typename__: Literal["VendorProvidedBankFinancialAccountFeature"] = Field(
        alias="__typename"
    )
    enabled: Optional[bool]


class GetAllOrganizationsOrganizationsCardProductsPageInfo(BaseModel):
    start_cursor: str = Field(alias="startCursor")
    end_cursor: str = Field(alias="endCursor")
    has_next_page: bool = Field(alias="hasNextPage")
    has_previous_page: bool = Field(alias="hasPreviousPage")


GetAllOrganizations.model_rebuild()
GetAllOrganizationsOrganizations.model_rebuild()
GetAllOrganizationsOrganizationsCardProducts.model_rebuild()
GetAllOrganizationsOrganizationsCardProductsEdges.model_rebuild()
GetAllOrganizationsOrganizationsCardProductsEdgesNode.model_rebuild()
GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccounts.model_rebuild()
GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdges.model_rebuild()
GetAllOrganizationsOrganizationsCardProductsEdgesNodeAccountsEdgesNode.model_rebuild()
