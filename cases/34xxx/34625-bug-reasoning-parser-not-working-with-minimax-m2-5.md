# vllm-project/vllm#34625: [Bug]: Reasoning Parser not working with Minimax m2.5

| 字段 | 值 |
| --- | --- |
| Issue | [#34625](https://github.com/vllm-project/vllm/issues/34625) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Reasoning Parser not working with Minimax m2.5

### Issue 正文摘录

### Your current environment I'm using vllm v0.15.1 with Minimax-M2.5. Here my vllm serve commande : ``` SAFETENSORS_FAST_GPU=1 vllm serve /root/.cache/huggingface/hub/models/MiniMaxAI/MiniMax-M2.5 \ --config /root/.cache/vllm-config-h200/config.yaml \ --gpu-memory-utilization 0.9 \ --trust-remote-code \ --enable_expert_parallel \ --tensor-parallel-size 8 \ --enable-auto-tool-choice \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2_append_think \ --served-model-name minimax-m2-5 ``` ### 🐛 Describe the bug I put the `--reasoning-parser minimax_m2_append_think` as you can see, but when I call the model I have this answer: ``` data: {"id":"chatcmpl-19aaba621548eee71c08f032b4aef98f","object":"chat.completion.chunk","created":1771253122,"model":"minimax-m2-5","choices":[{"index":0,"delta":{"role":"assistant","content":"","reasoning_content":null},"logprobs":null,"finish_reason":null}],"prompt_token_ids":null} data: {"id":"chatcmpl-19aaba621548eee71c08f032b4aef98f","object":"chat.completion.chunk","created":1771253122,"model":"minimax-m2-5","choices":[{"index":0,"delta":{"content":" The","reasoning_content":null},"logprobs":null,"finish_reason":null,"token_ids":null}]} dat...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm serve commande : ``` SAFETENSORS_FAST_GPU=1 vllm serve /root/.cache/huggingface/hub/models/MiniMaxAI/MiniMax-M2.5 \ --config /root/.cache/vllm-config-h200/config.yaml \ --gpu-memory-utilization 0.9 \ --trust-remote...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ) ? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ml \ --gpu-memory-utilization 0.9 \ --trust-remote-code \ --enable_expert_parallel \ --tensor-parallel-size 8 \ --enable-auto-tool-choice \ --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2_append_think \ --...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
