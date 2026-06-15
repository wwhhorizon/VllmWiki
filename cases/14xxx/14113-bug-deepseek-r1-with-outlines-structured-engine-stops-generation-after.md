# vllm-project/vllm#14113: [Bug]: DeepSeek R1 with outlines structured engine stops generation after `</think>`

| 字段 | 值 |
| --- | --- |
| Issue | [#14113](https://github.com/vllm-project/vllm/issues/14113) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: DeepSeek R1 with outlines structured engine stops generation after `</think>`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --enable-reasoning --reasoning-parser deepseek_r1 --enforce-eager ``` Runs with this example. It falls back to outlines engine because it has Enum in the JSON schema (Our xgrammar does not support this), and will generate token ids until . Then it stops. Did not encounter it with xgrammar. ```python # Guided decoding by JSON using Pydantic schema class CarType(str, Enum): sedan = "sedan" suv = "SUV" truck = "Truck" coupe = "Coupe" class CarDescription(BaseModel): brand: str model: str car_type: CarType json_schema = CarDescription.model_json_schema() prompt = ("Generate a JSON with the brand, model and car_type of" "the most iconic car from the 90's, think in 100 tokens") completion = client.chat.completions.create( model=model, messages=[{ "role": "user", "content": prompt, }], extra_body={"guided_json": json_schema}, ) print("reasoning_content: ", completion.choices[0].message.reasoning_content) print("content: ", completion.choices[0].message.content) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug ``` vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --enable-reasoning --reasoning-parser deepseek_r1 --enforce-eager ``` Runs with this example. It falls back to outlines engine because it h...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: uild;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
