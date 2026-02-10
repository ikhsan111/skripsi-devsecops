import time
import asyncio

async def proses_data():
    # Memblokir event loop dengan sleep sinkronus
    # Rule: "Use non-blocking sleep functions in asynchronous code"
    time.sleep(5) 
    return "Selesai"
