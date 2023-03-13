import sql
import asyncio

HEADER = 8
HOST = "0.0.0.0"
PORT = 12345
FORMAT = "utf-8"
ADDR = (HOST, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

async def handle(reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
    while True:
        try:
            print(writer.get_extra_info('peername'))
            data = await reader.read(100)
            message = data.decode()
            addr = writer.get_extra_info('peername')
            print(f"Received {message!r} from {addr!r}")
            print(f"Send: {message!r}")
            writer.write(data)
            await writer.drain()
            if message == DISCONNECT_MESSAGE:
                print("Close the connection")
                writer.close()
                await writer.wait_closed()
                break
        except:
            print("Close the connection")
            writer.close()
            await writer.wait_closed()
            break
async def main():
    server = await asyncio.start_server(handle, '127.0.0.1', 8888)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()
asyncio.run(main())