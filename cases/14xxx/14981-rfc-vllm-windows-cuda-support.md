# vllm-project/vllm#14981: [RFC]: vLLM Windows CUDA support

| 字段 | 值 |
| --- | --- |
| Issue | [#14981](https://github.com/vllm-project/vllm/issues/14981) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: vLLM Windows CUDA support

### Issue 正文摘录

### Motivation. _**Use cases:**_ **- AI open source community**: Currently, llama.cpp and ollama are the main backend for serving open source AI models to non-developer users, used by Oobabooga, LM Studio and others. Non-devs AI users are 99% on Windows. One thing I hate about current AI from a normal user point of view is the constant wheel reinvention. We can't have 25 server types, 5000 kernels with different optimizations depending which engine and server you choose, and 10 quantization types. Such fragmentation causes fatigue, and non-dev users become lost when trying to get in the AI world, forgetting about it. "Do you want to try Phi-4? Install this project, and his 400 dependencies. Do you want to try Deepseek? Install that project and his 500 dependencies. Do you want to try Llama Coder? Nice, install that another one project with 800 dependencies. Oh wait, that last one requires Cuda 11.8, but you have Cuda 12.4 that is required by the first one. Oh! The second one is broken because need Cuda 12.6 newest features." What a mess. vLLM is the best server for serving AI models, and I think is a must to become adopted by those UI projects, so they can stop reinventing the whe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: I hate about current AI from a normal user point of view is the constant wheel reinvention. We can't have 25 server types, 5000 kernels with different optimizations depending which engine and server you choose, and 10 q...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [RFC]: vLLM Windows CUDA support RFC ### Motivation. _**Use cases:**_ **- AI open source community**: Currently, llama.cpp and ollama are the main backend for serving open source AI models to non-developer users, used b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: otivation. _**Use cases:**_ **- AI open source community**: Currently, llama.cpp and ollama are the main backend for serving open source AI models to non-developer users, used by Oobabooga, LM Studio and others. Non-dev...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: AI open source community**: Currently, llama.cpp and ollama are the main backend for serving open source AI models to non-developer users, used by Oobabooga, LM Studio and others. Non-devs AI users are 99% on Windows. O...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: erent optimizations depending which engine and server you choose, and 10 quantization types. Such fragmentation causes fatigue, and non-dev users become lost when trying to get in the AI world, forgetting about it. "Do...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
