# vllm-project/vllm#1539: New Dockerfile build error

| 字段 | 值 |
| --- | --- |
| Issue | [#1539](https://github.com/vllm-project/vllm/issues/1539) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> New Dockerfile build error

### Issue 正文摘录

Hello trying to build the new pushed Dockerfile I get the following error: Command executed with docker 20.10.23 version (under Windows 10), the processes are progressively Killed. ` set DOCKER_BUILDKIT=1 docker build . --target vllm --tag vllm --build-arg max_jobs=8 ` ``` log 606.0 606.0 /workspace/csrc/quantization/awq/gemm_kernels.cu(277): warning #177-D: variable "blockIdx_x" was declared but never referenced 606.0 606.0 /workspace/csrc/quantization/awq/gemm_kernels.cu(291): warning #177-D: variable "ld_zero_flag" was declared but never referenced 606.0 606.0 /usr/local/lib/python3.10/dist-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero 606.0 detected during: 606.0 instantiation of "__nv_bool c10::detail::integer_iterator >::operator==(const c10::detail::integer_iterator > &) const [with I=size_t, one_sided=false, =0]" 606.0 (61): here 606.0 instantiation of "__nv_bool c10::detail::integer_iterator >::operator!=(const c10::detail::integer_iterator > &) const [with I=size_t, one_sided=false, =0]" 606.0 /usr/local/lib/python3.10/dist-packages/torch/include/c10/core/TensorImpl.h(77): here 606.0 606.0 /usr/local/lib/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: New Dockerfile build error Hello trying to build the new pushed Dockerfile I get the following error: Command executed with docker 20.10.23 version (under Windows 10), the processes are progressively Killed. ` set DOCKE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --tag vllm --build-arg max_jobs=8 ` ``` log 606.0 606.0 /workspace/csrc/quantization/awq/gemm_kernels.cu(277): warning #177-D: variable "blockIdx_x" was declared but never referenced 606.0 606.0 /workspace/csrc/quantiza...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ck_half2" was declared but never referenced 606.0 625.3 [3/3] /usr/local/cuda/bin/nvcc -I/usr/local/lib/python3.10/dist-packages/torch/include -I/usr/local/lib/python3.10/dist-packages/torch/include/torch/csrc/api/inclu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ce/csrc/quantization/awq/gemm_kernels.cu(277): warning #177-D: variable "blockIdx_x" was declared but never referenced 606.0 606.0 /workspace/csrc/quantization/awq/gemm_kernels.cu(291): warning #177-D: variable "ld_zero...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: d-arg max_jobs=8 ` ``` log 606.0 606.0 /workspace/csrc/quantization/awq/gemm_kernels.cu(277): warning #177-D: variable "blockIdx_x" was declared but never referenced 606.0 606.0 /workspace/csrc/quantization/awq/gemm_ker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
