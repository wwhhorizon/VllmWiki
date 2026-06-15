# vllm-project/vllm#3199: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.

| 字段 | 值 |
| --- | --- |
| Issue | [#3199](https://github.com/vllm-project/vllm/issues/3199) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github.

### Issue 正文摘录

sql_lora_path = "/home/zyn/models/slot_lora_gd" from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest llm = LLM(model="/home/models/dem_14b/base", enable_lora=True, trust_remote_code=True) sampling_params = SamplingParams(temperature=0, max_tokens=256, stop=["[/assistant]"]) prompts = [ "[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]", "[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_11 (nationality VARCHAR, elector VARCHAR)\n\n question: When Anchero Pantaleone was the elector what is under nationality? [/user] [assistant]", ] outputs = llm.generate(prompts, sampling_params, lora_request=LoRARequest("sql_adapter", 1, sql_lora_path)) llm = LLM(model="/home/models/dem_14b/base", File "/root/miniconda3/envs/qwen/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 109, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/root/miniconda3/envs/qwen/lib/python3.10/site-packages/vllm/engin...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ValueError: Model QWenLMHeadModel does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. stale sql_lora_path = "/home/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: the future. If this is important to you, please open an issue on github. stale sql_lora_path = "/home/zyn/models/slot_lora_gd" from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest llm = LLM(mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s enabled. Support for this model may be added in the future. If this is important to you, please open an issue on github. stale sql_lora_path = "/home/zyn/models/slot_lora_gd" from vllm import LLM, SamplingParams from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ased on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]", "[user] Write a SQL query to answer...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: please open an issue on github. stale sql_lora_path = "/home/zyn/models/slot_lora_gd" from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest llm = LLM(model="/home/models/dem_14b/base", enable_lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
