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


class Status(object):

    def __init__(self, params=None):
        if params is None:
            self.__user_id = None
            self.__status = None
            self.__fcm_token = None
            self.__create_at = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_status(params['status'] if 'status' in params.keys() else None)
            self.set_fcm_token(params['fcmToken'] if 'fcmToken' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)

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

    def get_status(self):
        """
        ステータスを取得
        :return: ステータス
        :rtype: unicode
        """
        return self.__status

    def set_status(self, status):
        """
        ステータスを設定
        :param status: ステータス
        :type status: unicode
        """
        self.__status = status

    def get_fcm_token(self):
        """
        Firebaseトークンを取得
        :return: Firebaseトークン
        :rtype: unicode
        """
        return self.__fcm_token

    def set_fcm_token(self, fcm_token):
        """
        Firebaseトークンを設定
        :param fcm_token: Firebaseトークン
        :type fcm_token: unicode
        """
        self.__fcm_token = fcm_token

    def get_create_at(self):
        """
        登録日時を取得
        :return: 登録日時
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        登録日時を設定
        :param create_at: 登録日時
        :type create_at: int
        """
        self.__create_at = create_at

    def to_dict(self):
        return {
            "userId": self.__user_id,
            "status": self.__status,
            "fcmToken": self.__fcm_token,
            "createAt": self.__create_at,
        }
