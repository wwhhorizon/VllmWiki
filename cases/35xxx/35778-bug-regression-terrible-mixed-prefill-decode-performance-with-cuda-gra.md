# vllm-project/vllm#35778: [Bug]: Regression: terrible mixed prefill-decode performance with CUDA graphs enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#35778](https://github.com/vllm-project/vllm/issues/35778) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Regression: terrible mixed prefill-decode performance with CUDA graphs enabled.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Some update between v0.11 and v0.16 made the following configuration unusable, as mixed prefill-decode performance is, who knows, about 10-100x (yes, x, not %) slower or so, spending most of (not all) the time at 0tk/s. No errors, no wrong answers, it's just terribly slow. Unfortunately, I have no idea when the issue started because v0.11 works fine and I never updated until now (as required for Qwen3.5 compatibility), and there are no Docker images older than 0.15.1 available that I could find. I'm not capable of setting up a native Linux environment, or build the older versions for source, etc., for testing at this point. A fix for v0.16 would be needed anyway for Qwen3.5 support. Issue didn't exist in v0.11. Issue happens in both the oldest available (v0.15.1) and 0.16.1rc1.dev92+gf5d1281c9 Docker Hub versions. Running on WSL2. 2x RTX 3090. Can't be a hardware/OS limitation since v0.11 still works correctly. Tests below were all with Qwen3 (to minimize changed variables), but issue is identical with Qwen3.5 in v0.16 (3.5 is even slower, in fact, but I suppose it's expected with the newer architecture). GPU is clearly underutil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ated until now (as required for Qwen3.5 compatibility), and there are no Docker images older than 0.15.1 available that I could find. I'm not capable of setting up a native Linux environment, or build the older versions...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Regression: terrible mixed prefill-decode performance with CUDA graphs enabled. bug;stale ### Your current environment ### 🐛 Describe the bug Some update between v0.11 and v0.16 made the following configuration u...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: disable-custom-all-reduce # always disabled for WSL Changing attention backend from Flashinfer to Triton makes it not even start; --enforce-eager # "fixes" it but makes performance with single request is unusable (~27tk...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Regression: terrible mixed prefill-decode performance with CUDA graphs enabled. bug;stale ### Your current environment ### 🐛 Describe the bug Some update between v0.11 and v0.16 made the following configuration u...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Describe the bug Some update between v0.11 and v0.16 made the following configuration unusable, as mixed prefill-decode performance is, who knows, about 10-100x (yes, x, not %) slower or so, spending most of (not all) t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
