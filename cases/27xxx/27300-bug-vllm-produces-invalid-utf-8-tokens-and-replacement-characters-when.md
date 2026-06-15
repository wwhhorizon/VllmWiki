# vllm-project/vllm#27300: [Bug]: vLLM produces invalid UTF-8 tokens and “�” replacement characters when returning logprobs

| 字段 | 值 |
| --- | --- |
| Issue | [#27300](https://github.com/vllm-project/vllm/issues/27300) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM produces invalid UTF-8 tokens and “�” replacement characters when returning logprobs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash # launch vllm server vllm serve facebook/opt-125m # In a separate terminal curl -X POST http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ --data-binary '{ "model": "facebook/opt-125m", "prompt": "In this example,", "temperature": 0, "top_p": 1, "logprobs": 0 }' | jq ``` Response ```bash "text": " the term “polarized” is used to refer to a region", "logprobs": { ..., "tokens": [ " the", " term", " �", "�", "p", "olar", "ized", "�", "�", " is", " used", " to", " refer", " to", " a", " region" ], "top_logprobs": [ { " the": -1.0254762172698975 }, { " term": -3.264568567276001 }, { " �": -0.8830230832099915 }, { "�": -0.13739712536334991 }, { "p": -4.646113872528076 }, { "olar": -3.0300464630126953 }, { "ized": -2.0098283290863037 }, { "�": -0.8669895529747009 }, ... ] }, ``` We use simple model "facebook/opt-125m" in our unit tests. The quotation marks were not correctly decoded but instead got "�" after moving to the new V1 engine. Fallback to V0 engine with `export VLLM_USE_V1=0` displays correct quotation marks. ``` ... "tokens": [ " the", " term", "", " “", "p", "olar", "ized", "", "”", " is",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: correctly decoded but instead got "�" after moving to the new V1 engine. Fallback to V0 engine with `export VLLM_USE_V1=0` displays correct quotation marks. ``` ... "tokens": [ " the", " term", "", " “", "p", "olar", "i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: book/opt-125m" in our unit tests. The quotation marks were not correctly decoded but instead got "�" after moving to the new V1 engine. Fallback to V0 engine with `export VLLM_USE_V1=0` displays correct quotation marks....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: etions \ -H "Content-Type: application/json" \ --data-binary '{ "model": "facebook/opt-125m", "prompt": "In this example,", "temperature": 0, "top_p": 1, "logprobs": 0 }' | jq ``` Response ```bash "text": " the term “po...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
