# vllm-project/vllm#10293: [Bug]: Can't use yarn rope config for long context in Qwen2 model

| 字段 | 值 |
| --- | --- |
| Issue | [#10293](https://github.com/vllm-project/vllm/issues/10293) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't use yarn rope config for long context in Qwen2 model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I add rope config in Qwen/Qwen2-72B-Instruct/config.json ``` json "rope_scaling": { "factor": 4.0, "original_max_position_embeddings": 32768, "type": "yarn" } ``` I get transformers warning: ``` "Unrecognized keys in `rope_scaling` for 'rope_type'='yarn': {'original_max_position_embeddings'}" ``` And, when LLM's input length is shorter than original_position_embedding_len, the response is OK. However, if input's len is larger than 32768(original_position_embedding_len), the model's output will be something confusing, similar to a kind of repetition of the input. this error happened in the version of 0.6.3.post1, but when I switch to v0.6.0, everything is OK. I find that transformers's repo from recent versions don't accept "original_max_position_embeddings", but vllm need it. Maybe this is a confict between transformers and vllm ? Does anyone know how to correctly enable the long context feature? Thanks ^_^ PS: I can't run collect_env.py script in v0.6.0's docker image, but 0.6.3.post1's docker image is OK. PPS: I just search issues about "original_max_position_embeddings", but got nothing...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: similar to a kind of repetition of the input. this error happened in the version of 0.6.3.post1, but when I switch to v0.6.0, everything is OK. I find that transformers's repo from recent versions don't accept "original...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Can't use yarn rope config for long context in Qwen2 model bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I add rope config in Qwen/Qwen2-72B-Instruct/confi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .6.0's docker image, but 0.6.3.post1's docker image is OK. PPS: I just search issues about "original_max_position_embeddings", but got nothing releated. ### Before submitting a new issue... - [X] Make sure you already s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Can't use yarn rope config for long context in Qwen2 model bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug when I add rope config in Qwen/Qwen2-72B-Instruct/confi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
