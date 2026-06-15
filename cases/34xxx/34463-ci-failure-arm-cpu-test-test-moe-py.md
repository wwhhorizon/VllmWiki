# vllm-project/vllm#34463: [CI Failure]: ARM CPU Test (test_moe.py)

| 字段 | 值 |
| --- | --- |
| Issue | [#34463](https://github.com/vllm-project/vllm/issues/34463) |
| 状态 | closed |
| 标签 | ci-failure;cpu |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: ARM CPU Test (test_moe.py)

### Issue 正文摘录

### Name of failing test `tests/kernels/moe/test_moe.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is appears to be a test infrastructure issue as the CI test fails with `ImportError: cannot import name 'TritonExperts' from 'vllm.model_executor.layers.fused_moe'` ``` ==================================== ERRORS ==================================== -- ________________ ERROR collecting tests/kernels/moe/test_moe.py ________________ ImportError while importing test module '/vllm-workspace/tests/kernels/moe/test_moe.py'. Hint: make sure your test modules/packages have valid Python names. Traceback: /opt/uv/python/cpython-3.12.12-linux-aarch64-gnu/lib/python3.12/importlib/__init__.py:90: in import_module return _bootstrap._gcd_import(name[level:], package, level) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ tests/kernels/moe/test_moe.py:21: in from tests.kernels.moe.utils import ( tests/kernels/moe/utils.py:10: in from vllm.model_executor.layers.fused_moe import ( E ImportError: cannot import name 'TritonExperts' from 'vllm.model_executor.layers.fused_moe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: ARM CPU Test (test_moe.py) ci-failure;cpu ### Name of failing test `tests/kernels/moe/test_moe.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: u ### Name of failing test `tests/kernels/moe/test_moe.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [CI Failure]: ARM CPU Test (test_moe.py) ci-failure;cpu ### Name of failing test `tests/kernels/moe/test_moe.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: cture issue as the CI test fails with `ImportError: cannot import name 'TritonExperts' from 'vllm.model_executor.layers.fused_moe'` ``` ==================================== ERRORS ==================================== --...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nels/moe/test_moe.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is appears to be a test infra...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
