# vllm-project/vllm#7880: [Bug]: Special tokens not generated for GGUF when tensor_parallel_size=2

| 字段 | 值 |
| --- | --- |
| Issue | [#7880](https://github.com/vllm-project/vllm/issues/7880) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Special tokens not generated for GGUF when tensor_parallel_size=2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using GGUF quants of LLAMA 3.1 8B (other sizes, models or non-gguf not tried) and using a `tensor_parallel_size` of `2` the inference process appears to be unable to generate special tokens. I put a debug print in the sampler function before any of the logits processors and it reliably showed an exact 0 for the stop tokens. Setting `tensor_parallel_size` to `1` on the same setup leads to expected behavior, with the model generating the end-of-response token when appropriate. Due to the fact that the bug triggering hinges on VLLM's tensor parallelism functionality begin enabled, I do not think this is a transformers issue and I'm not sure how an equivalent test could be run there. There is an external file required to run the test in the form of the model GGUF file. Huggingface link is included. ```python #!/usr/bin/env python3 from vllm import AsyncLLMEngine, AsyncEngineArgs, SamplingParams, TokensPrompt import asyncio llm = AsyncLLMEngine.from_engine_args(AsyncEngineArgs( model="Meta-Llama-3.1-8B-Instruct-Q8_0.gguf", # From https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF tensor_parallel_size=2, # Set this t...

## 现有链接修复摘要

#7954 [Bugfix] Fix incorrect vocal embedding shards for GGUF model in tensor parallelism

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Special tokens not generated for GGUF when tensor_parallel_size=2 bug ### Your current environment ### 🐛 Describe the bug When using GGUF quants of LLAMA 3.1 8B (other sizes, models or non-gguf not tried) and usi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: urrent environment ### 🐛 Describe the bug When using GGUF quants of LLAMA 3.1 8B (other sizes, models or non-gguf not tried) and using a `tensor_parallel_size` of `2` the inference process appears to be unable to genera...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: print(out_tokens) if len(out_tokens) 32K. Currently, chunked prefill might not work with some features or models. If you encounter any issues, please disable chunked prefill by setting --enable-chunked-prefill=False. IN...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug When using GGUF quants of LLAMA 3.1 8B (other sizes, models or non-gguf not tried) and using a `tensor_parallel_size` of `2` the inference process appears to be unable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Due to the fact that the bug triggering hinges on VLLM's tensor parallelism functionality begin enabled, I do not think this is a transformers issue and I'm not sure how an equivalent test could be run there. There is a...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7954](https://github.com/vllm-project/vllm/pull/7954) | closes_keyword | 0.95 | [Bugfix] Fix incorrect vocal embedding shards for GGUF model in tensor parallelism | FIX #7880 (*link existing issues this PR will resolve*) - ~~This PR aims to fix the incorrect logits' calculation for gguf model when using tensor parallelism.~~ - This PR fixes |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
