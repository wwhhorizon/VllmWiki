# vllm-project/vllm#36116: [Bug]: Pseudo-Streaming Issue When Using Tool Parser with Qwen3-Coder and MiniMax-M2

| 字段 | 值 |
| --- | --- |
| Issue | [#36116](https://github.com/vllm-project/vllm/issues/36116) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Pseudo-Streaming Issue When Using Tool Parser with Qwen3-Coder and MiniMax-M2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed and tested Qwen3-Coder-480B-A35B-Instruct-FP8 in the Function Call streaming output scenario on vLLM 0.16.0. The relevant configuration and test result are provided at the end. Please pay special attention to message 12. For details related to MiniMax-M2, please refer to #36073. During the tool_calls argument generation phase, the model does not return tokens in a streaming manner. We have located the relevant implementation in the tool-call-parser module and found that the issue appears to be related to the implementation of Qwen3-Coder. This behavior is similar to the pseudo-streaming issue we previously observed with MiniMax-M2, where the tool_calls arguments are buffered internally and returned all at once instead of being streamed token by token. We hope this implementation can be improved to support true streaming behavior in the tool_calls argument generation phase. ==================================Deployment Script============================== export HCCL_BUFFSIZE=8192 export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 export HCCL_OP_EXPANSION_MODE="AIV" export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True ex...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Pseudo-Streaming Issue When Using Tool Parser with Qwen3-Coder and MiniMax-M2 bug ### Your current environment ### 🐛 Describe the bug I deployed and tested Qwen3-Coder-480B-A35B-Instruct-FP8 in the Function Call...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ant configuration and test result are provided at the end. Please pay special attention to message 12. For details related to MiniMax-M2, please refer to #36073. During the tool_calls argument generation phase, the mode...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 🐛 Describe the bug I deployed and tested Qwen3-Coder-480B-A35B-Instruct-FP8 in the Function Call streaming output scenario on vLLM 0.16.0. The relevant configuration and test result are provided at the end. Please pay s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 72> ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: -batched-tokens 13107 \ --gpu-memory-utilization 0.95 \ --enable-expert-parallel \ --enable-chunked-prefill \ --enable-prefix-caching \ --trust-remote-code \ --mm_processor_cache_type="shm" \ --enable-auto-tool-choice \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
