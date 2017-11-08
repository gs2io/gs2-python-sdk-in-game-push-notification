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

class PublishResponse(object):

    def __init__(self, params=None):
        if params is None:
            self.__body = None
            self.__type = None
            self.__subject = None
        else:
            self.set_body(params['body'] if 'body' in params.keys() else None)
            self.set_type(params['type'] if 'type' in params.keys() else None)
            self.set_subject(params['subject'] if 'subject' in params.keys() else None)


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
        self.__body = body

    def get_type(self):
        """
        通知に使用した方式を取得
        :return: 通知に使用した方式
        :rtype: unicode
        """
        return self.__type

    def set_type(self, type):
        """
        通知に使用した方式を設定
        :param type: 通知に使用した方式
        :type type: unicode
        """
        self.__type = type

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
        self.__subject = subject

    def to_dict(self):
        return { 
            "body": self.__body,
            "type": self.__type,
            "subject": self.__subject,
        }