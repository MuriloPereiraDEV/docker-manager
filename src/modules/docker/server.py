import docker
from typing import Dict


class Server:
    def __init__(self, id: str, ip: str, port: int, name: str) -> None:
        self.id = id
        self.ip = ip
        self.port = port
        self.name = name

    def get_containers(self):
        try:
            client = docker.DockerClient(
                base_url=f"http://{self.ip}:{self.port}"
            )
            list_aux = client.containers.list()
            container_list = [container.attrs for container in list_aux]
            return container_list
        except Exception as exception:
            raise Exception(str(exception))

    def get_images(self):
        try:
            client = docker.DockerClient(
                base_url=f"http://{self.ip}:{self.port}"
            )
            list_aux = client.images.list()
            images_list = [image.attrs for image in list_aux]
            return images_list
        except Exception as exception:
            raise Exception(str(exception))

    def get_networks(self):
        try:
            client = docker.DockerClient(
                base_url=f"http://{self.ip}:{self.port}"
            )
            list_aux = client.networks.list()
            networks_list = [network.attrs for network in list_aux]
            return networks_list
        except Exception as exception:
            raise Exception(str(exception))

    def get_volumes(self):
        try:
            client = docker.DockerClient(
                base_url=f"http://{self.ip}:{self.port}"
            )
            list_aux = client.volumes.list()
            volume_list = [volume.attrs for volume in list_aux]
            return volume_list
        except Exception as exception:
            raise Exception(str(exception))
