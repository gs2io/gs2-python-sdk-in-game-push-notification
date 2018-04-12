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


class CreateGameRequest(Gs2BasicRequest):

    class Constant(Gs2InGamePushNotification):
        FUNCTION = "CreateGame"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateGameRequest, self).__init__(params)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__description = None
        else:
            self.set_description(params['description'] if 'description' in params.keys() else None)
        if params is None:
            self.__service_class = None
        else:
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
        if params is None:
            self.__offline_transfer = None
        else:
            self.set_offline_transfer(params['offlineTransfer'] if 'offlineTransfer' in params.keys() else None)
        if params is None:
            self.__notification_url = None
        else:
            self.set_notification_url(params['notificationUrl'] if 'notificationUrl' in params.keys() else None)
        if params is None:
            self.__notification_firebase_server_key = None
        else:
            self.set_notification_firebase_server_key(params['notificationFirebaseServerKey'] if 'notificationFirebaseServerKey' in params.keys() else None)
        if params is None:
            self.__create_certificate_trigger_script = None
        else:
            self.set_create_certificate_trigger_script(params['createCertificateTriggerScript'] if 'createCertificateTriggerScript' in params.keys() else None)
        if params is None:
            self.__create_certificate_done_trigger_script = None
        else:
            self.set_create_certificate_done_trigger_script(params['createCertificateDoneTriggerScript'] if 'createCertificateDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__delete_certificate_trigger_script = None
        else:
            self.set_delete_certificate_trigger_script(params['deleteCertificateTriggerScript'] if 'deleteCertificateTriggerScript' in params.keys() else None)
        if params is None:
            self.__delete_certificate_done_trigger_script = None
        else:
            self.set_delete_certificate_done_trigger_script(params['deleteCertificateDoneTriggerScript'] if 'deleteCertificateDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__publish_trigger_script = None
        else:
            self.set_publish_trigger_script(params['publishTriggerScript'] if 'publishTriggerScript' in params.keys() else None)
        if params is None:
            self.__publish_done_trigger_script = None
        else:
            self.set_publish_done_trigger_script(params['publishDoneTriggerScript'] if 'publishDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__set_firebase_token_trigger_script = None
        else:
            self.set_set_firebase_token_trigger_script(params['setFirebaseTokenTriggerScript'] if 'setFirebaseTokenTriggerScript' in params.keys() else None)
        if params is None:
            self.__set_firebase_token_done_trigger_script = None
        else:
            self.set_set_firebase_token_done_trigger_script(params['setFirebaseTokenDoneTriggerScript'] if 'setFirebaseTokenDoneTriggerScript' in params.keys() else None)

    def get_name(self):
        """
        ゲーム名を取得
        :return: ゲーム名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        ゲーム名を設定
        :param name: ゲーム名
        :type name: unicode
        """
        if not isinstance(name, unicode):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        ゲーム名を設定
        :param name: ゲーム名
        :type name: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_name(name)
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
        if not isinstance(description, unicode):
            raise TypeError(type(description))
        self.__description = description

    def with_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_description(description)
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
        if not isinstance(service_class, unicode):
            raise TypeError(type(service_class))
        self.__service_class = service_class

    def with_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_service_class(service_class)
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
        if not isinstance(offline_transfer, unicode):
            raise TypeError(type(offline_transfer))
        self.__offline_transfer = offline_transfer

    def with_offline_transfer(self, offline_transfer):
        """
        オフライン転送方式を設定
        :param offline_transfer: オフライン転送方式
        :type offline_transfer: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_offline_transfer(offline_transfer)
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
        if not isinstance(notification_url, unicode):
            raise TypeError(type(notification_url))
        self.__notification_url = notification_url

    def with_notification_url(self, notification_url):
        """
        オフライン転送先URLを設定
        :param notification_url: オフライン転送先URL
        :type notification_url: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_notification_url(notification_url)
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
        if not isinstance(notification_firebase_server_key, unicode):
            raise TypeError(type(notification_firebase_server_key))
        self.__notification_firebase_server_key = notification_firebase_server_key

    def with_notification_firebase_server_key(self, notification_firebase_server_key):
        """
        Firebaseのサーバーキーを設定
        :param notification_firebase_server_key: Firebaseのサーバーキー
        :type notification_firebase_server_key: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_notification_firebase_server_key(notification_firebase_server_key)
        return self

    def get_create_certificate_trigger_script(self):
        """
        クライアント証明書発行時 に実行されるGS2-Scriptを取得
        :return: クライアント証明書発行時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_certificate_trigger_script

    def set_create_certificate_trigger_script(self, create_certificate_trigger_script):
        """
        クライアント証明書発行時 に実行されるGS2-Scriptを設定
        :param create_certificate_trigger_script: クライアント証明書発行時 に実行されるGS2-Script
        :type create_certificate_trigger_script: unicode
        """
        if not isinstance(create_certificate_trigger_script, unicode):
            raise TypeError(type(create_certificate_trigger_script))
        self.__create_certificate_trigger_script = create_certificate_trigger_script

    def with_create_certificate_trigger_script(self, create_certificate_trigger_script):
        """
        クライアント証明書発行時 に実行されるGS2-Scriptを設定
        :param create_certificate_trigger_script: クライアント証明書発行時 に実行されるGS2-Script
        :type create_certificate_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_create_certificate_trigger_script(create_certificate_trigger_script)
        return self

    def get_create_certificate_done_trigger_script(self):
        """
        クライアント証明書発行完了時 に実行されるGS2-Scriptを取得
        :return: クライアント証明書発行完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__create_certificate_done_trigger_script

    def set_create_certificate_done_trigger_script(self, create_certificate_done_trigger_script):
        """
        クライアント証明書発行完了時 に実行されるGS2-Scriptを設定
        :param create_certificate_done_trigger_script: クライアント証明書発行完了時 に実行されるGS2-Script
        :type create_certificate_done_trigger_script: unicode
        """
        if not isinstance(create_certificate_done_trigger_script, unicode):
            raise TypeError(type(create_certificate_done_trigger_script))
        self.__create_certificate_done_trigger_script = create_certificate_done_trigger_script

    def with_create_certificate_done_trigger_script(self, create_certificate_done_trigger_script):
        """
        クライアント証明書発行完了時 に実行されるGS2-Scriptを設定
        :param create_certificate_done_trigger_script: クライアント証明書発行完了時 に実行されるGS2-Script
        :type create_certificate_done_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_create_certificate_done_trigger_script(create_certificate_done_trigger_script)
        return self

    def get_delete_certificate_trigger_script(self):
        """
        クライアント証明書削除時 に実行されるGS2-Scriptを取得
        :return: クライアント証明書削除時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__delete_certificate_trigger_script

    def set_delete_certificate_trigger_script(self, delete_certificate_trigger_script):
        """
        クライアント証明書削除時 に実行されるGS2-Scriptを設定
        :param delete_certificate_trigger_script: クライアント証明書削除時 に実行されるGS2-Script
        :type delete_certificate_trigger_script: unicode
        """
        if not isinstance(delete_certificate_trigger_script, unicode):
            raise TypeError(type(delete_certificate_trigger_script))
        self.__delete_certificate_trigger_script = delete_certificate_trigger_script

    def with_delete_certificate_trigger_script(self, delete_certificate_trigger_script):
        """
        クライアント証明書削除時 に実行されるGS2-Scriptを設定
        :param delete_certificate_trigger_script: クライアント証明書削除時 に実行されるGS2-Script
        :type delete_certificate_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_delete_certificate_trigger_script(delete_certificate_trigger_script)
        return self

    def get_delete_certificate_done_trigger_script(self):
        """
        クライアント証明書削除完了時 に実行されるGS2-Scriptを取得
        :return: クライアント証明書削除完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__delete_certificate_done_trigger_script

    def set_delete_certificate_done_trigger_script(self, delete_certificate_done_trigger_script):
        """
        クライアント証明書削除完了時 に実行されるGS2-Scriptを設定
        :param delete_certificate_done_trigger_script: クライアント証明書削除完了時 に実行されるGS2-Script
        :type delete_certificate_done_trigger_script: unicode
        """
        if not isinstance(delete_certificate_done_trigger_script, unicode):
            raise TypeError(type(delete_certificate_done_trigger_script))
        self.__delete_certificate_done_trigger_script = delete_certificate_done_trigger_script

    def with_delete_certificate_done_trigger_script(self, delete_certificate_done_trigger_script):
        """
        クライアント証明書削除完了時 に実行されるGS2-Scriptを設定
        :param delete_certificate_done_trigger_script: クライアント証明書削除完了時 に実行されるGS2-Script
        :type delete_certificate_done_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_delete_certificate_done_trigger_script(delete_certificate_done_trigger_script)
        return self

    def get_publish_trigger_script(self):
        """
        通知送信時 に実行されるGS2-Scriptを取得
        :return: 通知送信時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__publish_trigger_script

    def set_publish_trigger_script(self, publish_trigger_script):
        """
        通知送信時 に実行されるGS2-Scriptを設定
        :param publish_trigger_script: 通知送信時 に実行されるGS2-Script
        :type publish_trigger_script: unicode
        """
        if not isinstance(publish_trigger_script, unicode):
            raise TypeError(type(publish_trigger_script))
        self.__publish_trigger_script = publish_trigger_script

    def with_publish_trigger_script(self, publish_trigger_script):
        """
        通知送信時 に実行されるGS2-Scriptを設定
        :param publish_trigger_script: 通知送信時 に実行されるGS2-Script
        :type publish_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_publish_trigger_script(publish_trigger_script)
        return self

    def get_publish_done_trigger_script(self):
        """
        通知送信完了時 に実行されるGS2-Scriptを取得
        :return: 通知送信完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__publish_done_trigger_script

    def set_publish_done_trigger_script(self, publish_done_trigger_script):
        """
        通知送信完了時 に実行されるGS2-Scriptを設定
        :param publish_done_trigger_script: 通知送信完了時 に実行されるGS2-Script
        :type publish_done_trigger_script: unicode
        """
        if not isinstance(publish_done_trigger_script, unicode):
            raise TypeError(type(publish_done_trigger_script))
        self.__publish_done_trigger_script = publish_done_trigger_script

    def with_publish_done_trigger_script(self, publish_done_trigger_script):
        """
        通知送信完了時 に実行されるGS2-Scriptを設定
        :param publish_done_trigger_script: 通知送信完了時 に実行されるGS2-Script
        :type publish_done_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_publish_done_trigger_script(publish_done_trigger_script)
        return self

    def get_set_firebase_token_trigger_script(self):
        """
        Firebaseデバイストークン登録時 に実行されるGS2-Scriptを取得
        :return: Firebaseデバイストークン登録時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__set_firebase_token_trigger_script

    def set_set_firebase_token_trigger_script(self, set_firebase_token_trigger_script):
        """
        Firebaseデバイストークン登録時 に実行されるGS2-Scriptを設定
        :param set_firebase_token_trigger_script: Firebaseデバイストークン登録時 に実行されるGS2-Script
        :type set_firebase_token_trigger_script: unicode
        """
        if not isinstance(set_firebase_token_trigger_script, unicode):
            raise TypeError(type(set_firebase_token_trigger_script))
        self.__set_firebase_token_trigger_script = set_firebase_token_trigger_script

    def with_set_firebase_token_trigger_script(self, set_firebase_token_trigger_script):
        """
        Firebaseデバイストークン登録時 に実行されるGS2-Scriptを設定
        :param set_firebase_token_trigger_script: Firebaseデバイストークン登録時 に実行されるGS2-Script
        :type set_firebase_token_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_set_firebase_token_trigger_script(set_firebase_token_trigger_script)
        return self

    def get_set_firebase_token_done_trigger_script(self):
        """
        Firebaseデバイストークン登録完了時 に実行されるGS2-Scriptを取得
        :return: Firebaseデバイストークン登録完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__set_firebase_token_done_trigger_script

    def set_set_firebase_token_done_trigger_script(self, set_firebase_token_done_trigger_script):
        """
        Firebaseデバイストークン登録完了時 に実行されるGS2-Scriptを設定
        :param set_firebase_token_done_trigger_script: Firebaseデバイストークン登録完了時 に実行されるGS2-Script
        :type set_firebase_token_done_trigger_script: unicode
        """
        if not isinstance(set_firebase_token_done_trigger_script, unicode):
            raise TypeError(type(set_firebase_token_done_trigger_script))
        self.__set_firebase_token_done_trigger_script = set_firebase_token_done_trigger_script

    def with_set_firebase_token_done_trigger_script(self, set_firebase_token_done_trigger_script):
        """
        Firebaseデバイストークン登録完了時 に実行されるGS2-Scriptを設定
        :param set_firebase_token_done_trigger_script: Firebaseデバイストークン登録完了時 に実行されるGS2-Script
        :type set_firebase_token_done_trigger_script: unicode
        :return: this
        :rtype: CreateGameRequest
        """
        self.set_set_firebase_token_done_trigger_script(set_firebase_token_done_trigger_script)
        return self
