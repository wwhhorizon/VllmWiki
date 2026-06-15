# vllm-project/vllm#26989: [Bug]: Qwen 30ba3 VL Does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#26989](https://github.com/vllm-project/vllm/issues/26989) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | runtime_err |
| Operator 关键词 | attention;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 30ba3 VL Does not work

### Issue 正文摘录

### Your current environment on vllm v0.11.1rc0 - Nvidia GH200 (arm64) ``` File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen3_vl.py", line 190, in forward browser-1 | (EngineCore_DP0 pid=546) x = x + self.attn(self.norm1(x), browser-1 | (EngineCore_DP0 pid=546) ^^^^^^^^^^^^^^^^^^^^^^^^ browser-1 | (EngineCore_DP0 pid=546) File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1751, in _wrapped_call_impl browser-1 | (EngineCore_DP0 pid=546) return self._call_impl(*args, **kwargs) browser-1 | (EngineCore_DP0 pid=546) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ browser-1 | (EngineCore_DP0 pid=546) File "/usr/local/lib/python3.12/dist-packages/torch/nn/modules/module.py", line 1762, in _call_impl browser-1 | (EngineCore_DP0 pid=546) return forward_call(*args, **kwargs) browser-1 | (EngineCore_DP0 pid=546) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ browser-1 | (EngineCore_DP0 pid=546) File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen2_5_vl.py", line 384, in forward browser-1 | (EngineCore_DP0 pid=546) output = flash_attn_varlen_func(q, browser-1 | (EngineCore_DP0 pid=546) ^^^^^^^^^^^^^^^^^^^^^^^^^ browser-1 | (EngineCore_DP0 pid=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: browser-1 | (EngineCore_DP0 pid=546) RuntimeError: This flash attention build does not support headdim not being a multiple of 32. ``` ### 🐛 Describe the bug Using VLLM with FA2 or FA3 results in this error. For FA#, us...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ^^^^^^^^^^^^^^^ browser-1 | (EngineCore_DP0 pid=546) RuntimeError: This flash attention build does not support headdim not being a multiple of 32. ``` ### 🐛 Describe the bug Using VLLM with FA2 or FA3 results in this er...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen 30ba3 VL Does not work bug;stale ### Your current environment on vllm v0.11.1rc0 - Nvidia GH200 (arm64) ``` File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/qwen3_vl.py", line 190, in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: _attn_varlen_func browser-1 | (EngineCore_DP0 pid=546) out, softmax_lse = torch.ops._vllm_fa2_C.varlen_fwd( browser-1 | (EngineCore_DP0 pid=546) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ browser-1 | (EngineCore_DP0 pid=546) Fil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
