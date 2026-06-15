# vllm-project/vllm#9652: [RFC]: Add support for IBM Spyre accelerator

| 字段 | 值 |
| --- | --- |
| Issue | [#9652](https://github.com/vllm-project/vllm/issues/9652) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | install |
| Operator 关键词 | attention;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Add support for IBM Spyre accelerator

### Issue 正文摘录

### Motivation. IBM has recently [announced](https://wccftech.com/ibm-telum-ii-processor-spyre-ai-accelerator-8-cores-5-5-ghz-360-mb-cache/) its Spyre AI accelerator at Hot Chips 2024. This accelerator has been designed, in collaboration with IBM Research, to scale-up enterprise AI workloads running on IBM's mainframe systems (IBM Z), as well as on IBM's [Power platform](https://www.ibm.com/docs/en/announcements/statement-direction-spyre-accelerator-power-platform). Since IBM is building our [inference stack on top of vLLM](https://developer.ibm.com/articles/awb-the-open-source-ecosystem-of-watsonx/), we would like to enable support for IBM Spyre within the vLLM framework. Spyre has been designed to fit seamlessly into the PyTorch ecosystem via torch.compile. Specifically, IBM Research has developed a new backend for torch.compile that will compile torch FX graphs for execution on the Spyre hardware. In this sense, we envision that Spyre support in vLLM can work in a similar way to how the TPU support is working today (e.g., see [here](https://github.com/vllm-project/vllm/blob/main/vllm/worker/tpu_model_runner.py#L685-L688)). Today, there are two key limitations that affect this i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ents/statement-direction-spyre-accelerator-power-platform). Since IBM is building our [inference stack on top of vLLM](https://developer.ibm.com/articles/awb-the-open-source-ecosystem-of-watsonx/), we would like to enab...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [RFC]: Add support for IBM Spyre accelerator RFC;stale ### Motivation. IBM has recently [announced](https://wccftech.com/ibm-telum-ii-processor-spyre-ai-accelerator-8-cores-5-5-ghz-360-mb-cache/) its Spyre AI accelerato...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: elerator-8-cores-5-5-ghz-360-mb-cache/) its Spyre AI accelerator at Hot Chips 2024. This accelerator has been designed, in collaboration with IBM Research, to scale-up enterprise AI workloads running on IBM's mainframe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: system via torch.compile. Specifically, IBM Research has developed a new backend for torch.compile that will compile torch FX graphs for execution on the Spyre hardware. In this sense, we envision that Spyre support in...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s accelerator has been designed, in collaboration with IBM Research, to scale-up enterprise AI workloads running on IBM's mainframe systems (IBM Z), as well as on IBM's [Power platform](https://www.ibm.com/docs/en/annou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
