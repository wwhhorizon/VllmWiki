# vllm-project/vllm#20104: it run good

| 字段 | 值 |
| --- | --- |
| Issue | [#20104](https://github.com/vllm-project/vllm/issues/20104) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> it run good

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/7521c843-407a-41c8-b961-09ee7f7df95f) [sucvllm.txt](https://github.com/user-attachments/files/20913989/sucvllm.txt) ### 🐛 Describe the bug #/default/create_completion_v1_completions_post { "model": "Qwen/Qwen2.5-1.5B-Instruct", "prompt": "Who is Napoleon Bonaparte?", "max_tokens": 128, "temperature": 0.0 } { "id": "cmpl-4b3d25bf255944828dfcdac816c28cb1", "object": "text_completion", "created": 1750894412, "model": "Qwen/Qwen2.5-1.5B-Instruct", "choices": [ { "index": 0, "text": " Who was he and what did he do?\nNapoleon Bonaparte, born on August 15, 1769, in Ajaccio, Corsica, was a French military leader who rose to prominence during the French Revolution. He served as First Consul of France from 1799 to 1804 and Emperor of the French from 1804 until his abdication in 1814. After briefly returning to power in 1815, he was exiled to Saint Helena, where he died.\n\nKey aspects of Napoleon's life and accomplishments include:\n\n", "logprobs": null, "finish_reason": "length", "stop_reason": null, "prompt_logprobs": null } ], "usage": { "prompt_tokens": 7, "total_tokens": 135, "completion_tokens": 128, "pr...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Describe the bug #/default/create_completion_v1_completions_post { "model": "Qwen/Qwen2.5-1.5B-Instruct", "prompt": "Who is Napoleon Bonaparte?", "max_tokens": 128, "temperature": 0.0 } { "id": "cmpl-4b3d25bf255944828df...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: and what did he do?\nNapoleon Bonaparte, born on August 15, 1769, in Ajaccio, Corsica, was a French military leader who rose to prominence during the French Revolution. He served as First Consul of France from 1799 to 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: } } ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
