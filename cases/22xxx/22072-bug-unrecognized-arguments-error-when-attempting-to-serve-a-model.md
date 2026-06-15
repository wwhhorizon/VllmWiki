# vllm-project/vllm#22072: [Bug]: "unrecognized arguments" error when attempting to "serve" a model

| 字段 | 值 |
| --- | --- |
| Issue | [#22072](https://github.com/vllm-project/vllm/issues/22072) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "unrecognized arguments" error when attempting to "serve" a model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am deploying vllm with Docker Compose on an NVIDIA GeForce RTX 3060 Ti, on Ubuntu Server 24.04 LTS. I am getting the "unrecognized arguments" error on the `api_server.py` script when I try to run this container, in the Docker logs. The documentation for vLLM says that this is the command line to use to run the `serve` command. What is the actual correct command I should use, since the documentation seems to be incorrect? Documentation: https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html ```yml services: vllm: container_name: vllm image: vllm/vllm-openai:latest restart: unless-stopped ipc: host ports: - 10200:8000 deploy: resources: reservations: devices: - driver: nvidia count: all capabilities: [gpu] pull_policy: always volumes: - ./vllm/huggingface:/root/.cache/huggingface command: - serve - HuggingFaceTB/SmolLM3-3B - --dtype auto - --api-key asdfasdfasdfasdfasdfasdf ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of freq...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: be the bug I am deploying vllm with Docker Compose on an NVIDIA GeForce RTX 3060 Ti, on Ubuntu Server 24.04 LTS. I am getting the "unrecognized arguments" error on the `api_server.py` script when I try to run this conta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: "unrecognized arguments" error when attempting to "serve" a model bug;stale ### Your current environment ### 🐛 Describe the bug I am deploying vllm with Docker Compose on an NVIDIA GeForce RTX 3060 Ti, on Ubuntu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: current environment ### 🐛 Describe the bug I am deploying vllm with Docker Compose on an NVIDIA GeForce RTX 3060 Ti, on Ubuntu Server 24.04 LTS. I am getting the "unrecognized arguments" error on the `api_server.py` scr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: gingface command: - serve - HuggingFaceTB/SmolLM3-3B - --dtype auto - --api-key asdfasdfasdfasdfasdfasdf ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: "unrecognized arguments" error when attempting to "serve" a model bug;stale ### Your current environment ### 🐛 Describe the bug I am deploying vllm with Docker Compose on an NVIDIA GeForce RTX 3060 Ti, on Ubuntu Serv...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
