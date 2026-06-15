# vllm-project/vllm#25484: [Feature][WideEP]: More "masked-m" GEMM and quant kernels for use with DeepEP LowLatency + PPLX All2Alls

| 字段 | 值 |
| --- | --- |
| Issue | [#25484](https://github.com/vllm-project/vllm/issues/25484) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;frontend_api;gemm_linear;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | activation;cuda;fp8;gemm;kernel;moe;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][WideEP]: More "masked-m" GEMM and quant kernels for use with DeepEP LowLatency + PPLX All2Alls

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The `dispatch` operation in DeepEP LowLatency and PPLX-kernels is a `hidden_states` tensor with shape `[num_local_experts, max_num_tokens_per_expert, hidden_size]`. `max_num_tokens_per_expert` may be much larger than the actual number of tokens for each expert. To avoid useless work, we need efficient "masked-m" kernels that only work on the relevant parts of the tensors. Currently we use DeepGEMM and a fused-silu-mul-quant kernel for blocked fp8 formats. We'd need to expand on this to support more architectures + quantization formats. ### Alternatives Alternatively, we could use the DeepEP high throughput kernels, which have a different format that don't have masking and could work with grouped GEMM kernels instead. DeepEP HT doesn't support CUDA Graphs, so we'd need to figure out how to support CUDA Graphs in this format. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Feature][WideEP]: More "masked-m" GEMM and quant kernels for use with DeepEP LowLatency + PPLX All2Alls feature request;stale ### 🚀 The feature, motivation and pitch The `dispatch` operation in DeepEP LowLatency and PP...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Feature][WideEP]: More "masked-m" GEMM and quant kernels for use with DeepEP LowLatency + PPLX All2Alls feature request;stale ### 🚀 The feature, motivation and pitch The `dispatch` operation in DeepEP LowLatency and PP...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ][WideEP]: More "masked-m" GEMM and quant kernels for use with DeepEP LowLatency + PPLX All2Alls feature request;stale ### 🚀 The feature, motivation and pitch The `dispatch` operation in DeepEP LowLatency and PPLX-kerne...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nel for blocked fp8 formats. We'd need to expand on this to support more architectures + quantization formats. ### Alternatives Alternatively, we could use the DeepEP high throughput kernels, which have a different form...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: and quant kernels for use with DeepEP LowLatency + PPLX All2Alls feature request;stale ### 🚀 The feature, motivation and pitch The `dispatch` operation in DeepEP LowLatency and PPLX-kernels is a `hidden_states` tensor w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
