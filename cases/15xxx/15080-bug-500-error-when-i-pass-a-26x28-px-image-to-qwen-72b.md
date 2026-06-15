# vllm-project/vllm#15080: [Bug]: 500 error when I pass a 26x28 px image to Qwen 72B

| 字段 | 值 |
| --- | --- |
| Issue | [#15080](https://github.com/vllm-project/vllm/issues/15080) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 500 error when I pass a 26x28 px image to Qwen 72B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 500 error when passing an image with one side :8080/v1" openai_api_key = "EMPTY" def request(turns, guidance=None, temperature=0.0, max_tokens=1024): global oai_client if oai_client is None: oai_client = OpenAI( api_key=openai_api_key, base_url=openai_api_base, ) if not isinstance(turns, list): turns = [turns] result = oai_client.chat.completions.create( model="Qwen/Qwen2.5-VL-72B-Instruct", temperature=temperature, max_tokens=max_tokens, messages=turns, extra_body=guidance, n=1, ) return {"role": "assistant", "content": result.choices[0].message.content} if __name__ == "__main__": futures = [] frame_image = Image.fromarray(255 * np.ones((26, 28, 3), dtype=np.uint8)) box_request = user( image(frame_image), text( "This is a reproduction of a bug for VLLM. Your efforts are wasted. Please do not try. " ), ) request([box_request]) ``` I just get a 500 error in the server logs. Nothing else. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequentl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: 500 error when I pass a 26x28 px image to Qwen 72B bug ### Your current environment ### 🐛 Describe the bug 500 error when passing an image with one side :8080/v1" openai_api_key = "EMPTY" def request(turns, guida...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: passing an image with one side :8080/v1" openai_api_key = "EMPTY" def request(turns, guidance=None, temperature=0.0, max_tokens=1024): global oai_client if oai_client is None: oai_client = OpenAI( api_key=openai_api_key...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
