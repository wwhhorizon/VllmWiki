# vllm-project/vllm#39137: [Bug]: fp8_e5m2 kv-cache gate in _init_kv_cache_quant fires on any quantized checkpoint, not only fp8 checkpoints

| 字段 | 值 |
| --- | --- |
| Issue | [#39137](https://github.com/vllm-project/vllm/issues/39137) |
| 状态 | open |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8;gemm;kernel;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: fp8_e5m2 kv-cache gate in _init_kv_cache_quant fires on any quantized checkpoint, not only fp8 checkpoints

### Issue 正文摘录

Filing this as a separate issue per suggestion in #39133 so it doesn't get lost in the Gemma 4 KV thread. In `vllm/model_executor/layers/attention/attention.py`, `_init_kv_cache_quant` raises `ValueError("fp8_e5m2 kv-cache is not supported with fp8 checkpoints.")` when the checkpoint being loaded is not in fact an fp8 checkpoint. The gate that leads to the raise is `should_load_quant_weights(quant_method)`, which returns True for any quantization method other than `UnquantizedLinearMethod` — so an INT4 `compressed-tensors` checkpoint trips the raise even though there is nothing fp8 about it. ### Reproduction vLLM version on the running container: `0.1.dev1+gd56e95223` (custom build; same code path is present on `main`). Model: [`cyankiwi/gemma-4-31B-it-AWQ-4bit`](https://huggingface.co/cyankiwi/gemma-4-31B-it-AWQ-4bit). Its `quantization_config` from `config.json`: ```json "quantization_config": { "quant_method": "compressed-tensors", "format": "pack-quantized", "config_groups": { "group_0": { "weights": { "num_bits": 4, "group_size": 32, "observer": "mse", "strategy": "group", "symmetric": true, "type": "int" } } } } ``` Launched with: ``` vllm serve /models/cyankiwi/gemma-4-31B-...

## 现有链接修复摘要

#39195 [Bugfix] Narrow fp8_e5m2 kv-cache gate to only reject actual fp8 checkpoints

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: fp8_e5m2 kv-cache gate in _init_kv_cache_quant fires on any quantized checkpoint, not only fp8 checkpoints Filing this as a separate issue per suggestion in #39133 so it doesn't get lost in the Gemma 4 KV thread....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: a separate issue per suggestion in #39133 so it doesn't get lost in the Gemma 4 KV thread. In `vllm/model_executor/layers/attention/attention.py`, `_init_kv_cache_quant` raises `ValueError("fp8_e5m2 kv-cache is not supp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: raise even though there is nothing fp8 about it. ### Reproduction vLLM version on the running container: `0.1.dev1+gd56e95223` (custom build; same code path is present on `main`). Model: [`cyankiwi/gemma-4-31B-it-AWQ-4b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ompt '{"image": 0, "audio": 0}' \ --async-scheduling ``` Hardware: 2× RTX 3090 (SM 8.6). The choice of `fp8_e5m2` is deliberate — on SM 8.6, Triton only supports `fp8e4b15` and `fp8e5` fp8 dtypes, so `fp8_e5m2` is the o...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: fp8_e5m2 kv-cache gate in _init_kv_cache_quant fires on any quantized checkpoint, not only fp8 checkpoints Filing this as a separate issue per suggestion in #39133 so it doesn't get lost in the Gemma 4 KV thread....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39195](https://github.com/vllm-project/vllm/pull/39195) | closes_keyword | 0.95 | [Bugfix] Narrow fp8_e5m2 kv-cache gate to only reject actual fp8 checkpoints | Fixes #39137 The `fp8_e5m2` kv-cache dtype check in `_init_kv_cache_quant` incorrectly rejects **all** quantized checkpoints when combined with `--kv-cache-dtype fp8_e5m2`, even t |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
