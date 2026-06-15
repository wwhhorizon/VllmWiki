# vllm-project/vllm#15702: [Bug]: Engine crash periodically running Deepseek V3/R1 on Hopper GPUs in cutlass_scaled_mm_sm90()

| 字段 | 值 |
| --- | --- |
| Issue | [#15702](https://github.com/vllm-project/vllm/issues/15702) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Engine crash periodically running Deepseek V3/R1 on Hopper GPUs in cutlass_scaled_mm_sm90()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running DeepSeek V3 I experience periodic engine crashes (on average once per hour). This is on both vllm=0.8.0 and 0.8.1 and across different nodes. ```:actor_name:RayWorkerWrapper *** SIGFPE received at time=1743161210 on cpu 58 *** PC: @ 0x7f779811d273 (unknown) cutlass_scaled_mm_sm90() @ 0x7fa7e4207520 (unknown) (unknown) @ 0x1 1091664832 (unknown) @ 0x100000002 1810073080 (unknown) @ 0x7fa7bc3464e0 (unknown) (unknown) @ 0xec8348fb89485355 (unknown) (unknown) [2025-03-28 04:26:50,799 E 714 714] logging.cc:484: *** SIGFPE received at time=1743161210 on cpu 58 *** [2025-03-28 04:26:50,799 E 714 714] logging.cc:484: PC: @ 0x7f779811d273 (unknown) cutlass_scaled_mm_sm90() [2025-03-28 04:26:50,800 E 714 714] logging.cc:484: @ 0x7fa7e4207520 (unknown) (unknown) [2025-03-28 04:26:50,801 E 714 714] logging.cc:484: @ 0x1 1091664832 (unknown) [2025-03-28 04:26:50,803 E 714 714] logging.cc:484: @ 0x100000002 1810073080 (unknown) [2025-03-28 04:26:50,804 E 714 714] logging.cc:484: @ 0x7fa7bc3464e0 (unknown) (unknown) [2025-03-28 04:26:50,805 E 714 714] logging.cc:484: @ 0xec8348fb89485355 (unknown) (unknown) Fatal Python error: Floa...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: gine crash periodically running Deepseek V3/R1 on Hopper GPUs in cutlass_scaled_mm_sm90() bug;stale ### Your current environment ### 🐛 Describe the bug When running DeepSeek V3 I experience periodic engine crashes (on a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: Bug]: Engine crash periodically running Deepseek V3/R1 on Hopper GPUs in cutlass_scaled_mm_sm90() bug;stale ### Your current environment ### 🐛 Describe the bug When running DeepSeek V3 I experience periodic engine crash...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: b5f4ef33b133782fc2f638ce904b553c/lib/python3.9/site-packages/ray/util/tracing/tracing_helper.py", line 463 in _resume_span File "/tmp/ray/session_2025-03-24_09-51-24_612662_7/runtime_resources/conda/c509cf0bb5f4ef33b133...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Engine crash periodically running Deepseek V3/R1 on Hopper GPUs in cutlass_scaled_mm_sm90() bug;stale ### Your current environment ### 🐛 Describe the bug When running DeepSeek V3 I experience periodic engine cras...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ly running Deepseek V3/R1 on Hopper GPUs in cutlass_scaled_mm_sm90() bug;stale ### Your current environment ### 🐛 Describe the bug When running DeepSeek V3 I experience periodic engine crashes (on average once per hour)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
