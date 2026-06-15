# vllm-project/vllm#9557: [Bug]: MistralTokenizer Detokenization Issue

| 字段 | 值 |
| --- | --- |
| Issue | [#9557](https://github.com/vllm-project/vllm/issues/9557) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MistralTokenizer Detokenization Issue

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproducing the error case mentioned here - https://github.com/vllm-project/vllm/issues/8627#issuecomment-2364194419 ```python from vllm.transformers_utils.tokenizers import mistral tokenizer = mistral.MistralTokenizer.from_pretrained('/path/to/mistral/tokenizer') byte_string = "hello".encode() # input 1 tokenizer.convert_tokens_to_string(["hello", "there", byte_string, "🌶️"]) # input 2 tokenizer.convert_tokens_to_string([b""]) ``` ``` # input 1 Traceback (most recent call last): File " ", line 1, in File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/transformers_utils/tokenizers/mistral.py", line 191, in convert_tokens_to_string self.tokenizer._tekken_token2id_nospecial[t] + shift ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^ KeyError: b'\xf0\x9f\x8c\xb6\xef\xb8\x8f' # input 2 Traceback (most recent call last): File " ", line 1, in File "/workspace/my-vllm/lib64/python3.12/site-packages/vllm/transformers_utils/tokenizers/mistral.py", line 191, in convert_tokens_to_string self.tokenizer._tekken_token2id_nospecial[t] + shift ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^ KeyError: b'' ```...

## 现有链接修复摘要

#9625 [Bugfix] Fix edge cases for MistralTokenizer

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproducing the error case mentioned here - https://github.com/vllm-project/vllm/issues/8627#issuecomment-2364194419 ```python from vllm.transformers_utils.toke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency #9625 [Bugfix] Fix edge cases for MistralTokenizer Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lTokenizer Detokenization Issue bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Reproducing the error case mentioned here - https://github.com/vllm-project/vllm/issues/8627#is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency #9625 [Bugfix] Fix edge cases for MistralTokenizer Your current environ...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9625](https://github.com/vllm-project/vllm/pull/9625) | closes_keyword | 0.95 | [Bugfix] Fix edge cases for MistralTokenizer | FIX #9557 **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside this <details> section, markdown rendering do |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
