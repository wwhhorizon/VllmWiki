# vllm-project/vllm#33802: [CI Failure]: Distributed 2xH100 tests

| 字段 | 值 |
| --- | --- |
| Issue | [#33802](https://github.com/vllm-project/vllm/issues/33802) |
| 状态 | closed |
| 标签 | torch.compile;ci-failure;needs reproduction |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [CI Failure]: Distributed 2xH100 tests

### Issue 正文摘录

### Name of failing test tests/compile/distributed/test_async_tp.py::test_async_tp_pass_correctness ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test It seems like the server hangs in CI (cannot seem to repro locally on main), and then the test gives this error: ``` FAILED tests/compile/distributed/test_async_tp.py::test_async_tp_pass_correctness[False-mp-True-2-RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8] - TypeError: 'NoneType' object is not subscriptable ``` The hang error earlier: Note that this test had some flakiness as well beforehand, with this error on Tuesday nightly: ``` tests/compile/distributed/test_async_tp.py::test_async_tp_pass_correctness[False-mp-True-2-RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8] gpu memory used/total (GiB): 0=0.47/79.65; 1=0.47/79.65; -- Done waiting for free GPU memory on devices devices=[0, 1] (threshold='0.10') dur_s=0.00 Fork a new process to run a test 17763 Fork a new process to run a test 0 tokenizer_config.json: 55.4kB [00:00, 100MB/s] FAILED ... FAILED tests/compile/distributed/test_async_tp.py::test_async_tp_pass_correctness[False-...

## 现有链接修复摘要

#23465 [Attention][FA3] Update FA3 to include new swizzle optimization | #31034 [P/D] rework mooncake connector and introduce its bootstrap server | #33257 [MISC] Fix Tensor Parallelism for Quantized Mamba Models with n_groups=1 | #33613 [Bugfix] Disable TRTLLM FP8 MoE if router_logits_dtype==float32 and routing_method!=DeepSeekV3 | #33641 [torch.compile] Significantly speed up cold start times | #33841 Revert "[Attention][FA3] Update FA3 to include new swizzle optimization"

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: Distributed 2xH100 tests torch.compile;ci-failure;needs reproduction ### Name of failing test tests/compile/distributed/test_async_tp.py::test_async_tp_pass_correctness ### Basic information - [ ] Flaky t
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: _tp_pass_correctness[False-mp-True-2-RedHatAI/Meta-Llama-3.1-8B-Instruct-FP8] - TypeError: 'NoneType' object is not subscriptable ``` The hang error earlier: Note that this test had some flakiness as well beforehand, wi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: istributed/test_async_tp.py::test_async_tp_pass_correctness ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [CI Failure]: Distributed 2xH100 tests torch.compile;ci-failure;needs reproduction ### Name of failing test tests/compile/distributed/test_async_tp.py::test_async_tp_pass_correctness ### Basic information - [ ] Flaky te...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ntized Mamba Models with n_groups=1 | #33613 [Bugfix] Disable TRTLLM FP8 MoE if router_logits_dtype==float32 and routing_method!=DeepSeekV3 | #33641 [torch.compile] Significantly speed up cold start times | #33841 Rever...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23465](https://github.com/vllm-project/vllm/pull/23465) | mentioned | 0.45 | [Attention][FA3] Update FA3 to include new swizzle optimization | -9b46-4913-9abc-e06cf1588b8b&tab=output broken: tuesday at 11:20 am (#23465): https://buildkite.com/vllm/ci/builds/49808/steps/canvas?sid=019c244e-f4b2-46e4-bdea-4e8c0c0d8bb9&tab=… |
| [#31034](https://github.com/vllm-project/vllm/pull/31034) | mentioned | 0.45 | [P/D] rework mooncake connector and introduce its bootstrap server | a755-415d-bf06-95f07669c825&tab=output working: tuesday at 11:20 am (#31034): https://buildkite.com/vllm/ci/builds/49807/steps/canvas?jid=019c2965-758e-4024-8812-83500c2438b5&tab=… |
| [#33257](https://github.com/vllm-project/vllm/pull/33257) | mentioned | 0.45 | [MISC] Fix Tensor Parallelism for Quantized Mamba Models with n_groups=1 | te.com/vllm/ci/builds/49871/steps/canvas broken: tuesday at 3:10 pm (#33257): https://buildkite.com/vllm/ci/builds/49844/steps/canvas?sid=019c2521-f35a-42a8-aedb-620b548c59b3&open… |
| [#33613](https://github.com/vllm-project/vllm/pull/33613) | mentioned | 0.45 | [Bugfix] Disable TRTLLM FP8 MoE if router_logits_dtype==float32 and routing_method!=DeepSeekV3 | <summary> full history </summary> broken: daily: tuesday at 5:00 pm (#33613): daily: https://buildkite.com/vllm/ci/builds/49871/steps/canvas broken: tuesday at 3:10 pm (#33257): h… |
| [#33641](https://github.com/vllm-project/vllm/pull/33641) | mentioned | 0.45 | [torch.compile] Significantly speed up cold start times | -f35a-42a8-aedb-620b548c59b3&open=false broken: tuesday at 12:17 pm (#33641): https://buildkite.com/vllm/ci/builds/49822/steps/canvas?sid=019c2483-b888-43a3-aa4b-2862854c641a&tab=… |
| [#33841](https://github.com/vllm-project/vllm/pull/33841) | mentioned | 0.6 | Revert "[Attention][FA3] Update FA3 to include new swizzle optimization" | wizzle optimization" Reverts vllm-project/vllm#23465 As described in #33802, #23465 broke the Distributed Tests 2 GPUs (H100). - CI run for #23465: https://buildkite.com/vllm/ci/b… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
