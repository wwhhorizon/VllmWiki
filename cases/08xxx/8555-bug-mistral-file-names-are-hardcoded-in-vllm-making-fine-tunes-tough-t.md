# vllm-project/vllm#8555: [Bug]: Mistral file names are hardcoded in vllm, making fine tunes tough to use

| 字段 | 值 |
| --- | --- |
| Issue | [#8555](https://github.com/vllm-project/vllm/issues/8555) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mistral file names are hardcoded in vllm, making fine tunes tough to use

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug There are a lot of things hardcoded to work only with the file names in mistral HF repo and don't work if one fine-tunes the model and doesn't name their files exactly the same way. Eg, --config-format mistral looks for a params.json, --load-format mistral is hardcoded to look for *consolidated*.safetensors files, so if one's model shards are not named exactly like the vanilla model the load fails. Also, --tokenizer-mode mistral is hardcoded to look for tokenizer.model.v*, so if you don't have a tokenizer.model.v3, it fails. Is there a way to make loading mistral models more robust? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: g fine tunes tough to use bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug There are a lot of things hardcoded to work only with the file names in mistral HF repo and don...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: st? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ral file names are hardcoded in vllm, making fine tunes tough to use bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug There are a lot of things hardcoded to work only wit...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
