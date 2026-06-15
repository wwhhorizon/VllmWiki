# vllm-project/vllm#7550: [Bug]:  online fp8 quantization with jais model got assert error due to cutlass_scaled_mm()

| 字段 | 值 |
| --- | --- |
| Issue | [#7550](https://github.com/vllm-project/vllm/issues/7550) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  online fp8 quantization with jais model got assert error due to cutlass_scaled_mm()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug run `throughput benchmark.py` with jais-13B/30B models with following command: ```sh python3 /vllm/benchmarks/benchmark_throughput.py --model core42/jais-13b-chat --num-prompts $req -tp $tp --distributed-executor-backend mp --input-len $inp --output-len $out --trust-remote-code --dtype auto --enforce-eager --quantization fp8 ``` error logs as: ```yml [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/jais.py", line 206, in forward [rank0]: feed_forward_hidden_states = self.mlp(hidden_states) [rank0]: File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl [rank0]: return self._call_impl(*args, **kwargs) [rank0]: File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1562, in _call_impl [rank0]: return forward_call(*args, **kwargs) [rank0]: File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/jais.py", line 162, in forward [rank0]: hidden_states2, _ = self.c_fc2(hidden_states) [rank0]: File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl [rank0]: retu...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: online fp8 quantization with jais model got assert error due to cutlass_scaled_mm() bug;stale ### Your current environment ### 🐛 Describe the bug run `throughput benchmark.py` with jais-13B/30B models with follow...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: online fp8 quantization with jais model got assert error due to cutlass_scaled_mm() bug;stale ### Your current environment ### 🐛 Describe the bug run `throughput benchmark.py` with jais-13B/30B models with follow...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: assert (b.shape[0] % 16 == 0 and b.shape[1] % 16 == 0) ``` correctness ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;quantiz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tization with jais model got assert error due to cutlass_scaled_mm() bug;stale ### Your current environment ### 🐛 Describe the bug run `throughput benchmark.py` with jais-13B/30B models with following command: ```sh pyt...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: bug;stale ### Your current environment ### 🐛 Describe the bug run `throughput benchmark.py` with jais-13B/30B models with following command: ```sh python3 /vllm/benchmarks/benchmark_throughput.py --model core42/jais-13b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
