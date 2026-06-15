# vllm-project/vllm#8677: [Bug]: Neuron + Vllm inference broken with backward incompatible change

| 字段 | 值 |
| --- | --- |
| Issue | [#8677](https://github.com/vllm-project/vllm/issues/8677) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Neuron + Vllm inference broken with backward incompatible change

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Recent change as part of this [commit](https://github.com/vllm-project/vllm/commit/99aa4eddaf929f57dac405b00db3f5286624ee8b) has used new Python Custom Op High level APIs which are only supported with torch > 2.4. [Ref1](https://pytorch.org/tutorials/advanced/python_custom_ops.html) Neuron currently supports upto pytorch 2.1 so its leading to errors when following the installation steps here - https://docs.vllm.ai/en/latest/getting_started/neuron-installation.html and running the offline inference script - https://github.com/vllm-project/vllm/blob/main/examples/offline_inference_neuron.py with following error ``` Traceback (most recent call last): File "/home/Vllm_Upstream/bug_report/vllm/examples/offline_inference_neuron.py", line 3, in from vllm import LLM, SamplingParams File "/home/Vllm_Upstream/bug_report/vllm/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/home/Vllm_Upstream/bug_report/vllm/vllm/engine/arg_utils.py", line 11, in from vllm.config import (CacheConfig, ConfigFormat, DecodingConfig, File "/home/Vllm_Upstream/bug_report/vllm/v...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ly supports upto pytorch 2.1 so its leading to errors when following the installation steps here - https://docs.vllm.ai/en/latest/getting_started/neuron-installation.html and running the offline inference script - https...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: kward incompatible change bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Recent change as part of this [commit](https://github.com/vllm-project/vllm/commit/99aa4eddaf92...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g]: Neuron + Vllm inference broken with backward incompatible change bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Recent change as part of this [commit](https://githu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: del_support;quantization;speculative_decoding cuda;operator;quantization;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
