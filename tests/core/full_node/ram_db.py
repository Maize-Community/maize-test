from typing import Tuple
from pathlib import Path

import random
import aiosqlite

from maize.consensus.blockchain import Blockchain
from maize.consensus.constants import ConsensusConstants
from maize.full_node.block_store import BlockStore
from maize.full_node.coin_store import CoinStore
from maize.util.db_wrapper import DBWrapper2


async def create_ram_blockchain(consensus_constants: ConsensusConstants) -> Tuple[DBWrapper2, Blockchain]:
    uri = f"file:db_{random.randint(0, 99999999)}?mode=memory&cache=shared"
    connection = await aiosqlite.connect(uri, uri=True)
    db_wrapper = DBWrapper2(connection)
    await db_wrapper.add_connection(await aiosqlite.connect(uri, uri=True))
    block_store = await BlockStore.create(db_wrapper)
    coin_store = await CoinStore.create(db_wrapper)
    blockchain = await Blockchain.create(coin_store, block_store, consensus_constants, Path("."), 2)
    return db_wrapper, blockchain
