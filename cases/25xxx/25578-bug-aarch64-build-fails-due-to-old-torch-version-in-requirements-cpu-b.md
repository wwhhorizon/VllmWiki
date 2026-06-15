# vllm-project/vllm#25578: [Bug]: AArch64 build fails due to old torch version in requirements/cpu-build.txt

| 字段 | 值 |
| --- | --- |
| Issue | [#25578](https://github.com/vllm-project/vllm/issues/25578) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: AArch64 build fails due to old torch version in requirements/cpu-build.txt

### Issue 正文摘录

### 🐛 Describe the bug Build Error on AArch64 due to old version of torch in `cpu-build.txt` Reproducer: ``` pip install -r vllm/requirements/cpu-build.txt VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel ``` Error: ``` [249/260] Building CXX object CMakeFiles/_C.dir/csrc/moe/dynamic_4bit_int_moe_cpu.cpp.o FAILED: [code=1] CMakeFiles/_C.dir/csrc/moe/dynamic_4bit_int_moe_cpu.cpp.o ccache /usr/bin/c++ -DARM_BF16_SUPPORT -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -I/home/fadara01/vllm-prepack-weights/vllm/csrc -I/home/fadara01/vllm-prepack-weights/vllm/.deps/onednn-src/include -I/home/fadara01/vllm-prepack-weights/vllm/.deps/onednn-build/include -I/home/fadara01/vllm-prepack-weights/vllm/.deps/onednn-src/src/../include -isystem /usr/include/python3.10 -isystem /home/fadara01/vllm-prepack-weights/venv/lib/python3.10/site-packages/torch/include -isystem /home/fadara01/vllm-prepack-weights/venv/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -Wl,-rpath,/home/fadara01/vllm-reproduce/ComputeLibrary/build/ -O2 -g -DNDEBUG -std=gnu++17 -fPIC -fopenmp -DVLLM_CPU_EXTENSION -march=armv8.2-a+bf16+do...

## 现有链接修复摘要

#23809 [fix]: add Arm 4bit fused moe support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: AArch64 build fails due to old torch version in requirements/cpu-build.txt bug ### 🐛 Describe the bug Build Error on AArch64 due to old version of torch in `cpu-build.txt` Reproducer: ``` pip install -r vllm/requ...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: C.dir/csrc/moe/dynamic_4bit_int_moe_cpu.cpp.o ccache /usr/bin/c++ -DARM_BF16_SUPPORT -DPy_LIMITED_API=3 -DTORCH_EXTENSION_NAME=_C -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -D_C_EXPORTS -I/home/fadara0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: AArch64 build fails due to old torch version in requirements/cpu-build.txt bug ### 🐛 Describe the bug Build Error on AArch64 due to old version of torch in `cpu-build.txt` Reproducer: ``` pip install -r vllm/requ...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Build Error on AArch64 due to old version of torch in `cpu-build.txt` Reproducer: ``` pip install -r vllm/requirements/cpu-build.txt VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel ``` Error: ``` [249/260] Building...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: current environment correctness ci_build;frontend_api;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling build_error;mismatch;nan_inf dtype;env_dependency #23809 [fix]: ad...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23809](https://github.com/vllm-project/vllm/pull/23809) | mentioned | 0.45 | [fix]: add Arm 4bit fused moe support | h [here](https://github.com/pytorch/pytorch/pull/145505)) and used in #23809 fix should be to update the pytorch version in `requirements/cpu-build.txt` for aarch64 to match that… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
