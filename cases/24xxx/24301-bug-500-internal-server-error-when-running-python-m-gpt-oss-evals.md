# vllm-project/vllm#24301: [Bug]: 500 Internal Server Error when running `python -m gpt_oss.evals`

| 字段 | 值 |
| --- | --- |
| Issue | [#24301](https://github.com/vllm-project/vllm/issues/24301) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 500 Internal Server Error when running `python -m gpt_oss.evals`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Before the #22386, the following cmd worked: ``` vllm serve openai/gpt-oss-20b OPENAI_API_KEY="test" python -m gpt_oss.evals --sampler chat_completions --model openai/gpt-oss-20b --reasoning-effort low --n-threads 512 --eval gpqa ``` After the PR, it encountered ``` (APIServer pid=8050) INFO: 127.0.0.1:42504 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error (APIServer pid=8050) INFO: 127.0.0.1:45104 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error (APIServer pid=8050) INFO: 127.0.0.1:42014 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bug Before the #22386, the following cmd worked: ``` vllm serve openai/gpt-oss-20b OPENAI_API_KEY="test" python -m gpt_oss.evals --sampler chat_completions --model openai/gpt-oss-20b --reasoning-effort low --n-threads 5...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: 500 Internal Server Error when running `python -m gpt_oss.evals` bug ### Your current environment ### 🐛 Describe the bug Before the #22386, the following cmd worked: ``` vllm serve openai/gpt-oss-20b OPENAI_API_K...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
