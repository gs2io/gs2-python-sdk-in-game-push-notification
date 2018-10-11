# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.


class WebSocketHost(object):

    def __init__(self, params=None):
        if params is None:
            self.__game_id = None
            self.__endpoint = None
            self.__root_certificate = None
        else:
            self.set_game_id(params['gameId'] if 'gameId' in params.keys() else None)
            self.set_endpoint(params['endpoint'] if 'endpoint' in params.keys() else None)
            self.set_root_certificate(params['rootCertificate'] if 'rootCertificate' in params.keys() else None)

    def get_game_id(self):
        """
        ゲームGRNを取得
        :return: ゲームGRN
        :rtype: unicode
        """
        return self.__game_id

    def set_game_id(self, game_id):
        """
        ゲームGRNを設定
        :param game_id: ゲームGRN
        :type game_id: unicode
        """
        self.__game_id = game_id

    def get_endpoint(self):
        """
        エンドポイント名を取得
        :return: エンドポイント名
        :rtype: unicode
        """
        return self.__endpoint

    def set_endpoint(self, endpoint):
        """
        エンドポイント名を設定
        :param endpoint: エンドポイント名
        :type endpoint: unicode
        """
        self.__endpoint = endpoint

    def get_root_certificate(self):
        """
        ルート証明書を取得
        :return: ルート証明書
        :rtype: unicode
        """
        return self.__root_certificate

    def set_root_certificate(self, root_certificate):
        """
        ルート証明書を設定
        :param root_certificate: ルート証明書
        :type root_certificate: unicode
        """
        self.__root_certificate = root_certificate

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(WebSocketHost, self).__getitem__(key)

    def to_dict(self):
        return {
            "gameId": self.__game_id,
            "endpoint": self.__endpoint,
            "rootCertificate": self.__root_certificate,
        }
