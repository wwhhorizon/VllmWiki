# vllm-project/vllm#39827: [Bug]: VLLM Gemma4 output repeated token

| 字段 | 值 |
| --- | --- |
| Issue | [#39827](https://github.com/vllm-project/vllm/issues/39827) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM Gemma4 output repeated token

### Issue 正文摘录

### Your current environment vllm and tpu-inference are installed following https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#install-from-source Vllm commit: 08bfedc152f064d8e84f85c4f42b810e5a564229 tpu-inference: 6a488560b005aa71bbc2af6a32a2e9f814c71298 (from Apr 13) ### 🐛 Describe the bug Bug: Gemma4 has a repeated output token, resulting in incorrect output example: Gemma4 ouput: `[RequestOutput(request_id=0, prompt='Paris is', prompt_token_ids=[50429, 563], encoder_prompt=None, encoder_prompt_token_ids=None, prompt_logprobs=None, outputs=[CompletionOutput(index=0, text=' is is is is is is is is is is', token_ids=[563, 563, 563, 563, 563, 563, 563, 563, 563, 563], routed_experts=None, cumulative_logprob=None, logprobs=None, finish_reason=length, stop_reason=None)], finished=True, metrics=None, lora_request=None, num_cached_tokens=0)]` When changing VLLM model ID to "Qwen/Qwen3-30B-A3B", the output is “the capital of France. It is a city of” To reproduce the bug, run the following script: ```python import gc import logging import os from vllm import LLM, SamplingParams import jax from jax import config as jax_config VLLM_MODEL_ID="google/gemma-4-26B-A4B"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eated token bug ### Your current environment vllm and tpu-inference are installed following https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#install-from-source Vllm commit: 08bfedc152f064d8e84f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: VLLM Gemma4 output repeated token bug ### Your current environment vllm and tpu-inference are installed following https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#install-from-source Vllm...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: VLLM Gemma4 output repeated token bug ### Your current environment vllm and tpu-inference are installed following https://docs.vllm.ai/projects/tpu/en/latest/getting_started/installation/#install-from-source Vllm...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: en3-30B-A3B", the output is “the capital of France. It is a city of” To reproduce the bug, run the following script: ```python import gc import logging import os from vllm import LLM, SamplingParams import jax from jax...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
