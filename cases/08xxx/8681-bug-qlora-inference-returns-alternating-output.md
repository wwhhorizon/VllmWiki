# vllm-project/vllm#8681: [Bug]: QLoRA inference returns alternating output

| 字段 | 值 |
| --- | --- |
| Issue | [#8681](https://github.com/vllm-project/vllm/issues/8681) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: QLoRA inference returns alternating output

### Issue 正文摘录

### Your current environment ### Model Input Dumps Our waitress seemed less than happy about the prix fixe dinner choices and at one point said, Do you really need to hear the specials?\n\n### Response: ### 🐛 Describe the bug It was recently noted that QLoRA inferencing on some internal models is consistently producing alternating results. We've noticed that the alternating result is the same as output that not using the adapter would produce. Including some example output below while we continue to try to reproduce it using a public QLoRA model. Two separate adapters, returning `waitress: negative, prix fixe d..`: ``` INFO 09-20 19:00:46 logs.py:155] generate{input=[b'Input:\\\\nOur waitress seemed less...'] prefix_id= correlation_id=None adapter_id=llama-sentiment input_chars=[159] params=stopping { max_new_tokens: 10 } tokenization_time=585.34ms queue_time=281.77ms inference_time=1663.15ms time_per_token=166.32ms total_time=2530.26ms input_toks=37}: Request generated 10 tokens before MAX_TOKENS, output 46 chars: b' waitress: negative, prix fixe d...' INFO 09-20 19:00:46 logs.py:155] generate{input=[b'Input:\\\\nOur waitress seemed less...'] prefix_id= correlation_id=None adapte...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: QLoRA inference returns alternating output bug;stale ### Your current environment ### Model Input Dumps Our waitress seemed less than happy about the prix fixe dinner choices and at one point said, Do you really...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: dinner choices and at one point said, Do you really need to hear the specials?\n\n### Response: ### 🐛 Describe the bug It was recently noted that QLoRA inferencing on some internal models is consistently producing alter...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eturns alternating output bug;stale ### Your current environment ### Model Input Dumps Our waitress seemed less than happy about the prix fixe dinner choices and at one point said, Do you really need to hear the special...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: nd_api;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
