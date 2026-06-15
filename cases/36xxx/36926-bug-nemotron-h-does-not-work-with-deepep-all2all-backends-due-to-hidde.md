# vllm-project/vllm#36926: [Bug]: nemotron_h does not work with DeepEP all2all backends due to hidden dim rounding

| 字段 | 值 |
| --- | --- |
| Issue | [#36926](https://github.com/vllm-project/vllm/issues/36926) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support;moe |
| 子分类 | runtime_err |
| Operator 关键词 | moe |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: nemotron_h does not work with DeepEP all2all backends due to hidden dim rounding

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was doing some MoE testing and ran into a problem with the nemotron_h model and backends that require rounding the hidden dimension, e.g. `deepep_low_latency` and `deepep_high_throughput.` The weight_loader is getting the rounded dimension which it does not expect (see stack trace). I think there might also be a problem at runtime with the routed input transform dimensions. Repro steps: ``` python3 examples/offline_inference/data_parallel.py \ --model="nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16" \ --all2all-backend deepep_low_latency \ --trust-remote-code \ -dp=2 \ -tp=1 \ --enforce-eager ``` Stack: ``` ERROR 03-12 20:19:38 [multiproc_executor.py:844] WorkerProc failed to start. ERROR 03-12 20:19:38 [multiproc_executor.py:844] Traceback (most recent call last): ERROR 03-12 20:19:38 [multiproc_executor.py:844] File "/home/bnellnm/nm-vllm-new/vllm/v1/executor/multiproc_executor.py", line 813, in worker_main ERROR 03-12 20:19:38 [multiproc_executor.py:844] worker = WorkerProc(*args, **kwargs) ERROR 03-12 20:19:38 [multiproc_executor.py:844] ^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 03-12 20:19:38 [multiproc_executor.py:844] File "/home/bn...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ata_parallel.py \ --model="nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16" \ --all2all-backend deepep_low_latency \ --trust-remote-code \ -dp=2 \ -tp=1 \ --enforce-eager ``` Stack: ``` ERROR 03-12 20:19:38 [multiproc_execut...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: I was doing some MoE testing and ran into a problem with the nemotron_h model and backends that require rounding the hidden dimension, e.g. `deepep_low_latency` and `deepep_high_throughput.` The weight_loader is getting...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: our current environment ### 🐛 Describe the bug I was doing some MoE testing and ran into a problem with the nemotron_h model and backends that require rounding the hidden dimension, e.g. `deepep_low_latency` and `deepep...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ## Your current environment ### 🐛 Describe the bug I was doing some MoE testing and ran into a problem with the nemotron_h model and backends that require rounding the hidden dimension, e.g. `deepep_low_latency` and `de...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: nemotron_h does not work with DeepEP all2all backends due to hidden dim rounding bug ### Your current environment ### 🐛 Describe the bug I was doing some MoE testing and ran into a problem with the nemotron_h mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
