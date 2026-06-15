# vllm-project/vllm#9683: [Bug]: "gettid" was not declared error when build from source for cpu with version after v0.6.1

| 字段 | 值 |
| --- | --- |
| Issue | [#9683](https://github.com/vllm-project/vllm/issues/9683) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "gettid" was not declared error when build from source for cpu with version after v0.6.1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM_TARGET_DEVICE=cpu python setup.py develop running develop /home/wwei/miniconda/envs/vllm/lib/python3.10/site-packages/setuptools/command/develop.py:41: EasyInstallDeprecationWarning: easy_install command is deprecated. !! ******************************************************************************** Please avoid running ``setup.py`` and ``easy_install``. Instead, use pypa/build, pypa/installer or other standards-based tools. See https://github.com/pypa/setuptools/issues/917 for details. ******************************************************************************** !! easy_install.initialize_options(self) /home/wwei/miniconda/envs/vllm/lib/python3.10/site-packages/setuptools/_distutils/cmd.py:66: SetuptoolsDeprecationWarning: setup.py install is deprecated. !! ******************************************************************************** Please avoid running ``setup.py`` directly. Instead, use pypa/build, pypa/installer or other standards-based tools. See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details. ****************************************************...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Bug]: "gettid" was not declared error when build from source for cpu with version after v0.6.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM_TARGET_DEVICE=cpu py...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Make Warning at cmake/cpu_extension.cmake:69 (message): Disable AVX512-BF16 ISA support, no avx512_bf16 found in local CPU flags. If cross-compilation is required, please set env VLLM_CPU_AVX512BF16=1. Call Stack (most...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lm) ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tils.cpp.o FAILED: CMakeFiles/_C.dir/csrc/cpu/utils.cpp.o /opt/rh/gcc-toolset-13/root/usr/bin/c++ -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: with version after v0.6.1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug VLLM_TARGET_DEVICE=cpu python setup.py develop running develop /home/wwei/miniconda/envs/vllm/l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
