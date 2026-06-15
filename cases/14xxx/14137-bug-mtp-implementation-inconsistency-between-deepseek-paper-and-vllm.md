# vllm-project/vllm#14137: [Bug]: MTP Implementation Inconsistency Between DeepSeek Paper and vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#14137](https://github.com/vllm-project/vllm/issues/14137) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MTP Implementation Inconsistency Between DeepSeek Paper and vllm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems that the MTP described in DeepSeek's paper is inconsistent with the implementation in vllm #12755 . During the prefill phase, if the prompt is `t1, t2, t3, t4`, and the main model generates tokens `t2, t3, t4, t5`, these output tokens should be the input to the MTP. However, in the implementation of PR #12755 , the first input to the draft model is the same prompt which is `t1, t2, t3, t4`. Am I misunderstanding something, or is there an issue with the implementation in this PR? logs of prefill phase: ``` main model forward input_ids.shape=torch.Size([13]), tensor([ 0, 3476, 477, 260, 11502, 22896, 16, 128803, 18387, 477, 440, 33, 128804], device='cuda:0') mtp forward input_ids.shape=torch.Size([13]), input_ids=tensor([ 0, 3476, 477, 260, 11502, 22896, 16, 128803, 18387, 477, 440, 33, 128804], device='cuda:0') ``` ![Image](https://github.com/user-attachments/assets/a092842b-b6c2-47a2-bf58-d81036332735) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: g]: MTP Implementation Inconsistency Between DeepSeek Paper and vllm bug;stale ### Your current environment ### 🐛 Describe the bug It seems that the MTP described in DeepSeek's paper is inconsistent with the implementat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2, 22896, 16, 128803, 18387, 477, 440, 33, 128804], device='cuda:0') mtp forward input_ids.shape=torch.Size([13]), input_ids=tensor([ 0, 3476, 477, 260, 11502, 22896, 16, 128803, 18387, 477, 440, 33, 128804], device='cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: uring the prefill phase, if the prompt is `t1, t2, t3, t4`, and the main model generates tokens `t2, t3, t4, t5`, these output tokens should be the input to the MTP. However, in the implementation of PR #12755 , the fir...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
