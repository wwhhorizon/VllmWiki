# vllm-project/vllm#745: error: `cutlassF` is not supported because: xFormers wasn't build with CUDA support

| 字段 | 值 |
| --- | --- |
| Issue | [#745](https://github.com/vllm-project/vllm/issues/745) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> error: `cutlassF` is not supported because: xFormers wasn't build with CUDA support

### Issue 正文摘录

Hi team, I am getting the following error when loading a model. I had built vllm in a host with cuda 11.8 installed, although the host itself is a non-gpu host. I understand xformers also got packaged as part of vllm wheel creation. Can you please help with potential reasons for the issue below ? llm = LLM(model="_path_to_model__") File "bin/site-packages/vllm/model_executor/layers/attention.py", line 315, in forward return super().forward( File "site-packages/vllm/model_executor/layers/attention.py", line 202, in forward self.multi_query_kv_attention( File "bin/site-packages/vllm/model_executor/layers/attention.py", line 111, in multi_query_kv_attention out = xops.memory_efficient_attention_forward( File "bin/site-packages/xformers/ops/fmha/__init__.py", line 213, in memory_efficient_attention_forward return _memory_efficient_attention_forward( File "bin/site-packages/xformers/ops/fmha/__init__.py", line 308, in _memory_efficient_attention_forward _ensure_op_supports_or_raise(ValueError, "memory_efficient_attention", op, inp) File "bin/site-packages/xformers/ops/fmha/dispatch.py", line 45, in _ensure_op_supports_or_raise raise exc_type( ValueError: Operator `memory_efficient_atte...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: error: `cutlassF` is not supported because: xFormers wasn't build with CUDA support Hi team, I am getting the following error when loading a model. I had built vllm in a host with cuda 11.8 installed, although the host...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: error: `cutlassF` is not supported because: xFormers wasn't build with CUDA support Hi team, I am getting the following error when loading a model. I had built vllm in a host with cuda 11.8 installed, although the host...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s not support inputs: query : shape=(1, 2560, 32, 128) (torch.float16) key : shape=(1, 2560, 32, 128) (torch.float16) value : shape=(1, 2560, 32, 128) (torch.float16) attn_bias : p : 0.0 `cutlassF` is not supported beca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: error: `cutlassF` is not supported because: xFormers wasn't build with CUDA support Hi team, I am getting the following error when loading a model. I had built vllm in a host with cuda 11.8 installed, although the host...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h CUDA support Hi team, I am getting the following error when loading a model. I had built vllm in a host with cuda 11.8 installed, although the host itself is a non-gpu host. I understand xformers also got packaged as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
