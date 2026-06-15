# vllm-project/vllm#13515: [Bug]: Colocate example leads to errors

| 字段 | 值 |
| --- | --- |
| Issue | [#13515](https://github.com/vllm-project/vllm/issues/13515) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Colocate example leads to errors

### Issue 正文摘录

### Your current environment ![Image](https://github.com/user-attachments/assets/77e7a0e7-415f-46e9-be70-920f11c0941f) Driver Version : 525.125.06 CUDA Version : 12.0 Attached GPUs : 8 GPU 00000000:26:00.0 Product Name : NVIDIA A800-SXM4-80GB ### 🐛 Describe the bug Error message: ![Image](https://github.com/user-attachments/assets/f194bf11-9a6f-4748-a870-62a94d43851e) I tried to use a similar method to run LLM: ```python import ray from functools import cached_property from vllm import LLM from vllm.worker.worker import Worker class MyLLM(LLM): def __init__(self, *args, **kwargs): import os os.environ.pop("CUDA_VISIBLE_DEVICES", None) super().__init__(*args, **kwargs) class Runner: model_path: str = "/checkpoints/Qwen2.5-32B" data_path: str = "/data/math-train_7500.jsonl" num_gpus: int = 8 tensor_parallel_size: int = 4 num_prompts_per_iter: int = 128 num_rollouts_per_iter: int = 64 dtype: str = "bfloat16" gpu_memory_utilization: float = 0.9 def run(self): from vllm import SamplingParams sampling_params = SamplingParams(n=self.num_rollouts_per_iter) for batch in self.debug_data: futures = [] num_prompts_per_worker = len(batch) // len(self.workers) for indx, vllm_engine in enumerate...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: om/user-attachments/assets/77e7a0e7-415f-46e9-be70-920f11c0941f) Driver Version : 525.125.06 CUDA Version : 12.0 Attached GPUs : 8 GPU 00000000:26:00.0 Product Name : NVIDIA A800
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: num_prompts_per_iter: int = 128 num_rollouts_per_iter: int = 64 dtype: str = "bfloat16" gpu_memory_utilization: float = 0.9 def run(self): from vllm import SamplingParams sampling_params = SamplingParams(n=self.num_roll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: e) super().__init__(*args, **kwargs) class Runner: model_path: str = "/checkpoints/Qwen2.5-32B" data_path: str = "/data/math-train_7500.jsonl" num_gpus: int = 8 tensor_parallel_size: int = 4 num_prompts_per_iter: int =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 70-920f11c0941f) Driver Version : 525.125.06 CUDA Version : 12.0 Attached GPUs : 8 GPU 00000000:26:00.0 Product Name : NVIDIA A800-SXM4-80GB ### 🐛 Describe the bug Error messag
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: size=self.tensor_parallel_size, distributed_executor_backend="ray", gpu_memory_utilization=self.gpu_memory_utilization, enable_sleep_mode=True ) ) return workers @cached_property def token

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
