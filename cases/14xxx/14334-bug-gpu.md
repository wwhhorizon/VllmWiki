# vllm-project/vllm#14334: [Bug]: GPU索引指定失败

| 字段 | 值 |
| --- | --- |
| Issue | [#14334](https://github.com/vllm-project/vllm/issues/14334) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPU索引指定失败

### Issue 正文摘录

### Your current environment export CUDA_VISIBLE_DEVICES=2,3 && vllm serve QwQ-32B \ --dtype half \ --tensor-parallel-size 2 \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --port 9000 指定了GPU为2和3，但是启动模型依旧选择了0显卡，vllm版本0.7.2 ![Image](https://github.com/user-attachments/assets/2f54854a-943b-4ed7-86a4-df0053a4c3e6) ### 🐛 Describe the bug export CUDA_VISIBLE_DEVICES=2,3 && vllm serve QwQ-32B \ --dtype half \ --tensor-parallel-size 2 \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --port 9000 指定了GPU为2和3，但是启动模型依旧选择了0显卡，vllm版本0.7.2 ![Image](https://github.com/user-attachments/assets/328c74ba-cbd9-407c-b71b-ef0921f633de) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: GPU索引指定失败 bug;stale ### Your current environment export CUDA_VISIBLE_DEVICES=2,3 && vllm serve QwQ-32B \ --dtype half \ --tensor-parallel-size 2 \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --port 9000 指...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t environment export CUDA_VISIBLE_DEVICES=2,3 && vllm serve QwQ-32B \ --dtype half \ --tensor-parallel-size 2 \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --port 9000 指定了GPU为2和3，但是启动模型依旧选择了0显卡，vllm版本0.7.2 ![Ima...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: && vllm serve QwQ-32B \ --dtype half \ --tensor-parallel-size 2 \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --port 9000 指定了GPU为2和3，但是启动模型依旧选择了0显卡，vllm版本0.7.2 ![Image](https://github.com/user-attachments/assets...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: GPU索引指定失败 bug;stale ### Your current environment export CUDA_VISIBLE_DEVICES=2,3 && vllm serve QwQ-32B \ --dtype half \ --tensor-parallel-size 2 \ --cpu-offload-gb 1 \ --gpu-memory-utilization 0.9 \ --port 9000 指...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
