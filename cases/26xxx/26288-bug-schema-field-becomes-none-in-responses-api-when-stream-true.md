# vllm-project/vllm#26288: [Bug]: `schema` field becomes `None` in Responses API when `stream=True`

| 字段 | 值 |
| --- | --- |
| Issue | [#26288](https://github.com/vllm-project/vllm/issues/26288) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `schema` field becomes `None` in Responses API when `stream=True`

### Issue 正文摘录

### Your current environment vllm: 0.10.2 openai: 1.108.0 ### 🐛 Describe the bug #### 1. **Client Request Arrives** ```python stream = await client.responses.create( model=model, input=formatted_prompt, text={"format": {"name": "schema_ner", "schema": json_schema, "type": "json_schema", "strict": True}}, stream=True, ) ``` #### 2. **FastAPI/Pydantic Parses the Request** At `vllm/entrypoints/openai/api_server.py:516`: ```python async def create_responses(request: ResponsesRequest, raw_request: Request): ``` The JSON is parsed into a `ResponsesRequest` object where: - `text` field is type `Optional[ResponseTextConfig]` (from OpenAI library) - Inside that, `format` is type `ResponseFormatTextConfig` (a Union type) - When `type="json_schema"`, it becomes `ResponseFormatTextJSONSchemaConfig` #### 3. **Pydantic Field Alias Mapping** The OpenAI library defines the schema field with an alias: ```python # openai/types/responses/response_format_text_json_schema_config.py class ResponseFormatTextJSONSchemaConfig(BaseModel): schema_: Dict[str, object] = FieldInfo(alias="schema") # Note: field name has underscore, alias doesn't ``` **Pydantic's behavior:** - Sees JSON key: `"schema": {...}` -...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Request Arrives** ```python stream = await client.responses.create( model=model, input=formatted_prompt, text={"format": {"name": "schema_ner", "schema": json_schema, "type": "json_schema", "strict": True}}, stream=True...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: `schema` field becomes `None` in Responses API when `stream=True` bug;stale ### Your current environment vllm: 0.10.2 openai: 1.108.0 ### 🐛 Describe the bug #### 1. **Client Request Arrives** ```python stream = await...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: mes `ResponseFormatTextJSONSchemaConfig` #### 3. **Pydantic Field Alias Mapping** The OpenAI library defines the schema field with an alias: ```python # openai/types/responses/response_format_text_json_schema_config.py...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
