# vllm-project/vllm#2878: set_cuda_visible_devices in _init_workers_ray since vLLM 0.2.7

| 字段 | 值 |
| --- | --- |
| Issue | [#2878](https://github.com/vllm-project/vllm/issues/2878) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> set_cuda_visible_devices in _init_workers_ray since vLLM 0.2.7

### Issue 正文摘录

Hi vllm team, I notice that [llm_engine._init_workers_ray](https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py#L178) has been updated to manually use set_cuda_visible_devices to set gpu ids before init the Worker with lazy import to avoid torch set the gpus by default. However, this does affect a few code bases where a vllm model is wrapped inside a ray actor (when you need to load multiple vllm models in one job). Is this case covered or I'm I missing something?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: set_cuda_visible_devices to set gpu ids before init the Worker with lazy import to avoid torch set the gpus by default. However, this does affect a few code bases where a vllm model is wrapped inside a ray actor (when y...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: set_cuda_visible_devices in _init_workers_ray since vLLM 0.2.7 Hi vllm team, I notice that [llm_engine._init_workers_ray](https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py#L178) has been updated t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: gpus by default. However, this does affect a few code bases where a vllm model is wrapped inside a ray actor (when you need to load multiple vllm models in one job). Is this case covered or I'm I missing something?

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
