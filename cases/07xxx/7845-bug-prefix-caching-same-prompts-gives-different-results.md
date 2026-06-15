# vllm-project/vllm#7845: [Bug]: Prefix Caching same prompts gives different results

| 字段 | 值 |
| --- | --- |
| Issue | [#7845](https://github.com/vllm-project/vllm/issues/7845) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Prefix Caching same prompts gives different results

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug If you enable prefix caching, the 2nd time you call VLLM, the output is different from the first run. I'm assuming this isn't supposed to happen right? ```python vllm serve unsloth/Meta-Llama-3.1-8B-Instruct \ --max-model-len 16384 \ --kv-cache-dtype fp8 \ --quantization fp8 \ --dtype bfloat16 \ --seed 3407 \ --uvicorn-log-level debug \ --enable-prefix-caching ``` I tested prefix caching on ```python messages = [{"role": "user", "content": "Create a Flappy Bird Game."}] stream = client.chat.completions.create( model = "unsloth/Meta-Llama-3.1-8B-Instruct", messages = messages, stream = False, temperature = 0, ) messages += [{"role" : "assistant", "content" : stream.choices[0].message.content}, {"role": "user", "content": "List any issues with your code."}] stream = client.chat.completions.create( model = "unsloth/Meta-Llama-3.1-8B-Instruct", messages = messages, stream = False, ) messages += [{"role" : "assistant", "content" : stream.choices[0].message.content}, {"role": "user", "content": "Now make the game better."}] stream = client.chat.completions.create( model = "unsloth/Meta-Llama-3.1-8B-Instruct", messages = messages, strea...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: loth/Meta-Llama-3.1-8B-Instruct \ --max-model-len 16384 \ --kv-cache-dtype fp8 \ --quantization fp8 \ --dtype bfloat16 \ --seed 3407 \ --uvicorn-log-level debug \ --enable-prefix-caching ``` I tested prefix caching on `...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;quan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: I'm assuming this isn't supposed to happen right? ```python vllm serve unsloth/Meta-Llama-3.1-8B-Instruct \ --max-model-len 16384 \ --kv-cache-dtype fp8 \ --quantization fp8 \ --dtype bfloat16 \ --seed 3407 \ --uvicorn-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g this isn't supposed to happen right? ```python vllm serve unsloth/Meta-Llama-3.1-8B-Instruct \ --max-model-len 16384 \ --kv-cache-dtype fp8 \ --quantization fp8 \ --dtype bfloat16 \ --seed 3407 \ --uvicorn-log-level d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
