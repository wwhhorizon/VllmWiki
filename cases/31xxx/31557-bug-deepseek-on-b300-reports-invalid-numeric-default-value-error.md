# vllm-project/vllm#31557: [Bug]: DeepSeek on B300 reports `invalid numeric default value` error

| 字段 | 值 |
| --- | --- |
| Issue | [#31557](https://github.com/vllm-project/vllm/issues/31557) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepSeek on B300 reports `invalid numeric default value` error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve /home/ubuntu/vllm/Deepseek-R1 --load-format dummy -tp 8 ``` (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] File "/root/venv/lib/python3.10/site-packages/torch/_inductor/utils.py", line 3017, in run (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] out = model(new_inputs) (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] File "/tmp/torchinductor_root/aa/caaxqz3zace2333c7pgcxjpk4xv6km5jhat4mywtg53psdysuwfs.py", line 1078, in call (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] buf13 = torch.ops.vllm.moe_forward_shared.default(buf11, buf12, 'model.layers.3.mlp.experts') (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] File "/root/venv/lib/python3.10/site-packages/torch/_ops.py", line 841, in __call__ (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] return self._op(*args, **kwargs) (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] File "/root/vllm/vllm/model_executor/layers/fused_moe/layer.py", line 2098, in moe_forward_shared (...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: Your current environment ### 🐛 Describe the bug VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve /home/ubuntu/vllm/Deepseek-R1 --load-format dummy -tp 8 ``` (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:82...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: current environment ### 🐛 Describe the bug VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve /home/ubuntu/vllm/Deepseek-R1 --load-format dummy -tp 8 ``` (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] Fi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ;stale ### Your current environment ### 🐛 Describe the bug VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve /home/ubuntu/vllm/Deepseek-R1 --load-format dummy -tp 8 ``` (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_exe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: USE_FLASHINFER_MOE_FP8=1 vllm serve /home/ubuntu/vllm/Deepseek-R1 --load-format dummy -tp 8 ``` (Worker_TP1 pid=254284) ERROR 12-31 19:12:55 [multiproc_executor.py:824] File "/root/venv/lib/python3.10/site-packages/torc...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: DeepSeek on B300 reports `invalid numeric default value` error bug;stale ### Your current environment ### 🐛 Describe the bug VLLM_USE_FLASHINFER_MOE_FP8=1 vllm serve /home/ubuntu/vllm/Deepseek-R1 --load-format du...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
