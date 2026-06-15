# vllm-project/vllm#26363: [Bug]: xgrammar cleanup leakage

| 字段 | 值 |
| --- | --- |
| Issue | [#26363](https://github.com/vllm-project/vllm/issues/26363) |
| 状态 | open |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: xgrammar cleanup leakage

### Issue 正文摘录

### Your current environment Using xgrammar (auto) as a backend, leads to memory leakage and destroy-group issues. If I run the attached code block, the script ends with these warnings. ``` [rank0]:[W1007 18:43:37.018915692 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator()) nanobind: leaked 2 instances! - leaked instance 0x7fe320b95668 of type "xgrammar.xgrammar_bindings.GrammarMatcher" - leaked instance 0x7fe575b57468 of type "xgrammar.xgrammar_bindings.CompiledGrammar" nanobind: leaked 2 types! - leaked type "xgrammar.xgrammar_bindings.GrammarMatcher" - leaked type "xgrammar.xgrammar_bindings.CompiledGrammar" nanobind: leaked 16 functions! - leaked function "__init__" - leaked function "fill_next_token_bitmask" - leaked function "" - leaked function "" - leaked function "reset" - leaked function "accept_token" - leaked function "" - leaked function "_debug_print_internal_state" - leaked function "serialize_json" - leaked function "accept_string" - leaked function "deserialize_json" - leaked funct...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: r" - leaked instance 0x7fe575b57468 of type "xgrammar.xgrammar_bindings.CompiledGrammar" nanobind: leaked 2 types! - leaked type "xgrammar.xgrammar_bindings.GrammarMatcher" - leaked type "xgrammar.xgrammar_bindings.Comp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: s to memory leakage and destroy-group issues. If I run the attached code block, the script ends with these warnings. ``` [rank0]:[W1007 18:43:37.018915692 ProcessGroupNCCL.cpp:1538] Warning: WARNING: destroy_process_gro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nup leakage bug ### Your current environment Using xgrammar (auto) as a backend, leads to memory leakage and destroy-group issues. If I run the attached code block, the script ends with these warnings. ``` [rank0]:[W100...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ", "neutral"]}}, "required": ["sentiment"], } pipe = LLM(model="Qwen/Qwen2.5-0.5B-Instruct", max_model_len=1024) tokenizer = pipe.get_tokenizer() prompt = tokenizer.apply_chat_template( [{"role": "user", "content": "Is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
