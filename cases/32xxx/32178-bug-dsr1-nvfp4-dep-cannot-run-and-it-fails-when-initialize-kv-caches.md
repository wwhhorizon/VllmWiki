# vllm-project/vllm#32178: [Bug]: DSR1 NVFP4 DEP cannot run and it fails when _initialize_kv_caches

| 字段 | 值 |
| --- | --- |
| Issue | [#32178](https://github.com/vllm-project/vllm/issues/32178) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;moe |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DSR1 NVFP4 DEP cannot run and it fails when _initialize_kv_caches

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug B200 DEP8 cannot run. GB200 DEP4 cannot run. Error message: [0;36m(EngineCore_DP0 pid=718378)[0;0m INFO 01-09 09:11:11 [backends.py:278] Compiling a graph for compile range (1, 8192) takes 43.38 s [0;36m(EngineCore_DP0 pid=718378)[0;0m INFO 01-09 09:11:11 [monitor.py:34] torch.compile takes 51.55 s in total [0;36m(EngineCore_DP2 pid=718380)[0;0m INFO 01-09 09:11:11 [backends.py:261] Cache the graph of compile range (1, 8192) for later use [0;36m(EngineCore_DP6 pid=718384)[0;0m ERROR 01-09 09:11:11 [core.py:1018] EngineCore failed to start. [0;36m(EngineCore_DP6 pid=718384)[0;0m ERROR 01-09 09:11:11 [core.py:1018] Traceback (most recent call last): [0;36m(EngineCore_DP6 pid=718384)[0;0m ERROR 01-09 09:11:11 [core.py:1018] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 1001, in run_engine_core [0;36m(EngineCore_DP6 pid=718384)[0;0m ERROR 01-09 09:11:11 [core.py:1018] engine_core = DPEngineCoreProc(*args, **kwargs) [0;36m(EngineCore_DP6 pid=718384)[0;0m ERROR 01-09 09:11:11 [core.py:1018] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [0;36m(EngineCore_DP6 pid=718384)[0;0m ERROR 01-09 09:11:11 [core...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: DSR1 NVFP4 DEP cannot run and it fails when _initialize_kv_caches bug;stale ### Your current environment ### 🐛 Describe the bug B200 DEP8 cannot run. GB200 DEP4 cannot run. Error message: [0;36m(EngineCore_DP0 p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 18378)[0;0m INFO 01-09 09:11:11 [backends.py:278] Compiling a graph for compile range (1, 8192) takes 43.38 s [0;36m(EngineCore_DP0 pid=718378)[0;0m INFO 01-09 09:11:11 [monitor.py:34] torch.compile takes 51.55 s in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: =718384)[0;0m ERROR 01-09 09:11:11 [core.py:1018] self.model_runner.profile_run() [0;36m(EngineCore_DP6 pid=718384)[0;0m ERROR 01-09 09:11:11 [core.py:1018] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: aches bug;stale ### Your current environment ### 🐛 Describe the bug B200 DEP8 cannot run. GB200 DEP4 cannot run. Error message: [0;36m(EngineCore_DP0 pid=718378)[0;0m INFO 01-09 09:11:11 [backends.py:278] Compiling a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ]: DSR1 NVFP4 DEP cannot run and it fails when _initialize_kv_caches bug;stale ### Your current environment ### 🐛 Describe the bug B200 DEP8 cannot run. GB200 DEP4 cannot run. Error message: [0;36m(EngineCore_DP0 pid=7...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
