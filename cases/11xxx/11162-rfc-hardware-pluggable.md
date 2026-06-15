# vllm-project/vllm#11162: [RFC]: Hardware pluggable

| 字段 | 值 |
| --- | --- |
| Issue | [#11162](https://github.com/vllm-project/vllm/issues/11162) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | install |
| Operator 关键词 | attention;cuda;operator;sampling |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Hardware pluggable

### Issue 正文摘录

### Motivation. Currently, vLLM support many hardware backend(cpu, cuda, hpu, neuron, openvino, rocm, tpu, xpu). Some other backend are also eager to be integrated by vllm([ascend](https://github.com/vllm-project/vllm/issues/7692), [IBM Spyre](https://github.com/vllm-project/vllm/issues/9652)). But as VLLM’s backend is more and more, we have encountered some problems: - Each backend has its own executor, worker, runner, attention. It makes the code complex. we can see many backend specified code is left here and there. - It's not easy for community to make the backend keep working. For example, it needs fully CI coverage, maintainers continuous contribution and so on. - New features are hard to be added to vLLM as well, since the backend case is complex. To solve the problem, a good solution is to support **hardware pluggable**. There are some benefit: - The backend decoupling can make the code cleaner and easier to maintain - Developers can pay more attention to the generic feature, so that it is no longer troubled by the tedious backend category - Each backend can evolve by itself to ensure availability and realtime integration. ### Proposed Change. There are two related RFC bef...

## 现有链接修复摘要

#30455 [Doc] Add Baidu Kunlun XPU support

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: runner, attention. It makes the code complex. we can see many backend specified code is left here and there. - It's not easy for community to make the backend keep working. For example, it needs fully CI coverage, maint...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: tale ### Motivation. Currently, vLLM support many hardware backend(cpu, cuda, hpu, neuron, openvino, rocm, tpu, xpu). Some other backend are also eager to be integrated by vllm([ascend](https://github.com/vllm-project/v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uggable RFC;stale ### Motivation. Currently, vLLM support many hardware backend(cpu, cuda, hpu, neuron, openvino, rocm, tpu, xpu). Some other backend are also eager to be integrated by vllm([ascend](https://github.com/v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ect can be pluggable is not fully defined and supported. Currently, only Models support this mechanism base on `ModelRegistry` feature. The out-of-tree code would like: ``` from vllm import ModelRegistry def register():...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Hardware pluggable RFC;stale ### Motivation. Currently, vLLM support many hardware backend(cpu, cuda, hpu, neuron, openvino, rocm, tpu, xpu). Some other backend are also eager to be integrated by vllm([ascend](ht...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30455](https://github.com/vllm-project/vllm/pull/30455) | mentioned | 0.6 | [Doc] Add Baidu Kunlun XPU support | tation support to the vLLM community.​ ## Purpose Leveraging the RFC #11162 (Hardware Out-Of-Tree Plugin) standard, we introduce vllm-kunlun, a plugin designed for the Baidu Kunlu… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
