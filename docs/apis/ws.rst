*********
WebSocket
*********

The ``WebSocket`` protocol enables interaction between a ``web browser`` (or other client application) and a ``web server``
with lower overheads, facilitating real-time data transfer from and to the server. This is made possible by providing
a standardized way for the server to send content to the client without being first requested by the client,
and allowing messages to be passed back and forth while keeping the connection open.

``Remme`` provides a lot of data you could ``listen`` from the blockchain. For instance, be notified with newly created
transaction to your transfer or when your ``Atomic Swap`` transaction was approved.

Disclaimer
==========

For examples of the ``WebSockets`` requests, the ``wscat`` is used. Install the tool with the following command:

.. code-block:: console

    $ npm install -g wscat

Then check it out following the command below that sends request to echo server which will reply the same message that you send.

.. code-block:: console

    $ wscat -c ws://echo.websocket.org
    connected (press CTRL+C to quit)
    > hi remme
    < hi remme
    > you are awesome!
    < you are awesome!

If this stage is completed, go on farther reading!

URI to connect to
=================

To connect to the node"s ``WebSockets`` you need to reach the following URI via ``POST`` method — ``ws://node_address:node_port``.

When you want to connect to a local node, use ``ws://127.0.0.1:8080``. If to production one, choose preferred node in
:doc:`/introduction` section and fill the following pattern ``wss://<name>:8080``. For instance, ``wss://node-2-testnet.remme.io:8080``).

Event subscription
==================

To subscribe to some event you need to call a method in ``JSON RPC`` format:

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "event_type": "transfer",
            "address": "112007db8a00c010402e2e3a7d03491323e761e0ea612481c518605648ceeb5ed454f7"
        },
        "id": "42"
    }

With the ``wscat`` the same request is required to be in one line.

.. code-block:: console

    $ wscat -c ws://127.0.0.1:8080
    connected (press CTRL+C to quit)
    > {"jsonrpc":"2.0","method":"subscribe","params":{"event_type":"transfer", "address":"112007db8a00c010402e2e3a7d03491323e761e0ea612481c518605648ceeb5ed454f7"},"id":"42"}
    < {"jsonrpc": "2.0", "id": "42", "result": "SUBSCRIBED"}

As you see, if request completed successfully, you will get the response that informs you that you are subscribe on transfer events.

If request failed, for example from invalid address value, you will get the following response.


.. code-block:: console

    $ wscat -c ws://127.0.0.1:8080
    connected (press CTRL+C to quit)
    > {"jsonrpc":"2.0","method":"subscribe","params":{"event_type":"transfer", "address":"some-incorrect-transfer-address"},"id":"42"}
    < {"jsonrpc": "2.0", "error": {"code": -32602, "message": "Incorrect transfer address."}, "id": "42"}

Incoming events
===============

So when tokens are transferred to the specified address, you will be notified like.

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "id": "42",
        "result": {
            "event_type": "transfer",
            "attributes": {
                "from": {
                    "address": "112007be95c8bb240396446ec359d0d7f04d257b72aeb4ab1ecfe50cf36e400a96ab9c",
                    "balance": 999999999920.0
                },
                "to": {
                    "address": "112007db8a00c010402e2e3a7d03491323e761e0ea612481c518605648ceeb5ed454f7",
                    "balance": 80.0
                }
            }
        }
    }

In ``wscat`` it will occur in the following way.

.. code-block:: console

    $ wscat -c ws://127.0.0.1:8080
    connected (press CTRL+C to quit)
    > {"jsonrpc":"2.0","method":"subscribe","params":{"event_type":"transfer", "address":"112007db8a00c010402e2e3a7d03491323e761e0ea612481c518605648ceeb5ed454f7"},"id":"42"}
    < {"jsonrpc": "2.0", "id": "42", "result": "SUBSCRIBED"}
    < {"jsonrpc": "2.0", "id": "42", "result": {"event_type": "transfer", "attributes": {"from": {"address": "112007be95c8bb240396446ec359d0d7f04d257b72aeb4ab1ecfe50cf36e400a96ab9c", "balance": 999999999920.0}, "to": {"address": "112007db8a00c010402e2e3a7d03491323e761e0ea612481c518605648ceeb5ed454f7", "balance": 80.0}}}}

Unsubscription
==============

If you decide you do not need incoming events anymore, call unsubscribe method with the event type of subscription you want to unsubscribe from.

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "method": "unsubscribe",
        "params": {
            "event_type": "transfer"
        },
        "id": "42"
    }


In ``wscat`` it will occur in the following way.

.. code-block:: console

    $ wscat -c ws://127.0.0.1:8080
    connected (press CTRL+C to quit)
    > {"jsonrpc":"2.0","method":"unsubscribe","params":{"event_type":"transfer"},"id":"42"}
    < {"jsonrpc": "2.0", "id": "42", "result": "UNSUBSCRIBED"}

Subscriptions API
=================

Atomic Swap
-----------

Atomic Swap events.

**The example of the request:**

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "event_type": "atomic_swap",
            "id": "033102e41346242476b15a3a7966eb5249271025fc7fb0b37ed3fdb4bcce3884",
            "from_block": "aafb03931cf3b7a5cc8eace89f6262733c9b374b8dcc243b7d076a1b7ffe84f2387c11c1b02537c8d43ff0ecb78c267211e2f8c8ad493a3fe64470ce60233628"
        }
        "id": "42"
    }

+----------------------------------------------------------------------------------+
| **Subscriptions parameters**                                                     |
+----------------+----------+--------------+---------------------------------------+
| **Parameter**  | **Type** | **Required** | **Description**                       |
+----------------+----------+--------------+---------------------------------------+
| ``event_type`` | String   | Yes          | The value of the batch event type.    |
+----------------+----------+--------------+---------------------------------------+
| ``id``         | String   | Yes          | The identifier of the atomic swap.    |
+----------------+----------+--------------+---------------------------------------+
| ``from_block`` | String   | No           | To track event from the block.        |
+----------------+----------+--------------+---------------------------------------+

**The example of the response:**

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "id": "56b22978026bafc1f332eb86adfc87ccbcd8be9fd5cdfca0bbc815323b2127d7",
        "result": {
            "event_type": "atomic_swap",
            "attributes": {
                "address": "78173b40c633c5f2fbbb9e9c0b39e3e3ae3a3908a47aa322a890d7c7884cb7fbca1830",
                "sender_address": "112007be95c8bb240396446ec359d0d7f04d257b72aeb4ab1ecfe50cf36e400a96ab9c",
                "receiver_address": "112007db8a00c010402e2e3a7d03491323e761e0ea612481c518605648ceeb5ed454f7",
                "amount": "10",
                "swap_id": "033102e41346242476b15a3a7966eb5249271025fc7fb0b37ed3fdb4bcce3884",
                "secret_lock": "b605112c2d7489034bbd7beab083fb65ba02af787786bb5e3d99bb26709f4f68",
                "created_at": 1548951674,
                "sender_address_non_local": "0xe6ca0e7c974f06471759e9a05d18b538c5ced11e",
                "state": "OPENED",
                "email_address_encrypted_optional": "",
                "secret_key": "",
                "is_initiator": False
            }
        }
    }

+-----------------------------------------------------------------------------------------------------------------------------------+
| **Incoming attributes**                                                                                                           |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| **Attribute**                        | **Message**                                                                                |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``address``                          | Address to store swap information by.                                                      |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``sender_address``                   | Sender Remme account address.                                                              |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``receiver_address``                 | Receiver Remme account address.                                                            |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``amount``                           | Amount of Remme tokens to send.                                                            |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``swap_id``                          | Swap identifier.                                                                           |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``secret_lock``                      | `SHA-512 <https://en.wikipedia.org/wiki/SHA-2>`_ hash from secret key in hex format.       |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``created_at``                       | Swap `timestamp <https://www.unixtimestamp.com/>`_.                                        |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``sender_address_non_local``         | Sender Ethereum address to get swapped tokens.                                             |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``state``                            | State of the atomic swap (empty, opened, secret_lock_provided, approved, closed, expired). |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``email_address_encrypted_optional`` | Encrypted e-mail address to get notification to.                                           |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``secret_key``                       | `SHA-512 <https://en.wikipedia.org/wiki/SHA-2>`_ sequence.                                 |
+--------------------------------------+--------------------------------------------------------------------------------------------+
| ``is_initiator``                     | False if you are not initiator and do not provide secret lock.                             |
+--------------------------------------+--------------------------------------------------------------------------------------------+

Batch
-----

Delivers status updates on the batch with the provided identifier.

**The example of the request:**

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "event_type": "batch",
            "id": "ad4e984136defc35369aefbe6ebdaf7a2ea25c6ea3e7ba4bf2f747cabedd746d73bc0aade5f78a019f520831ac9560f6d18d59a698e453e683c7405db3472ea0"
        },
        "id": "42"
    }

+----------------------------------------------------------------------------------+
| **Subscriptions parameters**                                                     |
+----------------+----------+--------------+---------------------------------------+
| **Parameter**  | **Type** | **Required** | **Description**                       |
+----------------+----------+--------------+---------------------------------------+
| ``event_type`` | String   | Yes          | The value of the batch event type.    |
+----------------+----------+--------------+---------------------------------------+
| ``id``         | String   | Yes          | The identifier of the batch to track. |
+----------------+----------+--------------+---------------------------------------+

**The example of the response:**

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "id": 42,
        "result": {
            "event_type": "batch",
            "attributes": {
                "id": "ad4e984136defc35369aefbe6ebdaf7a2ea25c6ea3e7ba4bf2f747cabedd746d73bc0aade5f78a019f520831ac9560f6d18d59a698e453e683c7405db3472ea0",
                "status": "PENDING"
            }
        }
    }

+------------------------------------------------------------------------+
| **Incoming attributes**                                                |
+---------------+--------------------------------------------------------+
| **Attribute** | **Message**                                            |
+---------------+--------------------------------------------------------+
| ``id``        | Batch identifier.                                      |
+---------------+--------------------------------------------------------+
| ``status``    | Batch status (unknown, pending, invalid or committed). |
+---------------+--------------------------------------------------------+
| ``error``     | Error message. Occurs if batch status is invalid.      |
+---------------+--------------------------------------------------------+

**Known errors**

+----------------+--------------------------------------------------------+
| **Parameters** | **Message**                                            |
+----------------+--------------------------------------------------------+
| ``id``         | Incorrect batch identifier.                            |
+----------------+--------------------------------------------------------+
| ``id``         | Missed id                                              |
+----------------+--------------------------------------------------------+

Block
-----

Arrival of new blocks.

**The example of the request:**

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "event_type": "blocks"
        },
        "id": "42"
    }

+----------------------------------------------------------------------------------+
| **Subscriptions parameters**                                                     |
+----------------+----------+--------------+---------------------------------------+
| **Parameter**  | **Type** | **Required** | **Description**                       |
+----------------+----------+--------------+---------------------------------------+
| ``event_type`` | String   | Yes          | The value of the block event type.    |
+----------------+----------+--------------+---------------------------------------+

**The example of the response:**

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "id": "42",
        "result": {
            "event_type": "blocks",
            "attributes": {
                "id": "aafb03931cf3b7a5cc8eace89f6262733c9b374b8dcc243b7d076a1b7ffe84f2387c11c1b02537c8d43ff0ecb78c267211e2f8c8ad493a3fe64470ce60233628",
                "timestamp": 1548344543
            }
        }
    }

+----------------------------------------------------------------------+
| **Incoming attributes**                                              |
+---------------+------------------------------------------------------+
| **Attribute** | **Message**                                          |
+---------------+------------------------------------------------------+
| ``id``        | Block identifier.                                    |
+---------------+------------------------------------------------------+
| ``timestamp`` | Block `timestamp <https://www.unixtimestamp.com/>`_. |
+---------------+------------------------------------------------------+

Transfer
--------

Delivers new token transfers from or to an address.

**The example of the request:**

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "event_type": "transfer",
            "address": "112007db8a00c010402e2e3a7d03491323e761e0ea612481c518605648ceeb5ed454f7"
        },
        "id": "42"
    }

+------------------------------------------------------------------------------------+
| **Subscriptions parameters**                                                       |
+----------------+----------+--------------+-----------------------------------------+
| **Parameter**  | **Type** | **Required** | **Description**                         |
+----------------+----------+--------------+-----------------------------------------+
| ``event_type`` | String   | Yes          | The value of the transfer event type.   |
+----------------+----------+--------------+-----------------------------------------+
| ``address``    | String   | Yes          | An address of the transaction to track. |
+----------------+----------+--------------+-----------------------------------------+

**The example of the response:**

.. code-block:: javascript

    {
        "jsonrpc": "2.0",
        "id": "42",
        "result": {
            "event_type": "transfer",
            "attributes": {
                "from": {
                    "address": "112007be95c8bb240396446ec359d0d7f04d257b72aeb4ab1ecfe50cf36e400a96ab9c",
                    "balance": 999999999920.0
                },
                "to": {
                    "address": "112007db8a00c010402e2e3a7d03491323e761e0ea612481c518605648ceeb5ed454f7",
                    "balance": 80.0
                }
            }
        }
    }

+------------------------------------------------------------------------+
| **Incoming attributes**                                                |
+---------------+--------------------------------------------------------+
| **Attribute** | **Message**                                            |
+---------------+--------------------------------------------------------+
| ``from``      | Contains sender address and balance information.       |
+---------------+--------------------------------------------------------+
| ``to``        | Contains receiver address and balance information.     |
+---------------+--------------------------------------------------------+

**Known errors**

+---------------+--------------------------------------------------------+
| **Parameter** | **Message**                                            |
+---------------+--------------------------------------------------------+
| ``address``   | Incorrect transfer address.                            |
+---------------+--------------------------------------------------------+
| ``address``   | Missed address                                         |
+---------------+--------------------------------------------------------+
