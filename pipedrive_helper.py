import requests
from datetime import datetime
import json
import logging

class PipedriveHelper:
  api_token = None
  product_url = "https://api.pipedrive.com/v1/products"
  person_url = "https://api.pipedrive.com/v1/persons"
  deal_url = "https://api.pipedrive.com/v1/deals"
  add_org_url = "https://api.pipedrive.com/v1/organizations"
  person_fields_url = "https://api.pipedrive.com/v1/personFields"
  org_fields_url = "https://api.pipedrive.com/v1/organizationFields"
  product_fields_url = "https://api.pipedrive.com/v1/productFields"
  deal_fields_url = "https://api.pipedrive.com/v1/dealFields"

  headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
  }

  def __init__(self, api_token):
    self.api_token = {"api_token":api_token}

  # /********** START - PERSON FUNCTIONS **********/
  def add_person(self, person_args: dict) -> dict:
    """ Add a single person to your contacts in Piprdrive """

    data = person_args
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "POST", 
      self.person_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      logging.debug("Person Created: "+str(result.status_code))

      rest_result = {}
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      rest_result["data"] = json.loads(result.text)["data"]

      logging.debug(rest_result["data"])
      
      return rest_result
    else:
      raise ValueError(result.content)

  # /********** END - PERSON FUNCTIONS **********/

  # /********** START - PRODUCT FUNCTIONS **********/
  def add_product(self, product_args: dict) -> dict:
    """ Add a single person to your contacts in Piprdrive """
    data = product_args
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "POST", 
      self.product_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      # logging.debug("Product Created: "+str(result.status_code))

      rest_result = {}
      rest_result["data"] = "Product Created: "+str(result.status_code)
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)
  
  def update_product(self, product_args: dict, product_id: str):
    update_url = self.product_url+r"/"+product_id

    data = product_args
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time

    result = requests.request(
      "PUT", 
      update_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      # logging.debug("Product Updated: "+str(result.status_code))

      rest_result = {}
      rest_result["data"] = "Product Updated: "+str(result.status_code)
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)
  
  def delete_product(self, product_id: str):
    delete_url = self.product_url+r"/"+product_id

    result = requests.request(
      "DELETE", 
      delete_url, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "OK"):
      # logging.debug("Product Deleted: "+str(result.status_code))

      rest_result = {}
      rest_result["data"] = "Product Deleted: "+str(result.status_code)
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      return rest_result
    else:
      raise ValueError(result.content)

  # /********** END - PRODUCT FUNCTIONS **********/

  # /********** START - DEAL FUNCTIONS **********/
  def add_deal_custom(self, deal_args: dict):
    data = deal_args
    add_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data["add_time"] = add_time
    
    result = requests.request(
      "POST", 
      self.deal_url, 
      data=data, 
      headers=self.headers, 
      params=self.api_token
    )

    if(result.reason == "Created"):
      logging.debug("Deal Created: "+str(result.status_code))
      rest_result = {}
      rest_result["headers"] = (
        result.headers._store['x-ratelimit-limit'], 
        result.headers._store['x-ratelimit-remaining'],
        result.headers._store['x-ratelimit-reset'],
        result.headers._store['x-daily-requests-left']
      )
      rest_result["data"] = json.loads(result.text)["data"]
      return rest_result
    else:
      raise ValueError(result.content)
  # /********** END - DEAL FUNCTIONS **********/

if(__name__ == "__main__"):
  pipedrivehelper = PipedriveHelper(api_token='c1bb21ca57499126de776a86815cee1e70480709')
  data = {
    "name": "YAKUZA 0",
    "89eb02cf19edfffc65ad3f54cc696561f5a5085f": "Ryu ga Gotoku Studios",
    "d5055cfbacfe85a2eca715dae62d0544a924f36c": "Action Adventure, Open-World",
    "74f20ffc505c9708d4f0958333b0cc1df74a2ee9": 92,
    "38669eac9be36017c339ef6d9d7db63ab2534376": "M"
  }
  rest_result = pipedrivehelper.add_product(data)
  # rest_result = pipedrivehelper.update_product(data, "1")
  # rest_result = pipedrivehelper.delete_product("2")
  pass

