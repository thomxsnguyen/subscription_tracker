import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.asset_report_get_request import AssetReportGetRequest
import json
from configuration import secret, client_id

#https://sandbox.plaid.com (Sandbox)

configuration = plaid.Configuration(host=plaid.Environment.Sandbox, api_key={'clientId': client_id, 'secret': secret})

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)


def error():
  try:
      request = AssetReportGetRequest(
          asset_report_token=asset_report_token,
      )
      return client.asset_report_get(request)
  except plaid.ApiException as e:
      response = json.loads(e.body)
      if response['error_code'] == 'ITEM_LOGIN_REQURED':
          return ""
      else:
          return ""
      
def create_link():
    exchange_request = ItemPublicTokenExchangeRequest(
        public_token=pt_response['public_token']
    )
    exchange_response = client.item_public_token_exchange(exchange_request)
    access_token = exchange_response['access_token']


