# vllm-project/vllm#30584: [Bug]: GLM-4.6V-Flash + transformers v5: vLLM passes MediaWithBytes to HF image processor, causing 400 errors for multimodal requests

| 字段 | 值 |
| --- | --- |
| Issue | [#30584](https://github.com/vllm-project/vllm/issues/30584) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GLM-4.6V-Flash + transformers v5: vLLM passes MediaWithBytes to HF image processor, causing 400 errors for multimodal requests

### Issue 正文摘录

### Your current environment Environment vLLM: latest main branch (commit b4039c08b5dd0a14d5c1ccac8557aa11732d857c) transformers: v5.0.0rc1 Model: zai-org/GLM-4.6V-Flash Python: 3.12 System: DGX Spark (GB10) Blackwell; arm64 Serving mode: OpenAI-compatible /v1/chat/completions ### 🐛 Describe the bug **Summary** When serving GLM-4.6V / GLM-4.6V-Flash with vLLM (latest main) and transformers v5 (RC), all multimodal (image) requests fail with 400 Bad Request. Root cause: vLLM passes its internal MediaWithBytes wrapper directly into HuggingFace’s Glm46VProcessor, but the processor strictly rejects non-PIL / non-URL inputs, raising a TypeError. The exception is caught and surfaced as a generic 400, hiding the real cause. Text-only requests work as expected. **Error Observed** Client receives: 400 Bad Request BadRequestError: Failed to apply Glm46VProcessor on data=... Server logs do not include the underlying exception. **Root Cause (Confirmed)** Minimal reproducer outside vLLM: from transformers import AutoProcessor from vllm.multimodal.image import ImageMediaIO processor = AutoProcessor.from_pretrained("zai-org/GLM-4.6V-Flash") mm = ImageMediaIO() mw = mm.load_file("test.jpg") # Medi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: GLM-4.6V-Flash + transformers v5: vLLM passes MediaWithBytes to HF image processor, causing 400 errors for multimodal requests bug ### Your current environment Environment vLLM: latest main branch (commit b4039c0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Cause (Confirmed)** Minimal reproducer outside vLLM: from transformers import AutoProcessor from vllm.multimodal.image import ImageMediaIO processor = AutoProcessor.from_pretrained("zai-org/GLM-4.6V-Flash") mm = ImageMe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1 Model: zai-org/GLM-4.6V-Flash Python: 3.12 System: DGX Spark (GB10) Blackwell; arm64 Serving mode: OpenAI-compatible /v1/chat/completions ### 🐛 Describe the bug **Summary** When serving GLM-4.6V / GLM-4.6V-Flash with...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: MediaWithBytes to HF image processor, causing 400 errors for multimodal requests bug ### Your current environment Environment vLLM: latest main branch (commit b4039c08b5dd0a14d5c1ccac8557aa11732d857c) transformers: v5.0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ltimodal requests bug ### Your current environment Environment vLLM: latest main branch (commit b4039c08b5dd0a14d5c1ccac8557aa11732d857c) transformers: v5.0.0rc1 Model: zai-org/GLM-4.6V-Flash Python: 3.12 System: DGX Sp...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
