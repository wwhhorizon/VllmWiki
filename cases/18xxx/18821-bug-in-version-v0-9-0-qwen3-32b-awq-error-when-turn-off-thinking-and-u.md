# vllm-project/vllm#18821: [Bug]: In Version V0.9.0, Qwen3-32B-AWQ Error when turn off thinking and use guided_json simultaneously.

| 字段 | 值 |
| --- | --- |
| Issue | [#18821](https://github.com/vllm-project/vllm/issues/18821) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: In Version V0.9.0, Qwen3-32B-AWQ Error when turn off thinking and use guided_json simultaneously.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In version V0.9.0, when using qwen3-32B-awq, if both "thinking" is turned off and guided_json is used, the temperature can only be set to 0. If set to other values, the entire service will be blocked. # service command ```bash python -m vllm.entrypoints.openai.api_server --port 18101 --served-model-name Qwen-Text --model /data/modelscope/Qwen3-32B-AWQ --tokenizer /data/modelscope/Qwen3-32B-AWQ --max-model-len 16384 --gpu-memory-utilization 0.9 ``` # client code ```python from openai import OpenAI from pydantic import BaseModel client = OpenAI(api_key="xxx", base_url="http://127.0.0.1:18101/v1") class OutputModel(BaseModel): result: int prompt = """\ 123+456等于多少？ 结果以JSON格式给出: {{ "result": "结果" }} """ # or rsp = client.chat.completions.create( model="Qwen-Text", messages=[ {"role": "user", "content": prompt}, ], extra_body={"chat_template_kwargs": {"enable_thinking": False}, "guided_json": OutputModel.model_json_schema()}, temperature=0, ) print(rsp) # service will be blocked rsp = client.chat.completions.create( model="Qwen-Text", messages=[ {"role": "user", "content": prompt}, ], extra_body={"chat_template_kwargs": {"enable_think...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: In Version V0.9.0, Qwen3-32B-AWQ Error when turn off thinking and use guided_json simultaneously. bug ### Your current environment ### 🐛 Describe the bug In version V0.9.0, when using qwen3-32B-awq, if both "thin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: to any value other than 0, the service becomes unresponsive, and nvidia-smi consistently shows this state indefinitely! Volatile GPU-Util = 100% but Persistence-MPwr = 79W """ +------------------------------------------...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: can only be set to 0. If set to other values, the entire service will be blocked. # service command ```bash python -m vllm.entrypoints.openai.api_server --port 18101 --served-model-name Qwen-Text --model /data/modelscop...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: In Version V0.9.0, Qwen3-32B-AWQ Error when turn off thinking and use guided_json simultaneously. bug ### Your current environment ### 🐛 Describe the bug In version V0.9.0, when using qwen3-32B-awq, if both "thin...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
