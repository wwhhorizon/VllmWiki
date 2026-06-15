# vllm-project/vllm#29447: [Bug]: Multinode TP Errors when TP > number GPUS on 1 node, but <= world size

| 字段 | 值 |
| --- | --- |
| Issue | [#29447](https://github.com/vllm-project/vllm/issues/29447) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multinode TP Errors when TP > number GPUS on 1 node, but <= world size

### Issue 正文摘录

### Your current environment [vllm_out.log](https://github.com/user-attachments/files/23757025/vllm_out.log) 2x GB200 nodes, vllm 0.11.2 ### 🐛 Describe the bug On head node: `ray start --head --num-gpus 4` Copy output command for worker node `ray start --address=' : ' --num-gpus 4` Ensure 8 gpus are visible on `ray status`. On head node: `vllm serve meta-llama/Llama-3.3-70B-Instruct --gpu-memory-utilization 0.9 --served-model-name llama3.3-70b --tensor-parallel-size 8 --pipeline-parallel-size 1 --data-parallel-size 1 --max-model-len 2048 --port $port` [Output log (portions redacted)](https://github.com/user-attachments/files/23757034/vllm_out.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: https://github.com/user-attachments/files/23757025/vllm_out.log) 2x GB200 nodes, vllm 0.11.2 ### 🐛 Describe the bug On head node: `ray start --head --num-gpus 4` Copy output command for worker node `ray start --address=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sure 8 gpus are visible on `ray status`. On head node: `vllm serve meta-llama/Llama-3.3-70B-Instruct --gpu-memory-utilization 0.9 --served-model-name llama3.3-70b --tensor-parallel-size 8 --pipeline-parallel-size 1 --da...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
