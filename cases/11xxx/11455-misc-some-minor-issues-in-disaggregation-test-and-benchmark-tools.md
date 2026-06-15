# vllm-project/vllm#11455: [Misc]: some minor issues in disaggregation test and benchmark tools

| 字段 | 值 |
| --- | --- |
| Issue | [#11455](https://github.com/vllm-project/vllm/issues/11455) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: some minor issues in disaggregation test and benchmark tools

### Issue 正文摘录

### Anything you want to discuss about vllm. 1. disaggregation benchmark replies on `benchmark_serving.py` which has the `datasets` dependency. ![image](https://github.com/user-attachments/assets/55dc8c59-7705-4e03-b0a7-84c38e2ef356) 2. lsof command is not found ![image](https://github.com/user-attachments/assets/5bb81e18-f5e0-4476-abc8-4fc7c173ba55) 3. program exit immediately without waiting for two process. when I first run it, I though there's an issue. ![image](https://github.com/user-attachments/assets/9fcd3a9f-0b37-41e9-ad8b-d7736e42effa) 4. logs need more polishment in `kv_transfer` tests. I can not easily check the run status. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Misc]: some minor issues in disaggregation test and benchmark tools ### Anything you want to discuss about vllm. 1. disaggregation benchmark replies on `benchmark_serving.py` which has the `datasets` dependency. ![imag...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ion benchmark replies on `benchmark_serving.py` which has the `datasets` dependency. ![image](https://github.com/user-attachments/assets/55dc8c59-7705-4e03-b0a7-84c38e2ef356) 2. lsof command is not found ![image](https:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: us. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: b81e18-f5e0-4476-abc8-4fc7c173ba55) 3. program exit immediately without waiting for two process. when I first run it, I though there's an issue. ![image](https://github.com/user-attachments/assets/9fcd3a9f-0b37-41e9-ad8...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
