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


class Game(object):

    def __init__(self, params=None):
        if params is None:
            self.__game_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__service_class = None
            self.__offline_transfer = None
            self.__notification_url = None
            self.__notification_firebase_server_key = None
            self.__create_certificate_trigger_script = None
            self.__create_certificate_done_trigger_script = None
            self.__delete_certificate_trigger_script = None
            self.__delete_certificate_done_trigger_script = None
            self.__publish_trigger_script = None
            self.__publish_done_trigger_script = None
            self.__set_firebase_token_trigger_script = None
            self.__set_firebase_token_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_game_id(params['gameId'] if 'gameId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_offline_transfer(params['offlineTransfer'] if 'offlineTransfer' in params.keys() else None)
            self.set_notification_url(params['notificationUrl'] if 'notificationUrl' in params.keys() else None)
            self.set_notification_firebase_server_key(params['notificationFirebaseServerKey'] if 'notificationFirebaseServerKey' in params.keys() else None)
            self.set_create_certificate_trigger_script(params['createCertificateTriggerScript'] if 'createCertificateTriggerScript' in params.keys() else None)
            self.set_create_certificate_done_trigger_script(params['createCertificateDoneTriggerScript'] if 'createCertificateDoneTriggerScript' in params.keys() else None)
            self.set_delete_certificate_trigger_script(params['deleteCertificateTriggerScript'] if 'deleteCertificateTriggerScript' in params.keys() else None)
            self.set_delete_certificate_done_trigger_script(params['deleteCertificateDoneTriggerScript'] if 'deleteCertificateDoneTriggerScript' in params.keys() else None)
            self.set_publish_trigger_script(params['publishTriggerScript'] if 'publishTriggerScript' in params.keys() else None)
            self.set_publish_done_trigger_script(params['publishDoneTriggerScript'] if 'publishDoneTriggerScript' in params.keys() else None)
            self.set_set_firebase_token_trigger_script(params['setFirebaseTokenTriggerScript'] if 'setFirebaseTokenTriggerScript' in params.keys() else None)
            self.set_set_firebase_token_done_trigger_script(params['setFirebaseTokenDoneTriggerScript'] if 'setFirebaseTokenDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_game_id(self):
        """
        ゲームIDを取得
        :return: ゲームID
        :rtype: unicode
        """
        return self.__game_id

    def set_game_id(self, game_id):
        """
        ゲームIDを設定
        :param game_id: ゲームID
        :type game_id: unicode
        """
        self.__game_id = game_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

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
        self.__name = name

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

    def get_offline_transfer(self):
        """
        対象がオフライン時使用する転送方式を取得
        :return: 対象がオフライン時使用する転送方式
        :rtype: unicode
        """
        return self.__offline_transfer

    def set_offline_transfer(self, offline_transfer):
        """
        対象がオフライン時使用する転送方式を設定
        :param offline_transfer: 対象がオフライン時使用する転送方式
        :type offline_transfer: unicode
        """
        self.__offline_transfer = offline_transfer

    def get_notification_url(self):
        """
        http/https を選択した際の転送先URLを取得
        :return: http/https を選択した際の転送先URL
        :rtype: unicode
        """
        return self.__notification_url

    def set_notification_url(self, notification_url):
        """
        http/https を選択した際の転送先URLを設定
        :param notification_url: http/https を選択した際の転送先URL
        :type notification_url: unicode
        """
        self.__notification_url = notification_url

    def get_notification_firebase_server_key(self):
        """
        fcm を選択した際の Firebase サーバーキーを取得
        :return: fcm を選択した際の Firebase サーバーキー
        :rtype: unicode
        """
        return self.__notification_firebase_server_key

    def set_notification_firebase_server_key(self, notification_firebase_server_key):
        """
        fcm を選択した際の Firebase サーバーキーを設定
        :param notification_firebase_server_key: fcm を選択した際の Firebase サーバーキー
        :type notification_firebase_server_key: unicode
        """
        self.__notification_firebase_server_key = notification_firebase_server_key

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
        self.__create_certificate_trigger_script = create_certificate_trigger_script

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
        self.__create_certificate_done_trigger_script = create_certificate_done_trigger_script

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
        self.__delete_certificate_trigger_script = delete_certificate_trigger_script

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
        self.__delete_certificate_done_trigger_script = delete_certificate_done_trigger_script

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
        self.__publish_trigger_script = publish_trigger_script

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
        self.__publish_done_trigger_script = publish_done_trigger_script

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
        self.__set_firebase_token_trigger_script = set_firebase_token_trigger_script

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
        self.__set_firebase_token_done_trigger_script = set_firebase_token_done_trigger_script

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def to_dict(self):
        return {
            "gameId": self.__game_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "serviceClass": self.__service_class,
            "offlineTransfer": self.__offline_transfer,
            "notificationUrl": self.__notification_url,
            "notificationFirebaseServerKey": self.__notification_firebase_server_key,
            "createCertificateTriggerScript": self.__create_certificate_trigger_script,
            "createCertificateDoneTriggerScript": self.__create_certificate_done_trigger_script,
            "deleteCertificateTriggerScript": self.__delete_certificate_trigger_script,
            "deleteCertificateDoneTriggerScript": self.__delete_certificate_done_trigger_script,
            "publishTriggerScript": self.__publish_trigger_script,
            "publishDoneTriggerScript": self.__publish_done_trigger_script,
            "setFirebaseTokenTriggerScript": self.__set_firebase_token_trigger_script,
            "setFirebaseTokenDoneTriggerScript": self.__set_firebase_token_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
