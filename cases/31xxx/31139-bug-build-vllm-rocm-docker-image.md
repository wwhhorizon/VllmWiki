# vllm-project/vllm#31139: [Bug]: Build vllm/rocm docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#31139](https://github.com/vllm-project/vllm/issues/31139) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;quantization |
| 症状 | build_error;crash |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Build vllm/rocm docker image

### Issue 正文摘录

### Your current environment BUILD Docker ### 🐛 Describe the bug At build docker build -f docker/Dockerfile.rocm -t vllm-rocm-251222 . ``` 1257.0 /app/vllm/build/temp.linux-x86_64-cpython-312/csrc/quantization/gguf/moe_hip.cuh:702:1: warning: failed to meet occupancy target given by 'amdgpu-waves-per-eu' in '_ZL8moe_q6_KIN3c108BFloat16ELb1EEvPKvS3_PT_PKiS7_S7_iiiiiii': desired occupancy was 2, final occupancy is 1 [-Wpass-failed] 1257.0 54 warnings generated when compiling for gfx942. 1494.4 [34/37] Building HIP object CMakeFiles/_rocm_C.dir/csrc/rocm/attention.hip.o 1494.4 ninja: build stopped: subcommand failed. 1494.4 Traceback (most recent call last): 1494.4 File "/app/vllm/setup.py", line 791, in 1494.4 setup( 1494.4 File "/usr/local/lib/python3.12/dist-packages/setuptools/__init__.py", line 117, in setup 1494.4 return distutils.core.setup(**attrs) 1494.4 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 1494.4 File "/usr/local/lib/python3.12/dist-packages/setuptools/_distutils/core.py", line 186, in setup 1494.4 return run_commands(dist) 1494.4 ^^^^^^^^^^^^^^^^^^ 1494.4 File "/usr/local/lib/python3.12/dist-packages/setuptools/_distutils/core.py", line 202, in run_commands 1494.4 dist.run_comman...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Build vllm/rocm docker image bug;rocm ### Your current environment BUILD Docker ### 🐛 Describe the bug At build docker build -f docker/Dockerfile.rocm -t vllm-rocm-251222 . ``` 1257.0 /app/vllm/build/temp.linux-x...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -251222 . ``` 1257.0 /app/vllm/build/temp.linux-x86_64-cpython-312/csrc/quantization/gguf/moe_hip.cuh:702:1: warning: failed to meet occupancy target given by 'amdgpu-waves-per-eu' in '_ZL8moe_q6_KIN3c108BFloat16ELb1EEv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Build vllm/rocm docker image bug;rocm ### Your current environment BUILD Docker ### 🐛 Describe the bug At build docker build -f docker/Dockerfile.rocm -t vllm-rocm-251222 . ``` 1257.0 /app/vllm/build/temp.linux-x...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: , '.', '-j=32', '--target=_moe_C', '--target=cumem_allocator', '--target=triton_kernels', '--target=_rocm_C', '--target=_C']' returned non-zero exit status 1. ------ Dockerfile.rocm:55 ``` @tjtanaa can you check it plea...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sked questions. performance attention_kv_cache;ci_build;hardware_porting;model_support;quantization attention;quantization build_error;crash Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
