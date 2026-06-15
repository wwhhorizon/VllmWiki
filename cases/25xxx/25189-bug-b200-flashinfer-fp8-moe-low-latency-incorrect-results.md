# vllm-project/vllm#25189: [Bug]: B200 FlashInfer FP8 MoE low-latency - incorrect results

| 字段 | 值 |
| --- | --- |
| Issue | [#25189](https://github.com/vllm-project/vllm/issues/25189) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: B200 FlashInfer FP8 MoE low-latency - incorrect results

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 and VLLM_FLASHINFER_MOE_BACKEND="latency" produces an incorrect outputs. Here is the code sample (basic.py with DeepSeekR1 model set): ``` # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) def main(): # Create an LLM. llm = LLM(model="deepseek-ai/DeepSeek-R1-0528", tensor_parallel_size=8) # Generate texts from the prompts. # The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}") print(f"Output: {generated_text!r}") print("-" * 60) if __name__ == "__main__":...

## 现有链接修复摘要

#25895 [Bugfix] Fix accuracy issue of TRTLLM FP8 MOE and improve logging

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: FileCopyrightText: Copyright contributors to the vLLM project from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: B200 FlashInfer FP8 MoE low-latency - incorrect results bug ### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 and VLLM_FLASHINFER_MOE_BACKEND="lat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: B200 FlashInfer FP8 MoE low-latency - incorrect results bug ### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 and VLLM_FLASHINFER_MOE_BACKEND="lat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: B200 FlashInfer FP8 MoE low-latency - incorrect results bug ### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 and VLLM_FLASHINFER_MOE_BACKEND="lat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: B200 FlashInfer FP8 MoE low-latency - incorrect results bug ### Your current environment ### 🐛 Describe the bug Running DeepSeekR1 on 8xB200 with VLLM_USE_FLASHINFER_MOE_FP8=1 and VLLM_FLASHINFER_MOE_BACKEND="lat...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25895](https://github.com/vllm-project/vllm/pull/25895) | closes_keyword | 0.95 | [Bugfix] Fix accuracy issue of TRTLLM FP8 MOE and improve logging | Fixes #25189: accuracy issues for TRTLLM DSR1 Latency kernels Bugs introduced in #23991 and #23640 Also fixes incorrect logging prints for which kernels are used. When Flashinfe |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
