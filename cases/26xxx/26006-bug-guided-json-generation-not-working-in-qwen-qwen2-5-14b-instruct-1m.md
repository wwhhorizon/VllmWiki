# vllm-project/vllm#26006: [Bug]: Guided JSON generation not working in `Qwen/Qwen2.5-14B-Instruct-1M`

| 字段 | 值 |
| --- | --- |
| Issue | [#26006](https://github.com/vllm-project/vllm/issues/26006) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Guided JSON generation not working in `Qwen/Qwen2.5-14B-Instruct-1M`

### Issue 正文摘录

### Your current environment vLLM Version : 0.10.2 ### 🐛 Describe the bug The guided json generation doesn't seem to be working with `Qwen/Qwen2.5-14B-Instruct-1M`. **Sample code**: ```python from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedDecodingParams from pydantic import BaseModel import os os.environ["VLLM_ATTENTION_BACKEND"] = "DUAL_CHUNK_FLASH_ATTN" class Response(BaseModel): steps: str final_answer: str guided_decoding_params = GuidedDecodingParams(json=Response.model_json_schema()) sampling_params = SamplingParams( guided_decoding=guided_decoding_params, temperature=0, max_tokens=4096 ) llm = LLM( model="Qwen/Qwen2.5-14B-Instruct-1M", # model="Qwen/Qwen2.5-14B-Instruct", max_num_seqs=1, enforce_eager=True, max_model_len=10_000, ) message = [{"role": "user", "content": "Solve for x: x + 5 = 5?"}] outputs = llm.chat(message, sampling_params=sampling_params, use_tqdm=False) output = outputs[0].outputs[0].text.strip() print(output) ``` If I use `Qwen/Qwen2.5-14B-Instruct` and comment out the `VLLM_ATTENTION_BACKEND` environment variable line, the output seems to be in valid json format. I am not sure if `VLLM_ATTENTION_BACKEND="DUAL_CHUNK_FLASH_ATT...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: en/Qwen2.5-14B-Instruct-1M` bug;stale ### Your current environment vLLM Version : 0.10.2 ### 🐛 Describe the bug The guided json generation doesn't seem to be working with `Qwen/Qwen2.5-14B-Instruct-1M`. **Sample code**:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Guided JSON generation not working in `Qwen/Qwen2.5-14B-Instruct-1M` bug;stale ### Your current environment vLLM Version : 0.10.2 ### 🐛 Describe the bug The guided json generation doesn't seem to be working with...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ams from pydantic import BaseModel import os os.environ["VLLM_ATTENTION_BACKEND"] = "DUAL_CHUNK_FLASH_ATTN" class Response(BaseModel): steps: str final_answer: str guided_decoding_params = GuidedDecodingParams(json=Resp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: el? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: outputs = llm.chat(message, sampling_params=sampling_params, use_tqdm=False) output = outputs[0].outputs[0].text.strip() print(output) ``` If I use `Qwen/Qwen2.5-14B-Instruct` and comment out the `VLLM_ATTENTION_BACKEND...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
