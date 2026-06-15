# vllm-project/vllm#35679: [CI] Chat template missing for PowerMoE-3b model

| 字段 | 值 |
| --- | --- |
| Issue | [#35679](https://github.com/vllm-project/vllm/issues/35679) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI] Chat template missing for PowerMoE-3b model

### Issue 正文摘录

## Name of failing test - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_dp_server_info[4]` - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_lb_completion[4-ibm-research/PowerMoE-3b]` - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_lb_completion_streaming[4-ibm-research/PowerMoE-3b]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Tests (4 GPUs) **Category:** test ## Describe the failing test API server warmup fails during chat template processing because the ibm-research/PowerMoE-3b model's tokenizer does not define a chat template, which is required as of transformers v4.44. The error occurs in safe_apply_chat_template when trying to render chat messages during server initialization, preventing the OpenAI API server from starting successfully. ``` vllm.entrypoints.chat_utils.ChatTemplateResolutionError: As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one. ``` ## Relevant builds - [Build #53865](https://buildkite.com/vllm/ci/builds/53865) (bbf81f9a) - [Distributed Tests (4 GPUs)](https://buildkite....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI] Chat template missing for PowerMoE-3b model ci-failure ## Name of failing test - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_dp_server_info[4]` - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_lb_completion
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI] Chat template missing for PowerMoE-3b model ci-failure ## Name of failing test - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_dp_server_info[4]` - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_lb_completio...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: research/PowerMoE-3b]` ## Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries **Affected jobs:** Distributed Tests (4 GPUs) **Category:** test ## Describe the failing test A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: v1/distributed/test_hybrid_lb_dp.py::test_hybrid_lb_completion[4-ibm-research/PowerMoE-3b]` - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_lb_completion_streaming[4-ibm-research/PowerMoE-3b]` ## Basic information -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [CI] Chat template missing for PowerMoE-3b model ci-failure ## Name of failing test - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_dp_server_info[4]` - `v1/distributed/test_hybrid_lb_dp.py::test_hybrid_lb_completio...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
