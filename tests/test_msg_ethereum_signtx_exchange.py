# This file is part of the TREZOR project.
#
# Copyright (C) 2012-2016 Marek Palatinus <slush@satoshilabs.com>
# Copyright (C) 2012-2016 Pavol Rusnak <stick@satoshilabs.com>
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library.  If not, see <http://www.gnu.org/licenses/>.
#
# The script has been modified for KeepKey Device.

import unittest
import common
import binascii
import struct

import keepkeylib.messages_pb2 as proto
import keepkeylib.types_pb2 as proto_types
import keepkeylib.exchange_pb2 as proto_exchange
from keepkeylib.client import CallException

from rlp.utils import int_to_big_endian

class TestMsgEthereumtx_exch(common.KeepKeyTest):

    def test_eth_to_doge_exch(self):
        self.setup_mnemonic_nopin_nopassphrase()
	self.client.apply_policy('ShapeShift', 1)

        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('6d4dc95317'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='doge',
                                                address='DQTjL9vfXVbMfCGM49KWeYvvvNzRPaoiFp') ,
  
                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3d55d68b75d98ac3ac0d2ddf61554f00703d6357') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480978325881,
                                         quoted_rate=binascii.unhexlify('02ebe9834161'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0bebc200'),
#                                         order_id=binascii.unhexlify('4a2320f8267b4b739fa452196d320abb'),
                                         order_id=binascii.unhexlify('4a2320f8267b4b739fa452196d320abb'),
                                         ),
                                signature=binascii.unhexlify('207f69cf0569f81d5758efb8f2e186e35bc84ce37ab198f88ef31342ef5213072942d063fb159aa7546dc7a8e72fc6d57932b0fcc62289bbf949ca508fea5e0e0c')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Dogecoin',
                              withdrawal_address_n=[2147483692,2147483651,2147483648,0,0],
                              return_address_n=[2147483692,2147483708,2147483648,0,0],
                            )
        sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
            n=[2147483692,2147483708,2147483648,0,0],
            nonce=01,
            gas_price=20,
            gas_limit=20,
            to=binascii.unhexlify('3d55d68b75d98ac3ac0d2ddf61554f00703d6357'),
            value=146207570000000000,
            address_type=3,
            exchange_type=exchange_type_out1,
            )

        self.assertEqual(sig_v, 27)
        self.assertEqual(binascii.hexlify(sig_r), '442ef56b78c8ea8a0764fdb5527dc3f18086a8b672eefdee7249b5c661a584c6')
        self.assertEqual(binascii.hexlify(sig_s), '15a25a0704e46be3f60339443ce9183ac7193cbd7a49c564d14ffc41b571657a')
        self.assertEqual(binascii.hexlify(hash), 'ff73eec0846adace28b29aad84e53f97360e843947a079e7aeaaeb2fd92c9675')
        self.assertEqual(binascii.hexlify(signature_der), '30440220442ef56b78c8ea8a0764fdb5527dc3f18086a8b672eefdee7249b5c661a584c6022015a25a0704e46be3f60339443ce9183ac7193cbd7a49c564d14ffc41b571657a')

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_eth_to_ltc_exch(self):
        self.setup_mnemonic_nopin_nopassphrase()
	self.client.apply_policy('ShapeShift', 1)

        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,
  
                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776874,
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('1f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a420')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Litecoin',
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,1],
                              return_address_n=[2147483692,2147483708,2147483648,0,0]
                            )
        sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
            n=[2147483692,2147483708,2147483648,0,0],
            nonce=01,
            gas_price=20,
            gas_limit=20,
            to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206743'),
            value=146207570000000000,
            address_type=3,
            exchange_type=exchange_type_out1,
            )

        self.assertEqual(sig_v, 27)
        self.assertEqual(binascii.hexlify(sig_r), 'b82354764f4a206507365e63c40182748948624bb9e62651e1f1121f3a9f9095')
        self.assertEqual(binascii.hexlify(sig_s), '53b582ea05874f87eb84d8256248ff16cab872ba585305eaa9ba4d732df7b2d5')
        self.assertEqual(binascii.hexlify(hash), 'ac4f6a5e7f2543ad921029a805ddf07480aaf708811645ae9e0116d6bf87a284')
        self.assertEqual(binascii.hexlify(signature_der), '3045022100b82354764f4a206507365e63c40182748948624bb9e62651e1f1121f3a9f9095022053b582ea05874f87eb84d8256248ff16cab872ba585305eaa9ba4d732df7b2d5')

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_ethereum_exch_signature_error1(self):
        self.setup_mnemonic_nopin_nopassphrase()
	self.client.apply_policy('ShapeShift', 1)

        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,
  
                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776874,
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('0f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a420')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Litecoin',
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,1],
                              return_address_n=[2147483692,2147483708,2147483648,0,0]
                            )

        try:
            sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
            n=[2147483692,2147483708,2147483648,0,0],
            nonce=01,
            gas_price=20,
            gas_limit=20,
            to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206743'),
            value=146207570000000000,
            address_type=3,
            exchange_type=exchange_type_out1,
            )
        except CallException as e:
            self.assertEndsWith(e.args[1], 'Exchange signature error')
            print "Negative Test Passed (test_ethereum_exch_signature_error1)!" 
        else:
            self.assert_(False, "Failed to detect error condition")

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_ethereum_exch_signature_error2(self):
        self.setup_mnemonic_nopin_nopassphrase()
        self.client.apply_policy('ShapeShift', 1)

        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,

                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776874,
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('1f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a421')
                                                                                                                                                                                #error here   -^-
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Litecoin',
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,1],
                              return_address_n=[2147483692,2147483708,2147483648,0,0]
                            )

        try:
            sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
                n=[2147483692,2147483708,2147483648,0,0],
                nonce=01,
                gas_price=20,
                gas_limit=20,
                to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206743'),
                value=146207570000000000,
                address_type=3,
                exchange_type=exchange_type_out1,
                )
        except CallException as e:
            self.assertEndsWith(e.args[1], 'Exchange signature error')
            print "Negative Test Passed (test_ethereum_exch_signature_error2)!"
        else:
            self.assert_(False, "Failed to detect error condition")

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_ethereum_exch_signature_error3(self):
        self.setup_mnemonic_nopin_nopassphrase()
        self.client.apply_policy('ShapeShift', 1)

        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,

                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776875,
                                                 #error here   -^-
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('1f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a420')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Litecoin',
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,1],
                              return_address_n=[2147483692,2147483708,2147483648,0,0]
                            )

        try:
            sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
                n=[2147483692,2147483708,2147483648,0,0],
                nonce=01,
                gas_price=20,
                gas_limit=20,
                to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206743'),
                value=146207570000000000,
                address_type=3,
                exchange_type=exchange_type_out1,
                )
        except CallException as e:
            self.assertEndsWith(e.args[1], 'Exchange signature error')
            print "Negative Test Passed (test_ethereum_exch_signature_error3)!" 
        else:
            self.assert_(False, "Failed to detect error condition")

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_ethereum_exch_dep_addr_error(self):
        self.setup_mnemonic_nopin_nopassphrase()
        self.client.apply_policy('ShapeShift', 1)
        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,

                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776874,
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('1f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a420')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Litecoin',
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,1],
                              return_address_n=[2147483692,2147483708,2147483648,0,0]
                            )
        try:
            sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
            n=[2147483692,2147483708,2147483648,0,0],
            nonce=01,
            gas_price=20,
            gas_limit=20,
            to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206744'),
                                                           #error here   -^-
            value=146207570000000000,
            address_type=3,
            exchange_type=exchange_type_out1,
            )
        except CallException as e:
            self.assertEndsWith(e.args[1], 'Exchange deposit address error')
            print "Negative Test Passed (test_ethereum_exch_dep_addr_error)!"
        else:
            self.assert_(False, "Failed to detect error condition")

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_ethereum_exch_dep_amount_error(self):
        self.setup_mnemonic_nopin_nopassphrase()
        self.client.apply_policy('ShapeShift', 1)
        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,

                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776874,
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('1f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a420')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Litecoin',
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,1],
                              return_address_n=[2147483692,2147483708,2147483648,0,0]
                            )
        try:
            sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
            n=[2147483692,2147483708,2147483648,0,0],
            nonce=01,
            gas_price=20,
            gas_limit=20,
            to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206743'),
            value=146207570000000001,
              #error here         -^-
            address_type=3,
            exchange_type=exchange_type_out1,
            )
        except CallException as e:
            self.assertEndsWith(e.args[1], 'Exchange deposit amount error')
            print "Negative Test Passed (test_ethereum_exch_dep_amount_error)!"
        else:
            self.assert_(False, "Failed to detect error condition")

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_ethereum_exch_withdrawal_cointype_error(self):
        self.setup_mnemonic_nopin_nopassphrase()
        self.client.apply_policy('ShapeShift', 1)
        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,

                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776874,
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('1f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a420')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Bitcoin',
                                     #error here   -^-
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,1],
                              return_address_n=[2147483692,2147483708,2147483648,0,0]
                            )
        try:
            sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
                n=[2147483692,2147483708,2147483648,0,0],
                nonce=01,
                gas_price=20,
                gas_limit=20,
                to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206743'),
                value=146207570000000000,
                address_type=3,
                exchange_type=exchange_type_out1,
                )
        except CallException as e:
            self.assertEndsWith(e.args[1], 'Exchange withdrawal coin type error')
            print "Negative Test Passed (test_ethereum_exch_withdrawal_cointype_error)!"
        else:
            self.assert_(False, "Failed to detect error condition")

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_ethereum_exch_withdrawal_addr_error(self):
        self.setup_mnemonic_nopin_nopassphrase()
        self.client.apply_policy('ShapeShift', 1)

        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,

                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776874,
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('1f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a420')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Litecoin',
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,2],
                                                                        #error here   -^-
                              return_address_n=[2147483692,2147483708,2147483648,0,0]
                            )

        try:
            sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
                n=[2147483692,2147483708,2147483648,0,0],
                nonce=01,
                gas_price=20,
                gas_limit=20,
                to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206743'),
                value=146207570000000000,
                address_type=3,
                exchange_type=exchange_type_out1,
                )
        except CallException as e:
            self.assertEndsWith(e.args[1], 'Exchange withdrawal address error')
            print "Negative Test Passed (test_ethereum_exch_withdrawal_addr_error)!"
        else:
            self.assert_(False, "Failed to detect error condition")

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

    def test_ethereum_exch_return_addr_error(self):
        self.setup_mnemonic_nopin_nopassphrase()
        self.client.apply_policy('ShapeShift', 1)

        signed_exchange_out1=proto_exchange.SignedExchangeResponse(
                                responseV2=proto_exchange.ExchangeResponseV2(
                                         withdrawal_amount=binascii.unhexlify('01a69189'),
                                         withdrawal_address=proto_exchange.ExchangeAddress(
                                                coin_type='ltc',
                                                address='LhvxkkwMCjDAwyprNHhYW8PE9oNf6wSd2V') ,

                                         deposit_amount=binascii.unhexlify('02076f02a152b400'),
                                         deposit_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x8cfbb7ef910936ac801e4d07ae46599041206743') ,

                                         return_address=proto_exchange.ExchangeAddress(
                                                coin_type='eth',
                                                address='0x3f2329c9adfbccd9a84f52c906e936a42da18cb8') ,

                                         expiration=1480984776874,
                                         quoted_rate=binascii.unhexlify('0b54a1d6'),

                                         api_key=binascii.unhexlify('6ad5831b778484bb849da45180ac35047848e5cac0fa666454f4ff78b8c7399fea6a8ce2c7ee6287bcd78db6610ca3f538d6b3e90ca80c8e6368b6021445950b'),
                                         miner_fee=binascii.unhexlify('0186a0'),
                                         order_id=binascii.unhexlify('1924ae6635e34cdca8137861434d9ede'),
                                         ),
                                signature=binascii.unhexlify('1f61697158580925b64ba9b93677a47f996deac9529d98e15ee90fcc240b098ab84f2324a4ccab092a38f8720537636ef1d012903ac27697f184cc43269975a420')
                             )
        exchange_type_out1=proto_types.ExchangeType(
                              signed_exchange_response=signed_exchange_out1,
                              withdrawal_coin_name='Litecoin',
                              withdrawal_address_n=[2147483692,2147483650,2147483649,0,1],
                              return_address_n=[2147483692,2147483708,2147483648,0,1]
                                                                    #error here   -^-
                            )
        try:
            sig_v, sig_r, sig_s, hash, signature_der = self.client.ethereum_sign_tx(
                n=[2147483692,2147483708,2147483648,0,0],
                nonce=01,
                gas_price=20,
                gas_limit=20,
                to=binascii.unhexlify('8cfbb7ef910936ac801e4d07ae46599041206743'),
                value=146207570000000000,
                address_type=3,
                exchange_type=exchange_type_out1,
                )
        except CallException as e:
            self.assertEndsWith(e.args[1], 'Exchange return address error')
            print "Negative Test Passed (test_ethereum_exch_return_addr_error)!"
        else:
            self.assert_(False, "Failed to detect error condition")

        #reset policy ("ShapeShift")
        self.client.apply_policy('ShapeShift', 0)

if __name__ == '__main__':
    unittest.main()
