# vllm-project/vllm#10559: [Bug]: Speculative Decoding without enabling eager mode returns gibberish output after some tokens.

| 字段 | 值 |
| --- | --- |
| Issue | [#10559](https://github.com/vllm-project/vllm/issues/10559) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Speculative Decoding without enabling eager mode returns gibberish output after some tokens.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After some tokens, the output of a model with speculative decoding enabled under default conditions seems to be random garbage tokens. For example, with `vllm serve meta-llama/Llama-3.2-3B-Instruct --speculative-model meta-llama/Llama-3.2-3B-Instruct --num-speculative-tokens 8`: ``` curl http://localhost:8000/v1/completions -H "Content-Type: application/json" -d '{ "prompt": "I need to solve the puzzle with missing words. Both mis sing words should be anagrams. I blank that she always blank her glasses at home.", "max_tokens": 512, "temperature": 0.7, "model": "meta-llama/Llama-3.2-3B-Instruct"}' {"id":"cmpl-74ba09b9467849aab7f1ae4c6024b6c3","object":"text_completion","created":1732236573,"model":"meta-llama/Llama-3.2-3B-Instruct","choices":[{"index":0,"text":" \nClue: The wordpla y is based on a humorous interpretation of blind.\nAre the complete sentences correctly formatted with proper verb conjugation as follows?\n\"She sees her glasses at _______ (home, home i s blind ..., etc.)\"\n\ncan (home).\ncan isBlind.\nuse home..\ncan, isBlind is but loose so it can be “indisclable”. otherwise ones...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: and pris breakout simply alone already fragmented entity situations participate identified forgot th en meanwhile insight creature she resembled and immediately became not peach supported passed revised guilt scale grap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: arvation une apple Del green signal iron acidic idea says four richest cosmic rats regions subordinate GM strongest roman war stimulating colours ਪ hide Behavior ver informed stu died bore Bot concludes election give pe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: output after some tokens. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After some tokens, the output of a model with speculative decoding enabled under default condit...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Speculative Decoding without enabling eager mode returns gibberish output after some tokens. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After some tokens, the
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
