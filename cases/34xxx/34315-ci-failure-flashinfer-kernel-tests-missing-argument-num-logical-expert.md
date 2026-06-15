# vllm-project/vllm#34315: [CI Failure]: Flashinfer Kernel tests missing argument: 'num_logical_experts'

| 字段 | 值 |
| --- | --- |
| Issue | [#34315](https://github.com/vllm-project/vllm/issues/34315) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;moe;sampling_logits |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;moe;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Flashinfer Kernel tests missing argument: 'num_logical_experts'

### Issue 正文摘录

### Name of failing test tests/kernels/moe/test_flashinfer.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Saw in CI - https://buildkite.com/vllm/ci/builds/51024/steps/canvas?jid=019c4ab1-5052-4272-80b7-00cbbea53a4e ``` > moe_config = FusedMoEConfig( -- num_experts=e, experts_per_token=topk, hidden_dim=k, intermediate_size_per_partition=n, num_local_experts=e, activation=activation, device="cuda", moe_parallel_config=FusedMoEParallelConfig.make_no_parallel(), in_dtype=torch.bfloat16, is_act_and_mul=is_act_and_mul, routing_method=RoutingMethodType.TopK, ) E TypeError: FusedMoEConfig.__init__() missing 1 required positional argument: 'num_logical_experts' tests/kernels/moe/test_flashinfer.py:284: TypeError ``` ### 📝 History of failing test Seems like introduced in #32344, which was merged earlier today. ### CC List. _No response_

## 现有链接修复摘要

#34316 Fix CI failure - Flashinfer Kernel tests

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [CI Failure]: Flashinfer Kernel tests missing argument: 'num_logical_experts' ci-failure ### Name of failing test tests/kernels/moe/test_flashinfer.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Flashinfer Kernel tests missing argument: 'num_logical_experts' ci-failure ### Name of failing test tests/kernels/moe/test_flashinfer.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: cuda", moe_parallel_config=FusedMoEParallelConfig.make_no_parallel(), in_dtype=torch.bfloat16, is_act_and_mul=is_act_and_mul, routing_method=RoutingMethodType.TopK, ) E TypeError: FusedMoEConfig.__init__() missing 1 req...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [CI Failure]: Flashinfer Kernel tests missing argument: 'num_logical_experts' ci-failure ### Name of failing test tests/kernels/moe/test_flashinfer.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Name of failing test tests/kernels/moe/test_flashinfer.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34316](https://github.com/vllm-project/vllm/pull/34316) | closes_keyword | 0.95 | Fix CI failure - Flashinfer Kernel tests | Fix #34315 ## Test Plan Tested locally with ``` pytest -v -s tests/kernels/moe/test_flashinfer.py ``` ## Test Result --- <details> <summary> Essential Elements of an Effective P |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
