# vllm-project/vllm#11447: [Bug]: The value of --max-model-len may influence results although the length of input less than max-model-len

| 字段 | 值 |
| --- | --- |
| Issue | [#11447](https://github.com/vllm-project/vllm/issues/11447) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The value of --max-model-len may influence results although the length of input less than max-model-len

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python model = LLM(model='./model/' + modelID, trust_remote_code=True,max_model_len=32*1024 / 128 * 1024) ``` I think it should be a widespread problem, the value of --max-model-len may influence results although the length of input less than max-model-len. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: The value of --max-model-len may influence results although the length of input less than max-model-len bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: fluence results although the length of input less than max-model-len bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python model = LLM(model='./model/' + modelID, tr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
