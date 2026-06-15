# vllm-project/vllm#23832: [Bug]: gpt-oss `--kv-cache-dtype "fp8"` not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#23832](https://github.com/vllm-project/vllm/issues/23832) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss `--kv-cache-dtype "fp8"` not supported

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It seems that KV cache quantization is not supported for gpt-oss and fails when sending a request. I can successfully setup a server with FP8 KV cache. ``` export VLLM_FLASH_ATTN_VERSION=3 python -m vllm.entrypoints.openai.api_server \ --model openai/gpt-oss-120b \ --max_model_len 50000 \ --tensor-parallel-size 1 \ --max-num-seqs 1 \ --kv-cache-dtype "fp8" ``` But when sending a request the server breaks: ``` (EngineCore_0 pid=3418225) File "/attention/layer.py", line 499, in unified_attention_with_output (EngineCore_0 pid=3418225) self.impl.forward(self, r the (EngineCore_0 pid=3418225) File "vllm/v1/attention/backends/flash_attn.py", line 533, in forward (EngineCore_0 pid=3418225) flash_attn_varlen_func( (EngineCore_0 pid=3418225) File "vllm/vllm_flash_attn/flash_attn_interface.py", line 258, in flash_attn_varlen_func (EngineCore_0 pid=3418225) out, softmax_lse, _, _ = torch.ops._vllm_fa3_C.fwd( (EngineCore_0 pid=3418225) ^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_0 pid=3418225) File "torch/_ops.py", line 1158, in __call_ug-25_ (EngineCore_0 pid=3418225) return self._op(*args, **(kwargs or {})) (EngineCore_0 pid=3418225) ^^^^^^^^^^...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: gpt-oss `--kv-cache-dtype "fp8"` not supported bug ### Your current environment ### 🐛 Describe the bug It seems that KV cache quantization is not supported for gpt-oss and fails when sending a request. I can succ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: r the (EngineCore_0 pid=3418225) File "vllm/v1/attention/backends/flash_attn.py", line 533, in forward (EngineCore_0 pid=3418225) flash_attn_varlen_func( (Engine
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: gpt-oss `--kv-cache-dtype "fp8"` not supported bug ### Your current environment ### 🐛 Describe the bug It seems that KV cache quantization is not supported for gpt-oss and fails when sending a request. I can succ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gpt-oss `--kv-cache-dtype "fp8"` not supported bug ### Your current environment ### 🐛 Describe the bug It seems that KV cache quantization is not supported for gpt-oss and fails when sending a request. I can succ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ccessfully setup a server with FP8 KV cache. ``` export VLLM_FLASH_ATTN_VERSION=3 python -m vllm.entrypoints.openai.api_server \ --model openai/gpt-oss-120b \ --max_model_len 50000 \ --tensor-parallel-size 1 \ --max-num...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
