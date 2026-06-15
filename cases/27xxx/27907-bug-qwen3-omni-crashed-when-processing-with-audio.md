# vllm-project/vllm#27907: [Bug]:  qwen3-omni Crashed when processing with audio

| 字段 | 值 |
| --- | --- |
| Issue | [#27907](https://github.com/vllm-project/vllm/issues/27907) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  qwen3-omni Crashed when processing with audio

### Issue 正文摘录

### Your current environment I use the daily docker image build. 2025-11-1 I run `pip install vllm[audio]` ### 🐛 Describe the bug I send a request: ```json { "messages": [ { "content": "请将这段中文语音转换为纯文本。", "role": "system" }, { "content": [ { "audio_url": { "url": "http://172.21.30.114:8092/tanqi-diting/pub/files/620" }, "type": "audio_url" } ], "role": "user" } ], "model": "qwen3-omni-30b", "frequency_penalty": 1.0, "temperature": 0.3, "top_p": 0.95 } ``` It crashed, the log is: ```shell (APIServer pid=1) INFO 11-01 10:51:02 [api_server.py:1648] Supported tasks: ['generate'] (APIServer pid=1) INFO 11-01 10:51:02 [serving_responses.py:203] "auto" tool choice has been enabled please note that while the parallel_tool_calls client option is preset for compatibility reasons, it will be ignored. (APIServer pid=1) INFO 11-01 10:51:02 [serving_engine.py:282] "auto" tool choice has been enabled please note that while the parallel_tool_calls client option is preset for compatibility reasons, it will be ignored. (APIServer pid=1) INFO 11-01 10:51:02 [api_server.py:1934] Starting vLLM API server 0 on http://0.0.0.0:8000 (APIServer pid=1) INFO 11-01 10:51:02 [launcher.py:38] Available routes ar...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: processing with audio bug ### Your current environment I use the daily docker image build. 2025-11-1 I run `pip install vllm[audio]` ### 🐛 Describe the bug I send a request: ```json { "messages": [ { "content": "请将这段中文语...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: qwen3-omni Crashed when processing with audio bug ### Your current environment I use the daily docker image build. 2025-11-1 I run `pip install vllm[audio]` ### 🐛 Describe the bug I send a request: ```json { "me
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: -11-1 I run `pip install vllm[audio]` ### 🐛 Describe the bug I send a request: ```json { "messages": [ { "content": "请将这段中文语音转换为纯文本。", "role": "system" }, { "content": [ { "audio_url": {
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ods: POST (APIServer pid=1) INFO 11-01 10:51:02 [launcher.py:46] Route: /scale_elastic_ep, Methods: POST (APIServer pid=1) INFO 11-01 10:51:02 [launcher.py:46] Route: /is_scaling_elastic_ep, Methods: POST (APIServer pid...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ntinue using the slow processor, instantiate this class with `use_fast=False`. Note that this behavior will be extended to all models in a future release. (APIServer pid=1) INFO 11-01 10:54:05 [chat_utils.py:547] Detect...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
