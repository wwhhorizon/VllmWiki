# vllm-project/vllm#39245: [Bug]: VLLM_USE_FLASHINFER_MOE_INT4 broken

| 字段 | 值 |
| --- | --- |
| Issue | [#39245](https://github.com/vllm-project/vllm/issues/39245) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM_USE_FLASHINFER_MOE_INT4 broken

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Since FlashInfer 0.6.4, which added `do_finalize` to the MoE code, the INT4 MoE backend has been broken because it does not pass this flag. When `do_finalize` is not passed, it returns a tuple of extra args instead of returning a tensor, causing this error: ``` (Worker_TP4 pid=535719) ERROR 04-03 22:31:57 [multiproc_executor.py:949] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/quantization/utils/flashinfer_mxint4_moe.py", line 264, in flashinfer_trtllm_mxint4_moe (Worker_TP4 pid=535719) ERROR 04-03 22:31:57 [multiproc_executor.py:949] ).to(x.dtype) (Worker_TP4 pid=535719) ERROR 04-03 22:31:57 [multiproc_executor.py:949] ^^ (Worker_TP4 pid=535719) ERROR 04-03 22:31:57 [multiproc_executor.py:949] AttributeError: 'list' object has no attribute 'to' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: VLLM_USE_FLASHINFER_MOE_INT4 broken bug ### Your current environment ### 🐛 Describe the bug Since FlashInfer 0.6.4, which added `do_finalize` to the MoE code, the INT4 MoE backend has been broken because it does...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: VLLM_USE_FLASHINFER_MOE_INT4 broken bug ### Your current environment ### 🐛 Describe the bug Since FlashInfer 0.6.4, which added `do_finalize` to the MoE code, the INT4 MoE backend has been broken because it does...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: oc_executor.py:949] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/quantization/utils/flashinfer_mxint4_moe.py", line 264, in flashinfer_trtllm_mxint4_moe (Worker_TP4 pid=535719) ERROR 04-03 22...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: VLLM_USE_FLASHINFER_MOE_INT4 broken bug ### Your current environment ### 🐛 Describe the bug Since FlashInfer 0.6.4, which added `do_finalize` to the MoE code, the INT4 MoE backend has been broken because it does...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
