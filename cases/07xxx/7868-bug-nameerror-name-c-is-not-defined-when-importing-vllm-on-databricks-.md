# vllm-project/vllm#7868: [Bug]: `NameError: name '_C' is not defined` when importing `vllm` on Databricks Runtime 14.3 ML

| 字段 | 值 |
| --- | --- |
| Issue | [#7868](https://github.com/vllm-project/vllm/issues/7868) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `NameError: name '_C' is not defined` when importing `vllm` on Databricks Runtime 14.3 ML

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm encountering a `NameError` when trying to import the `vllm` package on Databricks using Databricks Runtime Version 14.3 LTS ML (includes Apache Spark 3.5.0, GPU, Scala 2.12) with Node type `g4dn.4xlarge [T4]` (64 GB Memory, 1 GPU). **Steps to Reproduce**: 1. Launch a Databricks cluster with Databricks Runtime Version 14.3 LTS ML. 2. Install the `vllm` package via pip. 3. Run the following code snippet: ```python from vllm import LLM ``` **Expected Result**: The import should work without any errors. **Actual Result**: The following error is raised: ``` NameError: name '_C' is not defined File , line 1 from vllm import LLM --- File /local_disk0/.ephemeral_nfs/envs/pythonEnv-595ff8b8-9a48-4042-8e08-10c7b10a86d7/lib/python3.10/site-packages/vllm/__init__.py:3 from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.engine.llm_engine import LLMEngine File /local_disk0/.ephemeral_nfs/envs/pythonEnv-595ff8b8-9a48-4042-8e08-10c7b10a86d7/lib/python3.10/site-packages/vllm/engine/arg_utils.py:8 import torch ... File /local_disk0/.ephemeral_nfs/envs/pythonEnv-595ff8b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: `NameError: name '_C' is not defined` when importing `vllm` on Databricks Runtime 14.3 ML bug;stale ### Your current environment ### 🐛 Describe the bug I'm encountering a `NameError` when trying to import the `vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: #). ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: is not defined` when importing `vllm` on Databricks Runtime 14.3 ML bug;stale ### Your current environment ### 🐛 Describe the bug I'm encountering a `NameError` when trying to import the `vllm` package on Databricks usi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 2) with Node type `g4dn.4xlarge [T4]` (64 GB Memory, 1 GPU). **Steps to Reproduce**: 1. Launch a Databricks cluster with Databricks Runtime Version 14.3 LTS ML. 2. Install the `vllm` package via pip. 3. Run the followin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
