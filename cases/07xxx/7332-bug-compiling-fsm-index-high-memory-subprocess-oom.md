# vllm-project/vllm#7332: [Bug]: Compiling FSM index high memory && subprocess OOM

| 字段 | 值 |
| --- | --- |
| Issue | [#7332](https://github.com/vllm-project/vllm/issues/7332) |
| 状态 | closed |
| 标签 | bug;structured-output |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Compiling FSM index high memory && subprocess OOM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug server ```bash python -m vllm.entrypoints.openai.api_server --model /model/Qwen1.5-14B-Chat-GPTQ-Int4 --quantization gptq --max-model-len 12720 ``` client ```python class ClassificationItem(BaseModel): name: str = Field(max_length=20, title="分类名") risk_level: conint(ge=0, lt=8) = Field(title="风险等级") class ClassificationSet(BaseModel): classification_list: List[ClassificationItem] = Field(min_items=100, title="分类名的列表") openai_client = OpenAI( base_url="http://192.168.91.25:8000/v1", api_key="EMPTY", ) client = instructor.from_openai(openai_client) resp = client.chat.completions.create( model="/model/Qwen1.5-14B-Chat-GPTQ-Int4", messages=[{"role": "user", "content": "你是一名数据安全运营专家，我是一个法律行业的公司，是一家律师事务所，我们公司负责响应客户的法律咨询、帮客户在法庭上辩护，我们公司里有很多机密类型的文件或者文档，请你为我列举一下这些'类型'，只需要给出类型名和该类型对应的风险等级，不需要输出json以外的内容"}], response_model=ClassificationSet ) ``` payload ```bash curl http://192.168.91.25:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "messages": [ { "role": "user", "content": "你是一名数据安全运营专家，我是一个法律行业的公司，是一家律师事务所，我们公司负责响应客户的法律咨询、帮客户在法庭上辩护，我们公司里有很多机密类型的文件或者文档，请你为我列举一下这些'类型'，只需要给出类型名和该类型对应的风险等级，不需要输出json以外的内容" } ], "model"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tokens=12635, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [151644, 8948, 198, 2610, 525, 264, 10950, 1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vllm.entrypoints.openai.api_server --model /model/Qwen1.5-14B-Chat-GPTQ-Int4 --quantization gptq --max-model-len 12720 ``` client ```python class ClassificationItem(BaseModel): name: str = Field(max_length=20, title="分类...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Compiling FSM index high memory && subprocess OOM bug;structured-output ### Your current environment ### 🐛 Describe the bug server ```bash python -m vllm.entrypoints.openai.api_server --model /model/Qwen1.5-14B-C...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: Compiling FSM index high memory && subprocess OOM bug;structured-output ### Your current environment ### 🐛 Describe the bug server ```bash python -m vllm.entrypoints.openai.api_server --model /model/Qwen1.5-14B-C...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e the bug server ```bash python -m vllm.entrypoints.openai.api_server --model /model/Qwen1.5-14B-Chat-GPTQ-Int4 --quantization gptq --max-model-len 12720 ``` client ```python class ClassificationItem(BaseModel): name: s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
