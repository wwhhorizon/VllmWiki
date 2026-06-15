# vllm-project/vllm#36440: [Feature] Add energy consumption metrics to benchmark suite

| 字段 | 值 |
| --- | --- |
| Issue | [#36440](https://github.com/vllm-project/vllm/issues/36440) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature] Add energy consumption metrics to benchmark suite

### Issue 正文摘录

## Feature Request ### Motivation vLLM's benchmark suite currently tracks throughput and latency, but not energy consumption. As sustainable AI becomes increasingly important, energy-per-token metrics would help users make informed deployment decisions. ### Proposal Add optional energy consumption tracking to vLLM's benchmark scripts using NVIDIA NVML, reporting: - Total energy (Joules) per benchmark run - Energy per output token (J/token) - Average GPU power draw (W) ### Evidence Systematic benchmarking across 12 model-precision configurations on NVIDIA RTX 4090D (Ada Lovelace) and RTX 5090 (Blackwell) shows that: - Quantization does **not** always reduce energy — NF4 increases energy by 25–56% for models below 3B parameters - Batch size has 84–96% impact on per-token energy, often outweighing precision choice - INT8 mixed-precision adds 17–33% energy overhead vs FP16 - These effects vary significantly across GPU architectures ### Data - Full dataset (200+ measurements): [Zenodo](https://zenodo.org/records/18900289) - Profiling toolkit: [EcoCompute-AI](https://github.com/hongping-zh/ecocompute-ai) - Interactive dashboard: [https://hongping-zh.github.io/ecocompute-dynamic-eval/](h...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Feature] Add energy consumption metrics to benchmark suite ## Feature Request ### Motivation vLLM's benchmark suite currently tracks throughput and latency, but not energy consumption. As sustainable AI becomes increas...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: stematic benchmarking across 12 model-precision configurations on NVIDIA RTX 4090D (Ada Lovelace) and RTX 5090 (Blackwell) shows that: - Quantization does **not** always reduce energy — NF4 increases energy by 25–56% fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: rage GPU power draw (W) ### Evidence Systematic benchmarking across 12 model-precision configurations on NVIDIA RTX 4090D (Ada Lovelace) and RTX 5090 (Blackwell) shows that: - Quantization does **not** always reduce ene...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ency, but not energy consumption. As sustainable AI becomes increasingly important, energy-per-token metrics would help users make informed deployment decisions. ### Proposal Add optional energy consumption tracking to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: NVIDIA RTX 4090D (Ada Lovelace) and RTX 5090 (Blackwell) shows that: - Quantization does **not** always reduce energy — NF4 increases energy by 25–56% for models below 3B parameters - Batch size has 84–96% impact on per...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
