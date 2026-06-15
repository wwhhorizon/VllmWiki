# vllm-project/vllm#30679: [RFC]: Replace `torch.cuda` API with `torch.accelerator` for better hardware compatiblity.

| 字段 | 值 |
| --- | --- |
| Issue | [#30679](https://github.com/vllm-project/vllm/issues/30679) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Replace `torch.cuda` API with `torch.accelerator` for better hardware compatiblity.

### Issue 正文摘录

### Motivation. vLLM is a framework support multi hardware backend. while there are some torch.cuda hard code call. this is unfriendly to non-cuda compatible device. Fortunately, there is a new set of `torch.accelerator` [API](https://docs.pytorch.org/docs/stable/accelerator.html) in pytorch which can dispatch based on platform. Meanwhile, we should add some lint tools to avoid add more `torch.cuda` call in new added code. first example is https://github.com/vllm-project/vllm/pull/30681. ### Proposed Change. Target time: Migration done by end of Q2(or earlier). torch accelerator API status on torch-2.9.0: |cuda API name| unified torch API name| torch API Status | vLLM replace status| |-------|-------|-------|-------| |[torch.cuda.Event](https://pytorch.org/docs/stable/generated/torch.cuda.Event.html)| [torch.Event](https://pytorch.org/docs/stable/generated/torch.Event.html) | torch 2.9 ready| ~done #26985~ | |[torch.cuda.Stream](https://pytorch.org/docs/stable/generated/torch.cuda.Stream.html)| [torch.Stream](https://pytorch.org/docs/stable/generated/torch.Stream.html) | ~torch 2.9 ready~ 2.11 (https://github.com/pytorch/pytorch/pull/171040)| https://github.com/vllm-project/vllm/p...

## 现有链接修复摘要

#26985 Replace `torch.cuda.Event` with `torch.Event` for better hardware compatibility | #33225 replace `with torch.cuda.stream()` | #36145 [Hardware] Replace torch.cuda.device_count/current_device/set_device API | #37031 [Hardware] Replace memory related torch.cuda APIs | #37134 [Hardware] replace torch.cuda.Stream with torch.Stream

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tiblity. RFC ### Motivation. vLLM is a framework support multi hardware backend. while there are some torch.cuda hard code call. this is unfriendly to non-cuda compatible device. Fortunately, there is a new set of `torc...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: erated/torch.cuda.graph_pool_handle.html) | NA | NA | | |[torch.cuda._is_compiled](https://pytorch.org/docs/stable/generated/torch.cuda._is_compiled.html) | NA | NA | | |[torch.cuda.nvtx](https://pytorch.org/docs/stable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [RFC]: Replace `torch.cuda` API with `torch.accelerator` for better hardware compatiblity. RFC ### Motivation. vLLM is a framework support multi hardware backend. while there are some torch.cuda hard code call. this is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ch.org/docs/stable/cuda.html#torch-cuda-nvtx) | NA | NA | | |[torch.cuda.profiler](https://pytorch.org/docs/stable/cuda.html#torch-cuda-profiler) | NA | NA | | |[torch.cuda._is_compiled](https://pytorch.org/docs/stable/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26985](https://github.com/vllm-project/vllm/pull/26985) | mentioned | 0.45 | Replace `torch.cuda.Event` with `torch.Event` for better hardware compatibility | .org/docs/stable/generated/torch.event.html) \| torch 2.9 ready\| ~done #26985~ \| \|[torch.cuda.stream](https://pytorch.org/docs/stable/generated/torch.cuda.stream.html)\| [torch.stre… |
| [#33225](https://github.com/vllm-project/vllm/pull/33225) | mentioned | 0.6 | replace `with torch.cuda.stream()` | replace `with torch.cuda.stream()` ## Purpose Part of #30679 In PyTorch, torch.Stream objects implement __enter__ / __exit__ and it should work well with context manager |
| [#36145](https://github.com/vllm-project/vllm/pull/36145) | mentioned | 0.45 | [Hardware] Replace torch.cuda.device_count/current_device/set_device API | ex.html#torch.accelerator.set_device_index) \| torch 2.10 ready \| done #36145\| \|[torch.cuda.streamcontext](https://pytorch.org/docs/stable/generated/torch.cuda.streamcontext.html)… |
| [#37031](https://github.com/vllm-project/vllm/pull/37031) | mentioned | 0.45 | [Hardware] Replace memory related torch.cuda APIs  | celerator.memory.reset_peak_memory_stats.html) \|torch 2.9 ready \|done #37031 \| \|[torch.cuda.mem_get_info()](https://pytorch.org/docs/stable/generated/torch.cuda.mem_get_info.html)… |
| [#37134](https://github.com/vllm-project/vllm/pull/37134) | mentioned | 0.6 | [Hardware] replace torch.cuda.Stream with torch.Stream | re] replace torch.cuda.Stream with torch.Stream ## Purpose part of #30679 update on March 18th: there are some places use `Stream.cuda_stream` for some cuda specific 3rd party lib… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
