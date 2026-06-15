# vllm-project/vllm#33917: [Feature]: Up to date docker images

| 字段 | 值 |
| --- | --- |
| Issue | [#33917](https://github.com/vllm-project/vllm/issues/33917) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
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

> [Feature]: Up to date docker images

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The official vllm-openai docker image appears to be significantly outdated -- even the nightly image! I was already having to base on top of the docker image and install a later transformers version to run some of the models that vllm claims to support. However, after installing a new host with CUDA 13.1, I found that the vllm image won't run even with that update, due to host nvidia driver and cuda library version incompatibilities. I'm having to apply the following Dockerfile to run vLLM. Suggest the official Dockerfile is updated along similar lines. ``` FROM vllm/vllm-openai:nightly ENV DEBIAN_FRONTEND=noninteractive RUN apt-get update && apt-get install -y git liberror-perl cuda-toolkit-13-1 && apt-get -y --purge remove \*cuda\*-12-\* RUN uv pip install --system git+https://github.com/huggingface/transformers.git RUN uv pip install --system sentencepiece ``` The noninteractive part is probably already set in the base, was just making sure. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Feature]: Up to date docker images feature request ### 🚀 The feature, motivation and pitch The official vllm-openai docker image appears to be significantly outdated -- even the nightly image! I was already having to b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s that vllm claims to support. However, after installing a new host with CUDA 13.1, I found that the vllm image won't run even with that update, due to host nvidia driver and cuda library version incompatibilities. I'm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: docker image and install a later transformers version to run some of the models that vllm claims to support. However, after installing a new host with CUDA 13.1, I found that the vllm image won't run even with that upda...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Up to date docker images feature request ### 🚀 The feature, motivation and pitch The official vllm-openai docker image appears to be significantly outdated -- even the nightly image! I was already having to b...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;frontend_api;model_support cuda env_dependency 🚀 The feature, mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
