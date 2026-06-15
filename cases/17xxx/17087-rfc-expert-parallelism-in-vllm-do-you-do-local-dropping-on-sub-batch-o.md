# vllm-project/vllm#17087: [RFC]: Expert parallelism in VLLM - do you do local dropping on sub-batch of token activations before going through gating layer to make each rank possess unique sub-batch of data?

| 字段 | 值 |
| --- | --- |
| Issue | [#17087](https://github.com/vllm-project/vllm/issues/17087) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Expert parallelism in VLLM - do you do local dropping on sub-batch of token activations before going through gating layer to make each rank possess unique sub-batch of data?

### Issue 正文摘录

### Motivation. Looking at image below from [paper](https://arxiv.org/pdf/2503.04398v3) - the first row of process for DeepSeed-MoE, I wonder if vllm also do local dropping to make each rank possessing unique sub-batch of data before going through gating? ![Image](https://github.com/user-attachments/assets/3055ce45-0a3f-4de4-a32c-6aa431a66412) ### Proposed Change. NA ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Expert parallelism in VLLM - do you do local dropping on sub-batch of token activations before going through gating layer to make each rank possess unique sub-batch of data? RFC;stale ### Motivation. Looking at i...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [RFC]: Expert parallelism in VLLM - do you do local dropping on sub-batch of token activations before going through gating layer to make each rank possess unique sub-batch of data? RFC;stale ### Motivation. Looking at i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ugh gating layer to make each rank possess unique sub-batch of data? RFC;stale ### Motivation. Looking at image below from [paper](https://arxiv.org/pdf/2503.04398v3) - the first row of process for DeepSeed-MoE, I wonde...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
