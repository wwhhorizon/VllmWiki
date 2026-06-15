# vllm-project/vllm#28538: [RFC]: 4-bit KV cache quantization through Hadamard transforms

| 字段 | 值 |
| --- | --- |
| Issue | [#28538](https://github.com/vllm-project/vllm/issues/28538) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;quantization |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: 4-bit KV cache quantization through Hadamard transforms

### Issue 正文摘录

### Motivation. Quantization has seen a lot of focus on rotations and Hadamard transforms in the past 2 years. This translated in a noticeable amount of interest and PRs in vLLM: - https://github.com/vllm-project/vllm/pull/15162 (March) - https://github.com/vllm-project/vllm/pull/16443 (April) - https://github.com/vllm-project/vllm/pull/22486 (August) - https://github.com/vllm-project/vllm/pull/24106 (September) - https://github.com/vllm-project/vllm/pull/24440 (October) Given the heightened focus on long-context: - Seed-OSS supporting 512k context (128GiB in FP16) - GLM4.6 upgrading to 202K context from 128K - Qwen3-coder-30B-A3B-Instruct and Qwen3-Coder-480B-A35B-Instruct supporting 256K context, up to 1M with YaRN - Qwen3 supporting 256K context - Minimax-M2 supporting 196K context - ... storing all of that in GPUs requires a significant amount of VRAM. I suggest we start exploring int4, mxfp4 and nvfp4 quantization for the KV-cache to significantly reduce KV-cache footprint while serving. I think there is enough evidence in theoretical research and maturity in backend libraries to tackle this growing need. For example a dequantization step would introduce extra latency but Qut...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: [RFC]: 4-bit KV cache quantization through Hadamard transforms RFC;stale ### Motivation. Quantization has seen a lot of focus on rotations and Hadamard transforms in the past 2 years. This translated in a noticeable amo...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: omparable to FP8 on very strong language models. This approach preserves numerically sensitive layers in higher precision, utilizes two-dimensional (2D) block scaling to maintain same quantized representations across fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: context (128GiB in FP16) - GLM4.6 upgrading to 202K context from 128K - Qwen3-coder-30B-A3B-Instruct and Qwen3-Coder-480B-A35B-Instruct supporting 256K context, up to 1M with YaRN - Qwen3 supporting 256K context - Minim...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: P4 format, we introduce a 4-bit training methodology that achieves accuracies comparable to FP8 on very strong language models. This approach preserves numerically sensitive layers in higher precision, utilizes two-dime...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: est and PRs in vLLM: - https://github.com/vllm-project/vllm/pull/15162 (March) - https://github.com/vllm-project/vllm/pull/16443 (April) - https://github.com/vllm-project/vllm/pull/22486 (August) - https://github.com/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
