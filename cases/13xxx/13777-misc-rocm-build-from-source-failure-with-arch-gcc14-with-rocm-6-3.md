# vllm-project/vllm#13777: [Misc] [ROCm]: Build from source failure with Arch/gcc14 with ROCm 6.3

| 字段 | 值 |
| --- | --- |
| Issue | [#13777](https://github.com/vllm-project/vllm/issues/13777) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 | build_fail |
| Operator 关键词 | quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc] [ROCm]: Build from source failure with Arch/gcc14 with ROCm 6.3

### Issue 正文摘录

### Anything you want to discuss about vllm. Hi team! Been trying to build vllm from source for ROCm 6.3 for gfx1100 on Arch/gcc14 following the instructions from the official documentation. Kept running into a compile error on the hipify step during the build:- Excerpt from error - ``` ... In file included from :1: In file included from /opt/rocm/lib/llvm/lib/clang/18/include/__clang_hip_runtime_wrapper.h:145: In file included from /opt/rocm/lib/llvm/lib/clang/18/include/cuda_wrappers/algorithm:55: In file included from /usr/lib64/gcc/x86_64-pc-linux-gnu/14.2.1/../../../../include/c++/14.2.1/algorithm:61: /usr/lib64/gcc/x86_64-pc-linux-gnu/14.2.1/../../../../include/c++/14.2.1/bits/stl_algo.h:3626:7: error: reference to __host__ function '__glibcxx_assert_fail' in __host__ __device__ function 3626 | __glibcxx_assert(!(__hi /Documents/sources/vllm/build/temp.linux-x86_64-cpython-312/csrc/quantization/compressed_tensors/int8_quant_kernels.hip:35:14: note: called by 'float_to_int8_rn' 35 | dst = std::clamp(dst, i8_min, i8_max); | ^ /home/ /Documents/sources/vllm/build/temp.linux-x86_64-cpython-312/csrc/quantization/compressed_tensors/int8_quant_kernels.hip:119:14: note: called by 's...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Misc] [ROCm]: Build from source failure with Arch/gcc14 with ROCm 6.3 stale ### Anything you want to discuss about vllm. Hi team! Been trying to build vllm from source for ROCm 6.3 for gfx1100 on Arch/gcc14 following t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Misc] [ROCm]: Build from source failure with Arch/gcc14 with ROCm 6.3 stale ### Anything you want to discuss about vllm. Hi team! Been trying to build vllm from source for ROCm 6.3 for gfx1100 on Arch/gcc14 following t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: !(__hi /Documents/sources/vllm/build/temp.linux-x86_64-cpython-312/csrc/quantization/compressed_tensors/int8_quant_kernels.hip:35:14: note: called by 'float_to_int8_rn' 35 | dst = std::clamp(dst, i8_min, i8_max); | ^ /h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ux-gnu/14.2.1/../../../../include/c++/14.2.1/x86_64-pc-linux-gnu/bits/c++config.h:608:3: note: '__glibcxx_assert_fail' declared here 608 | __glibcxx_assert_fail() | ^ 1 error generated when compiling for gfx1100. ... ``...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc] [ROCm]: Build from source failure with Arch/gcc14 with ROCm 6.3 stale ### Anything you want to discuss about vllm. Hi team! Been trying to build vllm from source for ROCm 6.3 for gfx1100 on Arch/gcc14 following t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
