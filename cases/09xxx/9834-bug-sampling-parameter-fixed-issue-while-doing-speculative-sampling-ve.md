# vllm-project/vllm#9834: [Bug]: Sampling parameter fixed issue while doing speculative sampling verification step

| 字段 | 值 |
| --- | --- |
| Issue | [#9834](https://github.com/vllm-project/vllm/issues/9834) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Sampling parameter fixed issue while doing speculative sampling verification step

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Example code** 1. server `python vllm/vllm/entrypoints/openai/api_server.py -tp 4 --model meta-llama/Llama-2-70b-hf --port 8000 --gpu-memory-utilization 0.8 --trust-remote-code --speculative-model meta-llama/Llama-2-7b-hf --use-v2-block-manager --num_speculative_tokens 1` 2. completion ``` openai_api_base = "http://0.0.0.0:8041/v1" client = OpenAI(base_url=openai_api_base,) models = client.models.list() model = models.data[0].id completion = client.completions.create( model=model, prompt="Hello, my name is", echo=False, n=1, stream=False, temperature=0.6, top_p=0.6, max_tokens=128, ) print(completion) ``` **Bug** - Setting I am running **speculative sampling** with num_speculative_tokens = 1. In this setting, verification with target model should sample two logits in parallel. - Problem - The bug here is that when I print out the top_p value of sampling parameters, **the first top_p is always fixed to 1,** which affects the acceptance of the token. (FYI, same with the example above, I used top_p as 0.6) - - It is also same when the num_speculative_tokens value is different. The first top_p va...

## 现有链接修复摘要

#10198 [Bugfix][SpecDecode] apply sampling parameters to target probabilities for consistency in rejection sampling.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Sampling parameter fixed issue while doing speculative sampling verification step bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Example code** 1. server `python vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ways fixed to 1. - The first top_p value should also be set to the specific sampling parameter value that is given as input. - Test setting - sampling param: top_p = 0.9 / temperature = 0.6 - Target model / Draft model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: -trust-remote-code --speculative-model meta-llama/Llama-2-7b-hf --use-v2-block-manager --num_speculative_tokens 1` 2. completion ``` openai_api_base = "http://0.0.0.0:8041/v1" client = OpenAI(base_url=openai_api_base,)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tive sampling verification step bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug **Example code** 1. server `python vllm/vllm/entrypoints/openai/api_server.py -tp 4 --model met...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#10198](https://github.com/vllm-project/vllm/pull/10198) | closes_keyword | 0.95 | [Bugfix][SpecDecode] apply sampling parameters to target probabilities for consistency in rejection sampling. | FIX #9834 (*link existing issues this PR will resolve*) ## Problem The current `BatchExpansionTop1Scorer` implements a speculative scoring mechanism that uses batch expansion t |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
