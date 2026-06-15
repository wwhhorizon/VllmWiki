# vllm-project/vllm#5107: [Misc]: Loading microsoft/Phi-3-medium-128k-instruct with vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#5107](https://github.com/vllm-project/vllm/issues/5107) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Loading microsoft/Phi-3-medium-128k-instruct with vLLM

### Issue 正文摘录

### Anything you want to discuss about vllm. i am using an NVIDIA A100 80GB MIG 3g.40gb slice to deploy microsoft/Phi-3-medium-128k-instruct (~26gb) using vllm. However, i keep running into OOM issues. here is how i am initializing the model: engine_args = AsyncEngineArgs( model="microsoft/Phi-3-medium-128k-instruct", gpu_memory_utilization=0.8, dtype=torch.float16, enforce_eager=True, trust_remote_code=True ) loaded_llm = AsyncLLMEngine.from_engine_args(engine_args) and this is the error: RuntimeError: NVML_SUCCESS == r INTERNAL ASSERT FAILED at "../c10/cuda/CUDACachingAllocator.cpp":844, please report a bug to PyTorch. any suggestions on what parameters to tweak to make this model fit in my 40g mig slice?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: odel="microsoft/Phi-3-medium-128k-instruct", gpu_memory_utilization=0.8, dtype=torch.float16, enforce_eager=True, trust_remote_code=True ) loaded_llm = AsyncLLMEngine.from_engine_args(engine_args) and this is the error:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: vLLM ### Anything you want to discuss about vllm. i am using an NVIDIA A100 80GB MIG 3g.40gb slice to deploy microsoft/Phi-3-medium-128k-instruct (~26gb) using vllm. However, i keep running into OOM issues. here is how...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: el fit in my 40g mig slice? performance model_support cuda oom dtype;env_dependency Anything you want to discuss about vllm.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: -3-medium-128k-instruct (~26gb) using vllm. However, i keep running into OOM issues. here is how i am initializing the model: engine_args = AsyncEngineArgs( model="microsoft/Phi-3-medium-128k-instruct", gpu_memory_utili...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: wever, i keep running into OOM issues. here is how i am initializing the model: engine_args = AsyncEngineArgs( model="microsoft/Phi-3-medium-128k-instruct", gpu_memory_utilization=0.8, dtype=torch.float16, enforce_eager...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
