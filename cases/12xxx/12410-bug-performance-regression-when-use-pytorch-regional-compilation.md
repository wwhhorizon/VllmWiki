# vllm-project/vllm#12410: [Bug]: Performance regression when use PyTorch regional compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#12410](https://github.com/vllm-project/vllm/issues/12410) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Performance regression when use PyTorch regional compilation

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Performance regression occurs when use regional compilation after https://github.com/vllm-project/vllm/pull/11967 When run : ``` python -u benchmarks/benchmark_throughput.py \ --model /path_to_model/Llama-2-7b-hf \ --device hpu \ --seed 2024 \ --backend vllm \ --dataset /path_to_dataset/ShareGPT_V3_unfiltered_cleaned_split.json \ --num-prompts 1000 \ --dtype bfloat16 \ --max-model-len 4096 \ --max-num-batched-tokens 8192 \ --max-num-seqs 128 \ --use-padding-aware-scheduling ``` The [regional compilation](https://pytorch.org/tutorials/recipes/regional_compilation.html) is used in [the code](https://github.com/HabanaAI/vllm-fork/blob/1b8b69e7b302857549ee95d34c0593bd675a71fd/vllm/worker/hpu_model_runner.py#L227C2-L258C37) I observe big throughput degradation due to recompilation happened due to indexing in attention layer: ``` torch/_dynamo/guards.py:2813] [1/4] [__recompiles] Recompiling function forward in /software/users/akotlowski/vllm-fork/vllm/model_executor/models/llama.py:267 torch/_dynamo/guards.py:2813] [1/4] [__recompiles] triggered by the following guard failure(s): torch/_dynamo/guard...

## 现有链接修复摘要

#12536 [Kernel] Use self.kv_cache and forward_context.attn_metadata in Attention.forward

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: heduling ``` The [regional compilation](https://pytorch.org/tutorials/recipes/regional_compilation.html) is used in [the code](https://github.com/HabanaAI/vllm-fork/blob/1b8b69e7b302857549ee95d34c0593bd675a71fd/vllm/wor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Performance regression when use PyTorch regional compilation bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Performance regression occurs when use regional compilation...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --num-prompts 1000 \ --dtype bfloat16 \ --max-model-len 4096 \ --max-num-batched-tokens 8192 \ --max-num-seqs 128 \
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: se PyTorch regional compilation bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Performance regression occurs when use regional compilation after https://github.com/vllm-proje...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --seed 2024 \ --backend vllm \ --dataset /path_to_dataset/ShareGPT_V3_unfiltered_cleaned_split.json \ --num-prompts 1000 \ --dtype bfloat16

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#12536](https://github.com/vllm-project/vllm/pull/12536) | closes_keyword | 0.95 | [Kernel] Use self.kv_cache and forward_context.attn_metadata in Attention.forward | fix #12410 CC @youkaichao |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
