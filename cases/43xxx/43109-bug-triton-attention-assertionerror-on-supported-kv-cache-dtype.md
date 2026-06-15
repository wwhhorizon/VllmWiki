# vllm-project/vllm#43109: [Bug]: Triton Attention AssertionError on supported kv_cache_dtype

| 字段 | 值 |
| --- | --- |
| Issue | [#43109](https://github.com/vllm-project/vllm/issues/43109) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Triton Attention AssertionError on supported kv_cache_dtype

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to load the GPT2 model [`inferno-project/vllm-gpt2-1`](https://huggingface.co/inferno-project/vllm-gpt2-1) leads to the following assertion error when `kv_cache_dtype` is one of `float16`, `bfloat16`: ```text (EngineCore pid=8748) File "/home/jlj/dev/inferno-repro/.venv/lib/python3.13/site-packages/vllm/v1/attention/ops/triton_reshape_and_cache_flash.py", line 353, in triton_reshape_and_cache_flash (EngineCore pid=8748) assert kv_cache_dtype == "auto" or is_quantized_kv_cache(kv_cache_dtype), ( (EngineCore pid=8748) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore pid=8748) AssertionError: unsupported kv_cache_dtype (str), got float16. ``` Triton attention should support these dtypes and indeed this doesn't happen with the model [`openai-community/gpt2`](https://huggingface.co/openai-community/gpt2). ## Reproducer ```python3 from vllm import LLM from vllm.config import AttentionConfig from vllm.v1.attention.backends.registry import AttentionBackendEnum llm = LLM( "inferno-project/vllm-gpt2-1", kv_cache_dtype="float16", ) llm.generate("token_0") ``` ## Full traceback [traceback.log](https://gith...

## 现有链接修复摘要

#43138 [Bugfix] Allow float16/bfloat16 as kv_cache_dtype in Triton attention ops

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: gingface.co/openai-community/gpt2). ## Reproducer ```python3 from vllm import LLM from vllm.config import AttentionConfig from vllm.v1.attention.backends.registry import AttentionBackendEnum llm = LLM( "inferno-project/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Triton Attention AssertionError on supported kv_cache_dtype bug ### Your current environment ### 🐛 Describe the bug Trying to load the GPT2 model [`inferno-project/vllm-gpt2-1`](https://huggingface.co/inferno-pro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: current environment ### 🐛 Describe the bug Trying to load the GPT2 model [`inferno-project/vllm-gpt2-1`](https://huggingface.co/inferno-project/vllm-gpt2-1) leads to the following assertion error when `kv_cache_dtype` i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Triton Attention AssertionError on supported kv_cache_dtype bug ### Your current environment ### 🐛 Describe the bug Trying to load the GPT2 model [`inferno-project/vllm-gpt2-1`](https://huggingface.co/inferno-pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: (EngineCore pid=8748) ERROR 05-19 16:24:47 [v1/engine/core.py:1140] cudagraph_memory_estimate = self.model_runner.profile_cudagraph_memory() (EngineCore pid=8748) ERROR 05-19 16:24:47 [v1/engine/core.py:1140] File "/hom...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43138](https://github.com/vllm-project/vllm/pull/43138) | closes_keyword | 0.95 | [Bugfix] Allow float16/bfloat16 as kv_cache_dtype in Triton attention ops | Fixes #43109 ## Why this is not a duplicate No other open PR addresses issue #43109. Verified with: ``` gh pr list --repo vllm-project/vllm --state open --search "43109 in:body" |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
