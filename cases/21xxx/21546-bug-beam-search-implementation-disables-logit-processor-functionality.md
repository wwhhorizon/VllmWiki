# vllm-project/vllm#21546: [Bug]: Beam search implementation disables logit processor functionality

| 字段 | 值 |
| --- | --- |
| Issue | [#21546](https://github.com/vllm-project/vllm/issues/21546) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Beam search implementation disables logit processor functionality

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi! Implementing `beam_search` outside of the engine and on top of `self.generate` has created a bug / faulty logic. In the `beam_search` function, to generate the next token you call `self.generate` with `max_length=1` instead of `llm_engine.step` directly. https://github.com/vllm-project/vllm/blob/a7272c23d09375515b58b213fc1599f203c6e4a7/vllm/entrypoints/llm.py#L690 https://github.com/vllm-project/vllm/blob/a7272c23d09375515b58b213fc1599f203c6e4a7/vllm/entrypoints/llm.py#L747 The [logit processors](https://github.com/vllm-project/vllm/blob/main/vllm/v1/sample/logits_processor.py) are called somewhere inside the engine in `execute_model` after `llm_engine.step`. Because for `self.generate` it's like it's predicting the first token in the answer at every step, the logit processors don't have access to the tokens generated so far, because the generation history is glued to the end of the prompt inside `beam_search`, and the prompt itself was never intended to be passed to the logit processors. The prompt and history are glued here at each iteration: https://github.com/vllm-project/vllm/blob/a7272c23d09375515b58b213fc1599f203c6e4a7...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: function is called directly inside `_beam_search`. Recreate: ```python import vllm model_name = "Qwen/Qwen3-8B" model = vllm.LLM(model=model_name, task="generate", max_model_len=32768, **{"compilation_config":{ "leve
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: /logits_processor.py) are called somewhere inside the engine in `execute_model` after `llm_engine.step`. Because for `self.generate` it's like it's predicting the first token in the answer at every step, the logit proce...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: , "use_cudagraph": False, "backend": "eager" }} ) question = "who was the person who escaped from alcatraz" prompt = f'Answer this question: \n{question}?\n /nothink' beam_width = 1 output = model.beam_search(
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Beam search implementation disables logit processor functionality bug;stale ### Your current environment ### 🐛 Describe the bug Hi! Implementing `beam_search` outside of the engine and on top of `self.generate` h...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Beam search implementation disables logit processor functionality bug;stale ### Your current environment ### 🐛 Describe the bug Hi! Implementing `beam_search` outside of the engine and on top of `self.generate` has c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
