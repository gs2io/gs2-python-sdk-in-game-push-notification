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

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_in_game_push_notification_client.Gs2InGamePushNotification import Gs2InGamePushNotification


class UpdateGameRequest(Gs2BasicRequest):

    class Constant(Gs2InGamePushNotification):
        FUNCTION = "UpdateGame"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateGameRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
            self.__notification_url = None
            self.__service_class = None
            self.__notification_firebase_server_key = None
            self.__offline_transfer = None
            self.__description = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
            self.set_notification_url(params['notificationUrl'] if 'notificationUrl' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_notification_firebase_server_key(params['notificationFirebaseServerKey'] if 'notificationFirebaseServerKey' in params.keys() else None)
            self.set_offline_transfer(params['offlineTransfer'] if 'offlineTransfer' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)

    def get_game_name(self):
        """
        ゲームの名前を取得
        :return: ゲームの名前
        :rtype: unicode
        """
        return self.__game_name

    def set_game_name(self, game_name):
        """
        ゲームの名前を設定
        :param game_name: ゲームの名前
        :type game_name: unicode
        """
        self.__game_name = game_name

    def with_game_name(self, game_name):
        """
        ゲームの名前を設定
        :param game_name: ゲームの名前
        :type game_name: unicode
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_game_name(game_name)
        return self

    def get_notification_url(self):
        """
        オフライン転送先URLを取得
        :return: オフライン転送先URL
        :rtype: unicode
        """
        return self.__notification_url

    def set_notification_url(self, notification_url):
        """
        オフライン転送先URLを設定
        :param notification_url: オフライン転送先URL
        :type notification_url: unicode
        """
        self.__notification_url = notification_url

    def with_notification_url(self, notification_url):
        """
        オフライン転送先URLを設定
        :param notification_url: オフライン転送先URL
        :type notification_url: unicode
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_notification_url(notification_url)
        return self

    def get_service_class(self):
        """
        サービスクラスを取得
        :return: サービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

    def with_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_service_class(service_class)
        return self

    def get_notification_firebase_server_key(self):
        """
        Firebaseのサーバーキーを取得
        :return: Firebaseのサーバーキー
        :rtype: unicode
        """
        return self.__notification_firebase_server_key

    def set_notification_firebase_server_key(self, notification_firebase_server_key):
        """
        Firebaseのサーバーキーを設定
        :param notification_firebase_server_key: Firebaseのサーバーキー
        :type notification_firebase_server_key: unicode
        """
        self.__notification_firebase_server_key = notification_firebase_server_key

    def with_notification_firebase_server_key(self, notification_firebase_server_key):
        """
        Firebaseのサーバーキーを設定
        :param notification_firebase_server_key: Firebaseのサーバーキー
        :type notification_firebase_server_key: unicode
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_notification_firebase_server_key(notification_firebase_server_key)
        return self

    def get_offline_transfer(self):
        """
        オフライン転送方式を取得
        :return: オフライン転送方式
        :rtype: unicode
        """
        return self.__offline_transfer

    def set_offline_transfer(self, offline_transfer):
        """
        オフライン転送方式を設定
        :param offline_transfer: オフライン転送方式
        :type offline_transfer: unicode
        """
        self.__offline_transfer = offline_transfer

    def with_offline_transfer(self, offline_transfer):
        """
        オフライン転送方式を設定
        :param offline_transfer: オフライン転送方式
        :type offline_transfer: unicode
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_offline_transfer(offline_transfer)
        return self

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: UpdateGameRequest
        """
        self.set_description(description)
        return self
