# vllm-project/vllm#23015: [Bug]: Is the chat template for gpt-oss hard-coded?

| 字段 | 值 |
| --- | --- |
| Issue | [#23015](https://github.com/vllm-project/vllm/issues/23015) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Is the chat template for gpt-oss hard-coded?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Served the gpt-oss-20b model from Huggingface using Docker vllm/vllm-openai:gptoss. The chat template adds the knowledge cutoff date and current date to the system prompt. I don't want to use these dates in my system prompt so I deleted the relevant lines in the chat template. Then, I served the model using the new chat template. I also modified the model identity in the system prompt to test if my change works. But based on the vllm server logs, the exact default chat template was used. I also tried to specify a different jinja template file using the `--chat-template` arg. Based on the server log, vllm correctly recognized this parameter, printed out the chat template, and warned me that this is different from the official chat template (kind of weird, how does it know what the official chat template is). But vllm server logs showed the exactly default system prompt when I made a request. The model was even able to give me the current date even after I delete the chat_template.jinja from the model directory and redploy. It seems that vllm is not using the provided chat template at all. ### Before submitting a new issue... - [x]...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Is the chat template for gpt-oss hard-coded? bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Served the gpt-oss-20b model from Huggingface using Docker vllm/vllm-openai:gptoss. The chat temp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 🐛 Describe the bug Served the gpt-oss-20b model from Huggingface using Docker vllm/vllm-openai:gptoss. The chat template adds the knowledge cutoff date and current date to the system prompt. I don't want to use these da...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Is the chat template for gpt-oss hard-coded? bug;stale;gpt-oss ### Your current environment ### 🐛 Describe the bug Served the gpt-oss-20b model from Huggingface using Docker vllm/vllm-openai:gptoss. The chat temp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ll. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: hat template. I also modified the model identity in the system prompt to test if my change works. But based on the vllm server logs, the exact default chat template was used. I also tried to specify a different jinja te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
