# vllm-project/vllm#40318: [Bug]: Mistral3 text-only startup fails when text_config.architectures is None

| 字段 | 值 |
| --- | --- |
| Issue | [#40318](https://github.com/vllm-project/vllm/issues/40318) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral3 text-only startup fails when text_config.architectures is None

### Issue 正文摘录

### Your current environment - vLLM versions tested: - `0.19.1` - `0.19.2rc1.dev16+g898beca5a` (built from `main` on 2026-04-20) - Transformers: `5.5.4` - Torch: `2.10.0` - Python: `3.11` - CUDA backend on Linux GPU pod ### Models tested Upstream model family: - `mistralai/Ministral-3-8B-Base-2512` - `mistralai/Ministral-3-8B-Instruct-2512` The same failure also reproduces on a fine-tuned derivative of this model family, so this does not appear to be specific to a custom checkpoint. ### Describe the bug `vllm serve` fails to start a `Mistral3ForConditionalGeneration` model in text-only mode even with `--language-model-only`. The top-level model config resolves correctly as `Mistral3ForConditionalGeneration`, but the nested text backbone path still crashes because `text_config.architectures` is `None`. The failure occurs in `vllm/model_executor/models/mistral3.py` when it calls back into the generic model loader, which then executes: - `tuple(getattr(model_config.hf_config, "architectures", []))` and gets `None`, leading to: - `TypeError: 'NoneType' object is not iterable` This reproduces on the Ministral-3 model family itself and also on a fine-tuned derivative. ### Reproduction C...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Mistral3 text-only startup fails when text_config.architectures is None ### Your current environment - vLLM versions tested: - `0.19.1` - `0.19.2rc1.dev16+g898beca5a` (built from `main` on 2026-04-20) - Transform...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n text_config.architectures is None ### Your current environment - vLLM versions tested: - `0.19.1` - `0.19.2rc1.dev16+g898beca5a` (built from `main` on 2026-04-20) - Transformers: `5.5.4` - Torch: `2.10.0` - Python: `3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mistral3 text-only startup fails when text_config.architectures is None ### Your current environment - vLLM versions tested: - `0.19.1` - `0.19.2rc1.dev16+g898beca5a` (built from `main` on 2026-04-20) - Transform...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 04-20) - Transformers: `5.5.4` - Torch: `2.10.0` - Python: `3.11` - CUDA backend on Linux GPU pod ### Models tested Upstream model family: - `mistralai/Ministral-3-8B-Base-2512` - `mistralai/Ministral-3-8B-Instruct-2512...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: -2512` - `mistralai/Ministral-3-8B-Instruct-2512` The same failure also reproduces on a fine-tuned derivative of this model family, so this does not appear to be specific to a custom checkpoint. ### Describe the bug `vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
