# vllm-project/vllm#25960: [Bug]: llama 4 family is incompatible with CUDA graph FULL_AND_PIECEWISE mode

| 字段 | 值 |
| --- | --- |
| Issue | [#25960](https://github.com/vllm-project/vllm/issues/25960) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: llama 4 family is incompatible with CUDA graph FULL_AND_PIECEWISE mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Phenomenon For the current main(0.11.0rc2.dev73+gfa7e254a7), llama 4 model family suffers from gibberish outputs for long context (beyond `torch.compile` length, that is): ```sh # Launch llama 4 maverick server with --max-num-batched-tokens 16K vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 \ --tensor-parallel-size 8 \ --max-model-len 512K \ --max-num-batched-tokens 16K \ --max-num-seqs 16 \ --enable-auto-tool-choice \ --tool-call-parser pythonic \ --mm-encoder-tp-mode data \ --limit-mm-per-prompt {"image":5} ``` ```python import json import uuid from transformers import AutoTokenizer from openai import OpenAI tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8") print("\n====needle-in-a-haystack test====\n") # Test NIAH type problem with input length 8K and 32K, resp. for context_len in [8 * 1024, 32 * 1024]: uuid_puzzle = {str(uuid.uuid4()): str(uuid.uuid4())} uuid_q, uuid_a = next(iter(uuid_puzzle.items())) puzzle_template = "JSON data:\n{uuid_puzzle}\nQ: \nKey: \"{uuid_q}\"\nThe value associated with the specified key is: " messages = [{"role": "system", "content": "You...

## 现有链接修复摘要

#25444 [Perf] Change default CUDAGraphMode from PIECEWISE to FULL_AND_PIECEWISE

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: el family suffers from gibberish outputs for long context (beyond `torch.compile` length, that is): ```sh # Launch llama 4 maverick server with --max-num-batched-tokens 16K vllm serve meta-llama/Llama-4-Maverick-17B-128...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: llama 4 family is incompatible with CUDA graph FULL_AND_PIECEWISE mode bug ### Your current environment ### 🐛 Describe the bug # Phenomenon For the current main(0.11.0rc2.dev73+gfa7e254a7), llama 4 model family s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: hed-tokens 16K vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 \ --tensor-parallel-size 8 \ --max-model-len 512K \ --max-num-batched-tokens 16K \ --max-num-seqs 16 \ --enable-auto-tool-choice \ --tool-call-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: llama 4 family is incompatible with CUDA graph FULL_AND_PIECEWISE mode bug ### Your current environment ### 🐛 Describe the bug # Phenomenon For the current main(0.11.0rc2.dev73+gfa7e254a7), llama 4 model family s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ion;sampling_logits;speculative_decoding cuda;fp8;gemm;operator;sampling;triton build_error;nan_inf dtype;env_dependency #25444 [Perf] Change default CUDAGraphMode from PIECEWISE to FULL_AND_PIECEWISE Your current envir...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25444](https://github.com/vllm-project/vllm/pull/25444) | mentioned | 0.45 | [Perf] Change default CUDAGraphMode from PIECEWISE to FULL_AND_PIECEWISE | e8e3e4e3a4d3e3f8e4e1e6d8f9f0e0e6c1e1f0e1e5f... ``` # analysis after #25444, the default cuda graph mode for most models has been changed from piecewise to full_and_piecewise. this… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
