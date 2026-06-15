# vllm-project/vllm#42431: [Build] DeepGEMM wheel integration: planned cleanups

| 字段 | 值 |
| --- | --- |
| Issue | [#42431](https://github.com/vllm-project/vllm/issues/42431) |
| 状态 | open |
| 标签 | feature request;keep-open |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Build] DeepGEMM wheel integration: planned cleanups

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Tracking issue for cleanups to the vendored DeepGEMM build path. Companion to upstream DeepGEMM's issue https://github.com/deepseek-ai/DeepGEMM/issues/333 ### Current state vLLM bundles DeepGEMM under `vllm/third_party/deep_gemm/` and ships a `_C.cpython-X.Y-*.so` for every CPython covered by `requires-python`, all side-by-side in the wheel. Python's loader picks the right one at import. The build is in `cmake/external_projects/deepgemm.cmake` and `tools/build_deepgemm_C.py`. This shape was settled on after the single-`_C.abi3.so` approach was tried and reverted (see #41476 / #41512); landed in #41516. ### What we'd like to clean up **1. Collapse the per-Python `_C` build down to a single `_C.abi3.so`.** Today's per-Python machinery exists because DeepGEMM's binding uses `PYBIND11_MODULE`, which inevitably links private CPython symbols (`_PyObject_GetDictPtr`, `_PyThreadState_UncheckedGet`, etc.) — so the `.so` is Python-version-coupled regardless of file naming. Two paths to fix: - **Upstream switches to `TORCH_LIBRARY` + a pytorch-shim layer** (cf. [[vllm-flash-attention/csrc/common/pytorch_shim.h](https://github.com/vllm-project/flash-att...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Build] DeepGEMM wheel integration: planned cleanups feature request;keep-open ### 🚀 The feature, motivation and pitch Tracking issue for cleanups to the vendored DeepGEMM build path. Companion to upstream DeepGEMM's iss
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nt state vLLM bundles DeepGEMM under `vllm/third_party/deep_gemm/` and ships a `_C.cpython-X.Y-*.so` for every CPython covered by `requires-python`, all side-by-side in the wheel. Python's loader picks the right one at...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: MM currently JIT-compiles its kernels at runtime, which is why we vendor CUTLASS + CCCL + DeepGEMM headers under `vllm/third_party/deep_gemm/include/`. That's several MB of wheel size and a hard runtime dependency on a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Build] DeepGEMM wheel integration: planned cleanups feature request;keep-open ### 🚀 The feature, motivation and pitch Tracking issue for cleanups to the vendored DeepGEMM build path. Companion to upstream DeepGEMM's is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Build] DeepGEMM wheel integration: planned cleanups feature request;keep-open ### 🚀 The feature, motivation and pitch Tracking issue for cleanups to the vendored DeepGEMM build path. Companion to upstream DeepGEMM's is...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
