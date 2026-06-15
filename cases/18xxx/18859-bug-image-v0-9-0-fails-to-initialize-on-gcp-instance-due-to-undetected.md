# vllm-project/vllm#18859: [Bug]: Image v0.9.0 Fails to Initialize on GCP instance Due to Undetected Platform

| 字段 | 值 |
| --- | --- |
| Issue | [#18859](https://github.com/vllm-project/vllm/issues/18859) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 | install |
| Operator 关键词 | kernel |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Image v0.9.0 Fails to Initialize on GCP instance Due to Undetected Platform

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Detail The vLLM server Docker image vllm/vllm-openai:v0.9.0 (from ) does not correctly detect the hardware environment when deployed on an GCP GPU instance (eg. L4 GPU). This leads to a RuntimeError during the server's startup. This issue prevents the server from becoming operational. ### Steps to Reproduce: 1. Provision an L4 GPU instance. 1. Pull the specified vLLM Docker image: docker pull vllm/vllm-openai:v0.9.0 (or by its digest sha256:df2c55e5107afea09ea1a50f9dd96c99ebf97a795334c4d08f691f3d79b2ab12). 1. Attempt to start the vLLM OpenAI API server using this image on the L4 GPU instance. **Expected Behavior:** The vLLM server should initialize successfully, correctly identify the L4 GPU platform, and become ready to handle API requests. This is the observed behavior with the previous version, v0.8.5 **Actual Behavior:** The server fails to start and exits with a RuntimeError. The logs indicate that the platform is "UnspecifiedPlatform". The critical error leading to the crash is: `RuntimeError: Failed to infer device type`. Key Log Output & Traceback: ``` INFO 05-28 14:02:21 [__init__.py:247] No platform detected, vLLM i...

## 现有链接修复摘要

#25766 [Bug]: Set LD_LIBRARY_PATH to include the 'standard' CUDA location

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: rrent environment ### 🐛 Describe the bug ### Detail The vLLM server Docker image vllm/vllm-openai:v0.9.0 (from ) does not correctly detect the hardware environment when deployed on an GCP GPU instance (eg. L4 GPU). This...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: This issue prevents the server from becoming operational. ### Steps to Reproduce: 1. Provision an L4 GPU instance. 1. Pull the specified vLLM Docker image: docker pull vllm/vllm-openai:v0.9.0 (or by its digest sha256:df...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: et `VLLM_PLUGINS` to control which plugins to load. INFO 05-28 14:02:26 [config.py:1909] Disabled the custom all-reduce kernel because it is not supported on current platform. Traceback (most recent call last): File " "...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: , correctly identify the L4 GPU platform, and become ready to handle API requests. This is the observed behavior with the previous version, v0.8.5 **Actual Behavior:** The server fails to start and exits with a RuntimeE...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25766](https://github.com/vllm-project/vllm/pull/25766) | closes_keyword | 0.95 | [Bug]: Set LD_LIBRARY_PATH to include the 'standard' CUDA location | Fixes #18859 ## Test Plan Verify the built image works with an automounted CUDA version provided by the container platform at /usr/local/nvidia/lib64. Start vLLM in a minimal con |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
