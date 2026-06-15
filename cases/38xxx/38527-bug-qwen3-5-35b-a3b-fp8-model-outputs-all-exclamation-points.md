# vllm-project/vllm#38527: [Bug]: Qwen3.5-35B-A3B-FP8 model outputs all exclamation points

| 字段 | 值 |
| --- | --- |
| Issue | [#38527](https://github.com/vllm-project/vllm/issues/38527) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8 |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-35B-A3B-FP8 model outputs all exclamation points

### Issue 正文摘录

### Your current environment model download from modelscope vllm:0.18.0 ( pip install vllm ) pytorch:2.10.0+cu128 model path:/home/pc/qwen-models/qwen3_5_35B_A3B_FP8 model : Qwen/Qwen3.5-35B-A3B-FP8 nvidia-smi: NVIDIA-SMI 580.126.09 Driver Version: 580.126.09 CUDA Version: 13.0 gpu: nvidia rtx pro 6000 blackwell workstation 96G * 2 nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2025 NVIDIA Corporation Built on Tue_Dec_16_07:23:41_PM_PST_2025 Cuda compilation tools, release 13.1, V13.1.115 Build cuda_13.1.r13.1/compiler.37061995_0 start script: #!/bin/bash export VLLM_RPC_TIMEOUT=300 export NCCL_IB_DISABLE=1 export NCCL_P2P_DISABLE=0 export NCCL_DEBUG=INFO export CUDA_DEVICE_ORDER=PCI_BUS_ID export OMP_NUM_THREADS=56 export TRITON_AUTOTUNE_KCACHE_LIMIT=1000000 VENV_PATH="/home/pc/qwen-models/qwen3_5_venv/bin/activate" MODEL_PATH="/home/pc/qwen-models/qwen3_5_35B_A3B" MODEL_NAME="qwen3.5-flash" REASONING_PARSER="qwen3" TOOL_CALL_PARSER="qwen3_coder" MAX_MODEL_LEN="262144" TP_SIZE=2 GPU_UTIL=0.5 HOST="0.0.0.0" PORT=16688 SWAP_SPACE=16 API_KEY="sk-av4b3456925d4380ac44h4674952y72c" MAX_NUM_SEQS="128" LOG_DIR="/home/pc/qwen-models/log/vllm/llm" PID_FILE="/home/pc/qwen-models/q...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: current environment model download from modelscope vllm:0.18.0 ( pip install vllm ) pytorch:2.10.0+cu128 model path:/home/pc/qwen-models/qwen3_5_35B_A3B_FP8 model : Qwen/Qwen3.5-35B-A3B-FP8 nvidia-smi: NVIDIA-SMI 580.12...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: /qwen-models/qwen3_5_35B_A3B_FP8 model : Qwen/Qwen3.5-35B-A3B-FP8 nvidia-smi: NVIDIA-SMI 580.126.09 Driver Version: 580.126.09 CUDA Version: 13.0 gpu: nvidia rtx pro 6000 blackwell workstation 96G * 2 nvcc: NVIDIA (R) C...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3.5-35B-A3B-FP8 model outputs all exclamation points bug ### Your current environment model download from modelscope vllm:0.18.0 ( pip install vllm ) pytorch:2.10.0+cu128 model path:/home/pc/qwen-models/qwen3...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5-35B-A3B-FP8 model outputs all exclamation points bug ### Your current environment model download from modelscope vllm:0.18.0 ( pip install vllm ) pytorch:2.10.0+cu128 model path:/home/pc/qwen-models/qwen3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: NFO export CUDA_DEVICE_ORDER=PCI_BUS_ID export OMP_NUM_THREADS=56 export TRITON_AUTOTUNE_KCACHE_LIMIT=1000000 VENV_PATH="/home/pc/qwen-models/qwen3_5_venv/bin/activate" MODEL_PATH="/home/pc/qwen-models/qwen3_5_35B_A3B"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
