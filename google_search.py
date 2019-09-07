import google_module



site_counter = []
sites = []

google_module.get_urls()


for x in google_module.get_pages_at_bottom():
    sites.append(x)
    
#print(sites)
print(google_module.get_page_nums())
print(google_module.get_page_n_on())
print(google_module.get_searches())
