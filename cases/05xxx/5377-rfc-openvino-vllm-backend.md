# vllm-project/vllm#5377: [RFC]: OpenVINO vLLM backend

| 字段 | 值 |
| --- | --- |
| Issue | [#5377](https://github.com/vllm-project/vllm/issues/5377) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: OpenVINO vLLM backend

### Issue 正文摘录

### Motivation. OpenVINO is open source solution for inference deep learning models, including LLMs. OpenVINO supports both Intel and ARM CPUs, Intel integrated and discrete GPUs, NPU and has a good reputation as production ready solution for client and server scenarios. The idea is to create OpenVINO backend for vLLM which will initially support x86 CPU as primary device, later other devices can be enabled. Because of Intel Optimum HuggingFace extension https://github.com/huggingface/optimum-intel, OpenVINO vLLM backend can support wide range of models, including https://docs.vllm.ai/en/stable/models/supported_models.html OpenVINO provides better performance compared to current vLLM CPU implementation, which will be shown in integration PR. Also, OpenVINO implementation of Paged Attention operation supports modern vLLM features like chunked prefill and prefix caching. ### Proposed Change. Introduce OpenVINO vLLM backend, which: - Loads model via optimum-intel extension for HuggingFace https://github.com/huggingface/optimum-intel - (Optional step) Compresses model weights to low-bit format - Automatically converts PyTorch model to OpenVINO IR representation, which contains PagedAt...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: otivation. OpenVINO is open source solution for inference deep learning models, including LLMs. OpenVINO supports both Intel and ARM CPUs, Intel integrated and discrete GPUs, NPU and has a good reputation as production...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: of Paged Attention operation supports modern vLLM features like chunked prefill and prefix caching. ### Proposed Change. Introduce OpenVINO vLLM backend, which: - Loads model via optimum-intel extension for HuggingFace...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [RFC]: OpenVINO vLLM backend RFC ### Motivation. OpenVINO is open source solution for inference deep learning models, including LLMs. OpenVINO supports both Intel and ARM CPUs, Intel integrated and discrete GPUs, NPU an...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
