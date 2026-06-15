# vllm-project/vllm#17047: [Bug]: ValueError when using Multi-Instance GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#17047](https://github.com/vllm-project/vllm/issues/17047) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError when using Multi-Instance GPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using the [Multi-Instance GPU](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#cuda-device-enumeration) feature, the device names are not integers. They are that start with the letters "MIG-". The current vllm implementation assumes that GPU names are integers. On line 53 in `vllm/platforms/cuda.py`, the device name is cast into integer. This leads to the following error message: ``` ValueError: invalid literal for int() with base 10: 'MIG-e3e1cf80-63a6-5b1d-8237-3daa43edde87' ``` It's possible supporting MIG is not possible, but the error message could be more descriptive. The could also be a mention of the issue in lvvm documentation. To properly reproduce the issue, you would need to set up Multi-Instance GPU. Once this is set up, the following command will reproduce the error: ```bash python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3-8B-Instruct ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GPU](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#cuda-device-enumeration) feature, the device names are not integers. They are that start with the letters "MIG-". The current vllm implementation a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: oduce the error: ```bash python -m vllm.entrypoints.openai.api_server --model meta-llama/Meta-Llama-3-8B-Instruct ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and as...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: could also be a mention of the issue in lvvm documentation. To properly reproduce the issue, you would need to set up Multi-Instance GPU. Once this is set up, the following command will reproduce the error: ```bash pyth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
