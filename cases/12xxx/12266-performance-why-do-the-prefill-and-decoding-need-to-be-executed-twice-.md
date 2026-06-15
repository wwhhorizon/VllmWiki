# vllm-project/vllm#12266: [Performance]:Why do the prefill and decoding need to be executed twice for the same task?

| 字段 | 值 |
| --- | --- |
| Issue | [#12266](https://github.com/vllm-project/vllm/issues/12266) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]:Why do the prefill and decoding need to be executed twice for the same task?

### Issue 正文摘录

### Proposal to improve performance ### Report of performance regression _No response_ ### Misc discussion on performance Hello, when I start the serving service using vllm serve and conduct tests using the benchmark_serving.py script, I captured the kernel pipeline of the CUDA backend through the nsight system. I found out why the prefill and decoding stages of the same task are executed twice? ![Image](https://github.com/user-attachments/assets/19c57ea0-bb61-49a5-ad3e-e2e4a678b845) At the same time, my commands are as follows: * serving: ``` vllm serve data/llama-3-8b-instruct \ --swap-space 16 \ --disable-log-requests \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.9 \ --dtype bfloat16 --enforce-eager ``` * client: ``` python3 vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --model data/llama-3-8b-instruct \ --profile \ --dataset-name random \ --random-input-len 2048 \ --random-output-len 200 \ --num-prompts 1 \ --trust-remote-code ``` I wonder, is there any trick for executing the prefill and decoding twice for the same prompt? ### Your current environment (if you think it is necessary) _No response_ ### Before submitting a new issue... - [x] Make sure you alre...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: rformance ### Proposal to improve performance ### Report of performance regression _No response_ ### Misc discussion on performance Hello, when I start the serving service using vllm serve and conduct tests using the be...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ensor-parallel-size 2 \ --gpu-memory-utilization 0.9 \ --dtype bfloat16 --enforce-eager ``` * client: ``` python3 vllm/benchmarks/benchmark_serving.py \ --backend vllm \ --model data/llama-3-8b-instruct \ --profile \ --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g the benchmark_serving.py script, I captured the kernel pipeline of the CUDA backend through the nsight system. I found out why the prefill and decoding stages of the same task are executed twice? ![Image](https://gith...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: he same time, my commands are as follows: * serving: ``` vllm serve data/llama-3-8b-instruct \ --swap-space 16 \ --disable-log-requests \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.9 \ --dtype bfloat16 --enfo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]:Why do the prefill and decoding need to be executed twice for the same task? performance ### Proposal to improve performance ### Report of performance regression _No response_ ### Misc discussion on perfor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
