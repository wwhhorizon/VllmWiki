# vllm-project/vllm#2646: [BUG] Compile source code error for ROCM6.0

| 字段 | 值 |
| --- | --- |
| Issue | [#2646](https://github.com/vllm-project/vllm/issues/2646) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | attention;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [BUG] Compile source code error for ROCM6.0

### Issue 正文摘录

**The error maybe caused by commit** #2279 ROCM Version: 6.0 @zhaoyang-star @zhuohan123 creating build/lib.linux-x86_64-3.10 creating build/lib.linux-x86_64-3.10/vllm x86_64-linux-gnu-g++ -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -g -fwrapv -O2 -Wl,-Bsymbolic-functions -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/activation_kernels.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/attention/attention_kernels.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/cache_kernels.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/hip_utils_kernels.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/layernorm_kernels.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/pos_encoding_kernels.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/pybind.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/quantization/gptq/q_gemm.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/quantization/squeezellm/quant_hip_kernel.o -L/projects/vllm_master/venv_rocm-6.0/lib/python3.10/site-packages/torch/lib -L/opt/...

## 现有链接修复摘要

#2279 Support FP8-E5M2 KV Cache

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [BUG] Compile source code error for ROCM6.0 **The error maybe caused by commit** #2279 ROCM Version: 6.0 @zhaoyang-star @zhuohan123 creating build/lib.linux-x86_64-3.10 creating build/lib.linux-x86_64-3.10/vllm x86_64-l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 10/csrc/pybind.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/quantization/gptq/q_gemm.o /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/quantization/squeezellm/quant_hip_kernel.o -L/projects/vllm_mas...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [BUG] Compile source code error for ROCM6.0 **The error maybe caused by commit** #2279 ROCM Version: 6.0 @zhaoyang-star @zhuohan123 creating build/lib.linux-x86_64-3.10 creating build/lib.linux-x86_64-3.10/vllm x86_64-l...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: attention;quantization build_error env_dependency #2279 Support FP8-E5M2 KV Cache **The error maybe caused by commit** #2279
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: O2 -Wl,-Bsymbolic-functions -g -fwrapv -O2 -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 /projects/vllm_master/build/temp.linux-x86_64-3.10/csrc/activation_kernels.o /proje...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#2279](https://github.com/vllm-project/vllm/pull/2279) | mentioned | 0.45 | Support FP8-E5M2 KV Cache | le source code error for rocm6.0 **the error maybe caused by commit** #2279 rocm version: 6.0 @zhaoyang-star @zhuohan123 creating build/lib.linux-x86_64-3.10 creating build/l |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
