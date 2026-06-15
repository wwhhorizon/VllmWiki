# vllm-project/vllm#7592: [Performance]: vllm 0.5.4 with enable_chunked_prefill =True, throughput is slightly lower than 0.5.3~0.5.0.

| 字段 | 值 |
| --- | --- |
| Issue | [#7592](https://github.com/vllm-project/vllm/issues/7592) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: vllm 0.5.4 with enable_chunked_prefill =True, throughput is slightly lower than 0.5.3~0.5.0.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Throughput and latency vary with max_num_seqs。 vllm 0.5.4 with enable_chunked_prefill =True, throughput is slightly lower than 0.5.3~0.5.1. very strange. ![chunked_prefill](https://github.com/user-attachments/assets/0250456a-60b8-45e9-82ad-316204f6e778) | max_num_seqs | requests/s | disable 0.5.4 | requests/s | disable 0.5.3 | requests/s | disable 0.5.2 | requests/s | disable 0.5.1 | requests/s | enable 0.5.4 | requests/s | enable 0.5.3 | requests/s | enable 0.5.2 | requests/s | enable 0.5.1 | |--------------|------------|---------------|------------|---------------|------------|---------------|------------|---------------|------------|--------------|------------|--------------|------------|--------------|------------|--------------| | 1024 | 2.5115 | 36.1 | 2.4747 | 36.69 | 2.4878 | 36.82 | 2.4972 | 36.33 | 3.1797 | 39.72 | 3.1341 | 40.15 | 3.1696 | 39.67 | 3.1745 | 39.61 | | 768 | 3.2838 | 42.6 | 3.2242 | 43.48 | 3.2608 | 42.93 | 3.2648 | 42.88 | 4.1047 | 43.4 | 3.9708 | 44.42 | 4.0413 | 43.6 | 4.0439 | 43.57 | | 512 | 4.1063 | 51.93 | 4.0102 | 53.22 | 4.0966 | 52.07 | 4.0998 | 51.97 | 4.6486 | 46.79 | 4.6377 | 46.25 | 4.7419 |...

## 现有链接修复摘要

#7874 [Bugfix] Fix #7592 vllm 0.5.4 enable_chunked_prefill throughput is slightly lower than 0.5.3~0.5.0.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: 55 | 1.593 | 19.44 | 1.5942 | 19.43 | ``` import os import random import numpy as np import time def benchmark(args): random.seed(args.seed) os.environ["VLLM_LOGGING_LEVEL"] = "ERROR" os.environ["VLLM_NO_USAGE_STATS"] =...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: vllm 0.5.4 with enable_chunked_prefill =True, throughput is slightly lower than 0.5.3~0.5.0. bug ### Your current environment ### 🐛 Describe the bug Throughput and latency vary with max_num_seqs。 vllm 0.5...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: rgs( model=args.model, tokenizer=args.tokenizer, quantization=args.quantization, tensor_parallel_size=args.tensor_parallel_size, seed=args.seed, trust_remote_code=args.trust_remote_code, dtype=args.dtype, max_model_len=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ms( n=args.n, temperature=0.0 if args.use_beam_search else 1.0, top_p=1.0, use_beam_search=args.use_beam_search, ignore_eos=True, max_tokens=output_len, ) engine.add_request(str(request_id), inputs, sampli
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ompt print(vllm.__version__) engine_args = EngineArgs( model=args.model, tokenizer=args.tokenizer, quantization=args.quantization, tensor_parallel_size=args.tensor_parallel_size, seed=args.seed, trust_remote_code=args.t...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7874](https://github.com/vllm-project/vllm/pull/7874) | closes_keyword | 0.95 | [Bugfix] Fix #7592 vllm 0.5.4 enable_chunked_prefill throughput is slightly lower than 0.5.3~0.5.0. | FIX #7592 [by definition](https://docs.vllm.ai/en/latest/models/performance.html#chunked-prefill) > By default, vLLM scheduler prioritizes prefills ... > Once chunked prefill |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
