# vllm-project/vllm#24590: [CI Failure]: CUTLASS MLA decode is flaky

| 字段 | 值 |
| --- | --- |
| Issue | [#24590](https://github.com/vllm-project/vllm/issues/24590) |
| 状态 | closed |
| 标签 | stale;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: CUTLASS MLA decode is flaky

### Issue 正文摘录

### Name of failing test `tests/kernels/test_cutlass_mla_decode.py::test_cutlass_mla_decode[torch_dtype1-False-True-64-512-576-1-16-4096-1-128]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test FP8 cases fail CUTLASS MLA decode test ``` def cal_diff(x: torch.Tensor, y: torch.Tensor, name: str, use_fp8: bool = False) -> None: x, y = x.double(), y.double() cos_diff = 1 - 2 * (x * y).sum().item() / max( (x * x + y * y).sum().item(), 1e-12) if (use_fp8): > assert cos_diff < 1e-4 E assert 1.0 < 0.0001 ``` ### 📝 History of failing test Started to fail when I added FP8 cases in #23289 (only FP8 cases fail) https://buildkite.com/vllm/ci/builds/29987#01992f55-5a98-42e8-9589-751e26e35165 ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: CUTLASS MLA decode is flaky stale;ci-failure ### Name of failing test `tests/kernels/test_cutlass_mla_decode.py::test_cutlass_mla_decode[torch_dtype1-False-True-64-512-576-1-16-4096-1-128]` ### Basic infor
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: `tests/kernels/test_cutlass_mla_decode.py::test_cutlass_mla_decode[torch_dtype1-False-True-64-512-576-1-16-4096-1-128]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external librari...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI Failure]: CUTLASS MLA decode is flaky stale;ci-failure ### Name of failing test `tests/kernels/test_cutlass_mla_decode.py::test_cutlass_mla_decode[torch_dtype1-False-True-64-512-576-1-16-4096-1-128]` ### Basic infor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [CI Failure]: CUTLASS MLA decode is flaky stale;ci-failure ### Name of failing test `tests/kernels/test_cutlass_mla_decode.py::test_cutlass_mla_decode[torch_dtype1-False-True-64-512-576-1-16-4096-1-128]` ### Basic infor...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 576-1-16-4096-1-128]` ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test FP8 cases fail CUTLASS MLA decode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
