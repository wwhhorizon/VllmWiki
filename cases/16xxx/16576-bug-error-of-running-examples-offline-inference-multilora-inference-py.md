# vllm-project/vllm#16576: [Bug]: Error of running examples/offline_inference/multilora_inference.py using vllm v0.8.3

| 字段 | 值 |
| --- | --- |
| Issue | [#16576](https://github.com/vllm-project/vllm/issues/16576) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error of running examples/offline_inference/multilora_inference.py using vllm v0.8.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I ran moltilora_inference.py without modification, it get error `"RuntimeError: The expanded size of the tensor (58) must match the existing size (3) at non-singleton dimension 0. Target sizes: [58, 256]. Tensor sizes: [3, 256]"` ```python # SPDX-License-Identifier: Apache-2.0 """ This example shows how to use the multi-LoRA functionality for offline inference. Requires HuggingFace credentials for access to Llama2. """ from typing import Optional from huggingface_hub import snapshot_download from vllm import EngineArgs, LLMEngine, RequestOutput, SamplingParams from vllm.lora.request import LoRARequest def create_test_prompts( lora_path: str ) -> list[tuple[str, SamplingParams, Optional[LoRARequest]]]: """Create a list of test prompts with their sampling parameters. 2 requests for base model, 4 requests for the LoRA. We define 2 different LoRA adapters (using the same model for demo purposes). Since we also set `max_loras=1`, the expectation is that the requests with the second LoRA adapter will be ran after all requests with the first adapter have finished. """ return [ ("A robot may not injure a human being", SamplingParams...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Requires HuggingFace credentials for access to Llama2. """ from typing import Optional from huggingface_hub import snapshot_download from vllm import EngineArgs, LLMEngine, RequestOutput, SamplingParams from vllm.lora.r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: how to use the multi-LoRA functionality for offline inference. Requires HuggingFace credentials for access to Llama2. """ from typing import Optional from huggingface_hub import snapshot_download from vllm import Engine...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: xamples/offline_inference/multilora_inference.py using vllm v0.8.3 bug;unstale ### Your current environment ### 🐛 Describe the bug When I ran moltilora_inference.py without modification, it get error `"RuntimeError: The...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ased on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]", # noqa: E501 SamplingParams(temperat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
