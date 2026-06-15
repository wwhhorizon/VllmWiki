# vllm-project/vllm#20885: [Bug] [ROCm]:  `tests/kernels/mamba/test_mamba_ssm_ssd.py::test_mamba_chunk_scan_cont_batch`: Core dump

| 字段 | 值 |
| --- | --- |
| Issue | [#20885](https://github.com/vllm-project/vllm/issues/20885) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [ROCm]:  `tests/kernels/mamba/test_mamba_ssm_ssd.py::test_mamba_chunk_scan_cont_batch`: Core dump

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `pytest -svvvv tests/kernels/mamba/test_mamba_ssm_ssd.py::test_mamba_chunk_scan_cont_batch`: Core dump Fail: ``` :0:rocdevice.cpp :2991: 1164852989842 us: Callback: Queue 0x7f56c1800000 aborting with error : HSA_STATUS_ERROR_MEMORY_APERTURE_VIOLATION: The agent attempted to access memory beyond the largest legal address. code: 0x29 Fatal Python error: Aborted File "/usr/local/lib/python3.10/dist-packages/_pytest/runner.py", line 117 in pytest_runtest_protocol File "/usr/local/lib/python3.10/dist-packages/pluggy/_callers.py", line 121 in _multicall File "/usr/local/lib/python3.10/dist-packages/pluggy/_manager.py", line 120 in _hookexec File "/usr/local/lib/python3.10/dist-packages/pluggy/_hooks.py", line 512 in __call__ File "/usr/local/lib/python3.10/dist-packages/_pytest/main.py", line 367 in pytest_runtestloop File "/usr/local/lib/python3.10/dist-packages/pluggy/_callers.py", line 121 in _multicall File "/usr/local/lib/python3.10/dist-packages/pluggy/_manager.py", line 120 in _hookexec File "/usr/local/lib/python3.10/dist-packages/pluggy/_hooks.py", line 512 in __call__ File "/usr/local/lib/python3.10/dist-packages/_pytest/main...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: y_umath, numpy.linalg._umath_linalg, torch._C, torch._C._dynamo.autograd_compiler, torch._C._dynamo.eval_frame, torch._C._dynamo.guards, torch._C._dynamo.utils, torch._C._fft, torch._C._linalg, torch._C._nest ed, torch....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug] [ROCm]: `tests/kernels/mamba/test_mamba_ssm_ssd.py::test_mamba_chunk_scan_cont_batch`: Core dump bug;stale ### Your current environment ### 🐛 Describe the bug `pytest -svvvv tests/kernels/mamba/test_mamba_ssm_ssd....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: C._nest ed, torch._C._nn, torch._C._sparse, torch._C._special, zstandard.backend_c, charset_normalizer.md, yaml._yaml, PIL._imaging, regex._regex, markupsafe._speedups, sklearn.__check_build._check_build, scipy._lib._cc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 512 in __call__ File "/usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py", line 175 in main File "/usr/local/lib/python3.10/dist-packages/_pytest/config/__init__.py", line 201 in console_main File "/usr/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: /test_mamba_ssm_ssd.py::test_mamba_chunk_scan_cont_batch`: Core dump bug;stale ### Your current environment ### 🐛 Describe the bug `pytest -svvvv tests/kernels/mamba/test_mamba_ssm_ssd.py::test_mamba_chunk_scan_cont_bat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
