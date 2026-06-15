# vllm-project/vllm#18416: [Bug][Failing Test]: weight-loading-multiple-gpu-test -

| 字段 | 值 |
| --- | --- |
| Issue | [#18416](https://github.com/vllm-project/vllm/issues/18416) |
| 状态 | closed |
| 标签 | bug;ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe;operator;quantization |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][Failing Test]: weight-loading-multiple-gpu-test -

### Issue 正文摘录

### Your current environment Still failing on main as of commit bca55b556f ### 🐛 Describe the bug Failing test: https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests/6873a23f-c2ec-8c01-9e20-bac3329482c0?tags=scm.branch%3Amain%2Cresult%3Afailed ``` FAILED weight_loading/test_weight_loading.py::test_weight_loading - RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {'EngineCore_0': 1} ```

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #18543 [Bugfix] Use random hidden states in dummy sampler run

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug][Failing Test]: weight-loading-multiple-gpu-test - bug;ci-failure ### Your current environment Still failing on main as of commit bca55b556f ### 🐛 Describe the bug Failing test: https://buildkite.com/organizations/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tend_api;model_support;moe;quantization;sampling_logits;scheduler_memory cuda;kernel;moe;operator;quantization build_error;crash;mismatch;oom dtype;env_dependency;memory_layout;shape #4 Use FlashAttention for `multi_que...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: correctness ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory cuda;kernel;moe;operator;quantization build_error;crash;mismatch;oom dtype;env_dependency;memory_lay...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: _memory cuda;kernel;moe;operator;quantization build_error;crash;mismatch;oom dtype;env_dependency;memory_layout;shape #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: neCore_0': 1} ``` correctness ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory cuda;kernel;moe;operator;quantization build_error;crash;mismatch;oom dtype;env_dep...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | dist-packages/torch/lib/libtorch_cpu.so) [2025-05-20t10:52:09z] frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | ist-packages/torch/lib/libtorch_cuda.so) [2025-05-20t10:52:09z] frame #6: <unknown function> + 0xdc253 (0x7f80b29b3253 in /lib/x86_64-linux-gnu/libstdc++.so.6) [2025-05-20t10:52:0… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | in /lib/x86_64-linux-gnu/libstdc++.so.6) [2025-05-20t10:52:09z] frame #7: <unknown function> + 0x94ac3 (0x7f81b3fb9ac3 in /lib/x86_64-linux-gnu/libc.so.6) [2025-05-20t10:52:09z] f… |
| [#18543](https://github.com/vllm-project/vllm/pull/18543) | closes_keyword | 0.95 | [Bugfix] Use random hidden states in dummy sampler run | FIX #18416 FIX #18417 FIX #18418 FIX #18425 FIX #18459 FIX #18462 FIX #18466 FIX #18498 FIX #18525 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
