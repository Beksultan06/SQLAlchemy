import asyncio
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '...'))

from queries.core import create_tables

create_tables()

asyncio.run(create_tables())