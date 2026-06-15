# vllm-project/vllm#36759: [Bug]: 在910b4上使用vLLM 部署 Qwen/Qwen3-VL-Reranker-2B报错

| 字段 | 值 |
| --- | --- |
| Issue | [#36759](https://github.com/vllm-project/vllm/issues/36759) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 在910b4上使用vLLM 部署 Qwen/Qwen3-VL-Reranker-2B报错

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 在昇腾910b4上使用vLLM 使用官方文档推荐的命令部署 Qwen/Qwen3-VL-Reranker-2B报错： 1、命令如下： vllm serve Qwen/Qwen3-VL-Reranker-2B \ --runner pooling \ --max-model-len 4096 \ --hf_overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \ --chat-template examples/pooling/score/template/qwen3_vl_reranker.jinja 2、报错如下： (EngineCore_DP0 pid=1424) INFO 03-11 08:10:39 [compilation.py:863] Using OOT custom backend for compilation. Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 23.00it/s] (EngineCore_DP0 pid=1424) (EngineCore_DP0 pid=1424) ERROR 03-11 08:10:43 [core.py:946] EngineCore failed to start. (EngineCore_DP0 pid=1424) ERROR 03-11 08:10:43 [core.py:946] Traceback (most recent call last): (EngineCore_DP0 pid=1424) ERROR 03-11 08:10:43 [core.py:946] File "/vllm-workspace/vllm/vllm/v1/engine/core.py", line 937, in run_engine_core (EngineCore_DP0 pid=1424) ERROR 03-11 08:10:43 [core.py:946] engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs) (EngineCore_DP0 pid...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: 在910b4上使用vLLM 部署 Qwen/Qwen3-VL-Reranker-2B报错 bug ### Your current environment ### 🐛 Describe the bug 在昇腾910b4上使用vLLM 使用官方文档推荐的命令部署 Qwen/Qwen3-VL-Reranker-2B报错： 1、命令如下： vllm serve Qwen/Qwen3-VL-Reranker-2B \ --run...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _DP0 pid=1424) INFO 03-11 08:10:39 [compilation.py:863] Using OOT custom backend for compilation. Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s] Loading safetensors checkpoint shards: 100% Co...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: unner pooling \ --max-model-len 4096 \ --hf_overrides '{"architectures": ["Qwen3VLForSequenceClassification"],"classifier_from_token": ["no", "yes"],"is_original_qwen3_reranker": true}' \ --chat-template examples/poolin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 08:10:43 [core.py:946] score_layer = language_model.score if is_vlm else model.score (EngineCore_DP0 pid=1424) ERROR 03-11 08:10:43 [core.py:946] ^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=1424) ERROR 03-11 08:10:43 [core...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
