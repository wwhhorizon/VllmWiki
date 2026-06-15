# vllm-project/vllm#30445: [Bug]: QuantTrio/MiniMax-M2-AWQ produces garbage in 12/10/2025 build

| 字段 | 值 |
| --- | --- |
| Issue | [#30445](https://github.com/vllm-project/vllm/issues/30445) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: QuantTrio/MiniMax-M2-AWQ produces garbage in 12/10/2025 build

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The model was working fine with yesterday's VLLM build (12/9/2025), but is broken with today's build (12/10/2025 as of 3pm PST). The model outputs gibberish when accessed through the completions endpoint: ```bash $ curl -X POST http://spark:8888/v1/chat/completions -H "Content-Type: application/json" -H "Authorization: Bearer none" -d '{ "model": "QuantTrio/MiniMax-M2-AWQ", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is a capital of France?"} ], "max_tokens": 100 }' {"id":"chatcmpl-a7c240e8b248aa65","object":"chat.completion","created":1765415001,"model":"QuantTrio/MiniMax-M2-AWQ","choices":[{"index":0,"message":{"role":"assistant","content":" We need to answer the question: \"What isIs 'the's capital the capital of France? France's capital?\" The question: \"What is France's capital? 'Is's\" '?\"?capital\"is\"s's'thecapital'scapital\"the?the\"????\"?\" \"What\"thecapital??\"is'thecapital's?\"??'s'capitalcapital\"?\"'s?\"?\"capital?\"France's capital's capital's\" ?capital's","refusal":null,"annotations":null,"audio":null,"function_call":null,"tool_calls":[],"reas...

## 现有链接修复摘要

#30486 [BugFix] Fix minimax m2 model partial_rotary_factor

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: QuantTrio/MiniMax-M2-AWQ produces garbage in 12/10/2025 build bug ### Your current environment ### 🐛 Describe the bug The model was working fine with yesterday's VLLM build (12/9/2025), but is broken with today's...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --host 0.0.0.0 --gpu-memory-utilization 0.7 -tp 2 --distributed-executor-backend ray --max-model-len 128000 --load-format fastsafetensors --enable-auto-tool-choice --tool-call-parser minimax_m2 --reasoning-parser minima...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: QuantTrio/MiniMax-M2-AWQ produces garbage in 12/10/2025 build bug ### Your current environment ### 🐛 Describe the bug The model was working fine with yesterday's VLLM build (12/9/2025), but is broken with today's...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: et. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 5 build bug ### Your current environment ### 🐛 Describe the bug The model was working fine with yesterday's VLLM build (12/9/2025), but is broken with today's build (12/10/2025 as of 3pm PST). The model outputs gibberis...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30486](https://github.com/vllm-project/vllm/pull/30486) | closes_keyword | 0.95 | [BugFix] Fix minimax m2 model partial_rotary_factor | fixed an inference issue with MiniMax-M2, but this caused some community-contributed quantized models to fail(#30445), some of which were forked before I added `partial_rotary_fact |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
