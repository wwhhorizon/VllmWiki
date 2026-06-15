# vllm-project/vllm#14365: [Bug]: API Connection Error after concurrent API calls

| 字段 | 值 |
| --- | --- |
| Issue | [#14365](https://github.com/vllm-project/vllm/issues/14365) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: API Connection Error after concurrent API calls

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I serve the vllm model like the following: ``` python -m vllm.entrypoints.openai.api_server --dtype auto --api-key token-abc123 --tensor-parallel-size 2 --enforce-eager --host 0.0.0.0 --port 8004 --model Qwen2.5-72B-Instruct-GPTQ-Int4 --gpu-memory-utilization 0.9 --max-model-len 16000 ``` My client looks like this: ``` class vLLM: def __init__(self, base_url, model_name, api_key): self.model_name = model_name self.base_url = base_url self.llm_client = AsyncOpenAI(base_url=self.base_url, api_key=api_key) async def invoke(self, prompt, system_prompt="", temperature=0.0): completion = await self.llm_client.chat.completions.create(model=self.model_name, messages=[ {"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}], extra_body={"temperature": temperature}) response = completion.choices[0].message.content return response ``` I use the AsyncOpenAI for making parallel llm calls to process every row of an excel sheet. The function which calls the llm looks like this: async def evaluate_records(records, user_query, llm, column_descriptions): """Evaluates a list of records against a user query in parallel (as...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: , column_descriptions) return index, result semaphore = asyncio.Semaphore(20) # Limit concurrent requests # Create a list of tasks tasks = [process_record(i, record, semaphore) for i, record in enumerate(records)] # Gat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: API Connection Error after concurrent API calls bug;unstale ### Your current environment ### 🐛 Describe the bug I serve the vllm model like the following: ``` python -m vllm.entrypoints.openai.api_server --dtype...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: like the following: ``` python -m vllm.entrypoints.openai.api_server --dtype auto --api-key token-abc123 --tensor-parallel-size 2 --enforce-eager --host 0.0.0.0 --port 8004 --model Qwen2.5-72B-Instruct-GPTQ-Int4 --gpu-m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ## Your current environment ### 🐛 Describe the bug I serve the vllm model like the following: ``` python -m vllm.entrypoints.openai.api_server --dtype auto --api-key token-abc123 --tensor-parallel-size 2 --enforce-eager...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
