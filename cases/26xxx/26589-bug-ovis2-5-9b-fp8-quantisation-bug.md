# vllm-project/vllm#26589: [Bug]: Ovis2.5 9B FP8 quantisation bug

| 字段 | 值 |
| --- | --- |
| Issue | [#26589](https://github.com/vllm-project/vllm/issues/26589) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Ovis2.5 9B FP8 quantisation bug

### Issue 正文摘录

### 🐛 Describe the bug I have quantised Ovis2.5 9B model using ms-swift and the quantisation method was fp8. Getting this error while serving that model in vLLM. **RuntimeError: size_n = 4304 is not divisible by tile_n_size = 64** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Ovis2.5 9B FP8 quantisation bug bug;stale ### 🐛 Describe the bug I have quantised Ovis2.5 9B model using ms-swift and the quantisation method was fp8. Getting this error while serving that model in vLLM. **Runtim...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 4** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sation bug bug;stale ### 🐛 Describe the bug I have quantised Ovis2.5 9B model using ms-swift and the quantisation method was fp8. Getting this error while serving that model in vLLM. **RuntimeError: size_n = 4304 is not...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Ovis2.5 9B FP8 quantisation bug bug;stale ### 🐛 Describe the bug I have quantised Ovis2.5 9B model using ms-swift and the quantisation method was fp8. Getting this error while serving that model in vLLM. **Runtim...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
