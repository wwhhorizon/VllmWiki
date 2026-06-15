# vllm-project/vllm#22234: [Bug]: VLLM v0.10.0: V1 GPU worker didn't consider num_gpu_blocks_override when calculating self.requested_memory

| 字段 | 值 |
| --- | --- |
| Issue | [#22234](https://github.com/vllm-project/vllm/issues/22234) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM v0.10.0: V1 GPU worker didn't consider num_gpu_blocks_override when calculating self.requested_memory

### Issue 正文摘录

### Your current environment It's irrelevant to the bug. ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/v0.10.0/vllm/v1/worker/gpu_worker.py#L164 In `init_device()`, when calculating `self.requested_memory`, the V1 GPU worker didn't consider `num_gpu_blocks_override`, or `--num-gpu-blocks-override` in CLI params. It will then raise the `ValueError` at line 168, if I set `--num-gpu-blocks-override` to a small number (like 5000), which fits in my GPU memory left on the device, but left `--gpu-memory-utilization` as default (0.9). The V0 worker didn't have the problem since it didn't check the device memory in `init_device()`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the `ValueError` at line 168, if I set `--num-gpu-blocks-override` to a small number (like 5000), which fits in my GPU memory left on the device, but left `--gpu-memory-utilization` as default (0.9). The V0 worker didn'...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: num-gpu-blocks-override` to a small number (like 5000), which fits in my GPU memory left on the device, but left `--gpu-memory-utilization` as default (0.9). The V0 worker didn't have the problem since it didn't check t...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: VLLM v0.10.0: V1 GPU worker didn't consider num_gpu_blocks_override when calculating self.requested_memory bug ### Your current environment It's irrelevant to the bug. ### 🐛 Describe the bug https://github.com/vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: GPU worker didn't consider num_gpu_blocks_override when calculating self.requested_memory bug ### Your current environment It's irrelevant to the bug. ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/v0....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
