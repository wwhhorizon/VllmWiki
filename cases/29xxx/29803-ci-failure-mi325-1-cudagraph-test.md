# vllm-project/vllm#29803: [CI Failure]: mi325_1: Cudagraph test

| 字段 | 值 |
| --- | --- |
| Issue | [#29803](https://github.com/vllm-project/vllm/issues/29803) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Cudagraph test

### Issue 正文摘录

### Name of failing test `pytest -v -s v1/cudagraph/test_cudagraph_dispatch.py && pytest -v -s v1/cudagraph/test_cudagraph_mode.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Tests verify that certain `cudagraph_mode` and `CompilationMode` combinations raise exceptions when unsupported. **Failure:** `Failed: DID NOT RAISE ` The test expects `PIECEWISE` and `FULL_AND_PIECEWISE` cudagraph modes with `CompilationMode.NONE` to raise an exception, but vLLM now accepts these combinations without error. **Configuration:** - `cudagraph_mode`: `PIECEWISE`, `FULL_AND_PIECEWISE` - `compilation_mode`: `CompilationMode.NONE` - `supported`: `False` (expected to fail, but didn't) **Likely cause:** The test expectations in `combo_cases_2` for ROCm appear outdated. The validation logic may have changed to allow `PIECEWISE`/`FULL_AND_PIECEWISE` with `CompilationMode.NONE`, or ROCm backend now handles these combinations gracefully. The `supported=False` flag should likely be updated to `True` for these cases. ### 📝 History of failing test AMD-CI build Buildkite references: - 1130 #...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lure ### Name of failing test `pytest -v -s v1/cudagraph/test_cudagraph_dispatch.py && pytest -v -s v1/cudagraph/test_cudagraph_mode.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_1: Cudagraph test ci-failure ### Name of failing test `pytest -v -s v1/cudagraph/test_cudagraph_dispatch.py && pytest -v -s v1/cudagraph/test_cudagraph_mode.py` ### Basic information - [ ] Flaky tes
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: mi325_1: Cudagraph test ci-failure ### Name of failing test `pytest -v -s v1/cudagraph/test_cudagraph_dispatch.py && pytest -v -s v1/cudagraph/test_cudagraph_mode.py` ### Basic information - [ ] Flaky test...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tch.py && pytest -v -s v1/cudagraph/test_cudagraph_mode.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: st_cudagraph_mode.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Tests verify that certain `cudagra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
