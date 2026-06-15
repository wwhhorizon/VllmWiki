# vllm-project/vllm#37387: [Bug]: [SM_120 / Blackwell] AWQ working with awq_marlin + TRITON_ATTN — field report

| 字段 | 值 |
| --- | --- |
| Issue | [#37387](https://github.com/vllm-project/vllm/issues/37387) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | attention;quantization |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [SM_120 / Blackwell] AWQ working with awq_marlin + TRITON_ATTN — field report

### Issue 正文摘录

### Your current environment Posting as a field report since I couldn't find existing documentation for this combination. **Setup:** - GPU: NVIDIA GeForce RTX 5060 Ti (compute capability 12.0 / SM_120) - OS: Windows 11 + WSL2 - PyTorch: 2.10.0+cu130 - vLLM: 0.17.2rc1.dev45+g761e0aa7a **Root cause:** SM_120 is forced to bfloat16. Standard `--quantization awq` requires float16 → immediate crash with pydantic ValidationError. **Working fix:** ```bash --quantization awq_marlin --attention-backend TRITON_ATTN ``` **Confirmed working — three architectures:** - hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4 (8B) — 338ms - casperhansen/mistral-nemo-instruct-2407-awq (12B) — 437ms - Qwen/Qwen2.5-14B-Instruct-AWQ (14B) — 520ms Confirmed NOT working on SM_120: standard awq, gptq, bitsandbytes, FlashAttention. Hope this is useful for SM_120 support going forward. ### 🐛 Describe the bug As above. not a bug a fix: [SM_120 / Blackwell] AWQ working with awq_marlin + TRITON_ATTN — field report ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: - vLLM: 0.17.2rc1.dev45+g761e0aa7a **Root cause:** SM_120 is forced to bfloat16. Standard `--quantization awq` requires float16 → immediate crash with pydantic ValidationError. **Working fix:** ```bash --quantization aw...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: [SM_120 / Blackwell] AWQ working with awq_marlin + TRITON_ATTN — field report bug ### Your current environment Posting as a field report since I couldn't find existing documentation for this combination. **Setup:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: [SM_120 / Blackwell] AWQ working with awq_marlin + TRITON_ATTN — field report bug ### Your current environment Posting as a field report since I couldn't find existing documentation for this combination. **Setup:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ``` **Confirmed working — three architectures:** - hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4 (8B) — 338ms - casperhansen/mistral-nemo-instruct-2407-awq (12B) — 437ms - Qwen/Qwen2.5-14B-Instruct-AWQ (14B) — 520m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;hardware_porting;quantization attention;quantization c...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
