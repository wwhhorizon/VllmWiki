# vllm-project/vllm#18962: [Bug]: Deserialisation of the model is taking several minutes.

| 字段 | 值 |
| --- | --- |
| Issue | [#18962](https://github.com/vllm-project/vllm/issues/18962) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Deserialisation of the model is taking several minutes.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The deserialization of the model is taking several minutes. The performance is much worse than the normal loading of the model. Code: ``` import os import time import torch from vllm import LLM from vllm.engine.arg_utils import EngineArgs from vllm.model_executor.model_loader.tensorizer import ( TensorizerConfig, tensorize_vllm_model ) os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True" def get_tensor_parallel_size() -> int: """Auto-detect number of available GPUs for tensor parallelism.""" return torch.cuda.device_count() if torch.cuda.is_available() else 1 def serialize_vllm_model(model_id: str, save_path: str, dtype: str, max_model_len: int) -> str: tensor_parallel_size = get_tensor_parallel_size() print(f"vLLM Model Serialization Detected {tensor_parallel_size} GPU(s).") vllm_use_v1_val = os.getenv('VLLM_USE_V1') print(f"{vllm_use_v1_val=}") tensorizer_config = TensorizerConfig(tensorizer_uri=save_path) engine_args = EngineArgs( model=model_id, dtype=dtype, tensor_parallel_size=tensor_parallel_size, max_model_len=max_model_len, ) start = time.time() tensorize_vllm_model(engine_args, tensorizer_config) end = tim...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: formance is much worse than the normal loading of the model. Code: ``` import os import time import torch from vllm import LLM from vllm.engine.arg_utils import EngineArgs from vllm.model_executor.model_loader.tensorize...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ilable() else 1 def serialize_vllm_model(model_id: str, save_path: str, dtype: str, max_model_len: int) -> str: tensor_parallel_size = get_tensor_parallel_size() print(f"vLLM Model Serialization Detected {tensor_paralle...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ( TensorizerConfig, tensorize_vllm_model ) os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True" def get_tensor_parallel_size() -> int: """Auto-detect number of available GPUs for tensor parallelism.""" ret...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Deserialisation of the model is taking several minutes. bug;stale ### Your current environment ### 🐛 Describe the bug The deserialization of the model is taking several minutes. The performance is much worse than...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Deserialisation of the model is taking several minutes. bug;stale ### Your current environment ### 🐛 Describe the bug The deserialization of the model is taking several minutes. The performance is much worse than...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
