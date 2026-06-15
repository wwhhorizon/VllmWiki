# vllm-project/vllm#2007: AssertionError: tensor model parallel group is already initialized

| 字段 | 值 |
| --- | --- |
| Issue | [#2007](https://github.com/vllm-project/vllm/issues/2007) |
| 状态 | closed |
| 标签 |  |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AssertionError: tensor model parallel group is already initialized

### Issue 正文摘录

If I set `prompt_logprobs`, I get `AssertionError: tensor model parallel group is already initialized`. ``` import time from vllm import LLM, SamplingParams prompts = [ "write a 10000 word essay on the topic of ai", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=int(2**0), prompt_logprobs=1, ) model_name_or_path = "TheBloke/Xwin-LM-13B-V0.2-AWQ" llm = LLM(model=model_name_or_path, quantization="awq", dtype="auto", ) for batch_size in range(1, 1000, 100): try: start = time.time() outputs = llm.generate(prompts * batch_size, sampling_params) print(f'Batch size: {batch_size}, Time taken: {time.time() - start:.2f} seconds') except Exception as e: print(e) break ``` Output: ``` WARNING 12-11 02:28:43 config.py:140] awq quantization is not fully optimized yet. The speed can be slower than non-quantized models. INFO 12-11 02:28:43 llm_engine.py:72] Initializing an LLM engine with config: model='TheBloke/Xwin-LM-13B-V0.2-AWQ', tokenizer='TheBloke/Xwin-LM-13B-V0.2-AWQ', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantizat...

## 现有链接修复摘要

#43376 [WIP] Add FlashInfer NVFP4 GEMM + reduce-scatter fusion

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: th = "TheBloke/Xwin-LM-13B-V0.2-AWQ" llm = LLM(model=model_name_or_path, quantization="awq", dtype="auto", ) for batch_size in range(1, 1000, 100): try: start = time.time() outputs = llm.generate(prompts * batch_size, s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: AssertionError: tensor model parallel group is already initialized If I set `prompt_logprobs`, I get `AssertionError: tensor model parallel group is already initialized`. ``` import time from vllm import LLM, SamplingPa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ssertionError: tensor model parallel group is already initialized`. ``` import time from vllm import LLM, SamplingParams prompts = [ "write a 10000 word essay on the topic of ai", ] sampling_params = SamplingParams(temp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=awq, seed=0) INFO 12-11 02:2...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;sampling crash;oom;slowdown dtype;env_dependency;shape #43376 [WIP] Add FlashInfer NVFP4 GEMM + reduce-scatter fusion If I set `prompt_logprobs`, I get `AssertionError: tensor model parallel group is already initialize...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43376](https://github.com/vllm-project/vllm/pull/43376) | mentioned | 0.6 | [WIP] Add FlashInfer NVFP4 GEMM + reduce-scatter fusion | EMM path added too much overhead, so E2E did not improve. FlashInfer #2007-style in-kernel reduce idea: useful as a reference, but replacing NCCL with in-kernel/multimem reduce wa… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
