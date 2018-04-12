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


class Certificate(object):

    def __init__(self, params=None):
        if params is None:
            self.__certificate_id = None
            self.__certificate = None
            self.__private_key = None
            self.__pfx = None
        else:
            self.set_certificate_id(params['certificateId'] if 'certificateId' in params.keys() else None)
            self.set_certificate(params['certificate'] if 'certificate' in params.keys() else None)
            self.set_private_key(params['privateKey'] if 'privateKey' in params.keys() else None)
            self.set_pfx(params['pfx'] if 'pfx' in params.keys() else None)

    def get_certificate_id(self):
        """
        証明書IDを取得
        :return: 証明書ID
        :rtype: unicode
        """
        return self.__certificate_id

    def set_certificate_id(self, certificate_id):
        """
        証明書IDを設定
        :param certificate_id: 証明書ID
        :type certificate_id: unicode
        """
        self.__certificate_id = certificate_id

    def get_certificate(self):
        """
        クライアント証明書を取得
        :return: クライアント証明書
        :rtype: unicode
        """
        return self.__certificate

    def set_certificate(self, certificate):
        """
        クライアント証明書を設定
        :param certificate: クライアント証明書
        :type certificate: unicode
        """
        self.__certificate = certificate

    def get_private_key(self):
        """
        秘密鍵を取得
        :return: 秘密鍵
        :rtype: unicode
        """
        return self.__private_key

    def set_private_key(self, private_key):
        """
        秘密鍵を設定
        :param private_key: 秘密鍵
        :type private_key: unicode
        """
        self.__private_key = private_key

    def get_pfx(self):
        """
        PFXフォーマットの秘密鍵を取得
        :return: PFXフォーマットの秘密鍵
        :rtype: unicode
        """
        return self.__pfx

    def set_pfx(self, pfx):
        """
        PFXフォーマットの秘密鍵を設定
        :param pfx: PFXフォーマットの秘密鍵
        :type pfx: unicode
        """
        self.__pfx = pfx

    def to_dict(self):
        return {
            "certificateId": self.__certificate_id,
            "certificate": self.__certificate,
            "privateKey": self.__private_key,
            "pfx": self.__pfx,
        }
