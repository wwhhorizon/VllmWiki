# vllm-project/vllm#33627: [Bug]: DeepSeek R1 with CUTLASS MLA Broken on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#33627](https://github.com/vllm-project/vllm/issues/33627) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek R1 with CUTLASS MLA Broken on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash launch_mtp: chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -tp {{GPUS}} --speculative_config '{"num_speculative_tokens":1, "method":"deepseek_mtp"}' --port {{PORT}} --enforce-eager --attention-backend CUTLASS_MLA ``` I get: ```bash (Worker_TP2 pid=404489) ERROR 02-02 20:46:37 [multiproc_executor.py:772] super().__init__( (Worker_TP2 pid=404489) ERROR 02-02 20:46:37 [multiproc_executor.py:772] TypeError: vllm.model_executor.layers.attention.mla_attention.MLACommonImpl.__init__() got multiple values for keyword argument 'q_pad_num_heads' [rank0]:[W202 20:46:37.582305111 ProcessGroupNCCL.cpp:1524] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator()) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: DeepSeek R1 with CUTLASS MLA Broken on B200 bug ### Your current environment ### 🐛 Describe the bug ```bash launch_mtp: chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -tp {{GPUS}} --speculative_config '{"num_spe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: DeepSeek R1 with CUTLASS MLA Broken on B200 bug ### Your current environment ### 🐛 Describe the bug ```bash launch_mtp: chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -tp {{GPUS}} --speculative_config '{"num_spe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: be the bug ```bash launch_mtp: chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -tp {{GPUS}} --speculative_config '{"num_speculative_tokens":1, "method":"deepseek_mtp"}' --port {{PORT}} --enforce-eager --attention-backen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nch_mtp: chg run --gpus {{GPUS}} -- vllm serve {{MODEL}} -tp {{GPUS}} --speculative_config '{"num_speculative_tokens":1, "method":"deepseek_mtp"}' --port {{PORT}} --enforce-eager --attention-backend CUTLASS_MLA ``` I ge...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
