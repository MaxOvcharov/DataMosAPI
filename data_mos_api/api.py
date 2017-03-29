# -*- coding: utf-8 -*-

import pprint

import requests
from requests import Session, Request

from local_settings import DATA_MOS_RU_API_KEY


class DataMosApi(object):

    @staticmethod
    def method_get(method, values=None):
        response = requests.get('https://apidata.mos.ru/v1/{0}'.format(method), params=values)
        print response.url

        if response.status_code == 200:
            return response.json()
        else: # TODO - use custom exceptions
            message = "A request to the DataMos API was unsuccessful. The server returned HTTP {0} {1}."
            return message.format(response.status_code, response.reason)

    @staticmethod
    def method_post(method, data_list=None):
        s = Session()
        req = Request('POST', 'https://apidata.mos.ru/v1/{0}'.format(method))
        prepped = req.prepare()
        prepped.body = data_list
        response = s.send(prepped)

        # response = requests.post('https://apidata.mos.ru/v1/{0}'.format(method), data=data_list)
        # print response.url

        if response.status_code == 200:
            return response.json()
        else:  # TODO - use custom exceptions
            message = "A request to the DataMos API was unsuccessful. The server returned HTTP {0} {1}."
            return message.format(response.status_code, response.reason)


class DataMos:
    __slots__ = '_data_mos'

    def __init__(self):
        self._data_mos = DataMosApi()

    def datasets_get(self, api_key, top=None, skip=None,
                 inlinecount=None, orderby=None,
                 filter=None, foreign=None):
        values = locals().copy()
        values.pop('self')
        for header, value in values.items():
            if value is not None:
                if header == 'foreign' or header == 'api_key':
                    values[header] = str(value).lower()
                else:
                    values["${0}".format(header)] = value
        return self._data_mos.method_get('datasets', values=values)

    def datasets_post(self, api_key, data_list=None):
        # data_list = locals().copy()
        # data_list.pop('self')
        # for header, value in values.items():
        #     if value is not None:
        #         if header == 'foreign' or header == 'api_key':
        #             values[header] = str(value).lower()
        #         else:
        #             values["${0}".format(header)] = value
        return self._data_mos.method_post('datasets', data_list=data_list)


if __name__ == "__main__":
    data_mos_ru_api = DataMos()
    # datasets_get = data_mos_ru_api.datasets_get(DATA_MOS_RU_API_KEY,
    #                                     top=5,
    #                                     inlinecount='allpages',
    #                                     filter='CategoryId eq 9',
    #                                     foreign="true")

    datasets_post = data_mos_ru_api.datasets_post(DATA_MOS_RU_API_KEY,
                                                  ["Id", "Caption", "SefUrl"])
    # pprint.pprint(datasets_get)
