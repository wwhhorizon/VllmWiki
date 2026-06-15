# vllm-project/vllm#8782: [RFC]: Add Goodput Metric to Benchmark Serving

| 字段 | 值 |
| --- | --- |
| Issue | [#8782](https://github.com/vllm-project/vllm/issues/8782) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Add Goodput Metric to Benchmark Serving

### Issue 正文摘录

### Motivation. Currently, all metrics vLLM has are more from the perspectives of GenAI Service Providers. In order to provide a measurement from the perspectives of GenAI Service Users, we, from [Hao AI Lab](https://hao-ai-lab.github.io/home/#:~:text=Welcome%20to%20the%20UCSD%20Hao%20AI%20Lab%20website!), propose a new user-defined metric, **Goodput**😎. For more context, see the google docs link in the following section.⬇️ ### Proposed Change. Doc: [Goodput Support Proposal with more details.](https://docs.google.com/document/d/1TcZS-igoZxPrD8rj6_NM-WmCiQwAvP_-JJf2mXZEyZY/edit?usp=sharing) TL; DR - While doing benchmark, users can define service level objectives and get a **Goodput** result. We also propose adding **Goodput** to the CI benchmark dashboard. ### Feedback Period. 3~5 bussiness days ### CC List. @zhisbug @youkaichao @KuntaiDu @WoosukKwon @ywang96 ### Any Other Things. _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ser-defined metric, **Goodput**😎. For more context, see the google docs link in the following section.⬇️ ### Proposed Change. Doc: [Goodput Support Proposal with more details.](https://docs.google.com/document/d/1TcZS-i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [RFC]: Add Goodput Metric to Benchmark Serving RFC ### Motivation. Currently, all metrics vLLM has are more from the perspectives of GenAI Service Providers. In order to provide a measurement from the perspectives of Ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
