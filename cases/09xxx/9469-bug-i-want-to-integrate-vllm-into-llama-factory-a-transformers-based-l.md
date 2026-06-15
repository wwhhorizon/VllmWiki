# vllm-project/vllm#9469: [Bug]: I want to integrate vllm into LLaMA-Factory, a transformers-based LLM training framework. However, I encountered two bugs: RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method & RuntimeError: NCCL error: invalid usage (run with NCCL_DEBUG=WARN for details)

| 字段 | 值 |
| --- | --- |
| Issue | [#9469](https://github.com/vllm-project/vllm/issues/9469) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: I want to integrate vllm into LLaMA-Factory, a transformers-based LLM training framework. However, I encountered two bugs: RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method & RuntimeError: NCCL error: invalid usage (run with NCCL_DEBUG=WARN for details)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to utilize VLLM to conduct LLM inference and efficiently derive the output probability distribution for token-level knowledge distillation. To achieve this, I need to first use VLLM for inference and then use its output to train student models. For the implementation, I integrated VLLM (0.6.2) into LLaMA-Factory (0.9.0), a Transformers (4.45.0)-based LLM training framework. However, when I run my code, I encounter the following bug: After debugging for hours and searching through [issues](https://github.com/vllm-project/vllm/issues/8937), I realized that both LLaMA-Factory and Transformers are calling ```torch.cuda``` functions, such as ```torch.cuda.is_available()```, before the initialization of vllm models (```source_model = LLM(model=model_args.cwc_source_model_name_or_path, tensor_parallel_size=training_args.world_size)```), which leads to the bug. However, there are numerous calls to ```torch.cuda``` functions throughout the project, and I cannot remove all of them. :( After reading this [issue](https://github.com/vllm-project/vllm/issues/6152#issuecomment-2211709345), I set ```exp...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: escribe the bug I want to utilize VLLM to conduct LLM inference and efficiently derive the output probability distribution for token-level knowledge distillation. To achieve this, I need to first use VLLM for inference...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ork. However, I encountered two bugs: RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method & RuntimeError: NCCL error: invalid usage (run...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: I want to integrate vllm into LLaMA-Factory, a transformers-based LLM training framework. However, I encountered two bugs: RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiproce...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: or: NCCL error: invalid usage (run with NCCL_DEBUG=WARN for details) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to utilize VLLM to conduct LLM inference and...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
