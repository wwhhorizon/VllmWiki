# vllm-project/vllm#31351: [Bug]: run test case in local failed: moe_expert_num = len(expert_map) TypeError: object of type 'NoneType' has no len()

| 字段 | 值 |
| --- | --- |
| Issue | [#31351](https://github.com/vllm-project/vllm/issues/31351) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: run test case in local failed: moe_expert_num = len(expert_map) TypeError: object of type 'NoneType' has no len()

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ` pytest -sv tests/e2e/singlecard/spec_decode_v1/test_v1_mtp_correctness.py::test_mtp1_correctness_eager ` ``` Worker_EP0 pid=168807) (Worker_EP0 pid=168807) INFO 12-25 12:19:14 [model_runner_v1.py:2224] Loading model weights took 11.2871 GB WorkerProc hit an exception. Traceback (most recent call last): File "/mnt/code/vllm/vllm/v1/executor/multiproc_executor.py", line 819, in worker_busy_loop output = func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/mnt/code/vllm-ascend/vllm_ascend/worker/worker.py", line 254, in determine_available_memory self.model_runner.profile_run() File "/mnt/code/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2194, in profile_run self._dummy_run(mc2_tokens_capacity, File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/mnt/code/vllm-ascend/vllm_ascend/worker/model_runner_v1.py", line 2140, in _dummy_run h...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: [Bug]: run test case in local failed: moe_expert_num = len(expert_map) TypeError: object of type 'NoneType' has no len() bug ### Your current environment ### 🐛 Describe the bug ` pytest -sv tests/e2e/singlecard/spec_dec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: run test case in local failed: moe_expert_num = len(expert_map) TypeError: object of type 'NoneType' has no len() bug ### Your current environment ### 🐛 Describe the bug ` pytest -sv tests/e2e/singlecard/spec_dec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: oe_comm_method.py", line 121, in fused_experts results = self.token_dispatcher.token_dispatch( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/token_dispatcher.py", line 198,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: er_v1.py", line 2194, in profile_run self._dummy_run(mc2_tokens_capacity, File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context return func(*args, **kwarg...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: fused_moe.py", line 367, in forward_impl final_hidden_states = self.quant_method.apply( ^^^^^^^^^^^^^^^^^^^^^^^^ File "/mnt/code/vllm-ascend/vllm_ascend/ops/fused_moe/fused_moe.py", line 124, in apply return moe_comm_me...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
