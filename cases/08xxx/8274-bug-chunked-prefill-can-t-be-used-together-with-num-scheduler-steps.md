# vllm-project/vllm#8274: [Bug]: --Chunked prefill can't be used together with num-scheduler-steps

| 字段 | 值 |
| --- | --- |
| Issue | [#8274](https://github.com/vllm-project/vllm/issues/8274) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --Chunked prefill can't be used together with num-scheduler-steps

### Issue 正文摘录

### Your current environment vllm 0.6.0 ### 🐛 Describe the bug when I try this vllm serve neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8 --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1234 --enable_prefix_caching --enable-chunked-prefill --max-model-len 32000 --num-scheduler-steps 8 I got this raise ValueError("Chunked prefill is not supported with " ValueError: Chunked prefill is not supported with multi-step (--num-scheduler-steps > 1) ERROR 09-08 13:11:00 api_server.py:186] RPCServer process died before responding to readiness probe is it an expected behavior? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: --Chunked prefill can't be used together with num-scheduler-steps bug;stale ### Your current environment vllm 0.6.0 ### 🐛 Describe the bug when I try this vllm serve neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8 --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 6.0 ### 🐛 Describe the bug when I try this vllm serve neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8 --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1234 --enable_prefix_caching --enable-chunked-prefill --max-mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: bug when I try this vllm serve neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8 --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1234 --enable_prefix_caching --enable-chunked-prefill --max-model-len 32000 --num-sch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
