# vllm-project/vllm#34702: [CI Failure]: Sequence Parallel Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#34702](https://github.com/vllm-project/vllm/issues/34702) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Sequence Parallel Tests

### Issue 正文摘录

### Name of failing test `tests/compile/correctness_e2e/test_sequence_parallel.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/51887#019c6a67-630c-4233-8dd6-bec7cfa9272e ```bash [2026-02-17T07:52:40Z] tests/compile/correctness_e2e/test_sequence_parallel.py:285: in _compare_sp -- [2026-02-17T07:52:40Z] compare_two_settings(model_id, tp_sp_args, tp_args, method=method) [2026-02-17T07:52:40Z] tests/utils.py:677: in compare_two_settings [2026-02-17T07:52:40Z] compare_all_settings( [2026-02-17T07:52:40Z] _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ [2026-02-17T07:52:40Z] [2026-02-17T07:52:40Z] > assert ref_result == compare_result, ( [2026-02-17T07:52:40Z] f"Results for {model=} are not the same.\n" [2026-02-17T07:52:40Z] f"{ref_args=} {ref_envs=}\n" [2026-02-17T07:52:40Z] f"{compare_args=} {compare_envs=}\n" [2026-02-17T07:52:40Z] f"{ref_result=}\n" [2026-02-17T07:52:40Z] f"{compare_result=}\n" [2026-02-17T07:52:40Z] ) [2026-02-17T07:52:40Z] E AssertionError: Results for model='hmellor/tiny-random...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: `tests/compile/correctness_e2e/test_sequence_parallel.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing tes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Sequence Parallel Tests ci-failure ### Name of failing test `tests/compile/correctness_e2e/test_sequence_parallel.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by ext
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: maForCausalLM' are not the same. [2026-02-17T07:52:40Z] E ref_args=['--dtype', 'float16', '--max-model-len', '2048', '--max-num-seqs', '8', '--enable-chunked-prefill', '--enforce-eager', '--tokenizer-mode', 'auto', '--t...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: e": 3, "compile_sizes": [4, 8], "pass_config": {"enable_sp": true, "fuse_gemm_comms": false, "fuse_norm_quant": false, "fuse_act_quant": false, "eliminate_noops": true}, "use_inductor_graph_partition": false}'] ref_envs...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: lel-size', '2', '--pipeline-parallel-size', '2', '--distributed-executor-backend', 'ray', '--compilation_config', '{"mode": 3, "compile_sizes": [4, 8], "pass_config": {"enable_sp": true, "fuse_gemm_comms": false, "fuse_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
