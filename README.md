# silero

Docker image CPU

> aspichakou/silero

Docker image GPU

> aspichakou/silero-gpu

## Docker for GPU
Add the following content to the file /etc/docker/daemon.json:

```json
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    },
    "default-runtime": "nvidia"
}
```
