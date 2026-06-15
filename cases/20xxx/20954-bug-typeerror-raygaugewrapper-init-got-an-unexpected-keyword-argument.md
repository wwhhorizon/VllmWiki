# vllm-project/vllm#20954: [Bug]: TypeError: RayGaugeWrapper.__init__() got an unexpected keyword argument

| 字段 | 值 |
| --- | --- |
| Issue | [#20954](https://github.com/vllm-project/vllm/issues/20954) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: RayGaugeWrapper.__init__() got an unexpected keyword argument

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Unable to use `RayPrometheusStatLogger` ``` engine = AsyncLLM.from_engine_args( engine_args, stat_loggers=[RayPrometheusStatLogger]) ``` Root cause: Ray metric wrappers do not conform to Prometheus API (https://github.com/ray-project/ray/issues/54611) ``` base) ray@ip-10-0-107-208:~/default/work/vllm/tests/v1/metrics$ pytest -vs test_ray_metrics.py INFO 07-14 16:54:51 [__init__.py:253] Automatically detected platform cuda. ============================================================================== test session starts =============================================================================== platform linux -- Python 3.11.11, pytest-8.4.1, pluggy-1.5.0 -- /home/ray/anaconda3/bin/python cachedir: .pytest_cache rootdir: /home/ray/default/work/vllm configfile: pyproject.toml plugins: asyncio-1.0.0, anyio-3.7.1 asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function collected 1 item test_ray_metrics.py::test_engine_log_metrics_ray[16-half-distilbert/distilgpt2] 2025-07-14 16:54:53,453 INFO worker.py:1747 -- Connecting to existing Ray cluster at address: 10.0.107.208:6379... 2...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: r. View the dashboard at https://session-154ds4pw3y7x28guz2qyjlud7s.i.anyscaleuserdata-staging.com 2025-07-14 16:54:53,470 INFO packaging.py:380 -- Pushing file package 'gcs://_ray_pkg_dbd5dab942b76cf8fa61cc2ba5c5d24b8d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: dtype=dtype, disable_log_stats=False, ) engine = AsyncLLM.from_engine_args( engine_args, stat_loggers=[RayPrometheusStatLogger]) for i, prompt in enumerate(example_prompts):
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: (EngineTestActor pid=15554) INFO 07-14 16:55:05 [config.py:2380] Chunked prefill is enabled with max_num_batched_tokens=2048. FAILED ==================================================================================== F...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: dir: /home/ray/default/work/vllm configfile: pyproject.toml plugins: asyncio-1.0.0, anyio-3.7.1 asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function collected 1 it...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y INFO 07-14 16:54:51 [__init__.py:253] Automatically detected platform cuda. ============================================================================== test session starts ==========================================...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
