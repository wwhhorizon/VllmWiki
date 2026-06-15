# vllm-project/vllm#37435: Speculative/MTP draft config appears to drop target --hf-overrides (breaks long-context YaRN/RoPE extension)

| 字段 | 值 |
| --- | --- |
| Issue | [#37435](https://github.com/vllm-project/vllm/issues/37435) |
| 状态 | open |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | quantization |
| 症状 | mismatch |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Speculative/MTP draft config appears to drop target --hf-overrides (breaks long-context YaRN/RoPE extension)

### Issue 正文摘录

### Your current environment - vLLM version: `main`-ish / dev container image `voipmonitor/vllm:dev-cu130` - Serving stack: 4x Blackwell on a single node - Model: `lukealonso/Qwen3.5-397B-A17B-NVFP4` - Speculative decoding: native MTP (`--speculative-config '{"method":"mtp","num_speculative_tokens":2}'`) - Context: `524288` - RoPE/YaRN extension: applied via `--hf-overrides` ### Describe the bug I believe speculative/MTP draft config is not inheriting target-model `--hf-overrides`, which can break long-context speculation when RoPE/YaRN scaling is injected at runtime rather than baked into the checkpoint config. In my setup, MTP works very well at shorter / ordinary contexts, but when requests get into very large prompts (for example large OpenClaw prompts well beyond the model's original context), the draft acceptance rate can collapse to ~0% while the target model still appears usable. That pattern looks like a draft/target positional-config mismatch: - target model sees `--hf-overrides` with YaRN factor 2 - draft/MTP side appears to rebuild its own `ModelConfig` - draft side does not appear to receive the same `hf_overrides` - beyond original context size, draft starts proposin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Speculative/MTP draft config appears to drop target --hf-overrides (breaks long-context YaRN/RoPE extension) ### Your current environment - vLLM version: `main`-ish / dev container image `voipmonitor/vllm:dev-cu130` - S...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s long-context YaRN/RoPE extension) ### Your current environment - vLLM version: `main`-ish / dev container image `voipmonitor/vllm:dev-cu130` - Serving stack: 4x Blackwell on a single node - Model: `lukealonso/Qwen3.5-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ck: 4x Blackwell on a single node - Model: `lukealonso/Qwen3.5-397B-A17B-NVFP4` - Speculative decoding: native MTP (`--speculative-config '{"method":"mtp","num_speculative_tokens":2}'`) - Context: `524288` - RoPE/YaRN e...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Speculative/MTP draft config appears to drop target --hf-overrides (breaks long-context YaRN/RoPE extension) ### Your current environment - vLLM version: `main`-ish / dev container image `voipmonitor/vllm:dev-cu130` - S
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ppears usable. That pattern looks like a draft/target positional-config mismatch: - target model sees `--hf-overrides` with YaRN factor 2 - draft/MTP side appears to rebuild its own `ModelConfig` - draft side does not a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
