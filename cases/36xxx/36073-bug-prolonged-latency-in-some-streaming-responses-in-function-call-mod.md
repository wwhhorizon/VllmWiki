# vllm-project/vllm#36073: [Bug]: Prolonged Latency in Some Streaming Responses in Function Call Mode（MiniMax model）

| 字段 | 值 |
| --- | --- |
| Issue | [#36073](https://github.com/vllm-project/vllm/issues/36073) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Prolonged Latency in Some Streaming Responses in Function Call Mode（MiniMax model）

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deployed and tested MiniMax-M2 in the Function Call streaming output scenario on both vLLM 0.14.1 and vLLM 0.16.0. The relevant configurations and test results are provided at the end. Please pay special attention to message 2568, it containing about 3500 characters. During the tool_calls argument generation phase, the model does not return tokens in a streaming manner. Instead, it blocks for a period of time and then returns the complete argument content all at once. We hope this behavior can be addressed and improved in future releases. A similar issue may also exist for other models. We hope this behavior can be addressed and improved in future releases. ==================================Deployment Script======================= export HCCL_BUFFSIZE=8192 export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 export HCCL_OP_EXPANSION_MODE="AIV" export PYTORCH_NPU_ALLOC_CONF=expandable_segments:True export VLLM_USE_V1=1 export VLLM_ASCEND_ENABLE_FLASHCOMM1=1 vllm serve model-path \ --served-model-name "minimax-m2.5-w8a8" \ --host 0.0.0.0 \ --port 8000 \ --tensor-parallel-size 8 \ --data-parallel-size 1 \ --max-num-seqs 8 \ --max-num-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: longed Latency in Some Streaming Responses in Function Call Mode（MiniMax model） bug ### Your current environment ### 🐛 Describe the bug I deployed and tested MiniMax-M2 in the Function Call streaming output scenario on...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Prolonged Latency in Some Streaming Responses in Function Call Mode（MiniMax model） bug ### Your current environment ### 🐛 Describe the bug I deployed and tested MiniMax-M2 in the Function Call streaming output sc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t configurations and test results are provided at the end. Please pay special attention to message 2568, it containing about 3500 characters. During the tool_calls argument generation phase, the model does not return to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ]}' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ase, the model does not return tokens in a streaming manner. Instead, it blocks for a period of time and then returns the complete argument content all at once. We hope this behavior can be addressed and improved in fut...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
