# vllm-project/vllm#6544: [Usage]: How to release GPU of vLLM model in python code

| 字段 | 值 |
| --- | --- |
| Issue | [#6544](https://github.com/vllm-project/vllm/issues/6544) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to release GPU of vLLM model in python code

### Issue 正文摘录

### Your current environment ```python llm = LLM(model=model1_path, tensor_parallel_size=torch.cuda.device_count()) llm = LLM(model=model2_path, tensor_parallel_size=torch.cuda.device_count()) ``` It will cause CUDA out of memory when execute the second line. ### How would you like to use vllm I want to use two model in pipeline in one python code to infer. When finish inference on the first model, how to release this model and release GPU memory to load another one, since directly reloading may cause CUDA OUT OF MEMORY for it doesn't release the first one.

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: nish inference on the first model, how to release this model and release GPU memory to load another one, since directly reloading may cause CUDA OUT OF MEMORY for it doesn't release the first one. performance model_supp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: it doesn't release the first one. performance model_support cuda oom env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nment ```python llm = LLM(model=model1_path, tensor_parallel_size=torch.cuda.device_count()) llm = LLM(model=model2_path, tensor_parallel_size=torch.cuda.device_count()) ``` It will cause CUDA out of memory when execute...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: How to release GPU of vLLM model in python code usage ### Your current environment ```python llm = LLM(model=model1_path, tensor_parallel_size=torch.cuda.device_count()) llm = LLM(model=model2_path, tensor_para...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
