# vllm-project/vllm#37468: [Bug]: FlashInfer allreduce fusion workspace uninitialized error

| 字段 | 值 |
| --- | --- |
| Issue | [#37468](https://github.com/vllm-project/vllm/issues/37468) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FlashInfer allreduce fusion workspace uninitialized error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve MiniMaxAI/MiniMax-M2.5 --trust-remote-code --stream-interval 20 --no-enable-prefix-caching --tensor-parallel-size 2 ``` Error on main: ``` [multiproc_executor.py:932] File "/vllm/vllm/compilation/piecewise_backend.py", line 197, in compiled_graph_wrapper [multiproc_executor.py:932] graph_output = compiled_graph(*args) [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^^^ [multiproc_executor.py:932] File "/vllm/.venv/lib/python3.12/site-packages/torch/_inductor/standalone_compile.py", line 312, in __call__ [multiproc_executor.py:932] return self.inner_fn(*args) [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^^ [multiproc_executor.py:932] File "/vllm/.venv/lib/python3.12/site-packages/torch/_dynamo/aot_compile_types.py", line 211, in __call__ [multiproc_executor.py:932] return self.compiled_fn(*args, **kwargs) [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [multiproc_executor.py:932] File "/vllm/.venv/lib/python3.12/site-packages/torch/_functorch/_aot_autograd/aot_autograd_result.py", line 679, in forward [multiproc_executor.py:932] return compiled_fn(list(runtime_args)) [multiproc_executor.py:932] ^^^^^^^^...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FlashInfer allreduce fusion workspace uninitialized error bug ### Your current environment ### 🐛 Describe the bug ``` vllm serve MiniMaxAI/MiniMax-M2.5 --trust-remote-code --stream-interval 20 --no-enable-prefix-...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _allreduce_norm.default(allreduce_in=buf0, residual=buf2, norm_out=buf1, quant_out=None, scale_out=None, rms_gamma=arg3_1, rms_eps=1e-06, pattern_code=1, world_size=2, launch_with_pdl=True, fp32_acc=True, max_token_num=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^ [multiproc_executor.py:932] File "/tmp/torchinductor_weizha/2s/c2sm7zcxi4ch574czlqwjjrbozol5vx2qx6wexgv4zxnlp6ysdsb.py", line 1085, in call [multiproc_executor.py:932] torch.ops.vllm.flashinfer_trtllm_fused_allred...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r.py:932] File "/vllm/.venv/lib/python3.12/site-packages/torch/_dynamo/eval_frame.py", line 1272, in _fn [multiproc_executor.py:932] return fn(*args, **kwargs) [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^ [multiproc_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: :932] File "/vllm/vllm/compilation/piecewise_backend.py", line 197, in compiled_graph_wrapper [multiproc_executor.py:932] graph_output = compiled_graph(*args) [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^^^ [multiproc...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
