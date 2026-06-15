# vllm-project/vllm#35321: [Feature]: Encoder self-attention for RocmAttentionImpl

| 字段 | 值 |
| --- | --- |
| Issue | [#35321](https://github.com/vllm-project/vllm/issues/35321) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Encoder self-attention for RocmAttentionImpl

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Encoder self-attention is not implemented for ROCM_ATTN. For example, when running the following test with ROCM_ATTN enabled instead of TRITON_ATTN: `pytest -v -s entrypoints/openai/test_run_batch.py::test_empty_file` this error is raised: `NotImplementedError: Encoder self-attention is not implemented for RocmAttentionImpl` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Feature]: Encoder self-attention for RocmAttentionImpl feature request;rocm ### 🚀 The feature, motivation and pitch Encoder self-attention is not implemented for ROCM_ATTN. For example, when running the following test...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ample, when running the following test with ROCM_ATTN enabled instead of TRITON_ATTN: `pytest -v -s entrypoints/openai/test_run_batch.py::test_empty_file` this error is raised: `NotImplementedError: Encoder self-attenti...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Encoder self-attention for RocmAttentionImpl feature request;rocm ### 🚀 The feature, motivation and pitch Encoder self-attention is not implemented for ROCM_ATTN. For example, when running the following test...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: s not implemented for ROCM_ATTN. For example, when running the following test with ROCM_ATTN enabled instead of TRITON_ATTN: `pytest -v -s entrypoints/openai/test_run_batch.py::test_empty_file` this error is raised: `No...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
