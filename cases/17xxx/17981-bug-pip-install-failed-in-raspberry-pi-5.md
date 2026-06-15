# vllm-project/vllm#17981: [Bug]: pip install failed in raspberry pi 5

| 字段 | 值 |
| --- | --- |
| Issue | [#17981](https://github.com/vllm-project/vllm/issues/17981) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: pip install failed in raspberry pi 5

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I was installing vllm on Raspberry Pi 5 with pip, but it failed with the following error: -- CPU extension compile flags: -fopenmp;-DVLLM_CPU_EXTENSION;-march=armv8.2-a+dotprod+fp16 -- Enabling C extension. -- Configuring done (2.1s) -- Generating done (0.0s) -- Build files have been written to: /tmp/pip-install-ssea1hah/vllm_9973e277d02d4e88b2b8ddcccbf51cf8/build/temp.linux-aarch64-cpython-311 [1/9] Building CXX object CMakeFiles/_C.dir/csrc/cpu/utils.cpp.o FAILED: CMakeFiles/_C.dir/csrc/cpu/utils.cpp.o /usr/bin/c++ -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -I/tmp/pip-install-ssea1hah/vllm_9973e277d02d4e88b2b8ddcccbf51cf8/csrc -isystem /usr/include/python3.11 -isystem /tmp/pip-build-env-rqaq1k06/overlay/lib/python3.11/site-packages/torch/include -isystem /tmp/pip-build-env-rqaq1k06/overlay/lib/python3.11/site-packages/torch/include/torch/csrc/api/include -O2 -g -DNDEBUG -std=gnu++17 -fPIC -fopenmp -DVLLM_CPU_EXTENSION -march=armv8.2-a+dotprod+fp16 -D_GLIBCXX_USE_CXX11_ABI=1 -MD -MT CMakeFiles/_C.dir/csrc/cpu/utils.cpp.o -MF CMakeFiles/_C.dir/csrc/cpu/ut...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: pip install failed in raspberry pi 5 bug ### Your current environment ### 🐛 Describe the bug I was installing vllm on Raspberry Pi 5 with pip, but it failed with the following error: -- CPU extension compile flag
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rocess/_in_process.py", line 251, in build_wheel return _build_backend().build_wheel(wheel_directory, config_settings, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/tmp/pip-build-env-rqaq1k06/ove...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : -- CPU extension compile flags: -fopenmp;-DVLLM_CPU_EXTENSION;-march=armv8.2-a+dotprod+fp16 -- Enabling C extension. -- Configuring done (2.1s) -- Generating done (0.0s) -- Build files have been written to: /tmp/pip-i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: int, int, int, int, int) [with scalar_t = float; int HEAD_SIZE = 32; int BLOCK_SIZE = 16]’ /tmp/pip-install-ssea1hah/vllm_9973e277d02d4e88b2b8ddcccbf51cf8/csrc/cpu/attention.cpp:413:7: required from ‘void {anonymous}::p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ON;-march=armv8.2-a+dotprod+fp16 -- Enabling C extension. -- Configuring done (2.1s) -- Generating done (0.0s) -- Build files have been written to: /tmp/pip-install-ssea1hah/vllm_9973e277d02d4e88b2b8ddcccbf51cf8/build/t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
