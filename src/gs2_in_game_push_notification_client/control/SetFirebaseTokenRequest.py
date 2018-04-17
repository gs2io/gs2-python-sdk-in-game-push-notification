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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_in_game_push_notification_client.Gs2InGamePushNotification import Gs2InGamePushNotification


class SetFirebaseTokenRequest(Gs2UserRequest):

    class Constant(Gs2InGamePushNotification):
        FUNCTION = "SetFirebaseCloudMessagingToken"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(SetFirebaseTokenRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
            self.__token = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
            self.set_token(params['token'] if 'token' in params.keys() else None)

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
        if _game_name and not (isinstance(_game_name, str) or isinstance(_game_name, unicode)):
            raise TypeError(type(game_name))
        self.__game_name = game_name

    def with_game_name(self, game_name):
        """
        ゲームの名前を設定
        :param game_name: ゲームの名前
        :type game_name: unicode
        :return: this
        :rtype: SetFirebaseTokenRequest
        """
        self.set_game_name(game_name)
        return self

    def get_token(self):
        """
        デバイストークンを取得
        :return: デバイストークン
        :rtype: unicode
        """
        return self.__token

    def set_token(self, token):
        """
        デバイストークンを設定
        :param token: デバイストークン
        :type token: unicode
        """
        if _token and not (isinstance(_token, str) or isinstance(_token, unicode)):
            raise TypeError(type(token))
        self.__token = token

    def with_token(self, token):
        """
        デバイストークンを設定
        :param token: デバイストークン
        :type token: unicode
        :return: this
        :rtype: SetFirebaseTokenRequest
        """
        self.set_token(token)
        return self
