# vllm-project/vllm#20479: [Bug]: AssertionError: expected size 250112==136064, stride 5120==4096 at dim=0; expected size 5120==4096, stride 1==1 at dim=1

| 字段 | 值 |
| --- | --- |
| Issue | [#20479](https://github.com/vllm-project/vllm/issues/20479) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError: expected size 250112==136064, stride 5120==4096 at dim=0; expected size 5120==4096, stride 1==1 at dim=1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve code: `CUDA_VISIBLE_DEVICES=0 \ vllm serve $model_path \ --swap-space 32 \ --disable-log-requests \ --tensor-parallel-size 1 \ --max-model-len 4096 \ --host xx \ --port xx` After deploying the 7B model, I encounter the following error when attempting to deploy the 14B model： `ERROR 07-04 08:11:17 [core.py:390] EngineCore hit an exception: Traceback (most recent call last): ERROR 07-04 08:11:17 [core.py:390] File "/usr/local/lib/python3.11/dist-packages/vllm/v1/engine/core.py", line 378, in run_engine_core ERROR 07-04 08:11:17 [core.py:390] engine_core = EngineCoreProc(*args, **kwargs) ERROR 07-04 08:11:17 [core.py:390] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 07-04 08:11:17 [core.py:390] File "/usr/local/lib/python3.11/dist-packages/vllm/v1/engine/core.py", line 319, in __init__ ERROR 07-04 08:11:17 [core.py:390] super().__init__(vllm_config, executor_class, log_stats) ERROR 07-04 08:11:17 [core.py:390] File "/usr/local/lib/python3.11/dist-packages/vllm/v1/engine/core.py", line 71, in __init__ ERROR 07-04 08:11:17 [core.py:390] self._initialize_kv_caches(vllm_config) ERROR 07-04 08:11:17 [core.py:390] File "/usr/local/lib...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Describe the bug vllm serve code: `CUDA_VISIBLE_DEVICES=0 \ vllm serve $model_path \ --swap-space 32 \ --disable-log-requests \ --tensor-parallel-size 1 \ --max-model-len 4096 \ --host xx \ --port xx` After deploying th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: vailable_memory ERROR 07-04 08:11:17 [core.py:390] self.model_runner.profile_run() ERROR 07-04 08:11:17 [core.py:390] File "/usr/local/lib/python3.11/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 1573, in prof...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: # Your current environment ### 🐛 Describe the bug vllm serve code: `CUDA_VISIBLE_DEVICES=0 \ vllm serve $model_path \ --swap-space 32 \ --disable-log-requests \ --tensor-parallel-size 1 \ --max-model-len 4096 \ --host x...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 5120==4096 at dim=0; expected size 5120==4096, stride 1==1 at dim=1 bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve code: `CUDA_VISIBLE_DEVICES=0 \ vllm serve $model_path \ --swap-space 32 \ --d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: py:390] File "/usr/local/lib/python3.11/dist-packages/vllm/compilation/backends.py", line 608, in __call__ ERROR 07-04 08:11:17 [core.py:390] return self.compiled_graph_for_general_shape(*args) ERROR 07-04 08:11:17 [cor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
