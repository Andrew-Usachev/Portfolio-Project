'''
This file contains pydantic schemas for validation
'''

from pydantic import BaseModel, EmailStr, HttpUrl, validator


class LoginResponseSchema(BaseModel):
    id: int
    email: EmailStr
    company_name: str = None
    first_name: str = None
    last_name: str = None
    city: str = None
    country: str
    address: str = None
    cell_phone: str = None
    site: HttpUrl = None
    official_email: EmailStr = None
    founded: str = None
    team_size: int = None
    rates: float = None
    facebook: HttpUrl = None
    twitter: HttpUrl = None
    linkedin: HttpUrl = None
    instagram: HttpUrl = None
    whatsapp: str = None
    youtube: HttpUrl = None
    telegram: str = None
    github: HttpUrl = None
    behance: HttpUrl = None
    telegram_chat_id: str = None
    logo: HttpUrl = None
    position: str = None
    business_phone: str = None
    representative_photo: HttpUrl = None
    representative_name: str = ""
    description: str = None
    type: int
    is_single_developer: int
    confirmation_code: str
    confirmed: int
    verified: int
    legal_documents: int
    referral_code: str = None
    is_pro_account: int
    pro_active_until: str
    stripe_subscribed: int
    stripe_subscribe_time: str
    stripe_subscription_expires: str
    connect_points: int
    terms_accepted: int
    terms_accepted_time: str
    created: str
    updated: str
    last_login_time: str
    receive_emails: int
    receive_telegram: int
    alert_position_level_id: int = None
    alert_work: str = None
    open_to_work: str = None
    start_in: str = None
    chat_email_sent_time: str
    cv: str = None
    position_level_id: int = None
    job_title_id: int = None
    additional_job_title_id: int = None
    years_experience: int = None
    hourly_rate: float = None
    monthly_rate: float = None
    rate_currency: str = None
    degree: str = None
    prize_winner: int = None
    tried_relocating: int = None
    ready_to_relocate: int = None
    send_data_to_partners: int = None
    relocate_to_usa: int = None
    relocate_to_sweden: int = None
    profile_fill_step: int = None
    token: str

    @validator('id')
    def validate_id(cls, id_value):
        if id_value <= 0:
            raise ValueError('ID can be only positive number')
        return id_value

    @validator('email')
    def validate_email(cls, email_value):
        if '@' not in email_value or '.' not in email_value:
            raise ValueError('Wrong email format')
        return email_value

    @validator('country')
    def validate_country(cls, country_value):
        allowed_countries = ['Bahamas', 'Canada', 'USA', 'UK']
        if country_value not in allowed_countries:
            raise ValueError('Incorrect country')
        return country_value

    @validator('type')
    def validate_type(cls, type_value):
        allowed_types = [1, 2, 3]
        if type_value not in allowed_types:
            raise ValueError('Incorrect type')
        return type_value

    @validator('pro_active_until')
    def validate_pro_active_until(cls, pro_active_until_value):
        if not pro_active_until_value.startswith("20"):
            raise ValueError('Wrong format pro_active_until value')
        return pro_active_until_value
