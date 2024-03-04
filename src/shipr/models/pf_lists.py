import pydantic as _p
import sqlmodel as sqm

from . import pf_ext, pf_shared


class HazardousGoods(pf_shared.BasePFType):
    hazardous_good: list[pf_shared.HazardousGood]


class ContentDetails(pf_shared.BasePFType):
    content_detail: list[pf_shared.ContentDetail]


class ParcelContents(pf_shared.BasePFType):
    item: list[pf_shared.ContentData]


class LabelData(pf_shared.BasePFType):
    item: list[pf_shared.LabelItem]


class Barcodes(pf_shared.BasePFType):
    barcode: list[pf_shared.Barcode]


class Images(pf_shared.BasePFType):
    image: list[pf_shared.Image]


class ManifestShipments(pf_shared.BasePFType):
    manifest_shipment: list[pf_shared.ManifestShipment]


class CompletedShipments(pf_shared.BasePFType):
    completed_shipment: list[pf_shared.CompletedShipment] = sqm.Field(default_factory=list)


class CompletedCancel(pf_shared.BasePFType):
    completed_cancel_info: pf_shared.CompletedCancelInfo | None = None


class Alerts(pf_shared.BasePFType):
    alert: list[pf_shared.Alert]


class Notifications(pf_shared.BasePFType):
    notification_type: list[str] = _p.Field(default_factory=list)


class NominatedDeliveryDatelist(pf_shared.BasePFType):
    nominated_delivery_date: list[str] = _p.Field(default_factory=list)


class SafePlacelist(pf_shared.BasePFType):
    safe_place: list[str] = _p.Field(default_factory=list)


class ServiceCodes(pf_shared.BasePFType):
    service_code: list[str] = _p.Field(default_factory=list)


class SpecifiedNeighbour(pf_shared.BasePFType):
    address: list[pf_ext.AddressRecipient] = _p.Field(default_factory=list)
