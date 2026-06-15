# vllm-project/vllm#14651: [Usage]: how to cache the lora adapter in memory

| 字段 | 值 |
| --- | --- |
| Issue | [#14651](https://github.com/vllm-project/vllm/issues/14651) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to cache the lora adapter in memory

### Issue 正文摘录

### Your current environment I want to build a multi-lora service, but the following code seems to reload the Lora adapter every time ```python class LoraModule(BaseModel): name: str path: str class UserRequest(BaseModel): lora_module: list[LoraModule] question: str @app.post("/") async def multi_loras(req: UserRequest): params = SamplingParams(max_tokens=512) tokenizer = await engine.get_tokenizer() messages = tokenizer.apply_chat_template( [{"role": "user", "content": req.question}], tokenize=False, add_generation_prompt=True, ) output = [] for i, lora in enumerate(req.lora_module): generator = engine.generate( messages, sampling_params=params, lora_request=LoRARequest( lora_name=lora.name, lora_path=lora.path, lora_int_id=i, ), request_id=str(uuid4().hex), ) final_output = None async for res in generator: final_output = res output.append(final_output) print(output) ``` ### How would you like to use vllm I noticed in the documentation that the service started via CLI seems to cache the lora adapter in memory, but I didn't find the code to implement it. Can you tell me where to implement it? ```shell vllm serve meta-llama/Llama-2-7b-hf \ --enable-lora \ --lora-modules sql-lora=$H...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ems to reload the Lora adapter every time ```python class LoraModule(BaseModel): name: str path: str class UserRequest(BaseModel): lora_module: list[LoraModule] question: str @app.post("/") async def multi_loras(req: Us...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/snapshots/0dfa347e8877a4d4ed19ee56c140fa518470028c/ ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and ask...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the lora adapter in memory usage ### Your current environment I want to build a multi-lora service, but the following code seems to reload the Lora adapter every time ```python class LoraModule(BaseModel): name: str pat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [{"role": "user", "content": req.question}], tokenize=False, add_generation_prompt=True, ) output = [] for i, lora in enumerate(req.lora_module): generator = engine.generate( messages, sampling_params=params, lor

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
