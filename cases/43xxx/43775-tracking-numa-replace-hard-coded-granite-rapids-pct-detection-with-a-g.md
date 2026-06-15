# vllm-project/vllm#43775: [Tracking][NUMA] Replace hard-coded Granite Rapids PCT detection with a generic, root-free path

| 字段 | 值 |
| --- | --- |
| Issue | [#43775](https://github.com/vllm-project/vllm/issues/43775) |
| 状态 | open |
| 标签 | feature request;keep-open |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Tracking][NUMA] Replace hard-coded Granite Rapids PCT detection with a generic, root-free path

### Issue 正文摘录

## Summary PR [#43270](https://github.com/vllm-project/vllm/pull/43270) adds opt-in NUMA pinning to Intel Priority Core Turbo (PCT) "priority" cores on Xeon 6776P / 6774P / 6962P, gated by a hard-coded SKU table in `vllm/utils/numa_utils.py::_PCT_CAPABLE_SKUS`. The workaround delivered a measurable end-to-end win on DGX B300 (Qwen3.5-397B-A17B-NVFP4, TP=8, 32K/2 prompts, MC=128: total token throughput **46.1k -> 75.8k tok/s, +64.4 %**), but it is intentionally narrow: - New PCT-capable SKUs require a vLLM patch that adds them to the table. - The `cpu_id % stride in (0, 1)` priority-core filter is empirical, not derived from the kernel. - The CPPC `highest_perf` value is hard-coded per SKU (4.6 GHz -> 46, 4.4 GHz -> 44). This issue tracks **removing that workaround** once we have a way to discover PCT priority cores without root and without per-SKU enumeration. ## Why the workaround exists today Quoting [#43270 (comment by @vadiklyutiy)](https://github.com/vllm-project/vllm/pull/43270#issuecomment-4523383323): ### 1. Kernel doesn't help In a perfect world the Linux scheduler would prefer PCT priority cores when there are fewer hot threads than priority cores, and vLLM wouldn't need...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ainers) typically can't grant root or rely on `intel-speed-select` being installed. ### 3. The two stop-gap alternatives are insufficient - "Document the manual `--numa-bind-cpus` recipe" — the users who need PCT pinnin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: und delivered a measurable end-to-end win on DGX B300 (Qwen3.5-397B-A17B-NVFP4, TP=8, 32K/2 prompts, MC=128: total token throughput **46.1k -> 75.8k tok/s, +64.4 %**), but it is intentionally narrow: - New PCT-capable S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y is root-only The only kernel interface that reports PCT / CLOS membership is `/dev/isst_interface`, used by `intel-speed-select`: ```text $ ls -l /dev/isst_interface crw------- 1 root root 10, 118 May 22 11:00 /dev/is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: SKUS`. The workaround delivered a measurable end-to-end win on DGX B300 (Qwen3.5-397B-A17B-NVFP4, TP=8, 32K/2 prompts, MC=128: total token throughput **46.1k -> 75.8k tok/s, +64.4 %**), but it is intentionally narrow: -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oded Granite Rapids PCT detection with a generic, root-free path feature request;keep-open ## Summary PR [#43270](https://github.com/vllm-project/vllm/pull/43270) adds opt-in NUMA pinning to Intel Priority Core Turbo (P...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
