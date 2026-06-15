# vllm-project/vllm#16189: [Bug]: use_irope error on run using vllm docker

| 字段 | 值 |
| --- | --- |
| Issue | [#16189](https://github.com/vllm-project/vllm/issues/16189) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: use_irope error on run using vllm docker

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to use the new llama4 and am running into unexpected argument use_irope. ``` ERROR 04-07 07:17:37 [engine.py:448] XFormersImpl.__init__() got an unexpected keyword argument 'use_irope' ERROR 04-07 07:17:37 [engine.py:448] Traceback (most recent call last): ERROR 04-07 07:17:37 [engine.py:448] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 436, in run_mp_engine ERROR 04-07 07:17:37 [engine.py:448] engine = MQLLMEngine.from_vllm_config( ERROR 04-07 07:17:37 [engine.py:448] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-07 07:17:37 [engine.py:448] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 128, in from_vllm_config ERROR 04-07 07:17:37 [engine.py:448] return cls( ERROR 04-07 07:17:37 [engine.py:448] ^^^^ ERROR 04-07 07:17:37 [engine.py:448] File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 82, in __init__ ERROR 04-07 07:17:37 [engine.py:448] self.engine = LLMEngine(*args, **kwargs) ERROR 04-07 07:17:37 [engine.py:448] ^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-07 07:17:37 [engine.py:448] File "/usr/local/li...

## 现有链接修复摘要

#16212 Add warning for Attention backends that do not support irope yet

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: use_irope error on run using vllm docker bug ### Your current environment ### 🐛 Describe the bug I'm trying to use the new llama4 and am running into unexpected argument use_irope. ``` ERROR 04-07 07:17:37 [engin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: urrent environment ### 🐛 Describe the bug I'm trying to use the new llama4 and am running into unexpected argument use_irope. ``` ERROR 04-07 07:17:37 [engine.py:448] XFormersImpl.__init__() got an unexpected keyword ar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 07:17:37 [engine.py:448] self.impl = impl_cls(num_heads, head_size, scale, num_kv_heads, ERROR 04-07 07:17:37 [engine.py:448] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 04-07 07:17:37 [engine.py:448] Type...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n;cuda;operator build_error;crash dtype #16212 Add warning for Attention backends that do not support irope yet Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#16212](https://github.com/vllm-project/vllm/pull/16212) | closes_keyword | 0.95 | Add warning for Attention backends that do not support irope yet | Fixes #16189 Tested linter happy with `pre-commit run --show-diff-on-failure --color=always --hook-stage manual --all-files` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
