# vllm-project/vllm#41682: [Bug]: Pipeline Parallelism scheduler does not split sequences into pipeline micro-batches

| 字段 | 值 |
| --- | --- |
| Issue | [#41682](https://github.com/vllm-project/vllm/issues/41682) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | kernel |
| 症状 | slowdown |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Pipeline Parallelism scheduler does not split sequences into pipeline micro-batches

### Issue 正文摘录

### Your current environment ### Environment - Hardware: NVIDIA GB300 (SM103) NVL72 - Model: DeepSeek-R1-0528-FP4 - Workload: ISL = 128K, OSL = 1, aggregated mode, single 4-GPU node ### 🐛 Describe the bug ### Summary Under `pipeline-parallel-size > 1`, the vLLM scheduler dispatches up to `max_running_seq` sequences at once to the first pipeline stage instead of splitting them into `max_running_seq / PP_size` micro-batches per stage. As a result, enabling chunked prefill under PP adds scheduling and kernel-launch overhead **without** activating pipeline parallelism — chunks are serialized rather than pipelined. ### Environment - Hardware: NVIDIA GB300 (SM103) NVL72 - Model: DeepSeek-R1-0528-FP4 - Workload: ISL = 128K, OSL = 1, aggregated mode, single 4-GPU node ### Reproduction Configuration: `--pipeline-parallel-size 4 --tensor-parallel-size 1 --enable-chunked-prefill --max-num-batched-tokens `. Sweep ` ` over {4K, 12K, 32K} and compare against no-chunk baseline. All other knobs identical. ### Observed behavior — chunk-size sweep on GB300, PP4, ISL=128K / OSL=1 | Config | Peak TPS/GPU | |----------------|:------------:| | No-chunk | **1,678** | | Chunk 32K | ~1,500 | | Chunk 12K |...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Pipeline Parallelism scheduler does not split sequences into pipeline micro-batches bug ### Your current environment ### Environment - Hardware: NVIDIA GB300 (SM103) NVL72 - Model: DeepSeek-R1-0528-FP4 - Workload...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: onment - Hardware: NVIDIA GB300 (SM103) NVL72 - Model: DeepSeek-R1-0528-FP4 - Workload: ISL = 128K, OSL = 1, aggregated mode, single 4-GPU node ### 🐛 Describe the bug ### Summary Under `pipeline-parallel-size > 1`, the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Pipeline Parallelism scheduler does not split sequences into pipeline micro-batches bug ### Your current environment ### Environment - Hardware: NVIDIA GB300 (SM103) NVL72 - Model: DeepSeek-R1-0528-FP4 - Workload...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: t environment ### Environment - Hardware: NVIDIA GB300 (SM103) NVL72 - Model: DeepSeek-R1-0528-FP4 - Workload: ISL = 128K, OSL = 1, aggregated mode, single 4-GPU node ### 🐛 Describe the bug ### Summary Under `pipeline-p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: chunks per request should produce **more** pipeline fill and **higher** throughput (4K > 12K > 32K > no-chunk). We observe the **opposite** ordering: smaller chunks are strictly worse, and every chunked configuration lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
