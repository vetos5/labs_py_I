from orgDictionary import *

print("Org list:")
display_orgs()


add_org(4, "Org D", generate_api_key("Org D", "2023-04-01"), "userD@example.com", "2023-04-01")
print("\nOrg added:")
display_orgs()


update_org(2, user="new_userB@example.com")
print("\nOrg updated :")
display_orgs()


delete_org(1)
print("\nID 1 org deleted:")
display_orgs()
