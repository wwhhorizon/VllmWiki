# vllm-project/vllm#41494: [Bug]: Qwen3ForEmbedding no longer works

| 字段 | 值 |
| --- | --- |
| Issue | [#41494](https://github.com/vllm-project/vllm/issues/41494) |
| 状态 | open |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3ForEmbedding no longer works

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug trying to serve voyageai/voyage-4-nano, which is listed as supported on the embedding page results in the following. i used the pooling runner exception: ``` (EngineCore pid=90910) ValueError: There is no module or parameter named 'linear' in Qwen3ForEmbedding. The available parameters belonging to (Qwen3ForEmbedding) are: {'model.layers.4.mlp.gate_up_proj.weight', 'model.layers.2.self_attn.k_norm.weight', 'model.layers.6.self_attn.qkv_proj.weight', 'model.layers.8.self_attn.o_proj.weight', 'model.layers.8.mlp.down_proj.weight', 'model.layers.10.mlp.gate_up_proj.weight', 'model.layers.7.post_attention_layernorm.weight', 'model.layers.9.self_attn.q_norm.weight', 'model.layers.8.self_attn.k_norm.weight', 'model.layers.0.mlp.down_proj.weight', 'model.layers.11.mlp.gate_up_proj.weight', 'model.layers.10.self_attn.k_norm.weight', 'model.layers.3.input_layernorm.weight', 'model.layers.4.post_attention_layernorm.weight', 'model.layers.10.input_layernorm.weight', 'model.layers.2.self_attn.q_norm.weight', 'model.layers.3.mlp.gate_up_proj.weight', 'model.layers.3.self_attn.q_norm.weight', 'model.layers.11.self_attn.q_norm.weight', 'model.l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: oop/__init__.py", line 96, in run (APIServer pid=90812) return __asyncio.run( (APIServer pid=90812) ~~~~~~~~~~~~~^ (APIServer pid=90812) wrapper(), (APIServer pid=90812) ^^^^^^^^^^ (APIServer pid=90812) ... ... (APIServ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3ForEmbedding no longer works bug ### Your current environment ### 🐛 Describe the bug trying to serve voyageai/voyage-4-nano, which is listed as supported on the embedding page results in the following. i use...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ntrypoints/cli/main.py", line 92, in main (APIServer pid=90812) args.dispatch_function(args) (APIServer pid=90812) ~~~~~~~~~~~~~~~~~~~~~~^^^^^^ (APIServer pid=90812) File "/home/anon/fiction_data/.venv/lib/python3.13/si...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rver pid=90812) ) as (engine_manager, coordinator, addresses, tensor_queue): (APIServer pid=90812) ^ (APIServer pid=90812) File "/home/anon/.local/share/uv/python/cpython-3.13.9-linux-x86_64-gnu/lib/python3.13/contextli...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
