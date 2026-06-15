# vllm-project/vllm#28085: [Feature][UX]: vLLM Kernel Configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#28085](https://github.com/vllm-project/vllm/issues/28085) |
| 状态 | closed |
| 标签 | feature request;stale;startup-ux |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][UX]: vLLM Kernel Configuration

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It would be nice if we could pretty print which kernels will be run for each layer of the model. Im thinking something human readable like: ```bash vLLM configured with: - QKV_PROJ: `cutlass_fp8` - O_PROJ: `cutlass_fp8` - MoE: `triton_moe` ``` Right now we have some ad-hoc logging, but no summary view. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: mething human readable like: ```bash vLLM configured with: - QKV_PROJ: `cutlass_fp8` - O_PROJ: `cutlass_fp8` - MoE: `triton_moe` ``` Right now we have some ad-hoc logging, but no summary view. ### Alternatives _No respo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature][UX]: vLLM Kernel Configuration feature request;stale;startup-ux ### 🚀 The feature, motivation and pitch It would be nice if we could pretty print which kernels will be run for each layer of the model. Im think...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][UX]: vLLM Kernel Configuration feature request;stale;startup-ux ### 🚀 The feature, motivation and pitch It would be nice if we could pretty print which kernels will be run for each layer of the model. Im think...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: human readable like: ```bash vLLM configured with: - QKV_PROJ: `cutlass_fp8` - O_PROJ: `cutlass_fp8` - MoE: `triton_moe` ``` Right now we have some ad-hoc logging, but no summary view. ### Alternatives _No response_ ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
