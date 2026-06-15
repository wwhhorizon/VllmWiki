# vllm-project/vllm#27154: [Installation]: How to reduce the vllm image

| 字段 | 值 |
| --- | --- |
| Issue | [#27154](https://github.com/vllm-project/vllm/issues/27154) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: How to reduce the vllm image

### Issue 正文摘录

### Your current environment Hi, I looked at docker pull vllm/vllm-openai:latest — the image is around 12 GB. I’m exploring ways to reduce the vLLM image size specifically for NVIDIA L40s (i use linux amd64). any ideas? does building vllm from source help to reduce the image? Here’s what I’ve tried so far (but not sure how to install flashinfer): ``` FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 # Install Python and pip RUN apt-get update && apt-get install -y python3 python3-pip && \ apt-get clean && rm -rf /var/lib/apt/lists/* # Install only vLLM and production dependencies RUN pip3 install --no-cache-dir vllm # Set CUDA arch for A100 (8.0) ENV TORCH_CUDA_ARCH_LIST="8.9+PTX" # Expose API port EXPOSE 8000 ENTRYPOINT ["python3", "-m", "vllm.entrypoints.openai.api_server"] ``` more infos: https://discuss.vllm.ai/t/current-vllm-docker-image-size-is-12-64gb-how-to-reduce-it/1204/4 https://docs.vllm.ai/en/latest/deployment/docker.html#building-vllm-s-docker-image-from-source pr: https://github.com/vllm-project/vllm/pull/22377 ### How you are installing vllm ```sh pip install -vvv vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: How to reduce the vllm image installation;stale ### Your current environment Hi, I looked at docker pull vllm/vllm-openai:latest — the image is around 12 GB. I’m exploring ways to reduce the vLLM image s
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: e tried so far (but not sure how to install flashinfer): ``` FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 # Install Python and pip RUN apt-get update && apt-get install -y python3 python3-pip && \ apt-get clean && rm -rf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: e the image? Here’s what I’ve tried so far (but not sure how to install flashinfer): ``` FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04 # Install Python and pip RUN apt-get update && apt-get install -y python3 python3-pip...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: How to reduce the vllm image installation;stale ### Your current environment Hi, I looked at docker pull vllm/vllm-openai:latest — the image is around 12 GB. I’m exploring ways to reduce the vLLM image s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: our current environment Hi, I looked at docker pull vllm/vllm-openai:latest — the image is around 12 GB. I’m exploring ways to reduce the vLLM image size specifically for NVIDIA L40s (i use linux amd64). any ideas? does...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
