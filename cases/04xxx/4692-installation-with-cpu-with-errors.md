# vllm-project/vllm#4692: Installation with CPU with errors

| 字段 | 值 |
| --- | --- |
| Issue | [#4692](https://github.com/vllm-project/vllm/issues/4692) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Installation with CPU with errors

### Issue 正文摘录

### Your current environment Following the instruction @ https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html and execute the section "Quick start using Dockerfile" for: `docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g .` and, received errors with the following logs: ``` VLLM_TARGET_DEVICE=cpu python3 setup.py install running install /usr/lib/python3/dist-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools. warnings.warn( /usr/lib/python3/dist-packages/setuptools/command/easy_install.py:158: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools. warnings.warn( running bdist_egg running egg_info writing vllm.egg-info/PKG-INFO writing dependency_links to vllm.egg-info/dependency_links.txt writing requirements to vllm.egg-info/requires.txt writing top-level names to vllm.egg-info/top_level.txt reading manifest file 'vllm.egg-info/SOURCES.txt' reading manifest template 'MANIFEST.in' adding license file 'LICENSE' writing manifest file 'vllm.egg-info/SOURCES.txt' installing library code to build...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Installation with CPU with errors installation ### Your current environment Following the instruction @ https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html and execute the section "Quick start using Doc
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: CMake Error at cmake/cpu_extension.cmake:57 (message): vLLM CPU backend requires AVX512 ISA support. Call Stack (most recent call first): CMakeLists.txt:88 (include) -- Configuring incomplete, errors occurred! Traceback...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: UT_DIRECTORY=/workspace/vllm/build/lib.linux-x86_64-3.10/vllm', '-DCMAKE_ARCHIVE_OUTPUT_DIRECTORY=build/temp.linux-x86_64-3.10', '-DVLLM_TARGET_DEVICE=cpu', '-DVLLM_PYTHON_EXECUTABLE=/usr/bin/python3', '-DCMAKE_JOB_POOL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: at /usr/local/lib/python3.10/dist-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message): static library kineto_LIBRARY-NOTFOUND not found. Call Stack (most recent call first): /usr/local/lib/python3.10/dist-pa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rrent environment Following the instruction @ https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html and execute the section "Quick start using Dockerfile" for: `docker build -f Dockerfile.cpu -t vllm-cpu-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
