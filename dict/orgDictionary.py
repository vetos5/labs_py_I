import hashlib


API_ERROR_MSG = 'API Already Exists'
ORG_NOT_FOUND_MSG = 'Organisation Not Found'


def generate_api_key(org_name, creation_date):
    unique_string = f"{org_name}{creation_date}"
    return hashlib.sha256(unique_string.encode()).hexdigest()


salesforce_orgs = {
    1: {"name": "Org A", "API key": generate_api_key("OrgA", "2024-01-04"), "user": "userA@example.com",
        "creation date": "2024-01-04"},
    2: {"name": "Org B", "API key": generate_api_key("OrgB", "2020-02-01"), "user": "userB@example.com",
        "creation date": "2020-02-01"},
    3: {"name": "Org C", "API key": generate_api_key("OrgC", "2018-05-10"), "user": "userC@example.com",
        "creation date": "2018-05-10"}
}


def display_orgs():
    for id, org in salesforce_orgs.items():
        print(f"ID: {id}, Name: {org['name']}, API key: {org['API key']}, "
              f"User: {org['user']}, Creation date: {org['creation date']}")


def add_org(org_id, name, api_key, user, creation_date):
    if api_key in [org["API key"] for org in salesforce_orgs.values()]:
        print(API_ERROR_MSG)
        exit(1)
    salesforce_orgs[org_id] = {"name": name, "API key": api_key, "user": user, "creation date": creation_date}


def delete_org(org_id):
    if org_id in salesforce_orgs:
        del salesforce_orgs[org_id]
    else:
        print(ORG_NOT_FOUND_MSG)
        exit(1)


def update_org(org_id, name=None, api_key=None, user=None, creation_date=None):
    if org_id in salesforce_orgs:
        if name:
            salesforce_orgs[org_id]["name"] = name
        if api_key:
            if api_key in [org["API key"] for org in salesforce_orgs.values()]:
                print(API_ERROR_MSG)
                return
            salesforce_orgs[org_id]["API key"] = api_key
        if user:
            salesforce_orgs[org_id]["user"] = user
        if creation_date:
            salesforce_orgs[org_id]["creation date"] = creation_date
    else:
        print(ORG_NOT_FOUND_MSG)
        exit(1)
