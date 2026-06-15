# vllm-project/vllm#43086: [CI Failure]: [Kernels (B200)

| 字段 | 值 |
| --- | --- |
| Issue | [#43086](https://github.com/vllm-project/vllm/issues/43086) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | kernel;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: [Kernels (B200)

### Issue 正文摘录

### Name of failing test `tests/models/quantization/test_nvfp4.py::test_nvfp4[flashinfer_trtllm-True-nvidia/Llama-3.1-8B-Instruct-NVFP4] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test [url](https://buildkite.com/vllm/ci/builds/66835/list?sid=019e3ed4-2546-4324-88d2-38d6305b8f60&tab=output) ``` =========================================================================== FAILURES =========================================================================== ____________________________________________ test_nvfp4[flashinfer_trtllm-True-nvidia/Llama-3.1-8B-Instruct-NVFP4] _____________________________________________ vllm_runner = , model = 'nvidia/Llama-3.1-8B-Instruct-NVFP4', eager = True, backend = 'flashinfer_trtllm' @pytest.mark.parametrize("model", ["nvidia/Llama-3.1-8B-Instruct-NVFP4"]) @pytest.mark.parametrize("eager", EAGER) @pytest.mark.parametrize( "backend", [ "emulation", "flashinfer_cudnn", "flashinfer_trtllm", # the small seq_len ensures trtllm_8x4_layout backend is used "flashinfer_cutlass", ], ) def test_nvfp4(vllm_runner, model, eager, backend): if ( not cu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [CI Failure]: [Kernels (B200) ci-failure ### Name of failing test `tests/models/quantization/test_nvfp4.py::test_nvfp4[flashinfer_trtllm-True-nvidia/Llama-3.1-8B-Instruct-NVFP4] ### Basic information - [ ] Flaky test
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [CI Failure]: [Kernels (B200) ci-failure ### Name of failing test `tests/models/quantization/test_nvfp4.py::test_nvfp4[flashinfer_trtllm-True-nvidia/Llama-3.1-8B-Instruct-NVFP4] ### Basic information - [ ] Flaky test -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: CI Failure]: [Kernels (B200) ci-failure ### Name of failing test `tests/models/quantization/test_nvfp4.py::test_nvfp4[flashinfer_trtllm-True-nvidia/Llama-3.1-8B-Instruct-NVFP4] ### Basic information - [ ] Flaky test - [...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: me of failing test `tests/models/quantization/test_nvfp4.py::test_nvfp4[flashinfer_trtllm-True-nvidia/Llama-3.1-8B-Instruct-NVFP4] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by exter...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ure]: [Kernels (B200) ci-failure ### Name of failing test `tests/models/quantization/test_nvfp4.py::test_nvfp4[flashinfer_trtllm-True-nvidia/Llama-3.1-8B-Instruct-NVFP4] ### Basic information - [ ] Flaky test - [ ] Can...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
