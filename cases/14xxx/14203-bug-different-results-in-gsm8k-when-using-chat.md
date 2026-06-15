# vllm-project/vllm#14203: [Bug]: Different results in gsm8k when using chat

| 字段 | 值 |
| --- | --- |
| Issue | [#14203](https://github.com/vllm-project/vllm/issues/14203) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Different results in gsm8k when using chat

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When testing on gms8k I get different results between HF and vllm this is the file used to generate the samples @ywang96 as mentioned on slack @hmellor since you were also in the slack chat EDIT: I had uploaded the wrong version of this file [evaluation_comparison.txt](https://github.com/user-attachments/files/19070706/evaluation_comparison.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: or since you were also in the slack chat EDIT: I had uploaded the wrong version of this file [evaluation_comparison.txt](https://github.com/user-attachments/files/19070706/evaluation_comparison.txt) ### Before submittin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Different results in gsm8k when using chat bug;stale ### Your current environment ### 🐛 Describe the bug When testing on gms8k I get different results between HF and vllm this is the file used to generate the sam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Describe the bug When testing on gms8k I get different results between HF and vllm this is the file used to generate the samples @ywang96 as mentioned on slack @hmellor since you were also in the slack chat EDIT: I had...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Different results in gsm8k when using chat bug;stale ### Your current environment ### 🐛 Describe the bug When testing on gms8k I get different results between HF and vllm this is the file used to generate the sam...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: bug;stale ### Your current environment ### 🐛 Describe the bug When testing on gms8k I get different results between HF and vllm this is the file used to generate the samples @ywang96 as mentioned on slack @hmellor since...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
