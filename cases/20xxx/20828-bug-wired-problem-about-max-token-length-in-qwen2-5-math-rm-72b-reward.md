# vllm-project/vllm#20828: [Bug]: Wired problem about max token length in Qwen2.5-Math-RM-72B reward task

| 字段 | 值 |
| --- | --- |
| Issue | [#20828](https://github.com/vllm-project/vllm/issues/20828) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Wired problem about max token length in Qwen2.5-Math-RM-72B reward task

### Issue 正文摘录

### Your current environment ```text ValueError: The decoder prompt (length 8274) is longer than the maximum model length of 4096. Make sure that `max_model_len` is no smaller than the number of text tokens. ``` ### 🐛 Describe the bug I used 'reward' task of Qwen2.5-Math-RM-72B to process long prompts which is normal in the original huggingface implementation, but get the above error in vllm. Rope scaling can enable a normal run, but i'm not sure this is right. BTW, i tried to set max_model_len, no error is reported but can get __nan__ tensor, which is wired. Also, i check the original config of Qwen2.5-Math-RM-72B, the max position embedding is indeed 4096, and i use their tokenizer to print rm_tokenizer.model_max_length, the result is 131072. So I'm really confused what is wrong... ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Wired problem about max token length in Qwen2.5-Math-RM-72B reward task bug ### Your current environment ```text ValueError: The decoder prompt (length 8274) is longer than the maximum model length of 4096. Make...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n the maximum model length of 4096. Make sure that `max_model_len` is no smaller than the number of text tokens. ``` ### 🐛 Describe the bug I used 'reward' task of Qwen2.5-Math-RM-72B to process long prompts which is no...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 2B reward task bug ### Your current environment ```text ValueError: The decoder prompt (length 8274) is longer than the maximum model length of 4096. Make sure that `max_model_len` is no smaller than the number of text...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
