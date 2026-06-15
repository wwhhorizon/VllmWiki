# vllm-project/vllm#8237: [Bug]: requests with response_format cause vllm to hang with pipeline parallel 

| 字段 | 值 |
| --- | --- |
| Issue | [#8237](https://github.com/vllm-project/vllm/issues/8237) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: requests with response_format cause vllm to hang with pipeline parallel 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When vllm running with `--pipeline-parallel-size 2` and receives a request containing the `response_format` parameter vllm will hang processing this request, not complete, and not run any subsequent requests. Removing `response_format` has the expected behaviour of the engine processing the request and returning the response. Additionally, vllm works as expected when `--pipeline-parallel-size` is 1 or when `--tensor-parallel-size` is 2. It seems to be isolated to PP. This is with the latest version of vllm (0.6.0) ```bash vllm serve NousResearch/Meta-Llama-3.1-8B-Instruct --pipeline-parallel-size 2 ```` ```python import os import json from openai import OpenAI client = OpenAI(api_key=os.environ["VLLM_API_KEY"], base_url=os.environ["VLLM_BASE_URL"]) def extract_dinos(sentence: str) -> dict: response = client.chat.completions.create( model="NousResearch/Meta-Llama-3.1-8B-Instruct", messages=[ { "role": "system", "content": """In JSON format extract a list of `dogs`, with their `name`, their `breed `, and whether its `size` is `large` or `small`. Only return the JSON.""" }, { "role": "user", "content": sentence } ], response_format=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: llel-size` is 2. It seems to be isolated to PP. This is with the latest version of vllm (0.6.0) ```bash vllm serve NousResearch/Meta-Llama-3.1-8B-Instruct --pipeline-parallel-size 2 ```` ```python import os import json...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: requests with response_format cause vllm to hang with pipeline parallel bug;stale ### Your current environment ### 🐛 Describe the bug When vllm running with `--pipeline-parallel-size 2` and receives a request con...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: requests with response_format cause vllm to hang with pipeline parallel bug;stale ### Your current environment ### 🐛 Describe the bug When vllm running with `--pipeline-parallel-size 2` and receives a request con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: s is with the latest version of vllm (0.6.0) ```bash vllm serve NousResearch/Meta-Llama-3.1-8B-Instruct --pipeline-parallel-size 2 ```` ```python import os import json from openai import OpenAI client = OpenAI(api_key=o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ature=0.7, top_p=1.0, top _k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=9907, mi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
