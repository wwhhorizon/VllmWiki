# vllm-project/vllm#37855: [Bug]: Qwen3-VL-Embedding-8B Image embedding failed

| 字段 | 值 |
| --- | --- |
| Issue | [#37855](https://github.com/vllm-project/vllm/issues/37855) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-Embedding-8B Image embedding failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug infer, Qwen3-VL-Embedding-8B Image embedding failed and report follow error: ``` root@pod-1484515165640695808:/vllm-workspace/vllm# python examples/pooling/embed/vision_embedding_online.py --model qwen3_vl Text embedding output: Embeddings: [-0.0052810548804700375, -0.004405908286571503, -0.015692276880145073, 0.006910637486726046, ...] (size=4096) Image embedding output: Traceback (most recent call last): File "/vllm-workspace/vllm/examples/pooling/embed/vision_embedding_online.py", line 415, in main(args) File "/vllm-workspace/vllm/examples/pooling/embed/vision_embedding_online.py", line 410, in main model_example_map[args.model](client, model_id) File "/vllm-workspace/vllm/examples/pooling/embed/vision_embedding_online.py", line 201, in run_qwen3_vl response = create_chat_embeddings( ^^^^^^^^^^^^^^^^^^^^^^^ File "/vllm-workspace/vllm/examples/pooling/embed/vision_embedding_online.py", line 43, in create_chat_embeddings return client.post( ^^^^^^^^^^^^ File "/usr/local/python3.11.14/lib/python3.11/site-packages/openai/_base_client.py", line 1297, in post return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL-Embedding-8B Image embedding failed bug ### Your current environment ### 🐛 Describe the bug infer, Qwen3-VL-Embedding-8B Image embedding failed and report follow error: ``` root@pod-1484515165640695808:/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error;crash env_dependency You...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: nai/_base_client.py", line 1297, in post return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/pytho...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _porting;model_support;multimodal_vlm;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
