# vllm-project/vllm#13294: [Usage]: restarting vllm --> "WARNING: process group has NOT been destroyed before we destruct ProcessGroupNCCL"

| 字段 | 值 |
| --- | --- |
| Issue | [#13294](https://github.com/vllm-project/vllm/issues/13294) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: restarting vllm --> "WARNING: process group has NOT been destroyed before we destruct ProcessGroupNCCL"

### Issue 正文摘录

### Your current environment Hey guys :) since version 0.6.6 up to the current V0.7.2 I have a slightly annoying problem. When I start up my AI server, vllm everything works fine. The model is loaded and can be used as desired. However, as soon as I end my start script and want to load the same model again, or even a different model, vLLM always freezes at this point: ``` [W214 15:20:56.973624780 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) [W214 15:20:56.008814328 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) [W214 15:20:56.104798409 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) [W214 15:20:56.107680744 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) [W214 15:20:56.196595399 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) [W214 15:20:56.199089483 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) [W214 15:20:56.205991785 C...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: g problem. When I start up my AI server, vllm everything works fine. The model is loaded and can be used as desired. However, as soon as I end my start script and want to load the same model again, or even a different m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rocessGroupNCCL" usage ### Your current environment Hey guys :) since version 0.6.6 up to the current V0.7.2 I have a slightly annoying problem. When I start up my AI server, vllm everything works fine. The model is loa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: model, vLLM always freezes at this point: ``` [W214 15:20:56.973624780 CUDAAllocatorConfig.h:28] Warning: expandable_segments not supported on this platform (function operator()) [W214 15:20:56.008814328 CUDAAllocatorCo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;frontend_api;model_support;multimodal_vlm cuda;opera...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
