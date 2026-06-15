# vllm-project/vllm#36456: [Bug]: Local GGUF path fails with "architecture qwen35 is not supported yet" even when --hf-config-path is provided

| 字段 | 值 |
| --- | --- |
| Issue | [#36456](https://github.com/vllm-project/vllm/issues/36456) |
| 状态 | open |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Local GGUF path fails with "architecture qwen35 is not supported yet" even when --hf-config-path is provided

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving a local `.gguf` file using a volume-mounted path, vLLM crashes at startup with: ``` ValueError: GGUF model with architecture qwen35 is not supported yet. ``` This error originates from `transformers.modeling_gguf_pytorch_utils.load_gguf_checkpoint`, which is called from `maybe_override_with_speculators` in `vllm/transformers_utils/config.py:520`. **The critical issue:** `maybe_override_with_speculators` calls `PretrainedConfig.get_config_dict()` with the raw `.gguf` file path directly, bypassing `--hf-config-path` entirely. So even when `--hf-config-path /model` is explicitly provided (pointing to a local directory containing a valid `config.json`), this function never reads it — it always tries to parse the `.gguf` file via transformers' GGUF parser, which does not yet support the `qwen35` architecture. **This is inconsistent behavior:** the `repo:quant` HuggingFace format (e.g. `unsloth/Qwen3.5-9B-GGUF:Q8_0`) works correctly because it takes a different code path in `maybe_override_with_speculators` that does not invoke the transformers GGUF parser. Local file paths do not get this treatment. --- **To reproduce** `...

## 现有链接修复摘要

#39559 [Model] Add GGUF support for Qwen 3.5 dense and MoE models

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Local GGUF path fails with "architecture qwen35 is not supported yet" even when --hf-config-path is provided bug ### Your current environment ### 🐛 Describe the bug When serving a local `.gguf` file using a volum...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: hf-config-path` entirely. So even when `--hf-config-path /model` is explicitly provided (pointing to a local directory containing a valid `config.json`), this function never reads it — it always tries to parse the `.ggu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: the `qwen35` architecture. **This is inconsistent behavior:** the `repo:quant` HuggingFace format (e.g. `unsloth/Qwen3.5-9B-GGUF:Q8_0`) works correctly because it takes a different code path in `maybe_override_with_spec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Local GGUF path fails with "architecture qwen35 is not supported yet" even when --hf-config-path is provided bug ### Your current environment ### 🐛 Describe the bug When serving a local `.gguf` file using a volum...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: is inconsistent behavior:** the `repo:quant` HuggingFace format (e.g. `unsloth/Qwen3.5-9B-GGUF:Q8_0`) works correctly because it takes a different code path in `maybe_override_with_speculators` that does not invoke the...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39559](https://github.com/vllm-project/vllm/pull/39559) | closes_keyword | 0.95 | [Model] Add GGUF support for Qwen 3.5 dense and MoE models | Fixes: #39198, #36456, #38122 ## Test Plan ```bash # Qwen 3.5 Dense vllm serve unsloth/Qwen3.5-0.8B-GGUF:UD-IQ2_XXS --tokenizer Qwen/Qwen3.5-0.8B --hf-config-path Qwen/Qwen3. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
