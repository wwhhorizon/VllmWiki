# vllm-project/vllm#2787: How to confirm the multi lora works?

| 字段 | 值 |
| --- | --- |
| Issue | [#2787](https://github.com/vllm-project/vllm/issues/2787) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to confirm the multi lora works?

### Issue 正文摘录

I'm running the example of `multilora_inference.py` Here is some code snippet. ```python def create_test_prompts(lora_path: str) -> List[Tuple[str, SamplingParams]]: """Create a list of test prompts with their sampling parameters. 2 requests for base model, 4 requests for the LoRA. We define 2 different LoRA adapters (using the same model for demo purposes). Since we also set `max_loras=1`, the expectation is that the requests with the second LoRA adapter will be ran after all requests with the first adapter have finished. """ return [ ("[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]", SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1, max_tokens=128, stop_token_ids=[32003]), LoRARequest("sql-lora", 1, lora_path)), ("[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_11 (nationality VARCHAR, elector VARCHAR)\n\n question: When Anchero Pantaleone was the elector what is under nationality? [/user] [assistant]", SamplingParams(n=3,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: of test prompts with their sampling parameters. 2 requests for base model, 4 requests for the LoRA. We define 2 different LoRA adapters (using the same model for demo purposes). Since we also set `max_loras=1`, the expe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ased on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]", SamplingParams(temperature=0.0, logp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: """Create a list of test prompts with their sampling parameters. 2 requests for base model, 4 requests for the LoRA. We define 2 different LoRA adapters (using the same model for demo purposes). Since we also set `max_l...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ultilora_inference.py` Here is some code snippet. ```python def create_test_prompts(lora_path: str) -> List[Tuple[str, SamplingParams]]: """Create a list of test prompts with their sampling parameters. 2 requests for ba...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
