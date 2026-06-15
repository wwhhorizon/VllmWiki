# vllm-project/vllm#6934: [Bug]: MiniCPM-V-2 does not appear to have a file named preprocessor_config.json

| 字段 | 值 |
| --- | --- |
| Issue | [#6934](https://github.com/vllm-project/vllm/issues/6934) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniCPM-V-2 does not appear to have a file named preprocessor_config.json

### Issue 正文摘录

### Your current environment ```text Versions of relevant libraries:[pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] sentence-transformers==2.7.0 [pip3] torch==2.3.1 [pip3] torchvision==0.18.1 [pip3] transformers==4.43.2 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==2.3.1 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] blas 1.0 mkl [conda] mkl 2023.1.0 h6d00ec8_46342 [conda] mkl-service 2.4.0 py311h5eee18b_1 [conda] mkl_fft 1.3.6 py311ha02d727_1 [conda] mkl_random 1.2.2 py311ha02d727_1 [conda] numpy 1.24.3 py311h08b1b3b_1 [conda] numpy-base 1.24.3 py311hf175353_1 [conda] numpydoc 1.5.0 py311h06a4308_0 [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] sentence-transformers 3.0.1 pypi_0 pypi [conda] torch 2.3.1 pypi_0 pypi [conda] transformers 4.42.4 pypi_0 pypi [conda] triton 2.3.1 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.3.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3 GPU4 GPU5 GPU6 GPU7 NIC0 NIC1 NIC2 NIC3 NIC4 CPU Affinity NUMA Affinity GPU NUMA ID GPU0 X NV8 NV8 NV8 NV8 NV8 NV8 NV8 NODE PXB NODE SYS SYS 0-31,64-95 0 N/A GPU1 NV8 X NV8 NV8 NV8 NV8...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: MiniCPM-V-2 does not appear to have a file named preprocessor_config.json bug ### Your current environment ```text Versions of relevant libraries:[pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] senten...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: named preprocessor_config.json bug ### Your current environment ```text Versions of relevant libraries:[pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] sentence-transformers==2.7.0 [pip3] torch==2.3.1 [pip3]...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: conda] triton 2.3.1 pypi_0 pypi ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.3.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: GPU0 GPU1 GPU2 GPU3...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: alize_kv_caches [rank0]: self.model_executor.determine_num_available_blocks()) [rank0]: File "/mllm/yangjirui03/workspace/ThirdPartyMLLM/MiniCPM_V/offical_vllm_for_miniCPM/vllm/vllm/executor/gpu_executor.py", line 94, i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.43.2 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==2.3.1 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] blas 1.0 mkl [conda] mkl 2023.1.0 h6d00ec8_46342 [conda] mkl-service

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
