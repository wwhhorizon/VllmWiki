# vllm-project/vllm#37173: [Bug]: AssertionError in cutlass_scaled_mm during profile_run for FP8 pooling/reranker models

| 字段 | 值 |
| --- | --- |
| Issue | [#37173](https://github.com/vllm-project/vllm/issues/37173) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertionError in cutlass_scaled_mm during profile_run for FP8 pooling/reranker models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I quantized fp8 qwen3 embedding and reranker, embedding works fine, but when trying to load reranker I get errors. AI analyzing the logs gave me this: Model: Qwen3ForSequenceClassification with FP8 quantization (block-scale w8a8) Runner: --runner pooling What happens: During startup, the V1 engine calls profile_run() to measure available GPU memory. This creates dummy hidden states and runs them through the full model including the pooler. The dummy tensor is created as torch.float32, but the model's actual dtype is torch.bfloat16. The root cause is clear from the traceback — the CUTLASS FP8 kernel asserts that out_dtype must be bfloat16 or float16, but the classifier head in the reranker's pooler is producing float32. This is a bug in vLLM 0.17.1 with Qwen3ForSequenceClassification + FP8 + tensor parallelism during the profile/memory-probe run. [logfile.txt](https://github.com/user-attachments/files/26019962/logfile.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/)...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: AssertionError in cutlass_scaled_mm during profile_run for FP8 pooling/reranker models bug ### Your current environment ### 🐛 Describe the bug I quantized fp8 qwen3 embedding and reranker, embedding works fine, b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t16 or float16, but the classifier head in the reranker's pooler is producing float32. This is a bug in vLLM 0.17.1 with Qwen3ForSequenceClassification + FP8 + tensor parallelism during the profile/memory-probe run. [lo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vLLM 0.17.1 with Qwen3ForSequenceClassification + FP8 + tensor parallelism during the profile/memory-probe run. [logfile.txt](https://github.com/user-attachments/files/26019962/logfile.txt) ### Before submitting a new i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: AssertionError in cutlass_scaled_mm during profile_run for FP8 pooling/reranker models bug ### Your current environment ### 🐛 Describe the bug I quantized fp8 qwen3 embedding and reranker, embedding works fine, b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e me this: Model: Qwen3ForSequenceClassification with FP8 quantization (block-scale w8a8) Runner: --runner pooling What happens: During startup, the V1 engine calls profile_run() to measure available GPU memory. This cr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
