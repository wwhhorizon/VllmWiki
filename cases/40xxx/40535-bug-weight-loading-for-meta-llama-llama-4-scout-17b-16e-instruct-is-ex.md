# vllm-project/vllm#40535: [Bug]: Weight loading for meta-llama/Llama-4-Scout-17B-16E-Instruct is extremely slow

| 字段 | 值 |
| --- | --- |
| Issue | [#40535](https://github.com/vllm-project/vllm/issues/40535) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Weight loading for meta-llama/Llama-4-Scout-17B-16E-Instruct is extremely slow

### Issue 正文摘录

### Your current environment [env.txt](https://github.com/user-attachments/files/26941850/env.txt) ### 🐛 Describe the bug Loading weights for meta-llama/Llama-4-Scout-17B-16E-Instruct is extremely slow. Running lm_eval (or other tests) usually leads to a timeout. Repro steps: ``` python3 examples/offline_inference/data_parallel.py \ --model="meta-llama/Llama-4-Scout-17B-16E-Instruct" \ --all2all-backend=allgather_reducescatter \ --trust-remote-code \ -dp=2 \ -tp=1 \ --enforce-eager \ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Weight loading for meta-llama/Llama-4-Scout-17B-16E-Instruct is extremely slow bug ### Your current environment [env.txt](https://github.com/user-attachments/files/26941850/env.txt) ### 🐛 Describe the bug Loading...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: meta-llama/Llama-4-Scout-17B-16E-Instruct is extremely slow. Running lm_eval (or other tests) usually leads to a timeout. Repro steps: ``` python3 examples/offline_inference/data_parallel.py \ --model="meta-llama/Llama-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: --model="meta-llama/Llama-4-Scout-17B-16E-Instruct" \ --all2all-backend=allgather_reducescatter \ --trust-remote-code \ -dp=2 \ -tp=1 \ --enforce-eager \ ``` ### Before submitting a new issue... - [x] Make sure you alre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
