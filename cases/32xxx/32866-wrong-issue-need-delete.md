# vllm-project/vllm#32866: wrong issue, need delete

| 字段 | 值 |
| --- | --- |
| Issue | [#32866](https://github.com/vllm-project/vllm/issues/32866) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;kernel;moe;operator;quantization;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> wrong issue, need delete

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash bash .buildkite/scripts/hardware_ci/run-cpu-test-arm.sh ``` ``` ============================= test session starts ============================== platform linux -- Python 3.12.12, pytest-9.0.2, pluggy-1.6.0 -- /opt/venv/bin/python3 cachedir: .pytest_cache hypothesis profile 'default' rootdir: /workspace plugins: shard-0.1.2, mock-3.15.1, cov-7.0.0, buildkite-test-collector-0.1.9, asyncio-1.3.0, typeguard-4.4.4, schemathesis-4.9.2, timeout-2.4.0, rerunfailures-16.1, forked-1.6.0, hypothesis-6.150.2, anyio-4.12.1 asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function collecting ... INFO 01-21 16:36:29 [scheduler.py:229] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 01-21 16:36:29 [vllm.py:618] Asynchronous scheduling is enabled. INFO 01-21 16:36:29 [vllm.py:625] Disabling NCCL for DP synchronization when using async scheduling. WARNING 01-21 16:36:29 [interface.py:598] Current platform cpu does not have '__test__' attribute. WARNING 01-21 16:36:29 [interface.py:598] Current platform cpu does not have '__bases__' attribute. WARNING 01-21 16...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: hard: tests/kernels/moe/test_moe.py::test_cpu_fused_moe_basic[silu-False-dtype0-2-8-128-128-1], tests/kernels/moe/test_moe.py::test_cpu_fused_moe_basic[silu-False-dtype0-2-8-128-128-33], tests/kernels/moe/test_moe.py::t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: u ### Your current environment ### 🐛 Describe the bug ```bash bash .buildkite/scripts/hardware_ci/run-cpu-test-arm.sh ``` ``` ============================= test session starts ============================== platform lin...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: 543 deselected / 8 selected Running 8 items in this shard: tests/kernels/moe/test_moe.py::test_cpu_fused_moe_basic[silu-False-dtype0-2-8-128-128-1], tests/kernels/moe/test_moe.py::test_cpu_fused_moe_basic[silu-False-dty...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: cio_default_test_loop_scope=function collecting ... INFO 01-21 16:36:29 [scheduler.py:229] Chunked prefill is enabled with max_num_batched_tokens=2048. INFO 01-21 16:36:29 [vllm.py:618] Asynchronous scheduling is enable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
