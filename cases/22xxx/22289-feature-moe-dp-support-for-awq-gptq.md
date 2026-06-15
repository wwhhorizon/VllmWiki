# vllm-project/vllm#22289: [Feature]: MoE DP support for AWQ/GPTQ

| 字段 | 值 |
| --- | --- |
| Issue | [#22289](https://github.com/vllm-project/vllm/issues/22289) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: MoE DP support for AWQ/GPTQ

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When trying to run `QuantTrio/GLM-4.5-AWQ` with `--enable-expert-parallel --tensor-parallel-size 2 --data-parallel-size 2` on a 4xH200 machine, I get this warning: > MoE DP setup unable to determine quantization scheme or unsupported quantization type. This model will not run with DP enabled * https://github.com/vllm-project/vllm/blob/4b29d2784b3753fd5434cded25cbcf0bce7b7da7/vllm/model_executor/layers/fused_moe/config.py#L468 I'm guessing it's because it's not supported. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: to determine quantization scheme or unsupported quantization type. This model will not run with DP enabled * https://github.com/vllm-project/vllm/blob/4b29d2784b3753fd5434cded25cbcf0bce7b7da7/vllm/model_executor/layers/...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Feature]: MoE DP support for AWQ/GPTQ feature request;stale ### 🚀 The feature, motivation and pitch When trying to run `QuantTrio/GLM-4.5-AWQ` with `--enable-expert-parallel --tensor-parallel-size 2 --data-parallel-siz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: MoE DP support for AWQ/GPTQ feature request;stale ### 🚀 The feature, motivation and pitch When trying to run `QuantTrio/GLM-4.5-AWQ` with `--enable-expert-parallel --tensor-parallel-size 2 --data-parallel-siz...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: quest;stale ### 🚀 The feature, motivation and pitch When trying to run `QuantTrio/GLM-4.5-AWQ` with `--enable-expert-parallel --tensor-parallel-size 2 --data-parallel-size 2` on a 4xH200 machine, I get this warning: > M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
