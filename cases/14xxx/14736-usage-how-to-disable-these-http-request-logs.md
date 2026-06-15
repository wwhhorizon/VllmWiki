# vllm-project/vllm#14736: [Usage]: how to disable these http request  logs

| 字段 | 值 |
| --- | --- |
| Issue | [#14736](https://github.com/vllm-project/vllm/issues/14736) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to disable these http request  logs

### Issue 正文摘录

### Your current environment vllm 0.7.3 `vllm serve "DeepSeek-R1-Distill-Qwen-14B-Int8-W8A16" --max-model-len 8192 --host 0.0.0.0 --port 8015 --disable-log-requests --max_num_seqs=12 --max_num_batched_tokens=256 -tp=2` how could I disable these logs as follows: ``` INFO: 127.0.0.1:34658 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34598 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34638 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34700 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34644 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34780 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34782 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34682 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34614 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34754 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34736 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34626 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34542 - "POST /v1/chat/completions HTTP/1.1" 200 OK INFO: 127.0.0.1:34544 - "POST /v1/chat/completion...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: # Your current environment vllm 0.7.3 `vllm serve "DeepSeek-R1-Distill-Qwen-14B-Int8-W8A16" --max-model-len 8192 --host 0.0.0.0 --port 8015 --disable-log-requests --max_num_seqs=12 --max_num_batched_tokens=256 -tp=2` ho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to disable these http request logs usage ### Your current environment vllm 0.7.3 `vllm serve "DeepSeek-R1-Distill-Qwen-14B-Int8-W8A16" --max-model-len 8192 --host 0.0.0.0 --port 8015 --disable-log-requests...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
