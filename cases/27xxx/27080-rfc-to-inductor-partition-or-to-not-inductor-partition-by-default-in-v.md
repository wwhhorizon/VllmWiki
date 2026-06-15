# vllm-project/vllm#27080: [RFC]: To Inductor partition or to not Inductor partition (by default in v0.11.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#27080](https://github.com/vllm-project/vllm/issues/27080) |
| 状态 | open |
| 标签 | RFC;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | activation;attention;fp8;quantization |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [RFC]: To Inductor partition or to not Inductor partition (by default in v0.11.1)

### Issue 正文摘录

**tl;dr:** Inductor partition is a semi-experimental feature in torch 2.9 that increases performance but also compile time and has risks, we should decide whether to enable it by default or not in 0.11.1. ## Motivation. Currently, on vLLM main, piecewise cudagraphs are achieved using Dynamo partitioning (splitting the fx.Graph before it enters Inductor). That makes piecewise cudagraphs incompatible with compilation passes that need to see the whole graph to work - like attention+quant fusion and sequence parallelism (and hence async tp). Apart from allreduce+rmsnorm(+quant) fusion, those are the passes that bring the most benefit. The vLLM x torch.compile collaboration yielded a custom Inductor partitioning solution (RFC: #23261, PR: #24281). It gives better performance by itself by reducing cudagraph replay overhead and it allows piecewise cudagraphs to be compatible with fullgraph custom passes. It requires torch==2.9, with a couple of monkeypatches and workarounds (listed below) in vLLM but they are not too bad. It also significantly increases cold-start (first-time) compilation time. Finally, it is somewhat of an experimental feature, and we've resolved most of the known issue...

## 现有链接修复摘要

#24281 [torch.compile] CUDAGraph Inductor partition integration | #24604 [torch.compile] Enable attention and allreduce fusion without custom ops enabled | #26735 [BugFix] Patch inductor partitioning logic | #26738 [DO NOT MERGE] 2.9, Inductor partition, standalone compile, monkeypatch fix(es) | #26847 [Frontend][torch.compile] CompilationConfig Overhaul (#20283): Set up -O infrastructure

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: lt or not in 0.11.1. ## Motivation. Currently, on vLLM main, piecewise cudagraphs are achieved using Dynamo partitioning (splitting the fx.Graph before it enters Inductor). That makes piecewise cudagraphs incompatible w...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ilation passes that need to see the whole graph to work - like attention+quant fusion and sequence parallelism (and hence async tp). Apart from allreduce+rmsnorm(+quant) fusion, those are the passes that bring the most...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: mi-experimental feature in torch 2.9 that increases performance but also compile time and has risks, we should decide whether to enable it by default or not in 0.11.1. ## Motivation. Currently, on vLLM main, piecewise c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ll being resolved). The performance benefit is between 2-10% for various models and QPS regimes. The startup cost is around 2-5x depending on the model - although warm start is actually slightly faster as there are fewe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: uctor partition or to not Inductor partition (by default in v0.11.1) RFC;stale **tl;dr:** Inductor partition is a semi-experimental feature in torch 2.9 that increases performance but also compile time and has risks, we...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24281](https://github.com/vllm-project/vllm/pull/24281) | mentioned | 0.45 | [torch.compile] CUDAGraph Inductor partition integration | b7f5b4-a9fd-4b0d-a9f0-dadc29457e75" /> #### startup time taken from #24281, anecdotally i've seen larger models compile for up to 100s on cold start as well but that was the most… |
| [#24604](https://github.com/vllm-project/vllm/pull/24604) | mentioned | 0.45 | [torch.compile] Enable attention and allreduce fusion without custom ops enabled | ning ### appendix: benchmarking results these numbers all use 2.9 + #24604. the h100 sp-asynctp numbers also use #26975. on b200, the following settings were used: - common: `--kv… |
| [#26735](https://github.com/vllm-project/vllm/pull/26735) | mentioned | 0.45 | [BugFix] Patch inductor partitioning logic | es (so far), but there could be more. monkeypatches & workarounds: - #26735: monkeypatch for partition rules - #26878: monkeypatch for memory plan output naming - #26956: aot cach… |
| [#26738](https://github.com/vllm-project/vllm/pull/26738) | mentioned | 0.45 | [DO NOT MERGE] 2.9, Inductor partition, standalone compile, monkeypatch fix(es) | uctor partition causes inductor codegen error - a few more ci issues: #26738, hoping to resolve these by eod friday ## proposed change. the big question to resolve is whether to e… |
| [#26847](https://github.com/vllm-project/vllm/pull/26847) | mentioned | 0.45 | [Frontend][torch.compile] CompilationConfig Overhaul (#20283): Set up -O infrastructure | g. with the planned addition of optimization levels (rfc: #20283, pr: #26847, more below), it will be as easy as `-o1`. this way there's an easy way to control the tradeoff betwee… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
