# vllm-project/vllm#3309: Fail to build vllm from source for H100

| 字段 | 值 |
| --- | --- |
| Issue | [#3309](https://github.com/vllm-project/vllm/issues/3309) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Fail to build vllm from source for H100

### Issue 正文摘录

It worked if I change `NVIDIA_SUPPORTED_ARCHS` in `setup.py` to `NVIDIA_SUPPORTED_ARCHS = {"8.0", "8.6"}` ``` #10 812.2 [1/12] /usr/local/cuda/bin/nvcc -I/tmp/pip-build-env-o232h5cp/overlay/local/lib/python3.10/dist-packages/torch/include -I/tmp/pip-build-env-o232h5cp/overlay/local/lib/python3.10/dist-packages/torch/include/torch/csrc/api/include -I/tmp/pip-build-env-o232h5cp/overlay/local/lib/python3.10/dist-packages/torch/include/TH -I/tmp/pip-build-env-o232h5cp/overlay/local/lib/python3.10/dist-packages/torch/include/THC -I/usr/local/cuda/include -I/usr/include/python3.10 -c -c /home/corvo/vllm/csrc/cuda_utils_kernels.cu -o /tmp/tmp6jq49t5c.build-temp/csrc/cuda_utils_kernels.o --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O2 -std=c++17 -D_GLIBCXX_USE_CXX11_ABI=0 -gencode arch=compute_90,code=sm_90 -gencode arch=compute_90,code=compute_90 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_80,code=sm_80 --threads 8 -DENABLE_FP8_E5M2 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Fail to build vllm from source for H100 It worked if I change `NVIDIA_SUPPORTED_ARCHS` in `setup.py` to `NVIDIA_SUPPORTED_ARCHS = {"8.0", "8.6"}` ``` #10 812.2 [1/12] /usr/local/cuda/bin/nvcc -I/tmp/pip-build-env-o232h5c
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e_86,code=sm_86 -gencode arch=compute_80,code=sm_80 --threads 8 -DENABLE_FP8_E5M2 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relax...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: Fail to build vllm from source for H100 It worked if I change `NVIDIA_SUPPORTED_ARCHS` in `setup.py` to `NVIDIA_SUPPORTED_ARCHS = {"8.0", "8.6"}` ``` #10 812.2 [1/12] /usr/local/cuda/bin/nvcc -I/tmp/pip-build-env-o232h5...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -fPIC -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: e -I/usr/include/python3.10 -c -c /home/corvo/vllm/csrc/quantization/awq/gemm_kernels.cu -o /tmp/tmp6jq49t5c.build-temp/csrc/quantization/awq/gemm_kernels.o --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"''...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
