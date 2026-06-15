# vllm-project/vllm#2797: from vllm._C import cuda_utils raise error

| 字段 | 值 |
| --- | --- |
| Issue | [#2797](https://github.com/vllm-project/vllm/issues/2797) |
| 状态 | closed |
| 标签 |  |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> from vllm._C import cuda_utils raise error

### Issue 正文摘录

ImportError: /root/autodl-tmp/conda/envs/wslconda/lib/python3.9/site-packages/vllm/_C.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE Used these command in linux. # Install vLLM with CUDA 11.8. export VLLM_VERSION=0.2.4 export PYTHON_VERSION=39 pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu118-cp${PYTHON_VERSION}-cp${PYTHON_VERSION}-manylinux1_x86_64.whl # Re-install PyTorch with CUDA 11.8. pip uninstall torch -y pip install torch --upgrade --index-url https://download.pytorch.org/whl/cu118 # Re-install xFormers with CUDA 11.8. pip uninstall xformers -y pip install --upgrade xformers --index-url https://download.pytorch.org/whl/cu118 nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2022 NVIDIA Corporation Built on Wed_Sep_21_10:33:58_PDT_2022 Cuda compilation tools, release 11.8, V11.8.89 Build cuda_11.8.r11.8/compiler.31833905_0 Maybe the torch and xFormers version should be set?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: from vllm._C import cuda_utils raise error ImportError: /root/autodl-tmp/conda/envs/wslconda/lib/python3.9/site-packages/vllm/_C.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: llm/_C.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE Used t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: from vllm._C import cuda_utils raise error ImportError: /root/autodl-tmp/conda/envs/wslconda/lib/python3.9/site-packages/vllm/_C.cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: .cpython-39-x86_64-linux-gnu.so: undefined symbol: _ZN2at4_ops15to_dtype_layout4callERKNS_6TensorEN3c108optionalINS5_10ScalarTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE Used these c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rTypeEEENS6_INS5_6LayoutEEENS6_INS5_6DeviceEEENS6_IbEEbbNS6_INS5_12MemoryFormatEEE Used these command in linux. # Install vLLM with CUDA 11.8. export VLLM_VERSION=0.2.4 export PYTHON_VERSION=39 pip install https://githu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
