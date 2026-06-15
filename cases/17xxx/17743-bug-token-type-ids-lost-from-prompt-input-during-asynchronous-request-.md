# vllm-project/vllm#17743: [Bug]: token_type_ids lost from prompt input during asynchronous request processing

| 字段 | 值 |
| --- | --- |
| Issue | [#17743](https://github.com/vllm-project/vllm/issues/17743) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: token_type_ids lost from prompt input during asynchronous request processing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `token_type_ids` is not properly passed from the `TokensPrompt` type into the actual model, only when using the AsyncLLMEngine. This causes models like cross encoders using the `score` type task to produce invalid values. Here is the minimum reproducible example as a standalone script, along with demonstration of the patched method - `InputPreprocessor._prompt_to_llm_inputs_async`: ```python #!/usr/bin/env python3 """Script to demonstrate regression in vLLM scoring between sync and async approaches.""" import asyncio import logging import sys from typing import Optional, Tuple import torch from typing_extensions import assert_never from vllm import LLM, AsyncEngineArgs, AsyncLLMEngine, PoolingParams, TokensPrompt from vllm.inputs import ( SingletonPrompt, TokenInputs, token_inputs, ) from vllm.inputs.parse import parse_singleton_prompt from vllm.inputs.preprocess import InputPreprocessor from vllm.lora.request import LoRARequest from vllm.multimodal.inputs import MultiModalInputs logging.basicConfig( level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s" ) logger = logging.getLogger(__name__) def get_sync_score(mo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: `score` type task to produce invalid values. Here is the minimum reproducible example as a standalone script, along with demonstration of the patched method - `InputPreprocessor._prompt_to_llm_inputs_async`: ```python #...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ids` is not properly passed from the `TokensPrompt` type into the actual model, only when using the AsyncLLMEngine. This causes models like cross encoders using the `score` type task to produce invalid values. Here is t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: x. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: token_type_ids lost from prompt input during asynchronous request processing bug;stale ### Your current environment ### 🐛 Describe the bug `token_type_ids` is not properly passed from the `TokensPrompt` type into...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ng the `score` type task to produce invalid values. Here is the minimum reproducible example as a standalone script, along with demonstration of the patched method - `InputPreprocessor._prompt_to_llm_inputs_async`: ```p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
