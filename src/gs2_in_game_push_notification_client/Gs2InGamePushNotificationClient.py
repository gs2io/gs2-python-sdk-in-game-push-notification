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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2InGamePushNotificationClient(AbstractGs2Client):

    ENDPOINT = "in-game-push-notification"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2InGamePushNotificationClient, self).__init__(credential, region)


    def create_certificate(self, request):
        """
        クライアント証明書を新規作成します<br>
        <br>
        MQTTサーバに接続するためのクライアント証明書の発行を行います。<br>
        1ユーザに対して発行できるクライアント証明書は同時に1つのみです。<br>
        異なるデバイスでMQTTサーバにアクセスする場合、クライアント証明書を削除して取り直すようにしてください。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.CreateCertificateRequest.CreateCertificateRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.CreateCertificateResult.CreateCertificateResult
        """
        body = { 
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_in_game_push_notification_client.control.CreateCertificateRequest import CreateCertificateRequest

        from gs2_in_game_push_notification_client.control.CreateCertificateResult import CreateCertificateResult
        return CreateCertificateResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/certificate",
            service=self.ENDPOINT,
            module=CreateCertificateRequest.Constant.MODULE,
            function=CreateCertificateRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_game(self, request):
        """
        ゲームを新規作成します<br>
        <br>
        GS2-InGamePushNotification の使用を開始するには、まずはゲームを作成します。<br>
        その後、ゲームに対してMQTTに接続するためのクライアント証明書の発行を依頼をします。<br>
        応答されたクライアント証明書と秘密鍵をデバイスに保存し、MQTTサーバへの接続に使用します。<br>
        <br>
        サーバサイドから ユーザに対してプッシュ通知を出すことが出来ます。<br>
        その際にユーザがMQTTに接続している場合はMQTTを使用して通知を出します。<br>
        もし、ユーザがMQTTに接続していない場合の挙動は ゲームの設定で変更できます。<br>
        <br>
        1つ目は何もしない。<br>
        2つ目は指定したURLに通知する。<br>
        3つ目は Firebase Cloud Messaging を使用してモバイルプッシュ通知する。です。<br>
        <br>
        http/https を指定した場合、以下のフォーマットでURLにPOSTします。<br>
        {<br>
          "_gs2_service": "gs2-in-game-push-notification",<br>
          "userId": ユーザID<br>
          "subject": サブジェクト,<br>
          "body": ボディ,<br>
        }<br>
        <br>
        APIリクエスト以外に各デバイスがMQTTサーバに新しく接続する際に クオータを10消費する点にご注意ください。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.CreateGameRequest.CreateGameRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.CreateGameResult.CreateGameResult
        """
        body = { 
            "serviceClass": request.get_service_class(),
            "name": request.get_name(),
            "offlineTransfer": request.get_offline_transfer(),
        }

        if request.get_notification_firebase_server_key() is not None:
            body["notificationFirebaseServerKey"] = request.get_notification_firebase_server_key()
        if request.get_notification_url() is not None:
            body["notificationUrl"] = request.get_notification_url()
        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.CreateGameRequest import CreateGameRequest

        from gs2_in_game_push_notification_client.control.CreateGameResult import CreateGameResult
        return CreateGameResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game",
            service=self.ENDPOINT,
            module=CreateGameRequest.Constant.MODULE,
            function=CreateGameRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def delete_certificate(self, request):
        """
        クライアント証明書を削除します。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.DeleteCertificateRequest.DeleteCertificateRequest

        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_in_game_push_notification_client.control.DeleteCertificateRequest import DeleteCertificateRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/certificate",
            service=self.ENDPOINT,
            module=DeleteCertificateRequest.Constant.MODULE,
            function=DeleteCertificateRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_game(self, request):
        """
        ゲームを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.DeleteGameRequest.DeleteGameRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.DeleteGameRequest import DeleteGameRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "",
            service=self.ENDPOINT,
            module=DeleteGameRequest.Constant.MODULE,
            function=DeleteGameRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def describe_game(self, request):
        """
        ゲームの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.DescribeGameRequest.DescribeGameRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.DescribeGameResult.DescribeGameResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.DescribeGameRequest import DescribeGameRequest

        from gs2_in_game_push_notification_client.control.DescribeGameResult import DescribeGameResult
        return DescribeGameResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game",
            service=self.ENDPOINT,
            module=DescribeGameRequest.Constant.MODULE,
            function=DescribeGameRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_service_class(self, request):
        """
        サービスクラスの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.DescribeServiceClassRequest.DescribeServiceClassRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.DescribeServiceClassResult.DescribeServiceClassResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.DescribeServiceClassRequest import DescribeServiceClassRequest

        from gs2_in_game_push_notification_client.control.DescribeServiceClassResult import DescribeServiceClassResult
        return DescribeServiceClassResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/serviceClass",
            service=self.ENDPOINT,
            module=DescribeServiceClassRequest.Constant.MODULE,
            function=DescribeServiceClassRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_status(self, request):
        """
        ユーザステータスの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.DescribeStatusRequest.DescribeStatusRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.DescribeStatusResult.DescribeStatusResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.DescribeStatusRequest import DescribeStatusRequest

        from gs2_in_game_push_notification_client.control.DescribeStatusResult import DescribeStatusResult
        return DescribeStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/user",
            service=self.ENDPOINT,
            module=DescribeStatusRequest.Constant.MODULE,
            function=DescribeStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_game(self, request):
        """
        ゲームを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.GetGameRequest.GetGameRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.GetGameResult.GetGameResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.GetGameRequest import GetGameRequest

        from gs2_in_game_push_notification_client.control.GetGameResult import GetGameResult
        return GetGameResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "",
            service=self.ENDPOINT,
            module=GetGameRequest.Constant.MODULE,
            function=GetGameRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_game_status(self, request):
        """
        ゲームの状態を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.GetGameStatusRequest.GetGameStatusRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.GetGameStatusResult.GetGameStatusResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.GetGameStatusRequest import GetGameStatusRequest

        from gs2_in_game_push_notification_client.control.GetGameStatusResult import GetGameStatusResult
        return GetGameStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/status",
            service=self.ENDPOINT,
            module=GetGameStatusRequest.Constant.MODULE,
            function=GetGameStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_mqtt_host(self, request):
        """
        MQTTサーバ情報を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.GetMqttHostRequest.GetMqttHostRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.GetMqttHostResult.GetMqttHostResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_in_game_push_notification_client.control.GetMqttHostRequest import GetMqttHostRequest

        from gs2_in_game_push_notification_client.control.GetMqttHostResult import GetMqttHostResult
        return GetMqttHostResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/server/mqtt",
            service=self.ENDPOINT,
            module=GetMqttHostRequest.Constant.MODULE,
            function=GetMqttHostRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_web_socket_host(self, request):
        """
        MQTT over Websocketサーバ情報を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.GetWebSocketHostRequest.GetWebSocketHostRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.GetWebSocketHostResult.GetWebSocketHostResult
        """

        query_strings = {

        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_in_game_push_notification_client.control.GetWebSocketHostRequest import GetWebSocketHostRequest

        from gs2_in_game_push_notification_client.control.GetWebSocketHostResult import GetWebSocketHostResult
        return GetWebSocketHostResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/server/webSocket",
            service=self.ENDPOINT,
            module=GetWebSocketHostRequest.Constant.MODULE,
            function=GetWebSocketHostRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))




    def publish(self, request):
        """
        通知を送信します。<br>
        <br>
        - 消費クオータ: 3<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.PublishRequest.PublishRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.PublishResult.PublishResult
        """
        body = { 
            "body": request.get_body(),
            "enableOfflineTransfer": request.get_enable_offline_transfer(),
            "subject": request.get_subject(),
        }

        if request.get_offline_transfer_sound() is not None:
            body["offlineTransferSound"] = request.get_offline_transfer_sound()
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.PublishRequest import PublishRequest

        from gs2_in_game_push_notification_client.control.PublishResult import PublishResult
        return PublishResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/user/" + str(("null" if request.get_user_id() is None else request.get_user_id())) + "",
            service=self.ENDPOINT,
            module=PublishRequest.Constant.MODULE,
            function=PublishRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def set_firebase_token(self, request):
        """
        Firebase のデバイストークンを設定します。<br>
        <br>
        - 消費クオータ: 10<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.SetFirebaseTokenRequest.SetFirebaseTokenRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.SetFirebaseTokenResult.SetFirebaseTokenResult
        """
        body = { 
            "token": request.get_token(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        from gs2_in_game_push_notification_client.control.SetFirebaseTokenRequest import SetFirebaseTokenRequest

        from gs2_in_game_push_notification_client.control.SetFirebaseTokenResult import SetFirebaseTokenResult
        return SetFirebaseTokenResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "/user",
            service=self.ENDPOINT,
            module=SetFirebaseTokenRequest.Constant.MODULE,
            function=SetFirebaseTokenRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def update_game(self, request):
        """
        ゲームを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_in_game_push_notification_client.control.UpdateGameRequest.UpdateGameRequest
        :return: 結果
        :rtype: gs2_in_game_push_notification_client.control.UpdateGameResult.UpdateGameResult
        """
        body = { 
            "serviceClass": request.get_service_class(),
            "offlineTransfer": request.get_offline_transfer(),
        }

        if request.get_notification_url() is not None:
            body["notificationUrl"] = request.get_notification_url()
        if request.get_notification_firebase_server_key() is not None:
            body["notificationFirebaseServerKey"] = request.get_notification_firebase_server_key()
        if request.get_description() is not None:
            body["description"] = request.get_description()
        headers = { 
        }
        from gs2_in_game_push_notification_client.control.UpdateGameRequest import UpdateGameRequest

        from gs2_in_game_push_notification_client.control.UpdateGameResult import UpdateGameResult
        return UpdateGameResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/game/" + str(("null" if request.get_game_name() is None else request.get_game_name())) + "",
            service=self.ENDPOINT,
            module=UpdateGameRequest.Constant.MODULE,
            function=UpdateGameRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))


