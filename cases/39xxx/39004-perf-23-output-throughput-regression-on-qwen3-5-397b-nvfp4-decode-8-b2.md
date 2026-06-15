# vllm-project/vllm#39004: [Perf]: ~23% output throughput regression on Qwen3.5-397B NVFP4 decode (8×B200) over the last 10 days

| 字段 | 值 |
| --- | --- |
| Issue | [#39004](https://github.com/vllm-project/vllm/issues/39004) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | moe |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Perf]: ~23% output throughput regression on Qwen3.5-397B NVFP4 decode (8×B200) over the last 10 days

### Issue 正文摘录

## Summary Output token throughput for `nvidia/Qwen3.5-397B-A17B-NVFP4` with `-dp 8 -ep` on 8×B200 has regressed **from ~47,200 tok/s to ~38,300 tok/s (−19%)** between March 28 and April 4. Three distinct regression steps are visible: | Window | Throughput drop | Magnitude | |--------|----------------|-----------| | Mar 28 → Mar 29 | 47,227 → 44,647 | −5.5% | | Mar 29 → Mar 30 | 44,647 → 39,347 | −11.9% | | Mar 30 → Mar 31 | 39,347 → 38,307 | −2.6% | The flashinfer upgrade from 0.6.6 → 0.6.7 landed on Mar 30 (`b4a2f3ac3`, #38423), which coincides with the larger drop. ## Environment - **GPU**: 8× NVIDIA B200 (183 GB each) - **vLLM**: `main` branch at various commits (see table below) - **Model**: `nvidia/Qwen3.5-397B-A17B-NVFP4` - **Config**: DP=8, expert-parallel enabled, language-model-only ## How to reproduce ### Server ```bash vllm serve nvidia/Qwen3.5-397B-A17B-NVFP4 \ -dp 8 \ --enable-expert-parallel \ --language-model-only \ --reasoning-parser qwen3 \ --stream-interval=100 ``` ### Client (benchmark) Run two iterations; the second is the measurement run: ```bash vllm bench serve \ --backend vllm \ --model nvidia/Qwen3.5-397B-A17B-NVFP4 \ --endpoint /v1/completions \ --datase...

## 现有链接修复摘要

#38423 [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Perf]: ~23% output throughput regression on Qwen3.5-397B NVFP4 decode (8×B200) over the last 10 days performance ## Summary Output token throughput for `nvidia/Qwen3.5-397B-A17B-NVFP4` with `-dp 8 -ep` on 8×B200 has re...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ade from 0.6.6 → 0.6.7 landed on Mar 30 (`b4a2f3ac3`, #38423), which coincides with the larger drop. ## Environment - **GPU**: 8× NVIDIA B200 (183 GB each) - **vLLM**: `main` branch at various commits (see table below)...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Perf]: ~23% output throughput regression on Qwen3.5-397B NVFP4 decode (8×B200) over the last 10 days performance ## Summary Output token throughput for `nvidia/Qwen3.5-397B-A17B-NVFP4` with `-dp 8 -ep` on 8×B200 has re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Perf]: ~23% output throughput regression on Qwen3.5-397B NVFP4 decode (8×B200) over the last 10 days performance ## Summary Output token throughput for `nvidia/Qwen3.5-397B-A17B-NVFP4` with `-dp 8 -ep` on 8×B200 has reg...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Perf]: ~23% output throughput regression on Qwen3.5-397B NVFP4 decode (8×B200) over the last 10 days performance ## Summary Output token throughput for `nvidia/Qwen3.5-397B-A17B-NVFP4` with `-dp 8 -ep` on 8×B200 has re...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38423](https://github.com/vllm-project/vllm/pull/38423) | mentioned | 0.45 | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 | flashinfer upgrade from 0.6.6 → 0.6.7 landed on mar 30 (`b4a2f3ac3`, #38423), which coincides with the larger drop. ## environment - **gpu**: 8× nvidia b200 (183 gb each) - **vllm… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
