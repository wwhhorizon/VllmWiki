# vllm-project/vllm#13367: [Bug]: Why does the worker node exit after running for a while after joining the head node, even though I did not send an exit signal?

| 字段 | 值 |
| --- | --- |
| Issue | [#13367](https://github.com/vllm-project/vllm/issues/13367) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Why does the worker node exit after running for a while after joining the head node, even though I did not send an exit signal?

### Issue 正文摘录

### Your current environment vllm-openai:v0.7.2 ### 🐛 Describe the bug [2025-02-16 18:29:17,459 W 1 1] global_state_accessor.cc:429: Retrying to get node with node ID 91bf9af69c7ffeb8e02ad6c6e69b4dcc3584ddb3e10953b515e47280 2025-02-16 18:29:05,057 INFO scripts.py:1047 -- Local node IP: 172.29.1.4 2025-02-16 18:29:18,461 SUCC scripts.py:1063 -- -------------------- 2025-02-16 18:29:18,461 SUCC scripts.py:1064 -- Ray runtime started. 2025-02-16 18:29:18,461 SUCC scripts.py:1065 -- -------------------- 2025-02-16 18:29:18,461 INFO scripts.py:1067 -- To terminate the Ray runtime, run 2025-02-16 18:29:18,461 INFO scripts.py:1068 -- ray stop 2025-02-16 18:29:18,461 INFO scripts.py:1076 -- --block 2025-02-16 18:29:18,461 INFO scripts.py:1077 -- This command will now block forever until terminated by a signal. 2025-02-16 18:29:18,461 INFO scripts.py:1080 -- Running subprocesses are monitored and a message will be printed if any of them terminate unexpectedly. Subprocesses exit with SIGTERM will be treated as graceful, thus NOT reported. node node ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ode ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .py:1068 -- ray stop 2025-02-16 18:29:18,461 INFO scripts.py:1076 -- --block 2025-02-16 18:29:18,461 INFO scripts.py:1077 -- This command will now block forever until terminated by a signal. 2025-02-16 18:29:18,461 INFO...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
