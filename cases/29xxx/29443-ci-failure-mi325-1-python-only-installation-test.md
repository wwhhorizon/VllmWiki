# vllm-project/vllm#29443: [CI Failure]: mi325_1: Python-only Installation Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29443](https://github.com/vllm-project/vllm/issues/29443) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_1: Python-only Installation Test

### Issue 正文摘录

### Name of failing test `bash standalone_tests/python_only_compile.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test validates **Python-only installation** of vLLM using precompiled binaries on systems without build tools. **Purpose:** Ensures users can deploy vLLM in environments lacking C/C++ compilers by leveraging precompiled wheels instead of source compilation. **Test Flow:** 1. Removes all compiler toolchains (`build-essential`) 2. Forces precompiled binary installation via `VLLM_USE_PRECOMPILED=1` 3. Injects a runtime marker into `__init__.py` to verify the Python package loads 4. Validates successful import and execution **Error Summary:** Python-only compilation test failed during setup. The script tried to restore source files with `mv src/vllm ./vllm` but the directory doesn't exist at that path. Test never reached the actual compilation validation. **Relevant Logs:** ``` + cd /vllm-workspace/ + pip3 uninstall -y vllm Found existing installation: vllm 0.11.2.dev223+g8ae654669.rocm710 Successfully uninstalled vllm-0.11.2.dev223+g8ae654669.rocm7...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [CI Failure]: mi325_1: Python-only Installation Test ci-failure ### Name of failing test `bash standalone_tests/python_only_compile.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: thon_only_compile.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This test validates **Python-only...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: stall -y vllm Found existing installation: vllm 0.11.2.dev223+g8ae654669.rocm710 Successfully uninstalled vllm-0.11.2.dev223+g8ae654669.rocm710 + mv src/vllm ./vllm mv: cannot stat 'src/vllm': No such file or directory...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ailing test `bash standalone_tests/python_only_compile.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_1: Python-only Installation Test ci-failure ### Name of failing test `bash standalone_tests/python_only_compile.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
