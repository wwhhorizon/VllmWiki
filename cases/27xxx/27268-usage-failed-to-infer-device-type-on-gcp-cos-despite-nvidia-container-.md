# vllm-project/vllm#27268: [Usage]: failed to infer device type on GCP COS despite nvidia container toolkit installed

| 字段 | 值 |
| --- | --- |
| Issue | [#27268](https://github.com/vllm-project/vllm/issues/27268) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: failed to infer device type on GCP COS despite nvidia container toolkit installed

### Issue 正文摘录

### Your current environment I failed to run this script on GCP COS. ### How would you like to use vllm I was trying to use VLLM on a Google Cloud (GCP) Container-Optimized OS (COS) instance via Docker. I followed GCP's [documentation](https://cloud.google.com/container-optimized-os/docs/how-to/run-gpus) to install the nvidia driver, including mapping nvidia driver-related dirs to the Docker container. All tests worked fine. However, when trying to start a VLLM server via Docker, I got the error that `libcuda.so.1` cannot be found and VLLM failed to infer device info. I tried to change the target dirs in the mapping to like `/usr/local/lib`, `/usr/local/cuda/lib`, etc. But no luck. I also tried adding the flags `--runtime nvidia --gpus all` per [this instruction](https://docs.vllm.ai/en/v0.8.4/deployment/docker.html) but got the error that `Error response from daemon: unknown or invalid runtime name: nvidia.` If someone can shed the light of where vllm official Docker image looks for CUDA stuff, it will be greatly appreciated. Thanks in advance. The complete command and error: ``` $ docker run -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN= " -p 801...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: failed to infer device type on GCP COS despite nvidia container toolkit installed usage;stale ### Your current environment I failed to run this script on GCP COS. ### How would you like to use vllm I was trying to use V...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: advance. The complete command and error: ``` $ docker run -v ~/.cache/huggingface:/root/.cache/huggingface --env "HUGGING_FACE_HUB_TOKEN= " -p 8010:8000 --ipc=host vllm/vllm-openai:latest --model mistralai/Mistral-7B-v0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: when trying to start a VLLM server via Docker, I got the error that `libcuda.so.1` cannot be found and VLLM failed to infer device info. I tried to change the target dirs in the mapping to like `/usr/local/lib`, `/usr/l...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: timized-os/docs/how-to/run-gpus) to install the nvidia driver, including mapping nvidia driver-related dirs to the Docker container. All tests worked fine. However, when trying to start a VLLM server via Docker, I got t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: device type on GCP COS despite nvidia container toolkit installed usage;stale ### Your current environment I failed to run this script on GCP COS. ### How would you like to use vllm I was trying to use VLLM on a Google...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
