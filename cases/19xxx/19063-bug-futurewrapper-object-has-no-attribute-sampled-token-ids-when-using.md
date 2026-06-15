# vllm-project/vllm#19063: [Bug]: 'FutureWrapper' object has no attribute 'sampled_token_ids' when using ray to perform pipeline parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#19063](https://github.com/vllm-project/vllm/issues/19063) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'FutureWrapper' object has no attribute 'sampled_token_ids' when using ray to perform pipeline parallelism

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran the first test function in vllm/tests/v1/engine/test_engine_core.py, and modified the EngineArgs by adding the parameters pipeline_parallel_size=2 and distributed_executor_backend='ray'. However, the error message shows that FutureWrapper has no attribute sampled_token_ids. At the same time, I modified the update_from_output method of the Scheduler class in vllm/v1/core/sched/scheduler.py, trying to extract result from model_runner_output, but this did not solve the problem. When running the test code, I encountered another error: 'ModelRunnerOutput' object has no attribute 'finished_req_ids'. It seems like somewhere inside Ray, a SchedulerOutput was expected, but a ModelRunnerOutput was actually passed. Below, I’ve included the two error messages and the function I used from the test folder. def test_engine_core(monkeypatch: pytest.MonkeyPatch): with monkeypatch.context() as m: m.setenv("VLLM_USE_V1", "1") """Setup the EngineCore.""" engine_args = EngineArgs(model=MODEL_NAME, pipeline_parallel_size=2, distributed_executor_backend='ray') vllm_config = engine_args.create_engine_config() executor_class = Executor.get_class(vl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: data/conda_envs/sllm-store/lib/python3.10/site-packages/ray/experimental/compiled_dag_ref.py", line 150, in get return _process_return_vals(return_vals, True) File "/data/conda_envs/sllm-store/lib/python3.10/site-packag...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ampled_token_ids' when using ray to perform pipeline parallelism bug;ray;stale ### Your current environment ### 🐛 Describe the bug I ran the first test function in vllm/tests/v1/engine/test_engine_core.py, and modified...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ttribute 'sampled_token_ids' when using ray to perform pipeline parallelism bug;ray;stale ### Your current environment ### 🐛 Describe the bug I ran the first test function in vllm/tests/v1/engine/test_engine_core.py, an...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: adding the parameters pipeline_parallel_size=2 and distributed_executor_backend='ray'. However, the error message shows that FutureWrapper has no attribute sampled_token_ids. At the same time, I modified the update_from...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: class in vllm/v1/core/sched/scheduler.py, trying to extract result from model_runner_output, but this did not solve the problem. When running the test code, I encountered another error: 'ModelRunnerOutput' object has no...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
