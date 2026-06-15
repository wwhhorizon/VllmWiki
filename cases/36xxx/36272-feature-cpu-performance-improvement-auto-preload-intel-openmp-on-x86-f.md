# vllm-project/vllm#36272: [Feature]: [CPU] Performance improvement: Auto-preload Intel OpenMP on x86 for multi-core CPU inference

| 字段 | 值 |
| --- | --- |
| Issue | [#36272](https://github.com/vllm-project/vllm/issues/36272) |
| 状态 | open |
| 标签 | feature request;cpu |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: [CPU] Performance improvement: Auto-preload Intel OpenMP on x86 for multi-core CPU inference

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## The feature, motivation and pitch I'm running vLLM CPU inference on Intel Xeon 6768P (128 cores, 2 sockets) and found that the default GNU OpenMP (`libgomp`) only utilizes ~12 of 128 physical cores during decode (~10% utilization). Switching to Intel OpenMP (`libiomp5`) via `LD_PRELOAD` enables full core utilization and dramatically improves throughput. vLLM already configures KMP settings when `libiomp5.so` is detected in `LD_PRELOAD` (in `vllm/platforms/cpu.py`). It also auto-preloads `libgomp` for ARM and POWERPC. However, there is no auto-detection and preloading of `libiomp5` for x86. The Docker image sets `LD_PRELOAD` in the Dockerfile, so Docker users are covered. But users who install via `pip install` on bare metal do not get this optimization automatically and must manually configure `LD_PRELOAD`. | Metric | libgomp (default) | libiomp5 (manual LD_PRELOAD) | |---|---|---| | Active cores during decode | ~12 of 128 | 128 of 128 | | Core utilization | ~9% | ~100% | | Throughput | Baseline | Dramatically improved | Related: vLLM #27369 (ARM/POWERPC libgomp preload), PyTorch #166087 (OpenMP library loading) ### Alternatives ## Altern...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r, there is no auto-detection and preloading of `libiomp5` for x86. The Docker image sets `LD_PRELOAD` in the Dockerfile, so Docker users are covered. But users who install via `pip install` on bare metal do not get thi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ull core utilization and dramatically improves throughput. vLLM already configures KMP settings when `libiomp5.so` is detected in `LD_PRELOAD` (in `vllm/platforms/cpu.py`). It also auto-preloads `libgomp` for ARM and PO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t: Auto-preload Intel OpenMP on x86 for multi-core CPU inference feature request;cpu ### 🚀 The feature, motivation and pitch ## The feature, motivation and pitch I'm running vLLM CPU inference on Intel Xeon 6768P (128 c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: via `LD_PRELOAD` enables full core utilization and dramatically improves throughput. vLLM already configures KMP settings when `libiomp5.so` is detected in `LD_PRELOAD` (in `vllm/platforms/cpu.py`). It also auto-preload...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: pu.py`) will then apply automatically. Environment: - vLLM: vllm-cpu-amxbf16 0.15.0 - PyTorch: 2.10.0+cpu - CPU: Intel Xeon 6768P, 2 sockets, 128 cores / 256 threads (Granite Rapids) - RAM: 503 GB (4 NUMA nodes, SNC ena...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
