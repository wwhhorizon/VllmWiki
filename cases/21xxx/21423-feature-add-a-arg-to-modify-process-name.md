# vllm-project/vllm#21423: [Feature]: add a arg to modify process_name

| 字段 | 值 |
| --- | --- |
| Issue | [#21423](https://github.com/vllm-project/vllm/issues/21423) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: add a arg to modify process_name

### Issue 正文摘录

### 🚀 The feature, motivation and pitch when I run nvidia-smi. I just see python. maybe I need to run mulit llm serve, and I want to kill a llm by root. I want to know which process_id. Or I need to know which llm has been launch. I know `setproctitle` can solve this problem. just use `setproctitle("xxx")`. could you add this feature in future version? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ature request ### 🚀 The feature, motivation and pitch when I run nvidia-smi. I just see python. maybe I need to run mulit llm serve, and I want to kill a llm by root. I want to know which process_id. Or I need to know w...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: em. just use `setproctitle("xxx")`. could you add this feature in future version? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already sear...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: add a arg to modify process_name feature request ### 🚀 The feature, motivation and pitch when I run nvidia-smi. I just see python. maybe I need to run mulit llm serve, and I want to kill a llm by root. I want...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
