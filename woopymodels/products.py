from typing import List, Literal, Optional
from pydantic import BaseModel
from datetime import datetime


class ProductDownload(BaseModel):
    """
    https://woocommerce.github.io/woocommerce-rest-api-docs/#product-downloads-properties
    """

    id: Optional[int] = None
    name: str
    file: str


class ProductDimensions(BaseModel):
    length: str = ""
    width: str = ""
    height: str = ""


class ProductCategory(BaseModel):
    """
    https://woocommerce.github.io/woocommerce-rest-api-docs/#product-categories-properties
    """

    id: Optional[int] = None
    name: Optional[str] = None
    slug: Optional[str] = None


class ProductTag(BaseModel):
    """
    https://woocommerce.github.io/woocommerce-rest-api-docs/#product-tags-properties
    """

    id: Optional[int] = None
    name: Optional[str] = None
    slug: Optional[str] = None


class ProductImage(BaseModel):
    """
    https://woocommerce.github.io/woocommerce-rest-api-docs/#product-images-properties
    """

    id: Optional[int] = None
    date_created: Optional[datetime] = None
    date_created_gmt: Optional[datetime] = None
    date_modified: Optional[datetime] = None
    date_modified_gmt: Optional[datetime] = None
    src: str
    name: str
    alt: Optional[str] = None


class ProductAttribute(BaseModel):
    """
    https://woocommerce.github.io/woocommerce-rest-api-docs/#product-attributes-properties
    """

    id: Optional[int] = None
    name: str
    position: int = 0
    visible: bool = False
    variation: bool = False
    options: List[str] = []


class ProductVariationAttribute(BaseModel):
    """
    https://woocommerce.github.io/woocommerce-rest-api-docs/#product-default-attributes-properties
    """

    id: Optional[int] = None
    name: str
    option: str


class MetaData(BaseModel):
    """
    https://woocommerce.github.io/woocommerce-rest-api-docs/#product-meta-data-properties
    """

    id: Optional[int] = None
    key: str
    value: Optional[str] = None


class Product(BaseModel):
    """https://woocommerce.github.io/woocommerce-rest-api-docs/#product-properties"""

    id: Optional[int] = None
    name: str
    slug: Optional[str] = None
    permalink: Optional[str] = None
    date_created: Optional[datetime] = None
    status: Literal["draft", "pending", "private", "publish"] = "publish"
    featured: bool = False
    catalog_visibility: Literal["visible", "catalog", "search", "hidden"] = "visible"
    description: str = ""
    short_description: str = ""
    sku: Optional[str] = None
    price: Optional[str] = None
    regular_price: Optional[str] = None
    sale_price: Optional[str] = None
    date_on_sale_from: Optional[datetime] = None
    date_on_sale_from_gmt: Optional[datetime] = None
    date_on_sale_to: Optional[datetime] = None
    date_on_sale_to_gmt: Optional[datetime] = None
    price_html: Optional[str] = None
    on_sale: bool = False
    purchasable: bool = True
    total_sales: Optional[int] = None
    virtual: bool = False
    downloadable: bool = False
    downloads: List[ProductDownload] = []
    download_limit: int = -1
    download_expiry: int = -1
    tax_status: Literal["taxable", "shipping", "none"] = "taxable"
    tax_class: Optional[str] = None
    manage_stock: bool = False
    stock_quantity: Optional[int] = None
    stock_status: Literal["instock", "outofstock", "onbackorder"] = "instock"
    backorders: Literal["no", "notify", "yes"] = "no"
    backorders_allowed: Optional[bool] = None
    backordered: Optional[bool] = None
    sold_individually: bool = False
    weight: str = ""
    dimensions: Optional[ProductDimensions] = None
    shipping_required: Optional[bool] = None
    shipping_taxable: Optional[bool] = None
    shipping_class: Optional[str] = None
    shipping_class_id: Optional[int] = None
    reviews_allowed: bool = True
    average_rating: Optional[str] = None
    rating_count: Optional[int] = None
    related_ids: List[int] = []
    upsell_ids: List[int] = []
    cross_sell_ids: List[int] = []
    parent_id: Optional[int] = None
    purchase_note: Optional[str] = None
    categories: List[ProductCategory]
    tags: List[ProductTag] = []
    images: List[ProductImage] = []
    attributes: List[ProductAttribute] = []
    grouped_products: List[int] = []
    meta_data: List[MetaData] = []
    variations: List[int] = []


class ProductVariation(BaseModel):
    id: Optional[int] = None
    permalink: Optional[str] = None
    date_created: Optional[datetime] = None
    status: Literal["draft", "pending", "private", "publish"] = "publish"
    description: str = ""
    sku: Optional[str] = None
    price: Optional[str] = None
    regular_price: Optional[str] = None
    sale_price: Optional[str] = None
    date_on_sale_from: Optional[datetime] = None
    date_on_sale_from_gmt: Optional[datetime] = None
    date_on_sale_to: Optional[datetime] = None
    date_on_sale_to_gmt: Optional[datetime] = None
    price_html: Optional[str] = None
    on_sale: bool = False
    purchasable: bool = True
    total_sales: Optional[int] = None
    virtual: bool = False
    downloadable: bool = False
    downloads: List[ProductDownload] = []
    download_limit: int = -1
    download_expiry: int = -1
    tax_status: Literal["taxable", "shipping", "none"] = "taxable"
    tax_class: Optional[str] = None
    manage_stock: bool = False
    stock_quantity: Optional[int] = None
    stock_status: Literal["instock", "outofstock", "onbackorder"] = "instock"
    backorders: Literal["no", "notify", "yes"] = "no"
    backorders_allowed: Optional[bool] = None
    backordered: Optional[bool] = None
    weight: str = ""
    dimensions: Optional[ProductDimensions] = None
    shipping_required: Optional[bool] = None
    shipping_taxable: Optional[bool] = None
    shipping_class: Optional[str] = None
    shipping_class_id: Optional[int] = None
    tags: List[ProductTag] = []
    image: Optional[ProductImage] = None
    attributes: List[ProductVariationAttribute] = []
    meta_data: List[MetaData] = []


class SimpleProduct(Product):
    type: Literal["simple"] = "simple"


class ExternalProduct(Product):
    external_url: str
    button_text: Optional[str] = None


class VariableProduct(Product):
    type: Literal["variable"] = "variable"
    variations: List[ProductVariation] = []
    default_attributes: List[ProductVariationAttribute] = []
