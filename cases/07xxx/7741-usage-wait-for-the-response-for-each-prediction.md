# vllm-project/vllm#7741: [Usage]: Wait for the response for each prediction

| 字段 | 值 |
| --- | --- |
| Issue | [#7741](https://github.com/vllm-project/vllm/issues/7741) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Wait for the response for each prediction

### Issue 正文摘录

### How would you like to use vllm I would like to wait for each response using vllm because I will use the previous predictions to complement the next ones. However, I don't know how to do this with vllm. ### Code ```py import pandas as pd from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest llm = LLM( model="maritaca-ai/sabia-7b", enable_lora=True, max_model_len=256, gpu_memory_utilization=0.95, enforce_eager=True, ) sampling_params = SamplingParams( temperature=0.001, max_tokens=256 ) df = pd.read_csv("prompts_bluche_test.csv") prev_5_words = '' next_5_words = '' last_filename_prefix = '' prompts = [] for index, row in df.iterrows(): filename_prefix = row['filename'][:8] next_filename_prefix = df.iloc[index+1]['filename'][:8] if index < len(df)-1 else '' if (last_filename_prefix == '' or filename_prefix == next_filename_prefix): next_5_words = row['next_5_words'] else: next_5_words = '' prompt = f""" ### Instrução: Corrija os erros pós-OCR presentes na linha. ### Palavras anteriores: {prev_5_words} ### Linha a corrigir: {row['input']} ### Palavras seguintes: {next_5_words} ### Resposta: """ output = llm.generate( prompt, sampling_params, lora_request=L...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Wait for the response for each prediction usage;stale ### How would you like to use vllm I would like to wait for each response using vllm because I will use the previous predictions to complement the next ones...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t ones. However, I don't know how to do this with vllm. ### Code ```py import pandas as pd from vllm import LLM, SamplingParams from vllm.lora.request import LoRARequest llm = LLM( model="maritaca-ai/sabia-7b", enable_l...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: filename_prefix = df.iloc[index+1]['filename'][:8] if index < len(df)-1 else '' if (last_filename_prefix == '' or filename_prefix == next_filename_prefix): next_5_words = row['next_5_words'] else: next_5_words = '' prom...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: SamplingParams from vllm.lora.request import LoRARequest llm = LLM( model="maritaca-ai/sabia-7b", enable_lora=True, max_model_len=256, gpu_memory_utilization=0.95, enforce_eager=True, ) sampling_params = SamplingParams(...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: emperature=0.001, max_tokens=256 ) df = pd.read_csv("prompts_bluche_test.csv") prev_5_words = '' next_5_words = '' last_filename_prefix = '' prompts = [] for index, row in df.iterrows(): filename_prefix = row['filename'...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
