# vllm-project/vllm#28852: [Bug]: When infer MiniMax-m2, during streaming returns, the think are contained in the 'content' field and cannot be separated.

| 字段 | 值 |
| --- | --- |
| Issue | [#28852](https://github.com/vllm-project/vllm/issues/28852) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When infer MiniMax-m2, during streaming returns, the think are contained in the 'content' field and cannot be separated.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I used the following setup: vllm/vllm-openai:nightly --model /data/damoxing/MiniMax-M2 --host 0.0.0.0 --port 8000 --trust-remote-code --max-model-len 131072 --tensor-parallel-size 8 --served-model-name MiniMax-M2 --enable-chunked-prefill --enable-expert-parallel --tool-call-parser minimax_m2 --enable-auto-tool-choice --reasoning-parser minimax_m2_append_think I found that: whether using streaming or non-streaming mode, when the large model returns, the 'content' field contains the and tags and they are not separated from the results. When using this: --reasoning-parser minimax_m2, I found that: in non-streaming mode, when the large model returns, the 'content' field contains the result, and the 'reasoning_content' field contains the reasoning. However, in streaming mode, when the large model returns, the 'content' field still contains the tags and they are not separated. My goal is to separate reasoning from results: whether in non-streaming or streaming mode, the returned result should have the 'content' field for the result and 'reasoning_content' field for the reasoning. Appreciate for your reply ### Before submitting a new is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ld for the result and 'reasoning_content' field for the reasoning. Appreciate for your reply ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ply ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Describe the bug I used the following setup: vllm/vllm-openai:nightly --model /data/damoxing/MiniMax-M2 --host 0.0.0.0 --port 8000 --trust-remote-code --max-model-len 131072 --tensor-parallel-size 8 --served-model-name...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: -size 8 --served-model-name MiniMax-M2 --enable-chunked-prefill --enable-expert-parallel --tool-call-parser minimax_m2 --enable-auto-tool-choice --reasoning-parser minimax_m2_append_think I found that: whether using str...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --tensor-parallel-size 8 --served-model-name MiniMax-M2 --enable-chunked-prefill --enable-expert-parallel --tool-call-parser minimax_m2 --enable-auto-tool-choice --reasoning-parser minimax_m2_append_think I found that:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
