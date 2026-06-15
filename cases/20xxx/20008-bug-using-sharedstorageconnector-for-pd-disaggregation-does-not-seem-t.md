# vllm-project/vllm#20008: [Bug]: Using SharedStorageConnector for PD disaggregation does not seem to support llm.chat

| 字段 | 值 |
| --- | --- |
| Issue | [#20008](https://github.com/vllm-project/vllm/issues/20008) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using SharedStorageConnector for PD disaggregation does not seem to support llm.chat

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am following the `examples/offline_inference/disaggregated-prefill-v1` example to experiment with PD disaggregation using `SharedStorageConnector`. The process works fine when using the `llm.generate() `function. Then, I want to test the performance of PD disaggregation with the `llm.chat()` function. I modified my `prefill_example.py` accordingly, but I encountered an error because `output.prompt` is `None`. Here is the modified code: ``` # SPDX-License-Identifier: Apache-2.0 # SPDX-FileCopyrightText: Copyright contributors to the vLLM project from vllm import LLM, SamplingParams from vllm.config import KVTransferConfig import json def load_prompts(json_file): with open(json_file, 'r', encoding='utf-8') as file: return json.load(file) # def read_prompts(): # prompts = load_prompts("./dataset/test_prompt.json") # prompt = prompts["prompt_bussiness1"] # messages = [ # {"role": "user", "content": prompt} # ] # return messages def main(): data = load_prompts("./dataset/test_prompt.json") prompts = [ {"role": "user", "content": data["prompt_bussiness1"]} ] # print(prompts) # not None sampling_params = SamplingParams(temperature=0.6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: FileCopyrightText: Copyright contributors to the vLLM project from vllm import LLM, SamplingParams from vllm.config import KVTransferConfig import json def load_prompts(json_file): with open(json_file, 'r', encoding='ut...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: tors to the vLLM project from vllm import LLM, SamplingParams from vllm.config import KVTransferConfig import json def load_prompts(json_file): with open(json_file, 'r', encoding='utf-8') as file: return json.load(file)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ageConnector for PD disaggregation does not seem to support llm.chat bug;stale ### Your current environment ### 🐛 Describe the bug I am following the `examples/offline_inference/disaggregated-prefill-v1` example to expe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
