# vllm-project/vllm#14657: [Bug]: Inconsistent output of mixed samplings compared with individual sampling

| 字段 | 值 |
| --- | --- |
| Issue | [#14657](https://github.com/vllm-project/vllm/issues/14657) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Inconsistent output of mixed samplings compared with individual sampling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug prompts = [ "Hello, my name is", "The president of the United States is", "Hello, today is" ] sampling_params = [ SamplingParams(max_tokens=5, temperature=0, ignore_eos=True), SamplingParams(max_tokens=4, temperature=1, top_p=0.7, top_k=4, ignore_eos=True), SamplingParams(max_tokens=10, temperature=1, min_p=0.7, ignore_eos=True) ] outputs = self.llm.generate(prompts, sampling_params) outputs0 = self.llm.generate(prompts[0], sampling_params[0]) outputs1 = self.llm.generate(prompts[1], sampling_params[1]) outputs2 = self.llm.generate(prompts[2], sampling_params[2]) These outputs are different. outputs[1] != outputs1 outputs[2] != outputs2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
