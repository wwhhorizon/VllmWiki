# vllm-project/vllm#20060: [Bug]: Sampling discrepancy between ollama and vLLM for gemma-3-27b-it et al.

| 字段 | 值 |
| --- | --- |
| Issue | [#20060](https://github.com/vllm-project/vllm/issues/20060) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 41; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Sampling discrepancy between ollama and vLLM for gemma-3-27b-it et al.

### Issue 正文摘录

### 🐛 Describe the bug This is what the code looks like: ```py from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedDecodingParams from pydantic import BaseModel, Field, create_model from typing import Literal, List, Optional import json llm = LLM(model="google/gemma-3-27b-it", quantization="bitsandbytes", trust_remote_code=True, max_model_len=2048, max_num_seqs=100) TYPE = "review on airlines posted on TripAdvisor" json_schema = {'properties': {'gender': {'enum': ['male', 'female', 'non-binary', 'other', 'prefer_not_to_say'], 'title': 'Gender', 'type': 'string'}, 'prename': {'title': 'Prename', 'type': 'string'}, 'surname': {'title': 'Surname', 'type': 'string'}, 'age': {'maximum': 120, 'minimum': 0, 'title': 'Age', 'type': 'integer'}, 'overall_mood': {'enum': ['joy', 'trust', 'fear', 'surprise', 'sadness', 'disgust', 'anger', 'anticipation'], 'title': 'Overall Mood', 'type': 'string'}, 'persona_description': {'title': 'Persona Description', 'type': 'string'}, 'review_title': {'title': 'Review Title', 'type': 'string'}, 'travel_class': {'title': 'Travel Class', 'type': 'string'}, 'trip_type': {'title': 'Trip Type', 'type': 'string'}, 'number_of_passengers':...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Sampling discrepancy between ollama and vLLM for gemma-3-27b-it et al. bug;stale ### 🐛 Describe the bug This is what the code looks like: ```py from vllm import LLM, SamplingParams from vllm.sampling_params impor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: # 🐛 Describe the bug This is what the code looks like: ```py from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedDecodingParams from pydantic import BaseModel, Field, create_model from typing imp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ts[0].text`: ``` '{ "gender": "female", "prename": "Laura", "surname": "Smith", "age": 35, "overall_mood": "disgust", "persona_description": "A meticulous and independent traveler who values comfort and reliability. She...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: mpling discrepancy between ollama and vLLM for gemma-3-27b-it et al. bug;stale ### 🐛 Describe the bug This is what the code looks like: ```py from vllm import LLM, SamplingParams from vllm.sampling_params import GuidedD...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: al, List, Optional import json llm = LLM(model="google/gemma-3-27b-it", quantization="bitsandbytes", trust_remote_code=True, max_model_len=2048, max_num_seqs=100) TYPE = "review on airlines posted on TripAdvisor" json_s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
