# vllm-project/vllm#18198: [Bug]: vllm crashes after when using quantized model on CPU with error "torch not compiled with CUDA enabled"

| 字段 | 值 |
| --- | --- |
| Issue | [#18198](https://github.com/vllm-project/vllm/issues/18198) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm crashes after when using quantized model on CPU with error "torch not compiled with CUDA enabled"

### Issue 正文摘录

### CPU (SPR instance) ### 🐛 Describe the bug Vllm crashes on version version 0.8.5.post1 when running on CPU quantized model. This issue was not observed in version 0.8.4 "--device", "cpu", "--pipeline-parallel-size", "$(VLLM_PP_SIZE)", "--dtype", "$(VLLM_DTYPE)", "--max_model_len", "$(VLLM_MAX_MODEL_LEN)", "--max-num-seqs", "$(VLLM_MAX_NUM_SEQS)", "--disable-log-requests", "--download-dir", "/data", "--speculative_config", '{"model": "ibm-ai-platform/llama3-8b-accelerator", "num_speculative_tokens": 4}', "--quantization", "awq"] ![Image](https://github.com/user-attachments/assets/3c45ed6d-5387-41ee-bfb4-881b1cb3a740) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lm crashes after when using quantized model on CPU with error "torch not compiled with CUDA enabled" bug;stale ### CPU (SPR instance) ### 🐛 Describe the bug Vllm crashes on version version 0.8.5.post1 when running on CP...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm crashes after when using quantized model on CPU with error "torch not compiled with CUDA enabled" bug;stale ### CPU (SPR instance) ### 🐛 Describe the bug Vllm crashes on version version 0.8.5.post1 when runn...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tized model on CPU with error "torch not compiled with CUDA enabled" bug;stale ### CPU (SPR instance) ### 🐛 Describe the bug Vllm crashes on version version 0.8.5.post1 when running on CPU quantized model. This issue wa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: vllm crashes after when using quantized model on CPU with error "torch not compiled with CUDA enabled" bug;stale ### CPU (SPR instance) ### 🐛 Describe the bug Vllm crashes on version version 0.8.5.post1 when runn...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er when using quantized model on CPU with error "torch not compiled with CUDA enabled" bug;stale ### CPU (SPR instance) ### 🐛 Describe the bug Vllm crashes on version version 0.8.5.post1 when running on CPU quantized mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
