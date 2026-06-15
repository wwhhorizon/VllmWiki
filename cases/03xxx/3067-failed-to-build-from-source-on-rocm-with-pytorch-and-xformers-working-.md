# vllm-project/vllm#3067: Failed to build from source on ROCm (with pytorch and xformers working correctly)

| 字段 | 值 |
| --- | --- |
| Issue | [#3067](https://github.com/vllm-project/vllm/issues/3067) |
| 状态 | closed |
| 标签 | installation;rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;quantization |
| 子分类 | install |
| Operator 关键词 | attention;kernel;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Failed to build from source on ROCm (with pytorch and xformers working correctly)

### Issue 正文摘录

OS: Linux 6.6.17-1-lts HW: AMD 4650G (Renoir), gfx90c SW: torch==2.3.0.dev20240224+rocm5.7, xformers==0.0.23 (both confirmed working). Description of the issue: Following the installation guide for ROCm to build from source: ```bash Total number of replaced kernel launches: 21 running install /home/toto/tmp/testenv/lib/python3.11/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools. warnings.warn( /home/toto/tmp/testenv/lib/python3.11/site-packages/setuptools/command/easy_install.py:144: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools. warnings.warn( running bdist_egg running egg_info writing vllm.egg-info/PKG-INFO writing dependency_links to vllm.egg-info/dependency_links.txt writing requirements to vllm.egg-info/requires.txt writing top-level names to vllm.egg-info/top_level.txt reading manifest file 'vllm.egg-info/SOURCES.txt' reading manifest template 'MANIFEST.in' adding license file 'LICENSE' writing manifest file 'vllm.egg-info/SOURCES.txt' installing library code to build/bdist.linux-x86_64/egg runni...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Failed to build from source on ROCm (with pytorch and xformers working correctly) installation;rocm OS: Linux 6.6.17-1-lts HW: AMD 4650G (Renoir), gfx90c SW: torch==2.3.0.dev20240224+rocm5.7, xformers==0.0.23 (both conf...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rc/pybind.o /home/toto/tmp/vllm/build/temp.linux-x86_64-cpython-311/csrc/quantization/gptq/q_gemm.o /home/toto/tmp/vllm/build/temp.linux-x86_64-cpython-311/csrc/quantization/squeezellm/quant_hip_kernel.o -L/home/toto/tm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Failed to build from source on ROCm (with pytorch and xformers working correctly) installation;rocm OS: Linux 6.6.17-1-lts HW: AMD 4650G (Renoir), gfx90c SW: torch==2.3.0.dev20240224+rocm5.7, xformers==0.0.23 (both conf...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: m_kernels.o /home/toto/tmp/vllm/build/temp.linux-x86_64-cpython-311/csrc/moe_align_block_size_kernels.o /home/toto/tmp/vllm/build/temp.linux-x86_64-cpython-311/csrc/pos_encoding_kernels.o /home/toto/tmp/vllm/build/temp....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: o /home/toto/tmp/vllm/build/temp.linux-x86_64-cpython-311/csrc/moe_align_block_size_kernels.o /home/toto/tmp/vllm/build/temp.linux-x86_64-cpython-311/csrc/pos_encoding_kernels.o /home/toto/tmp/vllm/build/temp.linux-x86_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
