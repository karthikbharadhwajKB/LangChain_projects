import json
import requests
import os
from typing import Dict

api_key = os.environ["PROXYCURL_API_KEY"]


def scrape_linkedIn_profile(linkedin_profile, use_api=False):
    """Scrapes given LinkedIn profile."""
    if use_api:
        headers = {"Authorization": "Bearer " + api_key}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {"linkedin_profile_url": linkedin_profile}
        response = requests.get(api_endpoint, params=params, headers=headers)

        return response.json()
    else:
        with open("data.json", "r") as f:
            data = json.load(f)
        return data


def data_preprocessing(data: Dict):
    """Does the preprocessing on json object
    Removes empty list, empty data.
    Cleaning the payloads"""
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", " ", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    # poping out profile_pic_url
    data.pop("profile_pic_url")

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


# linked_profile = "https://www.linkedin.com/in/williamhgates/"

# #response = get_response(linked_profile)

# response = '{"public_identifier": "williamhgates", "profile_pic_url": "https://s3.us-west-000.backblazeb2.com/proxycurl/person/williamhgates/profile?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=0004d7f56a0400b0000000001%2F20240211%2Fus-west-000%2Fs3%2Faws4_request&X-Amz-Date=20240211T055556Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=0b44e8652fb9377b5d1e259e9d2a5a0e925e5cf782b5b0af6f098a8b38fcfc7d", "background_cover_image_url": null, "first_name": "Bill", "last_name": "Gates", "full_name": "Bill Gates", "follower_count": 35017520, "occupation": "Co-chair at Bill & Melinda Gates Foundation", "headline": "Co-chair, Bill & Melinda Gates Foundation", "summary": "Co-chair of the Bill & Melinda Gates Foundation. Founder of Breakthrough Energy. Co-founder of Microsoft. Voracious reader. Avid traveler. Active blogger.", "country": "US", "country_full_name": "United States of America", "city": null, "state": null, "experiences": [{"starts_at": {"day": 1, "month": 1, "year": 2000}, "ends_at": null, "company": "Bill & Melinda Gates Foundation", "company_linkedin_profile_url": "https://www.linkedin.com/company/bill-&-melinda-gates-foundation", "title": "Co-chair", "description": null, "location": null, "logo_url": "https://media.licdn.com/dms/image/C4E0BAQE7Na_mKQhIJg/company-logo_400_400/0/1633731811337/bill__melinda_gates_foundation_logo?e=1713398400&v=beta&t=TIfwfhnwSKEBfVBabRcKAxx1si31IL-RL2VyQZwSF40"}, {"starts_at": {"day": 1, "month": 1, "year": 2015}, "ends_at": null, "company": "Breakthrough Energy ", "company_linkedin_profile_url": "https://www.linkedin.com/company/breakthrough-energy", "title": "Founder", "description": null, "location": null, "logo_url": "https://media.licdn.com/dms/image/C4D0BAQGwD9vNu044FA/company-logo_400_400/0/1630531940051/breakthrough_energy_ventures_logo?e=1713398400&v=beta&t=DuHR8fEorMAf9L5Jh-8nrL_AuNdp8w3k3CdnKAycXIo"}, {"starts_at": {"day": 1, "month": 1, "year": 1975}, "ends_at": null, "company": "Microsoft", "company_linkedin_profile_url": "https://www.linkedin.com/company/microsoft", "title": "Co-founder", "description": null, "location": null, "logo_url": "https://media.licdn.com/dms/image/C560BAQE88xCsONDULQ/company-logo_400_400/0/1630652622688/microsoft_logo?e=1713398400&v=beta&t=18Ii3c8i1PvAsIxZ7n66dq04q0xONLctUifQVNxGwIY"}], "education": [{"starts_at": {"day": 1, "month": 1, "year": 1973}, "ends_at": {"day": 31, "month": 12, "year": 1975}, "field_of_study": null, "degree_name": null, "school": "Harvard University", "school_linkedin_profile_url": "https://www.linkedin.com/company/1646/", "description": null, "logo_url": "https://media.licdn.com/dms/image/C4E0BAQF5t62bcL0e9g/company-logo_400_400/0/1631318058235?e=1713398400&v=beta&t=UhxxEys9Sgv-Wa4BUXxkL2PSwLg0TiFYPtDzeDybkBU", "grade": null, "activities_and_societies": null}, {"starts_at": null, "ends_at": null, "field_of_study": null, "degree_name": null, "school": "Lakeside School", "school_linkedin_profile_url": "https://www.linkedin.com/company/30288/", "description": null, "logo_url": "https://media.licdn.com/dms/image/D560BAQGFmOQmzpxg9A/company-logo_400_400/0/1683732883164/lakeside_school_logo?e=1713398400&v=beta&t=NnPJcnk3KbJI_XCdSknhWEQ-JkqN8bQq-a4KFi50tHg", "grade": null, "activities_and_societies": null}], "languages": [], "accomplishment_organisations": [], "accomplishment_publications": [], "accomplishment_honors_awards": [], "accomplishment_patents": [], "accomplishment_courses": [], "accomplishment_projects": [], "accomplishment_test_scores": [], "volunteer_work": [], "certifications": [], "connections": 9, "people_also_viewed": [], "recommendations": [], "activities": [], "similarly_named_profiles": [{"name": "Bill Gates", "link": "https://www.linkedin.com/in/bill-gates-610", "summary": "Looking for connections within the IT field.", "location": "Whitehall, PA"}, {"name": "Bill Gates", "link": "https://www.linkedin.com/in/bill-gates-50939b1a1", "summary": "Janitor at Bill Gates Associates", "location": "Tompkins County, NY"}, {"name": "Bill Gates", "link": "https://www.linkedin.com/in/bill-gates-b3320919", "summary": "GATES Solid Gold Investments ,Inc  LLC", "location": "Santa Rosa, CA"}, {"name": "Bill Gates", "link": "https://www.linkedin.com/in/bill-gates-03935451", "summary": "President & CEO at Bedford Materials, AIM Global Logistics", "location": "Boca Raton, FL"}], "articles": [], "groups": [], "skills": [], "inferred_salary": null, "gender": null, "birth_date": null, "industry": null, "extra": null, "interests": [], "personal_emails": [], "personal_numbers": []}'

# # loading json from str format (deserialize)
# data = json.loads(response)

# with open('data.json', 'w') as f:
#     json.dump(data, f)
