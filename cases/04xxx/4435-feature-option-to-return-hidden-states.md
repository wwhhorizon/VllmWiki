# vllm-project/vllm#4435: [Feature]: option to return hidden states

| 字段 | 值 |
| --- | --- |
| Issue | [#4435](https://github.com/vllm-project/vllm/issues/4435) |
| 状态 | closed |
| 标签 | feature request;unstale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: option to return hidden states

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am generating mutiple samples from the same prompt as in self-consistent Chain of Thought (CoT). I have trained a separate evaluation head (using the same backbone as the LLM generator) to assess the quality of each sample. Without the option to return hidden states, I would need to perform an additional forward pass to obtain them. The majority of the computational work is already done when the VLLM generates the samples. Having this option would significantly save on inference time. If I were to implement this, could someone point me in the right direction regarding which parts of the source code I should look at? Any pointers would be appreciated. Thanks! ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: option to return hidden states feature request;unstale ### 🚀 The feature, motivation and pitch I am generating mutiple samples from the same prompt as in self-consistent Chain of Thought (CoT). I have trained...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ch parts of the source code I should look at? Any pointers would be appreciated. Thanks! ### Alternatives _No response_ ### Additional context _No response_
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: as in self-consistent Chain of Thought (CoT). I have trained a separate evaluation head (using the same backbone as the LLM generator) to assess the quality of each sample. Without the option to return hidden states, I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
