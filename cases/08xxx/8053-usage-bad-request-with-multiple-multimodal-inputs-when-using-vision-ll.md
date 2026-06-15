# vllm-project/vllm#8053: [Usage]: Bad Request with multiple multimodal inputs when using vision LLM.

| 字段 | 值 |
| --- | --- |
| Issue | [#8053](https://github.com/vllm-project/vllm/issues/8053) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Bad Request with multiple multimodal inputs when using vision LLM.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I have tried InterVL and MimiCPM by requesting with multiple multimodal inputs, but both failed to response and it comes with bad request error. I have done some research and noticed some VLMs like phi-3 already support such inputs. https://github.com/vllm-project/vllm/issues/5820. Is this feature still under construction? or Did I miss anything? ### ONLINE INFER EXAMPLE ``` from openai import OpenAI client = OpenAI() response = client.chat.completions.create( model="xxx", messages=[ { "role": "user", "content": [ { "type": "text", "text": "What are in these images? Is there any difference between them?", }, { "type": "image_url", "image_url": { "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg", }, }, { "type": "image_url", "image_url": { "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg", }, }, ], } ], max_tokens=300, ) print(response.ch...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Bad Request with multiple multimodal inputs when using vision LLM. usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I have tried InterVL an...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: tion? or Did I miss anything? ### ONLINE INFER EXAMPLE ``` from openai import OpenAI client = OpenAI() response = client.chat.completions.create( model="xxx", messages=[ { "role": "user", "content": [ { "type": "text",...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed to response and it comes with bad request error. I have done some research and noticed some VLMs like phi-3 already support such inputs. https://github.com/vllm-project/vllm/issues/5820. Is this feature still under c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Bad Request with multiple multimodal inputs when using vision LLM. usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I have tried InterVL an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
