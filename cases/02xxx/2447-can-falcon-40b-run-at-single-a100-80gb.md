# vllm-project/vllm#2447: Can Falcon-40B run at single A100 80gb? 

| 字段 | 值 |
| --- | --- |
| Issue | [#2447](https://github.com/vllm-project/vllm/issues/2447) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can Falcon-40B run at single A100 80gb? 

### Issue 正文摘录

Can Falcon-40B run at single A100 80gb? I encountered error "ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine." Did I set something wrong? I run with the following command "python benchmark_throughput.py --input-len=1 --output-len=128 --model=/models/falcon-40B/ --tokenizer=/models/falcon-40B/ --n 1 --num-prompts=1 --enforce-eager"

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ne." Did I set something wrong? I run with the following command "python benchmark_throughput.py --input-len=1 --output-len=128 --model=/models/falcon-40B/ --tokenizer=/models/falcon-40B/ --n 1 --num-prompts=1 --enforce...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Can Falcon-40B run at single A100 80gb? Can Falcon-40B run at single A100 80gb? I encountered error "ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the en...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: A100 80gb? I encountered error "ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine." Did I set something wrong? I run with the following command "p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 0gb? I encountered error "ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine." Did I set something wrong? I run with the following command "python...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: command "python benchmark_throughput.py --input-len=1 --output-len=128 --model=/models/falcon-40B/ --tokenizer=/models/falcon-40B/ --n 1 --num-prompts=1 --enforce-eager"

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
