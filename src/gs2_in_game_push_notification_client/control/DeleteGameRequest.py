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


class DeleteGameRequest(Gs2BasicRequest):

    class Constant(Gs2InGamePushNotification):
        FUNCTION = "DeleteGame"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteGameRequest, self).__init__(params)
        if params is None:
            self.__game_name = None
        else:
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)

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
        if game_name and not isinstance(game_name, unicode):
            raise TypeError(type(game_name))
        self.__game_name = game_name

    def with_game_name(self, game_name):
        """
        ゲームの名前を設定
        :param game_name: ゲームの名前
        :type game_name: unicode
        :return: this
        :rtype: DeleteGameRequest
        """
        self.set_game_name(game_name)
        return self
