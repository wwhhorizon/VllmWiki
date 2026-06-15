# vllm-project/vllm#40452: [Usage]:  HunyuanImage-3.0 text-to-image fails due to expert parallel group not initialized on Ascend NPU Description

| 字段 | 值 |
| --- | --- |
| Issue | [#40452](https://github.com/vllm-project/vllm/issues/40452) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]:  HunyuanImage-3.0 text-to-image fails due to expert parallel group not initialized on Ascend NPU Description

### Issue 正文摘录

### Your current environment Hardware: Ascend NPU (8 cards, 60GB each) CANN version: 8.5.1 (V100R001C25SPC002B220) PyTorch version: 2.9.0+cpu docker image：quay.io/ascend/vllm-omni:v0.18.0 Model: Tencent-Hunyuan/HunyuanImage-3.0 (downloaded from HuggingFace/ModelScope) OS: Linux aarch64 ### How would you like to use vllm Steps to Reproduce Clone and install vLLM, vLLM-Ascend, vLLM-Omni (latest main branches). Download the model: bash git lfs clone https://huggingface.co/Tencent-Hunyuan/HunyuanImage-3.0 Run the following command (pure diffusion mode): bash vllm serve /path/to/HunyuanImage-3.0 --omni --port 8091 Or with a YAML config (stage_type: diffusion): yaml stage_args: - stage_id: 0 stage_type: "diffusion" runtime: process: true devices: "0,1,2,3,4,5,6,7" engine_args: trust_remote_code: true enforce_eager: true model: /path/to/HunyuanImage-3.0 max_num_seqs: 1 gpu_memory_utilization: 0.9 tensor_parallel_size: 8 final_output: true final_output_type: image Then run: bash vllm serve /path/to/HunyuanImage-3.0 --omni --port 8091 --stage-configs-path config.yaml Expected Behavior The service starts successfully and the /v1/images/generations endpoint works. Actual Behavior The service...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment Hardware: Ascend NPU (8 cards, 60GB each) CANN version: 8.5.1 (V100R001C25SPC002B220) PyTorch version: 2.9.0+cpu docker image：quay.io/ascend/vllm-omni:v0.18.0 Model: Tencent-Hunyuan/HunyuanImage...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: PyTorch version: 2.9.0+cpu docker image：quay.io/ascend/vllm-omni:v0.18.0 Model: Tencent-Hunyuan/HunyuanImage-3.0 (downloaded from HuggingFace/ModelScope) OS: Linux aarch64 ### How would you like to use vllm Steps to Rep...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Usage]: HunyuanImage-3.0 text-to-image fails due to expert parallel group not initialized on Ascend NPU Description usage ### Your current environment Hardware: Ascend NPU (8 cards, 60GB each) CANN version: 8.5.1 (V100...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ing to manually create _WORLD and _EP in parallel_state.py. Error 4: No backend type associated with device type npu (after creating dummy EP group) text RuntimeError: No backend type associated with device type npu Err...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: elScope) OS: Linux aarch64 ### How would you like to use vllm Steps to Reproduce Clone and install vLLM, vLLM-Ascend, vLLM-Omni (latest main branches). Download the model: bash git lfs clone https://huggingface.co/Tence...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
