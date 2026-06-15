# vllm-project/vllm#14897: [Bug]: Gemma3 Offline Batch Inference: Attempted to assign XXX multimodal tokens to YYY placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#14897](https://github.com/vllm-project/vllm/issues/14897) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma3 Offline Batch Inference: Attempted to assign XXX multimodal tokens to YYY placeholders

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug @WoosukKwon This error is likely a processor-related error. The error happens for both llm.chat() and llm.generate(). It says `Attempted to assign XXX multimodal tokens to YYY placeholders`. This error only happens when there are image inputs, but is arbitrary to image (i.e. it remains when replacing images with other images). This error happens only when `len(messages)>=32`, i.e. if I input messages individually for `len(messages)` times or using a mini-batched version, it does not raise an error. Minimum reproduction example: ``` from vllm import LLM, SamplingParams import torch if __name__ == '__main__': model = LLM( model="google/gemma-3-27b-it", max_model_len=8192, tensor_parallel_size=1, limit_mm_per_prompt={"image": 5}, tokenizer_mode="auto" ) sampling_params = SamplingParams(temperature=1,max_tokens=8192,stop_token_ids=None) messages = torch.load("messages.pt") # contanins 64 messages, the error does not matter whether you input any image or not response = model.chat( messages=messages, sampling_params=sampling_params, chat_template=None, ) outputs = [] for out in response: generated_text = out.outputs[0].text outputs.app...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e are image inputs, but is arbitrary to image (i.e. it remains when replacing images with other images). This error happens only when `len(messages)>=32`, i.e. if I input messages individually for `len(messages)` times...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma3 Offline Batch Inference: Attempted to assign XXX multimodal tokens to YYY placeholders bug ### Your current environment ### 🐛 Describe the bug @WoosukKwon This error is likely a processor-related error. The
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 16 12:28:39 [core.py:340] output = self.model_executor.execute_model(scheduler_output) ERROR 03-16 12:28:39 [core.py:340] File "/home/agi/vllm/vllm/v1/executor/abstract.py", line 80, in execute_model ERROR 03-16 12:28:3...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;slowdown env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
