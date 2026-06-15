# vllm-project/vllm#27409: [New Model]: ibm-granite/granite-4.0-h-small-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#27409](https://github.com/vllm-project/vllm/issues/27409) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;fp8;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [New Model]: ibm-granite/granite-4.0-h-small-FP8

### Issue 正文摘录

### The model to consider. https://huggingface.co/ibm-granite/granite-4.0-h-small-FP8 ### The closest model vllm already supports. RedHatAI/Qwen3-30B-A3B-quantized.w4a16 ### What's your difficulty of supporting the model you want? I have 2 rtx3090 connected over Connectx-3 with ray. I am also using a cuda compute version 8.6 build. ``` (EngineCore_DP0 pid=479) (RayWorkerWrapper pid=571) INFO 10-23 03:54:45 [pynccl.py:111] vLLM is using nccl==2.27.3 (EngineCore_DP0 pid=479) (RayWorkerWrapper pid=223, ip=192.168.141.7) INFO 10-23 03:54:46 [parallel_state.py:1325] rank 1 in world size 2 is assigned as DP rank 0, PP rank 1, TP rank 0, EP rank 0 (EngineCore_DP0 pid=479) (RayWorkerWrapper pid=223, ip=192.168.141.7) INFO 10-23 03:54:46 [gpu_model_runner.py:2860] Starting to load model ibm-granite/granite-4.0-h-small-FP8... (EngineCore_DP0 pid=479) (RayWorkerWrapper pid=571) INFO 10-23 03:54:46 [cuda.py:403] Using Flash Attention backend on V1 engine. (EngineCore_DP0 pid=479) (RayWorkerWrapper pid=223, ip=192.168.141.7) INFO 10-23 03:54:55 [weight_utils.py:419] Using model weights format ['*.safetensors'] (EngineCore_DP0 pid=479) (RayWorkerWrapper pid=571) [Gloo] Rank 0 is connected to 0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [New Model]: ibm-granite/granite-4.0-h-small-FP8 new-model;stale ### The model to consider. https://huggingface.co/ibm-granite/granite-4.0-h-small-FP8 ### The closest model vllm already supports. RedHatAI/Qwen3-30B-A3B-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [New Model]: ibm-granite/granite-4.0-h-small-FP8 new-model;stale ### The model to consider. https://huggingface.co/ibm-granite/granite-4.0-h-small-FP8 ### The closest model vllm already supports. RedHatAI/Qwen3-30B-A3B-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [New Model]: ibm-granite/granite-4.0-h-small-FP8 new-model;stale ### The model to consider. https://huggingface.co/ibm-granite/granite-4.0-h-small-FP8 ### The closest model vllm already supports. RedHatAI/Qwen3-30B-A3B-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: =479) (RayWorkerWrapper pid=571) INFO 10-23 03:54:46 [cuda.py:403] Using Flash Attention backend on V1 engine. (EngineCore_DP0 pid=479) (RayWorkerWrapper pid=223, ip=192.168.141.7) INFO 10-23 03:54:55 [weight_utils.py:4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: x3090 connected over Connectx-3 with ray. I am also using a cuda compute version 8.6 build. ``` (EngineCore_DP0 pid=479) (RayWorkerWrapper pid=571) INFO 10-23 03:54:45 [pynccl.py:111] vLLM is using nccl==2.27.3 (EngineC...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
