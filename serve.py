import grpc
import logging
import environ
from concurrent import futures

from gRPC.services import auth
from gRPC.protos import auth_pb2_grpc

env = environ.Env()
env.read_env(".env")

gRPC_HOST = env.str("GRPC_HOST", default="localhost")
gRPC_PORT = env.int("GRPC_PORT", default=50051)



def setup_logger():
    """Configure the logging module."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def serve(host: str, port: int) -> None:
    """Start and run the gRPC server."""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Register the Auth service
    auth_service = auth.AuthService()
    auth_pb2_grpc.add_AuthServicer_to_server(auth_service, server)

    server_address = f"{host}:{port}"
    server.add_insecure_port(server_address)
    server.start()

    logging.info("gRPC server is running at %s", server_address)
    server.wait_for_termination()


if __name__ == "__main__":
    setup_logger()
    serve(
        host=gRPC_HOST,
        port=gRPC_PORT
    )
