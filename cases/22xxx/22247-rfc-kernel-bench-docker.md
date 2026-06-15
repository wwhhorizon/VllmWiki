# vllm-project/vllm#22247: [RFC]: Kernel Bench Docker

| 字段 | 值 |
| --- | --- |
| Issue | [#22247](https://github.com/vllm-project/vllm/issues/22247) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Kernel Bench Docker

### Issue 正文摘录

### Motivation. https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_moe.py https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/fused_moe/configs ### Proposed Change. I would like to generate kernel configs at scale, so it would be cool to have a docker quick command to generate them. If you could provide some information if there already is such an implementation or what style of implementation you prefer for this i would love to add this to the documentation and generate some kernels. Since i am working with a lot of different GPU's for our customer projects i could generate that kernels for different models and different GPU versions at scale. ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ls/benchmark_moe.py https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/fused_moe/configs ### Proposed Change. I would like to generate kernel configs at scale, so it would be cool to have a docker...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [RFC]: Kernel Bench Docker RFC;stale ### Motivation. https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_moe.py https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/fused_moe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: FC;stale ### Motivation. https://github.com/vllm-project/vllm/blob/main/benchmarks/kernels/benchmark_moe.py https://github.com/vllm-project/vllm/tree/main/vllm/model_executor/layers/fused_moe/configs ### Proposed Change...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: onfigs ### Proposed Change. I would like to generate kernel configs at scale, so it would be cool to have a docker quick command to generate them. If you could provide some information if there already is such an implem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
