# vllm-project/vllm#37554: [Bug] --calculate-kv-scales produces corrupted FP8 KV cache on hybrid GDN+Attention models (Qwen3.5)

| 字段 | 值 |
| --- | --- |
| Issue | [#37554](https://github.com/vllm-project/vllm/issues/37554) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] --calculate-kv-scales produces corrupted FP8 KV cache on hybrid GDN+Attention models (Qwen3.5)

### Issue 正文摘录

### My current environment - vLLM version: v0.17.1 (also confirmed on v0.16.1rc1 and nightly v0.17.1rc1.dev88) - GPU: NVIDIA RTX PRO 6000 Blackwell (SM120, 96 GB VRAM) - Model: Qwen3.5-35B-A3B (FP8 block-quantized via llm-compressor, `Qwen3_5MoeForConditionalGeneration`) ### Bug description `--calculate-kv-scales` causes catastrophic output corruption when used with FP8 KV cache on hybrid GDN+Attention models. The corruption is silent — no errors or warnings — and manifests as hallucinated inputs, topic fixation loops, and gibberish on even the simplest queries. **Root cause:** `calc_kv_scales()` in `vllm/model_executor/layers/attention/attention.py` computes per-layer FP8 quantization scales from a single dummy forward pass during model profiling. In hybrid GDN+Attention models like Qwen3.5, the GDN (Gated Delta Network) layers have uninitialized recurrent state during this dummy pass. Their outputs are garbage, which feeds into downstream attention layers, producing wildly incorrect per-layer scales. These bad scales are then frozen and used for all subsequent inference, causing catastrophic FP8 quantization errors. **Fix:** Removing `--calculate-kv-scales` (scales default to 1....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug] --calculate-kv-scales produces corrupted FP8 KV cache on hybrid GDN+Attention models (Qwen3.5) ### My current environment - vLLM version: v0.17.1 (also confirmed on v0.16.1rc1 and nightly v0.17.1rc1.dev88) - GPU:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: also confirmed on v0.16.1rc1 and nightly v0.17.1rc1.dev88) - GPU: NVIDIA RTX PRO 6000 Blackwell (SM120, 96 GB VRAM) - Model: Qwen3.5-35B-A3B (FP8 block-quantized via llm-compressor, `Qwen3_5MoeForConditionalGeneration`)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: culate-kv-scales produces corrupted FP8 KV cache on hybrid GDN+Attention models (Qwen3.5) ### My current environment - vLLM version: v0.17.1 (also confirmed on v0.16.1rc1 and nightly v0.17.1rc1.dev88) - GPU: NVIDIA RTX...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: hybrid GDN+Attention models (Qwen3.5) ### My current environment - vLLM version: v0.17.1 (also confirmed on v0.16.1rc1 and nightly v0.17.1rc1.dev88) - GPU: NVIDIA RTX PRO 6000 Blackwell (SM120, 96 GB VRAM) - Model: Qwen...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: RTX PRO 6000 Blackwell (SM120, 96 GB VRAM) - Model: Qwen3.5-35B-A3B (FP8 block-quantized via llm-compressor, `Qwen3_5MoeForConditionalGeneration`) ### Bug description `--calculate-kv-scales` causes catastrophic output c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
