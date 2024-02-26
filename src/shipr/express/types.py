# generated by datamodel-codegen: EDITED
#   filename:  ShipServiceDefinitions-OpenApi31Yaml.yaml
#   timestamp: 2024-02-17T19:09:14+00:00

from __future__ import annotations

from pathlib import Path
from typing import List, Optional
from enum import Enum

from pydantic import BaseModel, Field

from pawsupport import convert_print_silent2
from .shared import BasePFType, Notifications


class PAF(BasePFType):
    postcode: Optional[str] = Field(None)
    count: Optional[int] = Field(None)
    specified_neighbour: Optional[List[SpecifiedNeighbour]] = Field(
        None, description=''
    )


class SpecifiedNeighbour(BasePFType):
    address: Optional[List[AddressPF]] = Field(None, description='')


class Enhancement(BasePFType):
    enhanced_compensation: Optional[str] = Field(None)
    saturday_delivery_required: Optional[bool] = Field(
        None
    )


class HazardousGood(BasePFType):
    lqdgun_code: Optional[str] = Field(None)
    lqdg_description: Optional[str] = Field(None)
    lqdg_volume: Optional[float] = Field(None)
    firearms: Optional[str] = Field(None)


class Returns(BasePFType):
    returns_email: Optional[str] = Field(None)
    email_message: Optional[str] = Field(None)
    email_label: bool = Field(...)


class ContentDetail(BasePFType):
    country_of_manufacture: str = Field(...)
    country_of_origin: Optional[str] = Field(None)
    manufacturers_name: Optional[str] = Field(None)
    description: str = Field(...)
    unit_weight: float = Field(...)
    unit_quantity: int = Field(...)
    unit_value: float = Field(...)
    currency: str = Field(...)
    tariff_code: Optional[str] = Field(None)
    tariff_description: Optional[str] = Field(None)
    article_reference: Optional[str] = Field(None)


class DateTimeRange(BasePFType):
    from_: str = Field(...)
    to: str = Field(...)


class ContentData(BasePFType):
    name: str = Field(...)
    data: str = Field(...)


class LabelItem(BasePFType):
    name: str = Field(...)
    data: str = Field(...)


class Barcode(BasePFType):
    name: str = Field(...)
    data: str = Field(...)


class Image(BasePFType):
    name: str = Field(...)
    data: str = Field(...)


class PrintType(Enum):
    all_parcels = 'ALL_PARCELS'
    single_parcel = 'SINGLE_PARCEL'


class Document(BasePFType):
    data: bytes = Field(...)

    def download(self, outpath: Path = Path('label_out.pdf')) -> Path:
        with open(outpath, 'wb') as f:
            f.write(self.data)
        return outpath

    def print_doc_arrayed(self):
        output = self.download()
        convert_print_silent2(output)


class ManifestShipment(BasePFType):
    shipment_number: str = Field(...)
    service_code: str = Field(...)


class CompletedShipment(BasePFType):
    shipment_number: Optional[str] = Field(None)
    out_bound_shipment_number: Optional[str] = Field(
        None
    )
    in_bound_shipment_number: Optional[str] = Field(None)
    partner_number: Optional[str] = Field(None)


class CompletedReturnInfo(BasePFType):
    status: str = Field(...)
    shipment_number: str = Field(...)
    collection_time: DateTimeRange = Field(...)


class CompletedCancelInfo(BasePFType):
    status: Optional[str] = Field(None)
    shipment_number: Optional[str] = Field(None)


class SafePlaceList(BasePFType):
    safe_place: Optional[List[str]] = Field(None, description='')


class NominatedDeliveryDateList(BasePFType):
    nominated_delivery_date: Optional[List[str]] = Field(
        None, description=''
    )


class ServiceCodes(BasePFType):
    service_code: Optional[List[str]] = Field(None, description='')


class Hours(BasePFType):
    open: Optional[str] = Field(None)
    close: Optional[str] = Field(None)
    close_lunch: Optional[str] = Field(None)
    after_lunch_opening: Optional[str] = Field(None)


class Position(BasePFType):
    longitude: Optional[float] = Field(None)
    latitude: Optional[float] = Field(None)


class InBoundDetails(BasePFType):
    contract_number: str = Field(...)
    service_code: str = Field(...)
    total_shipment_weight: Optional[str] = Field(None)
    enhancement: Optional[Enhancement] = Field(None)
    reference_number1: Optional[str] = Field(None)
    reference_number2: Optional[str] = Field(None)
    reference_number3: Optional[str] = Field(None)
    reference_number4: Optional[str] = Field(None)
    reference_number5: Optional[str] = Field(None)
    special_instructions1: Optional[str] = Field(None)
    special_instructions2: Optional[str] = Field(None)
    special_instructions3: Optional[str] = Field(None)
    special_instructions4: Optional[str] = Field(None)


class HazardousGoods(BasePFType):
    hazardous_good: List[HazardousGood] = Field(
        ..., description=''
    )


class ContentDetails(BasePFType):
    content_detail: List[ContentDetail] = Field(
        ..., description=''
    )


class CollectionInfo(BasePFType):
    collection_contact: ContactPF = Field(...)
    collection_address: AddressPF = Field(...)
    collection_time: Optional[DateTimeRange] = Field(None)


class ParcelContents(BasePFType):
    item: List[ContentData] = Field(..., description='')


class LabelData(BasePFType):
    item: List[LabelItem] = Field(..., description='')


class Barcodes(BasePFType):
    barcode: List[Barcode] = Field(..., description='')


class Images(BasePFType):
    image: List[Image] = Field(..., description='')


class ManifestShipments(BasePFType):
    manifest_shipment: List[ManifestShipment] = Field(
        ..., description=''
    )


class CompletedShipments(BasePFType):
    completed_shipment: List[CompletedShipment] = Field(
        ..., description=''
    )


class CompletedCancel(BasePFType):
    completed_cancel_info: Optional[CompletedCancelInfo] = Field(
        None
    )


class Department(BasePFType):
    department_id: Optional[List[int]] = Field(
        None, description=''
    )
    service_codes: Optional[List[ServiceCodes]] = Field(
        None, description=''
    )
    nominated_delivery_date_list: Optional[NominatedDeliveryDateList] = Field(
        None
    )


class Mon(BasePFType):
    hours: Optional[Hours] = Field(None)


class Tue(BasePFType):
    hours: Optional[Hours] = Field(None)


class Wed(BasePFType):
    hours: Optional[Hours] = Field(None)


class Thu(BasePFType):
    hours: Optional[Hours] = Field(None)


class Fri(BasePFType):
    hours: Optional[Hours] = Field(None)


class Sat(BasePFType):
    hours: Optional[Hours] = Field(None)


class Sun(BasePFType):
    hours: Optional[Hours] = Field(None)


class BankHol(BasePFType):
    hours: Optional[Hours] = Field(None)


class Parcel(BasePFType):
    weight: Optional[float] = Field(None)
    length: Optional[int] = Field(None)
    height: Optional[int] = Field(None)
    width: Optional[int] = Field(None)
    purpose_of_shipment: Optional[str] = Field(None)
    invoice_number: Optional[str] = Field(None)
    export_license_number: Optional[str] = Field(None)
    certificate_number: Optional[str] = Field(None)
    content_details: Optional[ContentDetails] = Field(None)
    shipping_cost: Optional[float] = Field(None)


class ParcelLabelData(BasePFType):
    parcel_number: Optional[str] = Field(None)
    shipment_number: Optional[str] = Field(None)
    journey_leg: Optional[str] = Field(None)
    label_data: Optional[LabelData] = Field(None)
    barcodes: Optional[Barcodes] = Field(None)
    images: Optional[Images] = Field(None)
    parcel_contents: Optional[List[ParcelContents]] = Field(
        None, description=''
    )


class CompletedManifestInfo(BasePFType):
    department_id: int = Field(...)
    manifest_number: str = Field(...)
    manifest_type: str = Field(...)
    total_shipment_count: int = Field(...)
    manifest_shipments: ManifestShipments = Field(...)


class CompletedShipmentInfoCreatePrint(BasePFType):
    lead_shipment_number: Optional[str] = Field(None)
    shipment_number: Optional[str] = Field(None)
    delivery_date: Optional[str] = Field(None)
    status: str = Field(...)
    completed_shipments: CompletedShipments = Field(...)


class Departments(BasePFType):
    department: Optional[List[Department]] = Field(
        None, description=''
    )


class OpeningHours(BasePFType):
    mon: Optional[Mon] = Field(None)
    tue: Optional[Tue] = Field(None)
    wed: Optional[Wed] = Field(None)
    thu: Optional[Thu] = Field(None)
    fri: Optional[Fri] = Field(None)
    sat: Optional[Sat] = Field(None)
    sun: Optional[Sun] = Field(None)
    bank_hol: Optional[BankHol] = Field(None)


class Parcels(BasePFType):
    parcel: List[Parcel] = Field(..., description='')


class ShipmentLabelData(BasePFType):
    parcel_label_data: List[ParcelLabelData] = Field(
        ..., description=''
    )


class CompletedManifests(BasePFType):
    completed_manifest_info: List[CompletedManifestInfo] = Field(
        ..., description=''
    )


class NominatedDeliveryDates(BasePFType):
    service_code: Optional[str] = Field(None)
    departments: Optional[Departments] = Field(None)


class PostcodeExclusion(BasePFType):
    delivery_postcode: Optional[str] = Field(None)
    collection_postcode: Optional[str] = Field(None)
    departments: Optional[Departments] = Field(None)


class PostOffice(BasePFType):
    post_office_id: Optional[str] = Field(None)
    business: Optional[str] = Field(None)
    address: Optional[AddressPF] = Field(None)
    opening_hours: Optional[OpeningHours] = Field(None)
    distance: Optional[float] = Field(None)
    availability: Optional[bool] = Field(None)
    position: Optional[Position] = Field(None)
    booking_reference: Optional[str] = Field(None)


class InternationalInfo(BasePFType):
    parcels: Optional[Parcels] = Field(None)
    exporter_customs_reference: Optional[str] = Field(
        None
    )
    recipient_importer_vat_no: Optional[str] = Field(
        None
    )
    original_export_shipment_no: Optional[str] = Field(
        None
    )
    documents_only: Optional[bool] = Field(None)
    documents_description: Optional[str] = Field(None)
    value_under200_us_dollars: Optional[bool] = Field(
        None
    )
    shipment_description: Optional[str] = Field(None)
    comments: Optional[str] = Field(None)
    invoice_date: Optional[str] = Field(None)
    terms_of_delivery: Optional[str] = Field(None)
    purchase_order_ref: Optional[str] = Field(None)


class ConvenientCollect(BasePFType):
    postcode: Optional[str] = Field(None)
    post_office: Optional[List[PostOffice]] = Field(
        None, description=''
    )
    count: Optional[int] = Field(None)
    post_office_id: Optional[str] = Field(None)


class SpecifiedPostOffice(BasePFType):
    postcode: Optional[str] = Field(None)
    post_office: Optional[List[PostOffice]] = Field(
        None, description=''
    )
    count: Optional[int] = Field(None)
    post_office_id: Optional[str] = Field(None)


class ContactPF(BasePFType):
    business_name: str = Field(...)
    email_address: str = Field(...)
    mobile_phone: str = Field(...)

    contact_name: Optional[str] = Field(None)
    telephone: Optional[str] = Field(None)
    fax: Optional[str] = Field(None)

    senders_name: Optional[str] = Field(None)
    notifications: Optional[Notifications] = Field(None)


class AddressPF(BasePFType):
    address_line1: str
    address_line2: Optional[str] = Field(None)
    address_line3: Optional[str] = Field(None)
    town: str
    postcode: str
    country: str = Field('GB')

    @property
    def addr_lines_str(self) -> str:
        lines = [self.address_line1, self.address_line2, self.address_line3]
        ls = ' '.join(line for line in lines if line)
        return ls

    # @model_validator(mode='after')
    # def town(self):
    #     if not self.town:
    #         addrs = [self.address_line1, self.address_line2, self.address_line3]
    #         addrs = [a for a in addrs if a]
    #         last_a = len(addrs)
    #         if last_a == 1:
    #             raise ValueError('Town is required')
    #         self.town = addrs[-1]
    #         setattr(self, f'address_line{last_a}', None)
    #     return self
    #
    #


class AddressPFPartial(AddressPF):
    town: Optional[str] = Field(None)


class DeliveryOptions(BasePFType):
    convenient_collect: Optional[ConvenientCollect] = Field(
        None
    )
    irts: Optional[bool] = Field(None)
    letterbox: Optional[bool] = Field(None)
    specified_post_office: Optional[SpecifiedPostOffice] = Field(
        None
    )
    specified_neighbour: Optional[str] = Field(None)
    safe_place: Optional[str] = Field(None)
    pin: Optional[int] = Field(None)
    named_recipient: Optional[bool] = Field(None)
    address_only: Optional[bool] = Field(None)
    nominated_delivery_date: Optional[str] = Field(None)
    personal_parcel: Optional[str] = Field(None)


class AddressChoice(BaseModel):
    address: AddressPF
    score: int
