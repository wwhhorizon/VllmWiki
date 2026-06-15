# vllm-project/vllm#39215: [Feature]: Use torch.compile Dynamo to see full trace for model forward pass

| 字段 | 值 |
| --- | --- |
| Issue | [#39215](https://github.com/vllm-project/vllm/issues/39215) |
| 状态 | open |
| 标签 | performance;feature request;torch.compile |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;frontend_api;gemm_linear;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | activation;cuda;fp8;kernel;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Use torch.compile Dynamo to see full trace for model forward pass

### Issue 正文摘录

### 🚀 The feature, motivation and pitch As mentioned by @WoosukKwon in last week's `#sig-model-perf` meeting, it can sometimes be difficult to dig through the many layers used in model code. This is necessary when looking for (missed) fusion opportunities, and developers often have to resort to looking at CUDA profiles. He was specifically talking about DS3.2, more info here: https://docs.google.com/document/d/1Ez5SXNAe0_lw3lDqk-XBrkA38eidJ1Yka5ryNg_wtTM/edit?tab=t.0 While it is already possible to look at an fx.Graph at every stage, those graphs are fully linearized, which makes reading this code very difficult. They also normally only display the last level of the stack trace, which doesn't really help determining where that call came from: for example, `QuantFP8.forward_cuda` does not tell us anything about where that `QuantFP8` instance lives. I'm proposing a custom graph dump that includes the full stack trace hierarchy. For DS31, this would look something like this: ``` DeepseekV2Model.forward VocabParallelEmbedding.forward_native long = l_input_ids_.long() output_parallel = torch.nn.functional.embedding(long, weight) DeepseekV2DecoderLayer[0].forward residual = output_paral...

## 现有链接修复摘要

#40721 [torch.compile] Add hierarchical module trace dump for FX graphs | #41378 [torch.compile] Replace depyf with custom graph-dump

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: doesn't really help determining where that call came from: for example, `QuantFP8.forward_cuda` does not tell us anything about where that `QuantFP8` instance lives. I'm proposing a custom graph dump that includes the f...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature]: Use torch.compile Dynamo to see full trace for model forward pass performance;feature request;torch.compile ### 🚀 The feature, motivation and pitch As mentioned by @WoosukKwon in last week's `#sig-model-perf`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fusion opportunities, and developers often have to resort to looking at CUDA profiles. He was specifically talking about DS3.2, more info here: https://docs.google.com/document/d/1Ez5SXNAe0_lw3lDqk-XBrkA38eidJ1Yka5ryNg_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: x_s = empty_1.permute(-1, -2) torch.ops
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: pile Dynamo to see full trace for model forward pass performance;feature request;torch.compile ### 🚀 The feature, motivation and pitch As mentioned by @WoosukKwon in last week's `#sig-model-perf` meeting, it can sometim...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40721](https://github.com/vllm-project/vllm/pull/40721) | closes_keyword | 0.95 | [torch.compile] Add hierarchical module trace dump for FX graphs | Closes #39215. As discussed in #sig-model-perf by @WoosukKwon and @ProExpertProg, it can be difficult to dig through the many layers used in model code when looking for fusion o |
| [#41378](https://github.com/vllm-project/vllm/pull/41378) | mentioned | 0.6 | [torch.compile] Replace depyf with custom graph-dump | raph dump path from #41296, including the structured trace shape from #39215. the existing user entry point stays the same: ```bash VLLM_DEBUG_DUMP_PATH=/tmp/vllm-dumps ... ``` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
