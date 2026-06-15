# vllm-project/vllm#40419: [Bug]: kimi k2.5 Int4 default `flashinfer_trtllm_mxint4_moe` not working B300 SM103

| 字段 | 值 |
| --- | --- |
| Issue | [#40419](https://github.com/vllm-project/vllm/issues/40419) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: kimi k2.5 Int4 default `flashinfer_trtllm_mxint4_moe` not working B300 SM103

### Issue 正文摘录

### Your current environment Kimi K2.5 INT4 `vllm/vllm-openai:v0.19.0-cu130` `moonshotai/Kimi-K2.5` ### 🐛 Describe the bug hi @xinli-sw @kedarpotdar-nv full reprod https://github.com/SemiAnalysisAI/InferenceX/blob/ce47b76574238b8672c7ea00ea23898f5e3c7459/benchmarks/single_node/kimik2.5_int4_b300.sh and full logs https://github.com/SemiAnalysisAI/InferenceX/actions/runs/24695560185/job/72227409591?pr=1071 ``` (Worker_TP5 pid=2071791) ERROR 04-20 23:50:01 [multiproc_executor.py:949] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py", line 132, in _moe_forward_shared (Worker_TP5 pid=2071791) ERROR 04-20 23:50:01 [multiproc_executor.py:949] return runner.forward_impl( (Worker_TP5 pid=2071791) ERROR 04-20 23:50:01 [multiproc_executor.py:949] ^^^^^^^^^^^^^^^^^^^^ (Worker_TP5 pid=2071791) ERROR 04-20 23:50:01 [multiproc_executor.py:949] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py", line 815, in forward_impl (Worker_TP5 pid=2071791) ERROR 04-20 23:50:01 [multiproc_executor.py:949] shared_output, hidden_states = self._apply_quant_method( (Worker_TP5 pid=2071791)...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: kimi k2.5 Int4 default `flashinfer_trtllm_mxint4_moe` not working B300 SM103 bug ### Your current environment Kimi K2.5 INT4 `vllm/vllm-openai:v0.19.0-cu130` `moonshotai/Kimi-K2.5` ### 🐛 Describe the bug hi @xinl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : kimi k2.5 Int4 default `flashinfer_trtllm_mxint4_moe` not working B300 SM103 bug ### Your current environment Kimi K2.5 INT4 `vllm/vllm-openai:v0.19.0-cu130` `moonshotai/Kimi-K2.5` ### 🐛 Describe the bug hi @xinli-sw...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: /SemiAnalysisAI/InferenceX/blob/ce47b76574238b8672c7ea00ea23898f5e3c7459/benchmarks/single_node/kimik2.5_int4_b300.sh and full logs https://github.com/SemiAnalysisAI/InferenceX/actions/runs/24695560185/job/72227409591?p...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: kimi k2.5 Int4 default `flashinfer_trtllm_mxint4_moe` not working B300 SM103 bug ### Your current environment Kimi K2.5 INT4 `vllm/vllm-openai:v0.19.0-cu130` `moonshotai/Kimi-K2.5` ### 🐛 Describe the bug hi @xinl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: oc_executor.py:949] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py", line 132, in _moe_forward_shared (Worker_TP5 pid=2071791) ERROR 04-20 23:50:01 [multi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
