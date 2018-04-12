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


class FirebaseToken(object):

    def __init__(self, params=None):
        if params is None:
            self.__user_id = None
            self.__token = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_token(params['token'] if 'token' in params.keys() else None)

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_token(self):
        """
        トークンを取得
        :return: トークン
        :rtype: unicode
        """
        return self.__token

    def set_token(self, token):
        """
        トークンを設定
        :param token: トークン
        :type token: unicode
        """
        self.__token = token

    def to_dict(self):
        return {
            "userId": self.__user_id,
            "token": self.__token,
        }
