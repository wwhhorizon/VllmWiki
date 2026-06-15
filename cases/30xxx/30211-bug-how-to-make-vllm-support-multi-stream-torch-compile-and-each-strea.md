# vllm-project/vllm#30211: [Bug]: How to make vLLM support multi stream torch compile and each stream capture cuda graph.

| 字段 | 值 |
| --- | --- |
| Issue | [#30211](https://github.com/vllm-project/vllm/issues/30211) |
| 状态 | closed |
| 标签 | bug;feature request;stale;nvidia |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: How to make vLLM support multi stream torch compile and each stream capture cuda graph.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug SGLang now supports multi stream torch compile and each stream capture cuda graph. The code link is https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/model_executor/cuda_graph_runner.py#L500-#L506 If I want to make vLLM support that. My code on vLLM bypass the vLLM backend and make it like sglang ``` import torch._dynamo.config import torch._inductor.config torch._inductor.config.coordinate_descent_tuning = True torch._inductor.config.triton.unique_kernel_names = True torch._inductor.config.freezing = True torch._inductor.config.fx_graph_cache = False # Experimental feature to reduce compilation times, will be on by default in future from vllm.model_executor.custom_op import CustomOp def _to_torch(model: torch.nn.Module, reverse: bool, num_tokens: int): for sub in model._modules.values(): # sub.enter_torch_compile(num_tokens=num_tokens) # if isinstance(sub, torch.nn.Module): # _to_torch(sub, reverse, num_tokens) if isinstance(sub, CustomOp): if reverse: sub.leave_torch_compile() else: sub.enter_torch_compile(num_tokens=num_tokens) if isinstance(sub, torch.nn.Module): _to_torch(sub, reverse, num_tokens) @contextman...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: How to make vLLM support multi stream torch compile and each stream capture cuda graph. bug;feature request;stale;nvidia ### Your current environment ### 🐛 Describe the bug SGLang now supports multi stream torch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: k is https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/model_executor/cuda_graph_runner.py#L500-#L506 If I want to make vLLM support that. My code on vLLM bypass the vLLM backend and make it like sglang...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: lti stream torch compile and each stream capture cuda graph. bug;feature request;stale;nvidia ### Your current environment ### 🐛 Describe the bug SGLang now supports multi stream torch compile and each stream capture cu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: to make vLLM support multi stream torch compile and each stream capture cuda graph. bug;feature request;stale;nvidia ### Your current environment ### 🐛 Describe the bug SGLang now supports multi stream torch compile and...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ductor.config.freezing = True torch._inductor.config.fx_graph_cache = False # Experimental feature to reduce compilation times, will be on by default in future from vllm.model_executor.custom_op import CustomOp def _to_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
