# vllm-project/vllm#10664: [Performance]: There is a 10x performance gap between the lora-modules deployment model and the Merge deployment model

| 字段 | 值 |
| --- | --- |
| Issue | [#10664](https://github.com/vllm-project/vllm/issues/10664) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: There is a 10x performance gap between the lora-modules deployment model and the Merge deployment model

### Issue 正文摘录

### Proposal to improve performance vllm serve /workspace/model/llm/Qwen/Qwen2_5-3B-Instruct\ --host 0.0.0.0 \ --port 2017 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.9 \ --trust-remote-code \ --enforce-eager \ --lora-modules question_ext3B=/workspace/output/question_extration/qwen/qwen2_5-3b-instruct/v0-20241122-142013/checkpoint-1200\ --enable-lora \ --max-lora-rank 32 \ time：23.94313097000122 vllm serve /workspace/output/question_extration/qwen/qwen2_5-3b-instruct/v0-20241122-142013/checkpoint-1200-merged time：2.6456634998321533 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) vllm 0.6.4.post1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nce]: There is a 10x performance gap between the lora-modules deployment model and the Merge deployment model performance;stale ### Proposal to improve performance vllm serve /workspace/model/llm/Qwen/Qwen2_5-3B-Instruc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: heckpoint-1200-merged time：2.6456634998321533 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) vllm 0.6.4.po...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: st1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lora-modules deployment model and the Merge deployment model performance;stale ### Proposal to improve performance vllm serve /workspace/model/llm/Qwen/Qwen2_5-3B-Instruct\ --host 0.0.0.0 \ --port 2017 \ --tensor-parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
