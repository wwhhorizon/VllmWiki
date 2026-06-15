# vllm-project/vllm#31253: [Bug]: `VLLM_USE_FLASHINFER_MOE_FP16=1` generate different logprob for the same prompt in different run

| 字段 | 值 |
| --- | --- |
| Issue | [#31253](https://github.com/vllm-project/vllm/issues/31253) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `VLLM_USE_FLASHINFER_MOE_FP16=1` generate different logprob for the same prompt in different run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `VLLM_USE_FLASHINFER_MOE_FP16=1` generate different logprob for a single prompt on different run. scripts ```python # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", # "The president of the United States is", # "The capital of France is", # "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0, max_tokens=1, logprobs=5) def main(): # Create an LLM. llm = LLM(model="Qwen/Qwen3-30B-A3B", enforce_eager=True, tensor_parallel_size=2, enable_expert_parallel=True) # Generate texts from the prompts. # The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for output in outputs: prompt = output.prompt print(f"Prompt: {prompt!r}") # print(f"Logprob: {output.outputs[0].logprobs[0]}") for logit, logprob in output.outputs[0].logprobs[0].items(): print(f"Logit No: {logit}") print(f"...

## 现有链接修复摘要

#31279 [Bugfix] Disable FlashInfer MoE in batch invariant mode for determinism

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ax_tokens=1, logprobs=5) def main(): # Create an LLM. llm = LLM(model="Qwen/Qwen3-30B-A3B", enforce_eager=True, tensor_parallel_size=2, enable_expert_parallel=True) # Generate texts from the prompts. # The output is a l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: FileCopyrightText: Copyright contributors to the vLLM project from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", # "The president of the United States is", # "The capital of France i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: `VLLM_USE_FLASHINFER_MOE_FP16=1` generate different logprob for the same prompt in different run bug ### Your current environment ### 🐛 Describe the bug `VLLM_USE_FLASHINFER_MOE_FP16=1` generate different logprob...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: `VLLM_USE_FLASHINFER_MOE_FP16=1` generate different logprob for the same prompt in different run bug ### Your current environment ### 🐛 Describe the bug `VLLM_USE_FLASHINFER_MOE_FP16=1` generate different logprob...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31279](https://github.com/vllm-project/vllm/pull/31279) | closes_keyword | 0.95 | [Bugfix] Disable FlashInfer MoE in batch invariant mode for determinism | Fixes #31253 🤖 Generated with [Claude Code](https://claude.com/claude-code) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
