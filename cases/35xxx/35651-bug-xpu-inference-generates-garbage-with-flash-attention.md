# vllm-project/vllm#35651: [Bug][XPU]: Inference generates garbage with flash attention

| 字段 | 值 |
| --- | --- |
| Issue | [#35651](https://github.com/vllm-project/vllm/issues/35651) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][XPU]: Inference generates garbage with flash attention

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using flash attention, garbage text is generated often. It breaks tool calling with this model because the model will often generate some invalid JSON string that python cannot parse. Triton attention seems OK. ### ⚡ Flash Attention test Using `vllm serve` with flash attention: ``` CCL_TOPO_FABRIC_VERTEX_CONNECTION_CHECK=0 VLLM_SLEEP_WHEN_IDLE=1 \ vllm serve mistralai/Devstral-Small-2-24B-Instruct-2512 --tool-call-parser mistral \ --enable-auto-tool-choice --port 8080 --max-model-len 96K --gpu-memory-utilization 0.95 \ --max-num-seqs 1 --tensor-parallel-size 2 --enforce-eager ``` Using `mistral-vibe` to prompt the model (output below). Garbage locations: * Line 1: `relatedE for too,6 we,` * Lines 64-67 ### 🔱 Triton Attention test Using `vllm serve` with triton attention: ``` CCL_TOPO_FABRIC_VERTEX_CONNECTION_CHECK=0 VLLM_SLEEP_WHEN_IDLE=1 \ vllm serve mistralai/Devstral-Small-2-24B-Instruct-2512 --tool-call-parser mistral \ --enable-auto-tool-choice --port 8080 --max-model-len 96K --gpu-memory-utilization 0.95 \ --max-num-seqs 1 --tensor-parallel-size 2 --enforce-eager --attention-backend TRITON_ATTN ``` Using `mistral-vibe`...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][XPU]: Inference generates garbage with flash attention bug ### Your current environment ### 🐛 Describe the bug When using flash attention, garbage text is generated often. It breaks tool calling with this model be...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: NECTION_CHECK=0 VLLM_SLEEP_WHEN_IDLE=1 \ vllm serve mistralai/Devstral-Small-2-24B-Instruct-2512 --tool-call-parser mistral \ --enable-auto-tool-choice --port 8080 --max-model-len 96K --gpu-memory-utilization 0.95 \ --m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ntion, garbage text is generated often. It breaks tool calling with this model because the model will often generate some invalid JSON string that python cannot parse. Triton attention seems OK. ### ⚡ Flash Attention te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
