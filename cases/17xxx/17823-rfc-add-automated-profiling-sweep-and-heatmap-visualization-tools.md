# vllm-project/vllm#17823: [RFC]: Add automated profiling sweep and heatmap visualization tools

| 字段 | 值 |
| --- | --- |
| Issue | [#17823](https://github.com/vllm-project/vllm/issues/17823) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | kernel;operator |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Add automated profiling sweep and heatmap visualization tools

### Issue 正文摘录

### Motivation. While `examples/offline_inference/profiling.py` provides detailed kernel-level timing in vLLM, its usability is limited when users want to: - Conduct profiling across multiple batch sizes and prompt lengths - Visualize performance trends and bottlenecks Currently, users must manually modify arguments and parse raw outputs, which is slow and error-prone. There's no convenient way to sweep inputs or generate visual summaries. We propose two tools to address this gap and extend the existing profiler for practical model-level profiling. ### Proposed Change. We propose upstreaming two lightweight utilities: #### 1. `sweep_profiling.py` A script to automate `profiling.py` runs across a set of batch sizes and prompt lengths. Features: - CLI flags: `--model`, `--tensor-parallel-size`, `--max-tokens` - Spawns subprocesses for each profiling job - Captures errors cleanly and logs failures - Output: multiple `profiling_bs{N}_pl{M}.json` traces **In addition to the overall model runner time, we also generate the profiling result for operator breakdown.** **Usage:** ``` python sweep_profiling.py [--model MODEL_NAME] [--max-tokens MAX_TOKENS] [--tensor-parallel-size TP_SIZE] ```...

## 现有链接修复摘要

#17933 [Misc][RFC] Add automated profiling sweep and heatmap visualization tools

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [RFC]: Add automated profiling sweep and heatmap visualization tools RFC;stale ### Motivation. While `examples/offline_inference/profiling.py` provides detailed kernel-level timing in vLLM, its usability is limited when...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ` Supports batch × prompt sweep. **Key logic:** ```python def extract_cuda_time(json_file, phase): with open(json_file) as f: data = json.load(f) entry = SummaryStatsEntry(**data[phase]["summary_stats"][0]["entry"]) ret...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tools to address this gap and extend the existing profiler for practical model-level profiling. ### Proposed Change. We propose upstreaming two lightweight utilities: #### 1. `sweep_profiling.py` A script to automate `p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC]: Add automated profiling sweep and heatmap visualization tools RFC;stale ### Motivation. While `examples/offline_inference/profiling.py` provides detailed kernel-level timing in vLLM, its usability is limited when...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: b11e-40e1-889c-ef39d217c485) #### Summary This RFC introduces a reproducible and automated profiling suite for vLLM that: - Enhances `profiling.py` with systematic benchmarking - Enables heatmap-based performance analys...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17933](https://github.com/vllm-project/vllm/pull/17933) | closes_keyword | 0.95 | [Misc][RFC] Add automated profiling sweep and heatmap visualization tools | FIX #17823 ### CC List @GindaChen @JJMN22 <!--- pyml disable-next-line no-emphasis-as-heading --> |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
