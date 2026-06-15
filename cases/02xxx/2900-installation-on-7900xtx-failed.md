# vllm-project/vllm#2900: Installation on 7900XTX failed

| 字段 | 值 |
| --- | --- |
| Issue | [#2900](https://github.com/vllm-project/vllm/issues/2900) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;quantization |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;operator;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Installation on 7900XTX failed

### Issue 正文摘录

# From source installation failed ## System information - OS: Ubuntu 23.10 - CPU: Intel 13700K - GPU: AMD Radeon 7900XTX - Python: 3.11.6 - PyTorch: 2.2.0+rocm5.7 - ROCm: 6.0.0 ## Steps to reproduce `python setup.py install` It's tested that whether `flash-attention`, `xformers` are installed doesn't matter. Part of the error message: ```shell running bdist_egg running egg_info writing vllm.egg-info/PKG-INFO writing dependency_links to vllm.egg-info/dependency_links.txt writing requirements to vllm.egg-info/requires.txt writing top-level names to vllm.egg-info/top_level.txt reading manifest file 'vllm.egg-info/SOURCES.txt' reading manifest template 'MANIFEST.in' adding license file 'LICENSE' writing manifest file 'vllm.egg-info/SOURCES.txt' installing library code to build/bdist.linux-x86_64/egg running install_lib running build_py running build_ext building 'vllm._C' extension Emitting ninja build file /home/orion/repo/vllm/build/temp.linux-x86_64-cpython-311/build.ninja... Compiling objects... Allowing ninja to set a default number of workers... (overridable by setting the environment variable MAX_JOBS=N) ninja: no work to do. x86_64-linux-gnu-g++ -shared -Wl,-O1 -Wl,-Bsymbolic-...

## 现有链接修复摘要

#36486 [Bugfix] Fix issues in quark emulative logic

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: /pybind.o /home/orion/repo/vllm/build/temp.linux-x86_64-cpython-311/csrc/quantization/gptq/q_gemm.o /home/orion/repo/vllm/build/temp.linux-x86_64-cpython-311/csrc/quantization/squeezellm/quant_hip_kernel.o -L/home/orion...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Installation on 7900XTX failed # From source installation failed ## System information - OS: Ubuntu 23.10 - CPU: Intel 13700K - GPU: AMD Radeon 7900XTX - Python: 3.11.6 - PyTorch: 2.2.0+rocm5.7 - ROCm: 6.0.0 ## Steps
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Intel 13700K - GPU: AMD Radeon 7900XTX - Python: 3.11.6 - PyTorch: 2.2.0+rocm5.7 - ROCm: 6.0.0 ## Steps to reproduce `python setup.py install` It's tested that whether `flash-attention`, `xformers` are installed doesn't...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: kernels.o /home/orion/repo/vllm/build/temp.linux-x86_64-cpython-311/csrc/moe_align_block_size_kernels.o /home/orion/repo/vllm/build/temp.linux-x86_64-cpython-311/csrc/pos_encoding_kernels.o /home/orion/repo/vllm/build/t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: csrc/hip_compat.h [skipped, already hipified] /home/orion/repo/vllm/csrc/dispatch_utils.h -> /home/orion/repo/vllm/csrc/dispatch_utils.h [skipped, no changes] /home/orion/repo/vllm/csrc/attention/attention_generic.cuh -...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36486](https://github.com/vllm-project/vllm/pull/36486) | closes_keyword | 0.95 | [Bugfix] Fix issues in quark emulative logic | Fix issues in quark emulative logic ## Issue When running the model with **AITER disabled**, the **emulation path does not take effect**. This issue was introduced by PR: [#2900 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
