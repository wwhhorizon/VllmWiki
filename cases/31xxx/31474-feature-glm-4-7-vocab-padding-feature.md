# vllm-project/vllm#31474: [Feature]: GLM 4.7 vocab padding feature

| 字段 | 值 |
| --- | --- |
| Issue | [#31474](https://github.com/vllm-project/vllm/issues/31474) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GLM 4.7 vocab padding feature

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The number of attention heads in GLM-4.7 is 96, so I’m trying to run the FP8 version with 6× H20 GPUs using tensor parallelism (tp=6). However, vllm serve fails and due to `151552 cannot be divided by 6`. This seems to be caused by the vocab size 151552 not being divisible by the TP size. In my understanding, this could be solvable by padding the vocab size up. Alternatively, is there any simpler workaround or recommended solution for this case? Thanks! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: I’m trying to run the FP8 version with 6× H20 GPUs using tensor parallelism (tp=6). However, vllm serve fails and due to `151552 cannot be divided by 6`. This seems to be caused by the vocab size 151552 not being divisi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: number of attention heads in GLM-4.7 is 96, so I’m trying to run the FP8 version with 6× H20 GPUs using tensor parallelism (tp=6). However, vllm serve fails and due to `151552 cannot be divided by 6`. This seems to be c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: The number of attention heads in GLM-4.7 is 96, so I’m trying to run the FP8 version with 6× H20 GPUs using tensor parallelism (tp=6). However, vllm serve fails and due to `151552 cannot be divided by 6`. This seems to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: GLM 4.7 vocab padding feature feature request ### 🚀 The feature, motivation and pitch The number of attention heads in GLM-4.7 is 96, so I’m trying to run the FP8 version with 6× H20 GPUs using tensor paralle...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
