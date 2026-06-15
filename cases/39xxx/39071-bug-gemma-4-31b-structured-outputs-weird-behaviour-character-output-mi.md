# vllm-project/vllm#39071: [Bug]: Gemma 4 31B Structured Outputs weird behaviour / character output - might be a quick solve

| 字段 | 值 |
| --- | --- |
| Issue | [#39071](https://github.com/vllm-project/vllm/issues/39071) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: Gemma 4 31B Structured Outputs weird behaviour / character output - might be a quick solve

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using guided regex since one year now, and it **worked fine with Gemma 3 27B**, Mistral and other LLMs. I appreciate the work of vLLM! To be more precise, I'm using it for Aspect-based Sentiment Analysis (ABSA). Given a text, e.g. "The pizza is delicious", ABSA extracts aspect term ("pizza"), category ("food general"), and sentiment ("positive"). However, I noticed weird behavior of Gemma 4 31B now in predicting the aspect term. Although I provide 100 (!) few-shot examples (see prompt here [prompt_temp.txt](https://gist.github.com/NilsHellwig/12d29f2092513f80013d8d26949ef265#file-prompt_temp-txt)), in most cases, Gemma 4 predicts ".", ",", or ":" as the aspect term which doesn't make any sense. Notably, I even use guided regex (**works fine with Gemma 3 27B**) to guide the LLM in predicting a valid list of (aspect term, aspect category, polarity) - tuples (see [regex_temp.txt](https://gist.github.com/NilsHellwig/12d29f2092513f80013d8d26949ef265#file-regex_temp-txt)). My regex allows any substring of the given text for the aspect term, although "." is very unrealistic. Code is here: [vllm_guided.py](https://gist.github.com/Nil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: and it **worked fine with Gemma 3 27B**, Mistral and other LLMs. I appreciate the work of vLLM! To be more precise, I'm using it for Aspect-based Sentiment Analysis (ABSA). Given a text, e.g. "The pizza is delicious", A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .** ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma 4 31B Structured Outputs weird behaviour / character output - might be a quick solve bug ### Your current environment ### 🐛 Describe the bug I'm using guided regex since one year now, and it **worked fine w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Gemma 4 31B Structured Outputs weird behaviour / character output - might be a quick solve bug ### Your current environment ### 🐛 Describe the bug I'm using guided regex since one year now, and it **worked fine w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
