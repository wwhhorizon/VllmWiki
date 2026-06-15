# vllm-project/vllm#38634: [Bug]: MLA + FP8 KV cache + CUDA Graph causes random NaN in decode phase

| 字段 | 值 |
| --- | --- |
| Issue | [#38634](https://github.com/vllm-project/vllm/issues/38634) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8 |
| 症状 | nan_inf |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MLA + FP8 KV cache + CUDA Graph causes random NaN in decode phase

### Issue 正文摘录

### Your current environment vLLM：0.12.0 Model： MLA Model like deepseek GPU：H200 ✅ enforce_eager=True + FP8 kv cache → Right ✅ enforce_eager=False + BF16 → Right ❌ enforce_eager=False + FP8 → q 、kv_c_normed、k_pe has Nan (in MLAAttention forward) ### 🐛 Describe the bug ✅ enforce_eager=True + FP8 kv cache → Right ✅ enforce_eager=False + BF16 → Right ❌ enforce_eager=False + FP8 → q 、kv_c_normed、k_pe has Nan (in MLAAttention forward) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: MLA + FP8 KV cache + CUDA Graph causes random NaN in decode phase bug ### Your current environment vLLM：0.12.0 Model： MLA Model like deepseek GPU：H200 ✅ enforce_eager=True + FP8 kv cache → Right ✅ enforce_eager=F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: MLA + FP8 KV cache + CUDA Graph causes random NaN in decode phase bug ### Your current environment vLLM：0.12.0 Model： MLA Model like deepseek GPU：H200 ✅ enforce_eager=True + FP8 kv cache → Right ✅ enforce_eager=F...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: MLA + FP8 KV cache + CUDA Graph causes random NaN in decode phase bug ### Your current environment vLLM：0.12.0 Model： MLA Model like deepseek GPU：H200 ✅ enforce_eager=True + FP8 kv cache → Right ✅ enforce_eager=F...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: GPU：H200 ✅ enforce_eager=True + FP8 kv cache → Right ✅ enforce_eager=False + BF16 → Right ❌ enforce_eager=False + FP8 → q 、kv_c_normed、k_pe has Nan (in MLAAttention forward) ### 🐛 Describe the bug ✅ enforce_eager=True +...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: random NaN in decode phase bug ### Your current environment vLLM：0.12.0 Model： MLA Model like deepseek GPU：H200 ✅ enforce_eager=True + FP8 kv cache → Right ✅ enforce_eager=False + BF16 → Right ❌ enforce_eager=False + FP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
