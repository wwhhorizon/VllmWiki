# vllm-project/vllm#35896: [Bug]: [CPU Backend] ARM build fails with distro/downstream PyTorch that does not vendor libgomp

| 字段 | 值 |
| --- | --- |
| Issue | [#35896](https://github.com/vllm-project/vllm/issues/35896) |
| 状态 | open |
| 标签 | cpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [CPU Backend] ARM build fails with distro/downstream PyTorch that does not vendor libgomp

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Building vLLM on ARM (AArch64) fails at `cmake/cpu_extension.cmake:225` when using a downstream/distro-packaged PyTorch that does not ship a vendored copy of libgomp: ``` CMake Error at cmake/cpu_extension.cmake:225 (find_library): Could not find OPEN_MP using the following names: gomp Call Stack (most recent call first): CMakeLists.txt:111 (include) ``` **Root cause:** PR #28059 (commit d44fbbab0e) introduced `vllm_prepare_torch_gomp_shim()` in `cmake/utils.cmake` which searches for a vendored `libgomp*.so*` inside `torch.libs/` or `torch/lib/`. The result is then used in `cpu_extension.cmake` with `find_library(OPEN_MP NAMES gomp PATHS ${VLLM_TORCH_GOMP_SHIM_DIR} NO_DEFAULT_PATH REQUIRED)`. The `NO_DEFAULT_PATH` flag prevents CMake from falling back to system library paths. This works fine with upstream manylinux PyTorch wheels (which bundle libgomp), but fails with distro/downstream PyTorch builds (e.g. Red Hat, Fedora, s390x) that link against the system's `/lib64/libgomp.so.1` from GCC and do not ship a vendored copy. This is different from #30470 (fixed by #30481), which was about PyTorch *nightly* changing the vendored lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: [CPU Backend] ARM build fails with distro/downstream PyTorch that does not vendor libgomp cpu ### Your current environment ### 🐛 Describe the bug Building vLLM on ARM (AArch64) fails at `cmake/cpu_extension.cmake...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: [CPU Backend] ARM build fails with distro/downstream PyTorch that does not vendor libgomp cpu ### Your current environment ### 🐛 Describe the bug Building vLLM on ARM (AArch64) fails at `cmake/cpu_extension.cmake...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r current environment ### 🐛 Describe the bug Building vLLM on ARM (AArch64) fails at `cmake/cpu_extension.cmake:225` when using a downstream/distro-packaged PyTorch that does not ship a vendored copy of libgomp: ``` CMa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
