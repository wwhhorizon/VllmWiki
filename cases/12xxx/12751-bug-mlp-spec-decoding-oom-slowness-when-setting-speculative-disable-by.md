# vllm-project/vllm#12751: [Bug]: MLP spec decoding OOM&slowness when setting --speculative-disable-by-batch-size with high arrival rate

| 字段 | 值 |
| --- | --- |
| Issue | [#12751](https://github.com/vllm-project/vllm/issues/12751) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MLP spec decoding OOM&slowness when setting --speculative-disable-by-batch-size with high arrival rate

### Issue 正文摘录

### Your current environment vllm main branch torch 2.5.1+cu124 ### 🐛 Describe the bug When running spec decoding with MLP speculator at high arrival ratea and with disable_all_speculation is on, the hidden states updating part( https://github.com/vllm-project/vllm/blob/main/vllm/spec_decode/spec_decode_worker.py#L653-L656) in run_no_spec() sometimes causes OOM when arrival rate is large. I guess it's because every time a new returned hidden states is append to the existing one and self.previous_hidden_states keeps growing large? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: MLP spec decoding OOM&slowness when setting --speculative-disable-by-batch-size with high arrival rate bug;stale ### Your current environment vllm main branch torch 2.5.1+cu124 ### 🐛 Describe the bug When running...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ge? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: MLP spec decoding OOM&slowness when setting --speculative-disable-by-batch-size with high arrival rate bug;stale ### Your current environment vllm main branch torch 2.5.1+cu124 ### 🐛 Describe the bug When running...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
