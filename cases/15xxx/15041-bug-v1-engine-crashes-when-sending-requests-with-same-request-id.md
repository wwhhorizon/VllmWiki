# vllm-project/vllm#15041: [Bug]: V1 Engine crashes when sending requests with same request id

| 字段 | 值 |
| --- | --- |
| Issue | [#15041](https://github.com/vllm-project/vllm/issues/15041) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 Engine crashes when sending requests with same request id

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Caller to the OpenAI Server can set request_id arbitarily. If sending requests with duplicate request_id to OpenAI Server, the V1 Engine will crash immediately. Below is an example how to trigger this bug. ```python from openai import OpenAI openai_api_key = "EMPTY" openai_base_url = "http://localhost:8800/v1" if __name__ == "__main__": client = OpenAI(api_key=openai_api_key, base_url=openai_base_url) prompt = "Write a one-sentence bedtime story about a unicorn." request_id = "test" model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B" completion = client.completions.create( model=model, prompt=prompt, max_tokens=10, extra_headers={ "X-Request-Id": request_id }, ) completion = client.completions.create( model=model, prompt=prompt, max_tokens=10, extra_headers={ "X-Request-Id": request_id }, ) ``` vllm reports the following error. ```text INFO: Started server process [2095823] INFO: Waiting for application startup. INFO: Application startup complete. INFO 03-18 14:46:40 [logger.py:39] Received request cmpl-test-0: prompt: 'Write a one-sentence bedtime story about a unicorn.', params: SamplingParams(n=1, presence_penalty=0.0, frequen...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ely. Below is an example how to trigger this bug. ```python from openai import OpenAI openai_api_key = "EMPTY" openai_base_url = "http://localhost:8800/v1" if __name__ == "__main__": client = OpenAI(api_key=openai_api_k...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: V1 Engine crashes when sending requests with same request id bug ### Your current environment ### 🐛 Describe the bug Caller to the OpenAI Server can set request_id arbitarily. If sending requests with duplicate r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: , stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=10, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=T...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ne-sentence bedtime story about a unicorn." request_id = "test" model = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B" completion = client.completions.create( model=model, prompt=prompt, max_tokens=10, extra_headers={ "X-R...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
