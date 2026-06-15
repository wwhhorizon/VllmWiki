# vllm-project/vllm#19824: [Feature]: Improve startup time UX

| 字段 | 值 |
| --- | --- |
| Issue | [#19824](https://github.com/vllm-project/vllm/issues/19824) |
| 状态 | open |
| 标签 | feature request;stale;startup-ux |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;kernel;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Improve startup time UX

### Issue 正文摘录

# 🚀 The feature, motivation and pitch vLLM startup time has become a pain-point for certain use cases, like auto-scaling instances or model swapping. This leads to poor user experience or even users choosing to use `--enforce-eager`, sacrificing performance. I'm creating this parent issue to track our work on better understanding the startup time as well as the throughput tradeoffs from skipping certain steps. ## 🚧 [WIP] Startup heavy hitters (most time-consuming) 1. P2P access check 2. Weight loading 3. Dynamo tracing 4. Inductor compilation a. Additional time spent on extra compile_sizes and max-autotune 5. CUDAGraph capture 6. PTX compilation ### Other - @ywang96 mentioned LMMs take a long time generating dummy multi-modal data in the profile_run - Recent measurements from @robertgshaw2-redhat: > Llama-70B-Fp8 on TP=8. I see the following: > - ~60s to check for P2P access manually. We can disable this check with VLLM_SKIP_P2P_CHECK=1 > - ~10s to load weights --- from hot page cache > - ~15s to convert dynamo bytecode > - ~70s to run torch.compile > - ~60s to capture the cudagraphs Comment from #17280: > Furthermore the very first request after starting up vLLM takes 30-60 secon...

## 现有链接修复摘要

#17280 [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120) | #19336 [Wheel Size] Only build FA2 8.0+PTX | #34648 [Feature] Add VLLM_TRITON_AUTOTUNE with functional autotune control | #39249 [Perf] Async GPU P2P access cache precomputation to reduce startup time

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: user experience or even users choosing to use `--enforce-eager`, sacrificing performance. I'm creating this parent issue to track our work on better understanding the startup time as well as the throughput tradeoffs fro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: on a. Additional time spent on extra compile_sizes and max-autotune 5. CUDAGraph capture 6. PTX compilation ### Other - @ywang96 mentioned LMMs take a long time generating dummy multi-modal data in the profile_run - Rec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Improve startup time UX feature request;stale;startup-ux # 🚀 The feature, motivation and pitch vLLM startup time has become a pain-point for certain use cases, like auto-scaling instances or model swapping. T...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: o track our work on better understanding the startup time as well as the throughput tradeoffs from skipping certain steps. ## 🚧 [WIP] Startup heavy hitters (most time-consuming) 1. P2P access check 2. Weight loading 3....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ofile_run - Recent measurements from @robertgshaw2-redhat: > Llama-70B-Fp8 on TP=8. I see the following: > - ~60s to check for P2P access manually. We can disable this check with VLLM_SKIP_P2P_CHECK=1 > - ~10s to load w...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17280](https://github.com/vllm-project/vllm/pull/17280) | mentioned | 0.45 | [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120) | to run torch.compile > - ~60s to capture the cudagraphs comment from #17280: > furthermore the very first request after starting up vllm takes 30-60 seconds. due to #19336, we onl… |
| [#19336](https://github.com/vllm-project/vllm/pull/19336) | mentioned | 0.45 | [Wheel Size] Only build FA2 8.0+PTX | ery first request after starting up vllm takes 30-60 seconds. due to #19336, we only build fa for sm80, sm90, and ptx. on another machine, ptx is compiled dynamically. ## proposed… |
| [#34648](https://github.com/vllm-project/vllm/pull/34648) | mentioned | 0.6 | [Feature] Add VLLM_TRITON_AUTOTUNE with functional autotune control | adds seconds to minutes depending on kernel count and shape variety (#19824, #20342) 3. **Cross-run instability** — same model + same hardware can produce different results (#2638… |
| [#39249](https://github.com/vllm-project/vllm/pull/39249) | mentioned | 0.6 | [Perf] Async GPU P2P access cache precomputation to reduce startup time | Partially addresses #19824. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
