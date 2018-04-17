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


class PublishRequest(Gs2BasicRequest):

    class Constant(Gs2InGamePushNotification):
        FUNCTION = "Publish"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(PublishRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
        if params is None:
            self.__subject = None
        else:
            self.set_subject(params['subject'] if 'subject' in params.keys() else None)
        if params is None:
            self.__body = None
        else:
            self.set_body(params['body'] if 'body' in params.keys() else None)
        if params is None:
            self.__enable_offline_transfer = None
        else:
            self.set_enable_offline_transfer(params['enableOfflineTransfer'] if 'enableOfflineTransfer' in params.keys() else None)
        if params is None:
            self.__offline_transfer_sound = None
        else:
            self.set_offline_transfer_sound(params['offlineTransferSound'] if 'offlineTransferSound' in params.keys() else None)

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
        if game_name and not (isinstance(game_name, str) or isinstance(game_name, unicode)):
            raise TypeError(type(game_name))
        self.__game_name = game_name

    def with_game_name(self, game_name):
        """
        ゲームの名前を設定
        :param game_name: ゲームの名前
        :type game_name: unicode
        :return: this
        :rtype: PublishRequest
        """
        self.set_game_name(game_name)
        return self

    def get_user_id(self):
        """
        通知の送信先ユーザIDを取得
        :return: 通知の送信先ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        通知の送信先ユーザIDを設定
        :param user_id: 通知の送信先ユーザID
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        通知の送信先ユーザIDを設定
        :param user_id: 通知の送信先ユーザID
        :type user_id: unicode
        :return: this
        :rtype: PublishRequest
        """
        self.set_user_id(user_id)
        return self

    def get_subject(self):
        """
        件名を取得
        :return: 件名
        :rtype: unicode
        """
        return self.__subject

    def set_subject(self, subject):
        """
        件名を設定
        :param subject: 件名
        :type subject: unicode
        """
        if subject and not (isinstance(subject, str) or isinstance(subject, unicode)):
            raise TypeError(type(subject))
        self.__subject = subject

    def with_subject(self, subject):
        """
        件名を設定
        :param subject: 件名
        :type subject: unicode
        :return: this
        :rtype: PublishRequest
        """
        self.set_subject(subject)
        return self

    def get_body(self):
        """
        本文を取得
        :return: 本文
        :rtype: unicode
        """
        return self.__body

    def set_body(self, body):
        """
        本文を設定
        :param body: 本文
        :type body: unicode
        """
        if body and not (isinstance(body, str) or isinstance(body, unicode)):
            raise TypeError(type(body))
        self.__body = body

    def with_body(self, body):
        """
        本文を設定
        :param body: 本文
        :type body: unicode
        :return: this
        :rtype: PublishRequest
        """
        self.set_body(body)
        return self

    def get_enable_offline_transfer(self):
        """
        対象ユーザがオフラインの場合に転送を実行するかを取得
        :return: 対象ユーザがオフラインの場合に転送を実行するか
        :rtype: bool
        """
        return self.__enable_offline_transfer

    def set_enable_offline_transfer(self, enable_offline_transfer):
        """
        対象ユーザがオフラインの場合に転送を実行するかを設定
        :param enable_offline_transfer: 対象ユーザがオフラインの場合に転送を実行するか
        :type enable_offline_transfer: bool
        """
        if enable_offline_transfer and not isinstance(enable_offline_transfer, bool):
            raise TypeError(type(enable_offline_transfer))
        self.__enable_offline_transfer = enable_offline_transfer

    def with_enable_offline_transfer(self, enable_offline_transfer):
        """
        対象ユーザがオフラインの場合に転送を実行するかを設定
        :param enable_offline_transfer: 対象ユーザがオフラインの場合に転送を実行するか
        :type enable_offline_transfer: bool
        :return: this
        :rtype: PublishRequest
        """
        self.set_enable_offline_transfer(enable_offline_transfer)
        return self

    def get_offline_transfer_sound(self):
        """
        Firebaseへの転送時に使用する通知音ファイル名を取得
        :return: Firebaseへの転送時に使用する通知音ファイル名
        :rtype: unicode
        """
        return self.__offline_transfer_sound

    def set_offline_transfer_sound(self, offline_transfer_sound):
        """
        Firebaseへの転送時に使用する通知音ファイル名を設定
        :param offline_transfer_sound: Firebaseへの転送時に使用する通知音ファイル名
        :type offline_transfer_sound: unicode
        """
        if offline_transfer_sound and not (isinstance(offline_transfer_sound, str) or isinstance(offline_transfer_sound, unicode)):
            raise TypeError(type(offline_transfer_sound))
        self.__offline_transfer_sound = offline_transfer_sound

    def with_offline_transfer_sound(self, offline_transfer_sound):
        """
        Firebaseへの転送時に使用する通知音ファイル名を設定
        :param offline_transfer_sound: Firebaseへの転送時に使用する通知音ファイル名
        :type offline_transfer_sound: unicode
        :return: this
        :rtype: PublishRequest
        """
        self.set_offline_transfer_sound(offline_transfer_sound)
        return self
