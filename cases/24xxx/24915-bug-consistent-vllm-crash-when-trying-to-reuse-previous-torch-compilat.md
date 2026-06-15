# vllm-project/vllm#24915: [Bug]: Consistent vLLM crash when trying to reuse previous torch compilation with DeepSeek R1 on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#24915](https://github.com/vllm-project/vllm/issues/24915) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Consistent vLLM crash when trying to reuse previous torch compilation with DeepSeek R1 on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When deploying deepseek R1 in a 1p1d config with the following config for the prefill node https://github.com/smarterclayton/ig-load/blob/pd_3/config/deploy_base_deepseek_r1_ep_pd.yaml#L85, I experience a crash when I try to reuse the torch compilation cache from a previous successful startup. Scenario: 1. `VLLM_CACHE_ROOT` is set to a directory 2. The decode and prefill instances start correctly the first time 3. If prefill restarts for any reason (crash, manual restart), subsequent prefill server starts fails with the included crash below 4. If I `rm -rf $VLLM_CACHE_ROOT/torch_compile_cache`, the next startup succeeds, but subsequent prefill starts continue to fail ``` (EngineCore_DP5 pid=953) DEBUG 09-15 16:35:12 [compilation/backends.py:124] Directly load the 118-th graph for dynamic shape from inductor_standalone via handle ('artifact_shape_None_subgraph_118', '/root/.nv/ComputeCache/.vllm/torch_compile_cache/3f2fad2cbf/rank_0_5/backbone/artifact_shape_None_subgraph_118') (EngineCore_DP5 pid=953) DEBUG 09-15 16:35:12 [compilation/backends.py:124] Directly load the 119-th graph for dynamic shape from inductor_standalone via h...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: g to reuse previous torch compilation with DeepSeek R1 on B200 bug;torch.compile ### Your current environment ### 🐛 Describe the bug When deploying deepseek R1 in a 1p1d config with the following config for the prefill...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: rash when trying to reuse previous torch compilation with DeepSeek R1 on B200 bug;torch.compile ### Your current environment ### 🐛 Describe the bug When deploying deepseek R1 in a 1p1d config with the following config f...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: deploying deepseek R1 in a 1p1d config with the following config for the prefill node https://github.com/smarterclayton/ig-load/blob/pd_3/config/deploy_base_deepseek_r1_ep_pd.yaml#L85, I experience a crash when I try to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: =953) ERROR 09-15 16:35:15 [v1/engine/core.py:712] self.model_runner.profile_run() (EngineCore_DP5 pid=953) ERROR 09-15 16:35:15 [v1/engine/core.py:712] File "/app/vllm/vllm/v1/worker/gpu_model_runner.py", line 3047, in...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: to fail ``` (EngineCore_DP5 pid=953) DEBUG 09-15 16:35:12 [compilation/backends.py:124] Directly load the 118-th graph for dynamic shape from inductor_standalone via handle ('artifact_shape_None_subgraph_118', '/root/.n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
