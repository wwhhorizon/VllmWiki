# vllm-project/vllm#40388: [Bug]:  Gemma 4 fails to initialize with per-token-head KV cache quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#40388](https://github.com/vllm-project/vllm/issues/40388) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cache;cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Gemma 4 fails to initialize with per-token-head KV cache quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Gemma 4 fails to initialize in vLLM V1 when `--kv_cache_dtype int8_per_token_head` is enabled. The same issue also affects `fp8_per_token_head`. The failure is caused by Gemma 4's hybrid attention layout using two different KV head dimensions: - sliding/local layers use `head_dim = 256` - global/full-attention layers use `head_dim = 512` With per-token-head KV quantization, each KV head also stores scale metadata per token. That extra scale payload breaks the exact 2:1 page-size ratio between the 512-dim and 256-dim layers, so V1 KV page-size unification fails during initialization. Minimal reproduction: ```bash vllm serve \ --kv_cache_dtype int8_per_token_head ``` Observed result: ```text (Worker_TP1 pid=248) ERROR 04-19 14:16:08 [multiproc_executor.py:971] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/core/kv_cache_utils.py", line 942, in unify_kv_cache_spec_page_size (Worker_TP1 pid=248) ERROR 04-19 14:16:08 [multiproc_executor.py:971] raise NotImplementedError( (Worker_TP1 pid=248) ERROR 04-19 14:16:08 [multiproc_executor.py:971] NotImplementedError: The page size of the layer is not divisible by the maximum page size...

## 现有链接修复摘要

#40391 Fix Gemma4 KV cache page-size alignment for per-token-head quantization

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: fp8_per_token_head`. The failure is caused by Gemma 4's hybrid attention layout using two different KV head dimensions: - sliding/local layers use `head_dim = 256` - global/full-attention layers use `head_dim = 512` Wit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: visible by `520`, so the current page-size unification logic cannot reconcile the two layer types by changing `block_size` alone. Relevant code paths: - `vllm/model_executor/models/gemma4.py` - `vllm/model_executor/laye...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Gemma 4 fails to initialize with per-token-head KV cache quantization bug ### Your current environment ### 🐛 Describe the bug Gemma 4 fails to initialize in vLLM V1 when `--kv_cache_dtype int8_per_token_head` is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 26efe177bf22874743d11dfdfef9247dbfb5ff0) | | **GPU** | 2× NVIDIA GeForce RTX 2080 Ti (22 GB, CC 7.5, Turing) | | **CUDA Driver** | 580.126.18, CUDA 13.0 | | **Python** | 3.12 (Docker) | | **Model** | Gemma4-31B AWQ 4-bi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Gemma 4 fails to initialize with per-token-head KV cache quantization bug ### Your current environment ### 🐛 Describe the bug Gemma 4 fails to initialize in vLLM V1 when `--kv_cache_dtype int8_per_token_head` is...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40391](https://github.com/vllm-project/vllm/pull/40391) | closes_keyword | 0.95 | Fix Gemma4 KV cache page-size alignment for per-token-head quantization | Fixes issue #40388. ### Test Plan Runtime reproduction for issue validation on Gemma4 environment: ``` bash vllm serve <gemma4-model> --kv_cache_dtype int8_per_token_head `` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
