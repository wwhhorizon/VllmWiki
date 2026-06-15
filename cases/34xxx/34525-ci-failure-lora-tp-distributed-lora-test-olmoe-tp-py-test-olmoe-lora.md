# vllm-project/vllm#34525: [CI Failure] LoRA TP (Distributed): lora/test_olmoe_tp.py::test_olmoe_lora

| 字段 | 值 |
| --- | --- |
| Issue | [#34525](https://github.com/vllm-project/vllm/issues/34525) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure] LoRA TP (Distributed): lora/test_olmoe_tp.py::test_olmoe_lora

### Issue 正文摘录

## CI Failure Details **Job:** LoRA TP (Distributed) **Category:** test **Failure Type:** lora/test_olmoe_tp.py::test_olmoe_lora **Buildkite:** https://buildkite.com/vllm/ci/builds/51461#019c55cd-e6e7-4c6d-a913-fde3126a2f10 ## Error ``` AssertionError: assert False + where False = ('SELECT count(*) FROM candidate') + where = 'SELECT COUNT(Candidate_ID) FROM candidate;'.startswith ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure] LoRA TP (Distributed): lora/test_olmoe_tp.py::test_olmoe_lora ci-failure ## CI Failure Details **Job:** LoRA TP (Distributed) **Category:** test **Failure Type:** lora/test_olmoe_tp.py::test_olmoe_lora **Bu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 9c55cd-e6e7-4c6d-a913-fde3126a2f10 ## Error ``` AssertionError: assert False + where False = ('SELECT count(*) FROM candidate') + where = 'SELECT COUNT(Candidate_ID) FROM candidate;'.startswith ```
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [CI Failure] LoRA TP (Distributed): lora/test_olmoe_tp.py::test_olmoe_lora ci-failure ## CI Failure Details **Job:** LoRA TP (Distributed) **Category:** test **Failure Type:** lora/test_olmoe_tp.py::test_olmoe_lora **Bu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure] LoRA TP (Distributed): lora/test_olmoe_tp.py::test_olmoe_lora ci-failure ## CI Failure Details **Job:** LoRA TP (Distributed) **Category:** test **Failure Type:** lora/test_olmoe_tp.py::test_olmoe_lora **Bu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
