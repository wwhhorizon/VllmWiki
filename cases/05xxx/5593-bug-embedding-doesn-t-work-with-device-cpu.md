# vllm-project/vllm#5593: [Bug]: Embedding doesn't work with `device="cpu"`

| 字段 | 值 |
| --- | --- |
| Issue | [#5593](https://github.com/vllm-project/vllm/issues/5593) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Embedding doesn't work with `device="cpu"`

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 06-17 14:57:49 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node inference, please install Ray with `pip install ray`. PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version: Could not collect CMake version: version 3.29.5 Libc version: glibc-2.35 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-91-generic-x86_64-with-glibc2.35 Is CUDA available: False CUDA runtime version: 12.4.99 ``` ### 🐛 Describe the bug code is ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=0.8, top_p=0.95) # Create an LLM. llm = LLM(model="intfloat/e5-mistral-7b-instruct", device = "cpu"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ronment information... WARNING 06-17 14:57:49 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node inference, please install Ray with `pip install ray`. PyTorch version...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: with `pip install ray`. PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubuntu1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ```text The output of `python collect_env.py` Collecting environment information... WARNING 06-17 14:57:49 ray_utils.py:46] Failed to import Ray with ModuleNotFoundError("No module named 'ray'"). For multi-node inferenc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Embedding doesn't work with `device="cpu"` bug;stale ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... WARNING 06-17 14:57:49 ray_utils.py:46] Failed...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Ray with `pip install ray`. PyTorch version: 2.3.1+cpu Is debug build: False CUDA used to build PyTorch: Could not collect ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 12.3.0-1ubu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
