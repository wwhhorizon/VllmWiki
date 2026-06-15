# vllm-project/vllm#23261: [RFC]: Address piecewise graph splitting and attention fusion incompatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#23261](https://github.com/vllm-project/vllm/issues/23261) |
| 状态 | closed |
| 标签 | RFC;torch.compile |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;fp8;operator;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: Address piecewise graph splitting and attention fusion incompatibility

### Issue 正文摘录

**UPDATE**: we chose approach 2, implemented in #24281 and pytorch/pytorch#162207. ## Motivation. I wanted to get a quick opinion from people on possible solutions on the issue where attention+quant fusion is incompatible with splitting_ops and hence piecewise cudagraphs. I've thought about it before but @nvpohanh brought it up in a DM this morning. I am looking for feedback on both possible solutions and whether this is worth solving. ### Problem: > There is an incompatibility between @fhl2000 ’s `FULL_AND_PIECEWISE` and the `splitting_ops` setting. In vLLM, we are currently splitting the FX graph before we start to apply graph fusion passes. However, we would like to enable Attn+Q fusions, so we clear the `splitting_ops` to keep the Attn op in the FX graph, but that breaks the `FULL_AND_PIECEWISE` mode because now we cannot capture piece-wise cuda graphs with full FX graph. ## Proposed Change. There are a few possible solutions: 1. Set `splitting_ops=[]` and use `cudagraph_mode=FULL` (current approach) 2. Split the graph in Inductor after custom passes 3. Split the graph after AotDispatcher (and custom passes) but before Inductor 4. While splitting the graph, make modifications...

## 现有链接修复摘要

#24281 [torch.compile] CUDAGraph Inductor partition integration

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: piecewise graph splitting and attention fusion incompatibility RFC;torch.compile **UPDATE**: we chose approach 2, implemented in #24281 and pytorch/pytorch#162207. ## Motivation. I wanted to get a quick opinion from peo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: k opinion from people on possible solutions on the issue where attention+quant fusion is incompatible with splitting_ops and hence piecewise cudagraphs. I've thought about it before but @nvpohanh brought it up in a DM t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: it the graph in Inductor after custom passes 3. Split the graph after AotDispatcher (and custom passes) but before Inductor 4. While splitting the graph, make modifications to enable fusion More details and the specific...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion+quant fusion is incompatible with splitting_ops and hence piecewise cudagraphs. I've thought about it before but @nvpohanh brought it up in a DM this morning. I am looking for feedback on both possible solutions an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: `cudagraph_mode=FULL` There are a few issues with this approach: - Mixed decode-prefill batches can be faster with piecewise cudagraphs. - Cascade attention requires piecewise cudagraphs. - Some attention backends don't...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24281](https://github.com/vllm-project/vllm/pull/24281) | mentioned | 0.45 | [torch.compile] CUDAGraph Inductor partition integration | usion incompatibility **update**: we chose approach 2, implemented in #24281 and pytorch/pytorch#162207. ## motivation. i wanted to get a quick opinion from people on possible sol… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
