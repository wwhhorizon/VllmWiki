# vllm-project/vllm#9609: [Performance]: test speculative decode accuracy

| 字段 | 值 |
| --- | --- |
| Issue | [#9609](https://github.com/vllm-project/vllm/issues/9609) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: test speculative decode accuracy

### Issue 正文摘录

### Proposal to improve performance I use lm-evaluation-harness to test vllm accuracy 1.when don't enable spec decode,I got some result below num_concurrent=1 ![image](https://github.com/user-attachments/assets/dfa6ef55-216e-4460-9ef4-d387e0ce460e) num_concurrent=8 ![image](https://github.com/user-attachments/assets/505d051f-f119-4275-a5d4-5683b74be398) num_concurrent=16 ![image](https://github.com/user-attachments/assets/87e7c9c6-f2de-43de-8a20-96f82c4c9c7c) num_concurrent=32 ![image](https://github.com/user-attachments/assets/312e2703-cfc8-42c7-9751-22a0b1aba21d) 2.when enable spec decode,I got some result below num_concurrent=1 ![image](https://github.com/user-attachments/assets/6681a17f-3bc7-4d52-b0e5-5451a40dfcf4) num_concurrent=8 ![image](https://github.com/user-attachments/assets/4a1878a8-2da7-475e-9ecd-8400a6fc0620) num_concurrent=16 ![image](https://github.com/user-attachments/assets/fc9ca925-a57c-4c6f-9a07-1fa056e67d66) num_concurrent=32 ![image](https://github.com/user-attachments/assets/67d284c2-9023-440c-88fa-f61c3f6090de) Has anyone done such experiments? Does vLLM's speculative decoding affect output accuracy? ### Report of performance regression _No response_ ### M...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: test speculative decode accuracy performance ### Proposal to improve performance I use lm-evaluation-harness to test vllm accuracy 1.when don't enable spec decode,I got some result below num_concurrent=1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: test speculative decode accuracy performance ### Proposal to improve performance I use lm-evaluation-harness to test vllm accuracy 1.when don't enable spec decode,I got some result below num_concurrent=1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: response_ ### Your current environment (if you think it is necessary) h100 1gpu ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom r...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Performance]: test speculative decode accuracy performance ### Proposal to improve performance I use lm-evaluation-harness to test vllm accuracy 1.when don't enable spec decode,I got some result below num_concurrent=1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
