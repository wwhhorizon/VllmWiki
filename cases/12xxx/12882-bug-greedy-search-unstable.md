# vllm-project/vllm#12882: [Bug]: greedy search unstable

| 字段 | 值 |
| --- | --- |
| Issue | [#12882](https://github.com/vllm-project/vllm/issues/12882) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: greedy search unstable

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Even though I have set top_k=-1 and temperature=0, I still cannot get stable greedy search results. The following is my script for running the curl command 100 times. The return behavior of each execution 100 times is uncertain. Sometimes it is completely consistent, and sometimes there are several inconsistencies. ``` for i in {1..100}; do ( curl -s -X POST http://127.0.0.1:8081/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "llama3.1", "messages": [ { "role": "system", "content": "Please translate the below English text into Japanese." }, { "role": "user", "content": "Same with me. I must have been 11 or so. Nintendo is valued at over $85 billion" } ], "max_tokens": 1024, "temperature": 0.0, "top_p": 1.0, "top_k": -1, "repetition_penalty":1.05, "stop_token_ids": [128009], "seed":1234, "stream": false }' | jq -r '.choices[0].message.content' &) ; done ``` actual results ``` 私も同じでした。 11歳くらいだったと思います。 ニンテンドーの評価額は850億ドル以上です 私も同じでした。 11歳くらいだったと思います。 ニンテンドーの評価額は850億ドル以上です 私も同じでした。 11歳くらいだったと思います。 ニンテンドーの評価額は850億ドル以上です 私も同じでした。 11歳くらいだったと思います。 ニンテンドーの評価額は850億ドル以上です 私も同じでした。 11歳くらいだったと思います。 ニンテンドーの評価額は850億ドル以...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: it is completely consistent, and sometimes there are several inconsistencies. ``` for i in {1..100}; do ( curl -s -X POST http://127.0.0.1:8081/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: greedy search unstable bug;stale ### Your current environment ### 🐛 Describe the bug Even though I have set top_k=-1 and temperature=0, I still cannot get stable greedy search results. The following is my script...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: /chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "llama3.1", "messages": [ { "role": "system", "content": "Please translate the below English text into Japanese." }, { "role": "user", "content":...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rontend_api;hardware_porting;model_support;sampling_logits cuda;sampling;triton build_error env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ":1.05, "stop_token_ids": [128009], "seed":1234, "stream": false }' | jq -r '.choices[0].message.content' &) ; done ``` actual results ``` 私も同じでした。 11歳くらいだったと思います。 ニンテンドーの評価額は850億ドル以上です 私も同じでした。 11歳くらいだったと思います。 ニンテンドーの評...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
