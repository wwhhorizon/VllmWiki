# vllm-project/vllm#32959: [Bug]: KeyError: `merging_layer.weight` when loading Mistral/vision-enabled checkpoints after PR #32780 refactor

| 字段 | 值 |
| --- | --- |
| Issue | [#32959](https://github.com/vllm-project/vllm/issues/32959) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KeyError: `merging_layer.weight` when loading Mistral/vision-enabled checkpoints after PR #32780 refactor

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Summary After the refactor in PR #32780, loading certain Mistral or multimodal checkpoints fails during `load_weights` with a `KeyError: 'merging_layer.weight'` (or similar `multi_modal_projector.patch_merger.*` keys). The failure occurs while `model.load_weights(...)` tries to look up a parameter name that isn't present in the post-refactor mapping/patch merger dictionary. The stack trace shows the loader raising a `KeyError` inside `pixtral.py/mistral.py` mapping logic. ### Reproduction ```bash vllm serve mistralai/Devstral-Small-2-24B-Instruct-2512 \ --tokenizer-mode mistral \ --config-format mistral \ --load-format mistral \ --dtype half \ --quantization fp8 \ --kv-cache-dtype fp8 \ --enable-auto-tool-choice \ --tool-call-parser mistral \ --gpu-memory-utilization 0.7 \ --max-num-seqs 8 \ --cpu-offload-gb 0 \ --swap-space 0 \ --host 0.0.0.0 ``` 1. Use the current code that includes PR #32780 (eg. the main branch containing the change). 2. Attempt to load a Mistral family model that includes multimodal projector / patch_merger weights (e.g. `devstral-small-2` model with vision or other checkpoints that have `multi_modal_pro...

## 现有链接修复摘要

#33406 [BUGFIX] Pixtral cannot be loaded with --limit-mm-per-prompt 0

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: ### Summary After the refactor in PR #32780, loading certain Mistral or multimodal checkpoints fails during `load_weights` with a `KeyError: 'merging_layer.weight'` (or similar `multi_modal_projector.patch_merger.*` key...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: h `KeyError`). ### Suspected root cause PR #32780 refactors Mistral-specific mapping code out of `llama.py` into `mistral.py`. During that refactor the mapping logic for patch merger / multimodal projector parameter nam...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: mode mistral \ --config-format mistral \ --load-format mistral \ --dtype half \ --quantization fp8 \ --kv-cache-dtype fp8 \ --enable-auto-tool-choice \ --tool-call-parser mistral \ --gpu-memory-utilization 0.7 \ --max-n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: mapping logic. ### Reproduction ```bash vllm serve mistralai/Devstral-Small-2-24B-Instruct-2512 \ --tokenizer-mode mistral \ --config-format mistral \ --load-format mistral \ --dtype half \ --quantization fp8 \ --kv-cac...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: \ --load-format mistral \ --dtype half \ --quantization fp8 \ --kv-cache-dtype fp8 \ --enable-auto-tool-choice \ --tool-call-parser mistral \ --gpu-memory-utilization 0.7 \ --max-num-seqs 8 \ --cpu-offload-gb 0 \ --swap...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33406](https://github.com/vllm-project/vllm/pull/33406) | closes_keyword | 0.95 | [BUGFIX] Pixtral cannot be loaded with --limit-mm-per-prompt 0 | Fix #32959 in place of https://github.com/vllm-project/vllm/pull/33006 or https://github.com/vllm-project/vllm/pull/33008. Thanks @dbary for informing me that the error was still |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
