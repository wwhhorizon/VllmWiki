# vllm-project/vllm#21861: [Bug]: vllm/vllm-openai:latest is not compatible with 5090 anymore

| 字段 | 值 |
| --- | --- |
| Issue | [#21861](https://github.com/vllm-project/vllm/issues/21861) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm/vllm-openai:latest is not compatible with 5090 anymore

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi ! I pull today `docker pull vllm/vllm-openai:latest` But every model I tried I got: ``` NVIDIA GeForce RTX 5090 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90. If you want to use the NVIDIA GeForce RTX 5090 GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/ ``` It is strange because weeks ago used to works very well ! by the way: ``` root@srv-ia-010:/var/models# docker run --rm -it --entrypoint python3 vllm/vllm-openai:latest -c "import torch; print(torch.__version__)" 2.7.0+cu126 root@srv-ia-010:/var/models# ``` why cuda 12.6 ???????????? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment ### 🐛 Describe the bug Hi ! I pull today `docker pull vllm/vllm-openai:latest` But every model I tried I got: ``` NVIDIA GeForce RTX 5090 with CUDA capability sm_120 is not compatible with the c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: /vllm-openai:latest` But every model I tried I got: ``` NVIDIA GeForce RTX 5090 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyTorch install supports CUDA capabilities...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bug Hi ! I pull today `docker pull vllm/vllm-openai:latest` But every model I tried I got: ``` NVIDIA GeForce RTX 5090 with CUDA capability sm_120 is not compatible with the current PyTorch installation. The current PyT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm/vllm-openai:latest is not compatible with 5090 anymore bug;stale ### Your current environment ### 🐛 Describe the bug Hi ! I pull today `docker pull vllm/vllm-openai:latest` But every model I tried I got: ```...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: vllm/vllm-openai:latest is not compatible with 5090 anymore bug;stale ### Your current environment ### 🐛 Describe the bug Hi ! I pull today `docker pull vllm/vllm-openai:latest` But every model I tried I got: ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
