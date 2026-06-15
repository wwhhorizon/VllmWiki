# vllm-project/vllm#4651: [Bug]: openapi running but "POST /v1/chat/completions HTTP/1.1" 404 Not Found

| 字段 | 值 |
| --- | --- |
| Issue | [#4651](https://github.com/vllm-project/vllm/issues/4651) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: openapi running but "POST /v1/chat/completions HTTP/1.1" 404 Not Found

### Issue 正文摘录

### Your current environment ubuntu + k8s + vllm/vllm-openai:latest ### 🐛 Describe the bug I keep getting the error message: "POST /v1/chat/completions HTTP/1.1" 404 Not Found The command I use is: containers: - command: [ "python3", "-m", "vllm.entrypoints.openai.api_server" ] args: [ "--model=/share_nfs/hf_models/llama2-70b-chat-hf", "--chat-template=/share_nfs/hf_models/llama2-70b-chat-hf/llama-2-chat.jinja", "--gpu-memory-utilization=0.9", "--disable-log-requests", "--trust-remote-code", "--port=8000", "--max-model-len=4096", "--max-num-seqs=512", "--max-seq_len-to-capture=4096", "--tensor-parallel-size=8" ] and yes, I have already set the right entry point vllm.entrypoints.openai.api_server and yes, I have already set the chat template which is downloaded from here: https://github.com/chujiezheng/chat_templates/blob/main/chat_templates/llama-2-chat.jinja no errors during startup but I get 404 for /v1/chat/completions BTW, /v1/models and /v1/completion are both ok. What am I missing ? thanks!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hon3", "-m", "vllm.entrypoints.openai.api_server" ] args: [ "--model=/share_nfs/hf_models/llama2-70b-chat-hf", "--chat-template=/share_nfs/hf_models/llama2-70b-chat-hf/llama-2-chat.jinja", "--gpu-memory-utilization=0.9"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: "--gpu-memory-utilization=0.9", "--disable-log-requests", "--trust-remote-code", "--port=8000", "--max-model-len=4096", "--max-num-seqs=512", "--max-seq_len-to-capture=4096",
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ound bug ### Your current environment ubuntu + k8s + vllm/vllm-openai:latest ### 🐛 Describe the bug I keep getting the error message: "POST /v1/chat/completions HTTP/1.1" 404 Not Found The command I use is: containers:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
