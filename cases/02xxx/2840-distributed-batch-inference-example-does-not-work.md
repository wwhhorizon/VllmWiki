# vllm-project/vllm#2840: Distributed batch inference example does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#2840](https://github.com/vllm-project/vllm/issues/2840) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Distributed batch inference example does not work

### Issue 正文摘录

There is an example of batch inference from multiple GPUs. [https://github.com/vllm-project/vllm/commit/4abf6336ec65c270343eb895e7b18786e9274176](https://github.com/vllm-project/vllm/commit/4abf6336ec65c270343eb895e7b18786e9274176) However, running this code throws an error because the llm instance is not serializable. To make it run, I hade to modify the code as follows: ```python class Predictor: def __init__(self): pass def __call__(self, batch: Dict[str, np.ndarray]) -> Dict[str, list]: # prepare samples... llm = LLM(model="model name") # Generate translations from the prompts. outputs = llm.generate(prompts, sampling_params) del llm llm = None destroy_model_parallel() gc.collect() if torch.cuda.is_available(): torch.cuda.empty_cache() if torch.backends.mps.is_available(): torch.mps.empty_cache() torch.cuda.synchronize() # process... return result ```

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: da.is_available(): torch.cuda.empty_cache() if torch.backends.mps.is_available(): torch.mps.empty_cache() torch.cuda.synchronize() # process... return result ``` development distributed_parallel;model_support cuda env_d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eturn result ``` development distributed_parallel;model_support cuda env_dependency;race_condition;shape There is an example of batch inference from multiple GPUs.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: stroy_model_parallel() gc.collect() if torch.cuda.is_available(): torch.cuda.empty_cache() if torch.backends.mps.is_available(): torch.mps.empty_cache() torch.cuda.synchronize() # process... return result
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y]) -> Dict[str, list]: # prepare samples... llm = LLM(model="model name") # Generate translations from the prompts. outputs = llm.generate(prompts, sampling_params) del llm llm = None destroy_model_parallel()

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
