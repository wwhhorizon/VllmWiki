# vllm-project/vllm#34532: [Bug]: Realtime API crashes when client terminates connection "incorrectly"

| 字段 | 值 |
| --- | --- |
| Issue | [#34532](https://github.com/vllm-project/vllm/issues/34532) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Realtime API crashes when client terminates connection "incorrectly"

### Issue 正文摘录

### Your current environment I have an Nvidia GeForce RTX 3090 and I'm running this stuff within a Docker environment. I am unable to run your environment collecting scripts because it is not designed to run in a generic Python environment that does not have vLLM installed. Perhaps a fallback that would provide what information is available would have been useful here. ### 🐛 Describe the bug I decided I would try to give Voxtral Mini 4B 2602 a shot. Apparently, it's designed for real-time streaming, unlike what I've been using. It's also advertised to be production ready with vLLM's Realtime API. Unfortunately, it seems that whoever wrote that did not share my view of what production-ready means. First, I have to use a `nightly` image. I fail to see how that's production-ready, but okay. To me, production ready also means that a server should not crash if a client sends a malformed or unexpected request. I'm here to report that the vLLM server crashes completely if the client terminates the Realtime API WebSocket connection in an "unexpected" way. In order to reproduce this bug, please follow these steps: 1. You will need to run vLLM with the `mistralai/Voxtral-Mini-4B-Realtime-26...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: t I have an Nvidia GeForce RTX 3090 and I'm running this stuff within a Docker environment. I am unable to run your environment collecting scripts because it is not designed to run in a generic Python environment that d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: at a server should not crash if a client sends a malformed or unexpected request. I'm here to report that the vLLM server crashes completely if the client terminates the Realtime API WebSocket connection in an "unexpect...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: es not have vLLM installed. Perhaps a fallback that would provide what information is available would have been useful here. ### 🐛 Describe the bug I decided I would try to give Voxtral Mini 4B 2602 a shot. Apparently,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: mistralai/Voxtral-Mini-4B-Realtime-2602 --host 0.0.0.0 --port 8001 --dtype bfloat16 --tokenizer-mode mistral --config-format mistral --load-format mistral --trust-remote-code --compilation-config '{"cudagraph_mode":"PIE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: "incorrectly" bug ### Your current environment I have an Nvidia GeForce RTX 3090 and I'm running this stuff within a Docker environment. I am unable to run your environment collecting scripts because it is not designed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
